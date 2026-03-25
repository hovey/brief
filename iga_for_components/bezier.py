"""This module demonstrates Bezier polynomials, which are used in isogeometric analysis (IGA) interpolation and approximation of functions."""

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

# ── Basis functions (Bernstein mapped to [-1, 1]) ──────────────────────────────


def bernstein_linear(x):
    t = (x + 1) / 2
    return [1 - t, t]


def bernstein_quadratic(x):
    t = (x + 1) / 2
    return [(1 - t) ** 2, 2 * t * (1 - t), t**2]


def bernstein_cubic(x):
    t = (x + 1) / 2
    return [(1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t**2 * (1 - t), t**3]


# ── Helper: draw one panel ────────────────────────────────────────────────────


def draw_bezier_panel(ax, x, basis_fns, title, labels):
    ax.set_facecolor(PANEL_BG)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#AAAAAA")

    ax.axhline(0, color=GRID_COLOR, linewidth=0.8, zorder=0)
    ax.axhline(1, color=GRID_COLOR, linewidth=0.8, linestyle="--", zorder=0)

    for i, (B, label, color) in enumerate(zip(basis_fns, labels, COLORS)):
        ax.plot(x, B, color=color, linewidth=2.4, label=label, zorder=3)

    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-0.1, 1.1)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$B_{i,n}(x)$", fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
    ax.legend(
        fontsize=9.5,
        framealpha=0.9,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=len(basis_fns),
    )
    ax.set_xticks([-1, 0, 1])


def main():
    x = np.linspace(-1, 1, 500)
    fig = plt.figure(figsize=(5.5, 10), facecolor=BG_COLOR)
    fig.suptitle(
        "Bezier (Bernstein) Basis Functions\non the Reference Element $[-1, 1]$",
        fontsize=15,
        fontweight="bold",
        y=1,
    )

    gs = gridspec.GridSpec(
        3, 1, figure=fig, top=0.93, bottom=0.1, left=0.13, right=0.97, hspace=0.65
    )

    ax1 = fig.add_subplot(gs[0, 0])
    draw_bezier_panel(ax1, x, bernstein_linear(x), "Linear Bezier", [r"$B_{0,1}$", r"$B_{1,1}$"])

    ax2 = fig.add_subplot(gs[1, 0])
    draw_bezier_panel(
        ax2,
        x,
        bernstein_quadratic(x),
        "Quadratic Bezier",
        [r"$B_{0,2}$", r"$B_{1,2}$", r"$B_{2,2}$"],
    )

    ax3 = fig.add_subplot(gs[2, 0])
    draw_bezier_panel(
        ax3,
        x,
        bernstein_cubic(x),
        "Cubic Bezier",
        [r"$B_{0,3}$", r"$B_{1,3}$", r"$B_{2,3}$", r"$B_{3,3}$"],
    )

    out = "bezier.pdf"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"Figure saved → {out}")
    plt.show()


if __name__ == "__main__":
    main()
