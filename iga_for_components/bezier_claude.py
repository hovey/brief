"""This module demonstrates Bernstein–Bézier basis functions (Bernstein polynomials),
which form the mathematical foundation of Bézier curves and are also used in isogeometric
analysis (IGA) and p-FEM. For degree n, the n+1 Bernstein basis polynomials are defined as

    B_{i,n}(t) = C(n,i) * t^i * (1-t)^{n-i},   t ∈ [0, 1]

They are non-negative, sum to 1 (partition of unity), and each attains its maximum at
t = i/n. The domain is mapped to [-1, 1] for visual consistency with lagrange.py."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from math import comb

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
BG_COLOR   = "#F8F9FA"
PANEL_BG   = "#FFFFFF"


# ── Bernstein basis ───────────────────────────────────────────────────────────


def bernstein(t, n):
    """Return the n+1 Bernstein basis polynomials of degree n evaluated at t ∈ [0,1].

    B_{i,n}(t) = C(n,i) · t^i · (1-t)^{n-i}
    """
    return [comb(n, i) * t**i * (1 - t) ** (n - i) for i in range(n + 1)]


def t_of_x(x):
    """Map reference coordinate x ∈ [-1, 1]  →  t ∈ [0, 1]."""
    return (x + 1) / 2


# ── Control-point abscissae (uniformly spaced in [-1,1]) ─────────────────────
#    The i-th basis function peaks at t = i/n, i.e. x = 2i/n - 1.
def control_points(n):
    return np.array([2 * i / n - 1 for i in range(n + 1)])


# ── Helper: draw one panel ────────────────────────────────────────────────────


def draw_panel(ax, x, basis_fns, nodes, title, labels, peak_x):
    """Plot all Bernstein basis functions for one degree."""
    ax.set_facecolor(PANEL_BG)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#AAAAAA")

    ax.axhline(0, color=GRID_COLOR, linewidth=0.8, zorder=0)
    ax.axhline(1, color=GRID_COLOR, linewidth=0.8, linestyle="--", zorder=0)
    # Vertical guides at control-point locations
    for xn in nodes:
        ax.axvline(xn, color=GRID_COLOR, linewidth=0.6, linestyle=":", zorder=0)

    for B, label, color in zip(basis_fns, labels, COLORS):
        ax.plot(x, B, color=color, linewidth=2.4, label=label, zorder=3)

    # Mark the peak of each basis function
    for i, (xp, color, B) in enumerate(zip(peak_x, COLORS, basis_fns)):
        peak_val = B[np.argmin(np.abs(x - xp))]
        ax.scatter([xp], [peak_val], color=color, s=80, zorder=5,
                   edgecolors="white", linewidths=1.2)

    # Mark B_{i,n}(0) and B_{i,n}(1) — endpoints are 0 except for the outermost
    for i, (color, B) in enumerate(zip(COLORS, basis_fns)):
        for xend in [-1.0, 1.0]:
            val = B[0] if xend == -1.0 else B[-1]
            marker = "D" if np.isclose(val, 1.0) else "o"
            ax.scatter([xend], [val], color=color, s=55, zorder=5,
                       edgecolors="white", linewidths=1.0,
                       marker=marker, alpha=0.85)

    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-0.10, 1.25)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$B_{i,n}(x)$", fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
    ax.legend(
        fontsize=9.5,
        framealpha=0.9,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=len(nodes),
    )
    ax.tick_params(labelsize=9)

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
            # Express as simple fraction where possible
            from fractions import Fraction
            frac = Fraction(n).limit_denominator(6)
            if abs(float(frac) - n) < 1e-10:
                if frac.denominator == 1:
                    tick_labels.append(f"${frac.numerator}$")
                else:
                    sign = "-" if frac < 0 else ""
                    tick_labels.append(
                        rf"${sign}\frac{{{abs(frac.numerator)}}}{{{frac.denominator}}}$"
                    )
            else:
                tick_labels.append(f"${n:.3f}$")
    ax.set_xticklabels(tick_labels, fontsize=9)


# ── Main ──────────────────────────────────────────────────────────────────────


def main():
    x = np.linspace(-1, 1, 600)
    t = t_of_x(x)

    fig = plt.figure(figsize=(5.5, 10), facecolor=BG_COLOR)
    fig.suptitle(
        r"Bernstein--Bézier Basis Functions" "\n"
        r"$B_{i,n}(t),\quad t = \tfrac{x+1}{2} \in [0,1]$",
        fontsize=14,
        fontweight="bold",
        y=1.0,
    )

    gs = gridspec.GridSpec(
        3, 1, figure=fig,
        top=0.92, bottom=0.1, left=0.13, right=0.97, hspace=0.65,
    )

    # ── Panel 1 – Degree 1 (linear, 2 functions) ─────────────────────────────
    n1 = 1
    cp1 = control_points(n1)        # [-1, 1]
    b1  = bernstein(t, n1)
    ax1 = fig.add_subplot(gs[0, 0])
    draw_panel(
        ax1, x, b1, cp1,
        r"Degree $n=1$ (2 basis functions)",
        [r"$B_{0,1} = 1-t$", r"$B_{1,1} = t$"],
        peak_x=cp1,
    )

    # ── Panel 2 – Degree 2 (quadratic, 3 functions) ──────────────────────────
    n2 = 2
    cp2 = control_points(n2)        # [-1, 0, 1]
    b2  = bernstein(t, n2)
    ax2 = fig.add_subplot(gs[1, 0])
    draw_panel(
        ax2, x, b2, cp2,
        r"Degree $n=2$ (3 basis functions)",
        [r"$B_{0,2}=(1-t)^2$", r"$B_{1,2}=2t(1-t)$", r"$B_{2,2}=t^2$"],
        peak_x=cp2,
    )

    # ── Panel 3 – Degree 3 (cubic, 4 functions) ──────────────────────────────
    n3 = 3
    cp3 = control_points(n3)        # [-1, -1/3, 1/3, 1]
    b3  = bernstein(t, n3)
    ax3 = fig.add_subplot(gs[2, 0])
    draw_panel(
        ax3, x, b3, cp3,
        r"Degree $n=3$ (4 basis functions)",
        [
            r"$B_{0,3}=(1-t)^3$",
            r"$B_{1,3}=3t(1-t)^2$",
            r"$B_{2,3}=3t^2(1-t)$",
            r"$B_{3,3}=t^3$",
        ],
        peak_x=cp3,
    )

    out = "bezier.pdf"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"Figure saved → {out}")
    plt.show()


if __name__ == "__main__":
    main()
