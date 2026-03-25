"""This module demonstrates Legendre polynomials, which are used in finite element analysis (FEA) for interpolation and approximation of functions."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ── Colour palette & Styling ──────────────────────────────────────────────────
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

# ── Basis functions ───────────────────────────────────────────────────────────


def linear_basis(x):
    return [(1 - x) / 2, (1 + x) / 2]


def quadratic_basis(x):
    return [(x**2 - x) / 2, 1 - x**2, (x**2 + x) / 2]


def cubic_gll_basis(x):
    xi = np.sqrt(0.2)  # GLL internal nodes for N=3
    L0 = (x + xi) * (x - xi) * (x - 1) / ((-1 + xi) * (-1 - xi) * (-1 - 1))
    L1 = (x + 1) * (x - xi) * (x - 1) / ((-xi + 1) * (-xi - xi) * (-xi - 1))
    L2 = (x + 1) * (x + xi) * (x - 1) / ((xi + 1) * (xi + xi) * (xi - 1))
    L3 = (x + 1) * (x + xi) * (x - xi) / ((1 + 1) * (1 + xi) * (1 - xi))
    return [L0, L1, L2, L3]


# ── Node positions ────────────────────────────────────────────────────────────
LINEAR_NODES = np.array([-1, 1])
QUADRATIC_NODES = np.array([-1, 0, 1])
CUBIC_NODES = np.array([-1, -1 * np.sqrt(0.2), np.sqrt(0.2), 1])


def draw_panel(ax, x, basis_fns, nodes, title, labels):
    ax.set_facecolor(PANEL_BG)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#AAAAAA")

    ax.axhline(0, color=GRID_COLOR, linewidth=0.8, zorder=0)
    ax.axhline(1, color=GRID_COLOR, linewidth=0.8, linestyle="--", zorder=0)
    for xn in nodes:
        ax.axvline(xn, color=GRID_COLOR, linewidth=0.6, linestyle=":", zorder=0)

    for i, (L, label, color) in enumerate(zip(basis_fns, labels, COLORS)):
        ax.plot(x, L, color=color, linewidth=2.4, label=label, zorder=3)

    for i, (xn, color) in enumerate(zip(nodes, COLORS)):
        ax.scatter([xn], [1], color=color, s=80, zorder=5, edgecolors="white", linewidths=1.2)
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
        bbox_to_anchor=(0.5, -0.15),
        ncol=len(nodes),
    )

    ax.set_xticks(nodes)
    if len(nodes) == 4:
        ax.set_xticklabels([r"$-1$", r"$-\sqrt{1/5}$", r"$\sqrt{1/5}$", r"$1$"], fontsize=9)
    else:
        ax.set_xticklabels(
            [str(int(n)) if n == int(n) else str(round(n, 3)) for n in nodes], fontsize=9
        )


def main():
    x = np.linspace(-1, 1, 500)
    fig = plt.figure(figsize=(5.5, 10), facecolor=BG_COLOR)
    fig.suptitle(
        "Legendre (GLL) Interpolation Basis Functions\non the Reference Element $[-1, 1]$",
        fontsize=15,
        fontweight="bold",
        y=1,
    )

    gs = gridspec.GridSpec(
        3, 1, figure=fig, top=0.93, bottom=0.1, left=0.13, right=0.97, hspace=0.65
    )

    ax1 = fig.add_subplot(gs[0, 0])
    draw_panel(ax1, x, linear_basis(x), LINEAR_NODES, "Linear GLL (2 nodes)", [r"$L_0$", r"$L_1$"])

    ax2 = fig.add_subplot(gs[1, 0])
    draw_panel(
        ax2,
        x,
        quadratic_basis(x),
        QUADRATIC_NODES,
        "Quadratic GLL (3 nodes)",
        [r"$L_0$", r"$L_1$", r"$L_2$"],
    )

    ax3 = fig.add_subplot(gs[2, 0])
    draw_panel(
        ax3,
        x,
        cubic_gll_basis(x),
        CUBIC_NODES,
        "Cubic GLL (4 nodes)",
        [r"$L_0$", r"$L_1$", r"$L_2$", r"$L_3$"],
    )

    out = "legendre.pdf"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"Figure saved → {out}")
    plt.show()


if __name__ == "__main__":
    main()
