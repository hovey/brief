"""This module demonstrates Lagrange polynomials, which are used in finite element analysis (FEA) for interpolation and approximation of functions. The Lagrange polynomials are defined based on a set of distinct points, and they form a basis for polynomial interpolation."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

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
NODE_COLOR = "#59A14F"
GRID_COLOR = "#CCCCCC"
BG_COLOR = "#F8F9FA"
PANEL_BG = "#FFFFFF"

# ── Basis functions ───────────────────────────────────────────────────────────


def linear_basis(x):
    """2-node linear element on [-1, 1]."""
    L0 = (1 - x) / 2
    L1 = (1 + x) / 2
    return [L0, L1]


def quadratic_basis(x):
    """3-node quadratic element on [-1, 1]."""
    L0 = (x**2 - x) / 2
    L1 = 1 - x**2
    L2 = (x**2 + x) / 2
    return [L0, L1, L2]


def cubic_basis(x):
    """4-node cubic element on [-1, -1/3, 1/3, 1]."""
    L0 = -(9 / 16) * (x**3 - x**2 - x / 9 + 1 / 9)
    L1 = (27 / 16) * (x**3 - x**2 / 3 - x + 1 / 3)
    L2 = -(27 / 16) * (x**3 + x**2 / 3 - x - 1 / 3)
    L3 = (9 / 16) * (x**3 + x**2 - x / 9 - 1 / 9)
    return [L0, L1, L2, L3]


# ── Node positions ────────────────────────────────────────────────────────────
LINEAR_NODES = np.array([-1, 1])
QUADRATIC_NODES = np.array([-1, 0, 1])
CUBIC_NODES = np.array([-1, -1 / 3, 1 / 3, 1])

# ── Helper: draw one panel ────────────────────────────────────────────────────


def draw_panel(ax, x, basis_fns, nodes, title, labels):
    """Plot all basis functions for one element type."""
    ax.set_facecolor(PANEL_BG)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#AAAAAA")

    # Light reference lines
    ax.axhline(0, color=GRID_COLOR, linewidth=0.8, zorder=0)
    ax.axhline(1, color=GRID_COLOR, linewidth=0.8, linestyle="--", zorder=0)
    for xn in nodes:
        ax.axvline(xn, color=GRID_COLOR, linewidth=0.6, linestyle=":", zorder=0)

    # Plot each basis function
    for i, (L, label, color) in enumerate(zip(basis_fns, labels, COLORS)):
        ax.plot(x, L, color=color, linewidth=2.4, label=label, zorder=3)

    # Mark nodes: each basis function equals 1 at its own node, 0 at others
    for i, (xn, color) in enumerate(zip(nodes, COLORS)):
        # value of each basis fn at its own node is 1
        ax.scatter([xn], [1], color=color, s=80, zorder=5, edgecolors="white", linewidths=1.2)
        # zeros at other nodes
        for j, xm in enumerate(nodes):
            if j != i:
                ax.scatter(
                    [xm],
                    [0],
                    color=color,
                    s=50,
                    zorder=5,
                    edgecolors="white",
                    linewidths=1.0,
                    marker="o",
                    alpha=0.7,
                )

    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-0.55, 1.25)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$L_i(x)$", fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
    ax.legend(
        fontsize=9.5,
        framealpha=0.9,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.25),
        ncol=len(nodes),
    )
    ax.tick_params(labelsize=9)

    # Annotate node positions on x-axis
    ax.set_xticks(nodes)
    if len(nodes) == 4:
        ax.set_xticklabels([r"$-1$", r"$-\frac{1}{3}$", r"$\frac{1}{3}$", r"$1$"], fontsize=9)
    else:
        ax.set_xticklabels(
            [str(int(n)) if n == int(n) else str(round(n, 3)) for n in nodes], fontsize=9
        )


# ── Main ──────────────────────────────────────────────────────────────────────


def main():
    """The main entry point."""
    x = np.linspace(-1, 1, 500)

    # ── Figure layout ─────────────────────────────────────────────────────────
    fig = plt.figure(figsize=(5.5, 10), facecolor=BG_COLOR)
    fig.suptitle(
        "Lagrange Interpolation Basis Functions\non the Reference Element $[-1,\\ 1]$",
        fontsize=15,
        fontweight="bold",
        y=1,
    )

    gs = gridspec.GridSpec(
        3, 1, figure=fig, top=0.93, bottom=0.1, left=0.13, right=0.97, hspace=0.65
    )

    # ── Panel 1 – Linear ──────────────────────────────────────────────────────
    ax1 = fig.add_subplot(gs[0, 0])
    draw_panel(
        ax1,
        x,
        linear_basis(x),
        LINEAR_NODES,
        "Linear Element (2 nodes)",
        [r"$L_0$", r"$L_1$"],
    )

    # ── Panel 2 – Quadratic ───────────────────────────────────────────────────
    ax2 = fig.add_subplot(gs[1, 0])
    draw_panel(
        ax2,
        x,
        quadratic_basis(x),
        QUADRATIC_NODES,
        "Quadratic Element (3 nodes)",
        [r"$L_0$", r"$L_1$", r"$L_2$"],
    )

    # ── Panel 3 – Cubic ───────────────────────────────────────────────────────
    ax3 = fig.add_subplot(gs[2, 0])
    draw_panel(
        ax3,
        x,
        cubic_basis(x),
        CUBIC_NODES,
        r"Cubic Element (4 nodes)",
        [r"$L_0$", r"$L_1$", r"$L_2$", r"$L_3$"],
    )

    # ── Save ──────────────────────────────────────────────────────────────────
    # out = "lagrange.png"
    out = "lagrange.pdf"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"Figure saved → {out}")
    plt.show()


if __name__ == "__main__":
    main()
