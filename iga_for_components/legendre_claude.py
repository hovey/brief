"""This module demonstrates Legendre interpolation basis functions used in spectral/hp
finite element methods. Nodes are chosen as Gauss-Lobatto-Legendre (GLL) points, which
include the endpoints ±1 and the interior roots of P'_{n-1}(x). GLL quadrature achieves
spectral accuracy and is widely used in high-order FEA and CFD codes."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from numpy.polynomial.legendre import legroots

# ── Colour palette ────────────────────────────────────────────────────────────
plt.rcParams.update(
    {
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": ["Computer Modern Roman"],
        "text.latex.preamble": r"\usepackage{amsmath}",
    }
)

COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
GRID_COLOR = "#CCCCCC"
BG_COLOR = "#F8F9FA"
PANEL_BG = "#FFFFFF"


# ── GLL node computation ──────────────────────────────────────────────────────


def gll_nodes(n):
    """Return n Gauss-Lobatto-Legendre nodes on [-1, 1].

    GLL points = { -1 } ∪ roots of P'_{n-1}(x) ∪ { +1 }
    where P_{n-1} is the Legendre polynomial of degree n-1.

    Parameters
    ----------
    n : int  – total number of nodes (must be ≥ 2)
    """
    if n < 2:
        raise ValueError("Need at least 2 GLL nodes.")
    if n == 2:
        return np.array([-1.0, 1.0])

    # Derivative P'_{n-1} has coefficients of P_{n-1} differentiated once.
    # numpy represents Legendre coefficients as [c0, c1, ..., cn].
    # P_{n-1}(x): coefficient vector with 1 at position n-1, zeros elsewhere.
    pn1_coeffs = np.zeros(n)
    pn1_coeffs[-1] = 1.0  # degree n-1 polynomial

    # Differentiate to get P'_{n-1}
    from numpy.polynomial.legendre import legder
    dpn1_coeffs = legder(pn1_coeffs)

    interior = np.sort(legroots(dpn1_coeffs).real)
    return np.concatenate([[-1.0], interior, [1.0]])


# ── Lagrange basis through GLL nodes ─────────────────────────────────────────


def lagrange_basis_at(x, nodes):
    """Evaluate all Lagrange basis polynomials through *nodes* at points *x*.

    L_i(x) = ∏_{j≠i} (x - x_j) / (x_i - x_j)
    """
    n = len(nodes)
    basis = []
    for i in range(n):
        L = np.ones_like(x, dtype=float)
        for j in range(n):
            if j != i:
                L *= (x - nodes[j]) / (nodes[i] - nodes[j])
        basis.append(L)
    return basis


# ── Node sets ─────────────────────────────────────────────────────────────────
LINEAR_NODES    = gll_nodes(2)   # [-1, 1]
QUADRATIC_NODES = gll_nodes(3)   # [-1, 0, 1]
CUBIC_NODES     = gll_nodes(4)   # [-1, -1/√5, 1/√5, 1]  (approx ±0.4472)


# ── Helper: draw one panel ────────────────────────────────────────────────────


def draw_panel(ax, x, basis_fns, nodes, title, labels):
    """Plot all GLL basis functions for one element order."""
    ax.set_facecolor(PANEL_BG)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#AAAAAA")

    ax.axhline(0, color=GRID_COLOR, linewidth=0.8, zorder=0)
    ax.axhline(1, color=GRID_COLOR, linewidth=0.8, linestyle="--", zorder=0)
    for xn in nodes:
        ax.axvline(xn, color=GRID_COLOR, linewidth=0.6, linestyle=":", zorder=0)

    for L, label, color in zip(basis_fns, labels, COLORS):
        ax.plot(x, L, color=color, linewidth=2.4, label=label, zorder=3)

    for i, (xn, color) in enumerate(zip(nodes, COLORS)):
        ax.scatter([xn], [1], color=color, s=80, zorder=5,
                   edgecolors="white", linewidths=1.2)
        for j, xm in enumerate(nodes):
            if j != i:
                ax.scatter([xm], [0], color=color, s=50, zorder=5,
                           edgecolors="white", linewidths=1.0,
                           marker="o", alpha=0.7)

    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-0.55, 1.25)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$\phi_i(x)$", fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
    ax.legend(
        fontsize=9.5,
        framealpha=0.9,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=len(nodes),
    )
    ax.tick_params(labelsize=9)

    # Format node tick labels
    ax.set_xticks(nodes)
    tick_labels = []
    for n in nodes:
        if np.isclose(n, -1):
            tick_labels.append(r"$-1$")
        elif np.isclose(n, 1):
            tick_labels.append(r"$1$")
        elif np.isclose(n, 0):
            tick_labels.append(r"$0$")
        else:
            tick_labels.append(f"${n:.4f}$")
    ax.set_xticklabels(tick_labels, fontsize=8)


# ── Main ──────────────────────────────────────────────────────────────────────


def main():
    x = np.linspace(-1, 1, 500)

    fig = plt.figure(figsize=(5.5, 10), facecolor=BG_COLOR)
    fig.suptitle(
        "GLL Lagrange Basis Functions\non the Reference Element $[-1,\\ 1]$\n"
        r"(Gauss--Lobatto--Legendre nodes)",
        fontsize=14,
        fontweight="bold",
        y=1.0,
    )

    gs = gridspec.GridSpec(
        3, 1, figure=fig,
        top=0.92, bottom=0.1, left=0.13, right=0.97, hspace=0.65,
    )

    # ── Panel 1 – Linear (2 GLL nodes: ±1) ───────────────────────────────────
    ax1 = fig.add_subplot(gs[0, 0])
    draw_panel(
        ax1, x,
        lagrange_basis_at(x, LINEAR_NODES),
        LINEAR_NODES,
        "Order 1 — 2 GLL nodes",
        [r"$\phi_0$", r"$\phi_1$"],
    )

    # ── Panel 2 – Quadratic (3 GLL nodes: −1, 0, 1) ──────────────────────────
    ax2 = fig.add_subplot(gs[1, 0])
    draw_panel(
        ax2, x,
        lagrange_basis_at(x, QUADRATIC_NODES),
        QUADRATIC_NODES,
        "Order 2 — 3 GLL nodes",
        [r"$\phi_0$", r"$\phi_1$", r"$\phi_2$"],
    )

    # ── Panel 3 – Cubic (4 GLL nodes: ±1, ±1/√5) ────────────────────────────
    n3 = CUBIC_NODES
    xi_str = [f"${v:.4f}$" if not np.isclose(abs(v), 1) else ("$-1$" if v < 0 else "$1$")
              for v in n3]
    ax3 = fig.add_subplot(gs[2, 0])
    draw_panel(
        ax3, x,
        lagrange_basis_at(x, CUBIC_NODES),
        CUBIC_NODES,
        r"Order 3 — 4 GLL nodes",
        [r"$\phi_0$", r"$\phi_1$", r"$\phi_2$", r"$\phi_3$"],
    )

    out = "legendre.pdf"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"Figure saved → {out}")
    plt.show()


if __name__ == "__main__":
    main()
