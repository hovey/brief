"""This module demonstrates Bezier polynomials, which are used in isogeometric analysis (IGA) interpolation and approximation of functions."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ── Colour palette & Styling (Matching lagrange.py) ─────────────────────────
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

# ── Basis functions (Bernstein mapped to [-1, 1]) ──────────────────────────


def bernstein_linear(x):
    t = (x + 1) / 2
    return [1 - t, t]


def bernstein_quadratic(x):
    t = (x + 1) / 2
    return [(1 - t) ** 2, 2 * t * (1 - t), t**2]


def bernstein_cubic(x):
    t = (x + 1) / 2
    return [(1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t**2 * (1 - t), t**3]


# ── Control Point Mappings (xi = -1 + 2*(i/n)) ────────────────────────────


def get_control_points(degree):
    """Returns the x-coordinates of the control points mapped to [-1, 1]."""
    return np.linspace(-1, 1, degree + 1)


# ── Helper: draw one panel with Control Points ──────────────────────────────


def draw_bezier_panel(ax, x, basis_fns, title, labels):
    ax.set_facecolor(PANEL_BG)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#AAAAAA")

    ax.axhline(0, color=GRID_COLOR, linewidth=0.8, zorder=0)
    ax.axhline(1, color=GRID_COLOR, linewidth=0.8, linestyle="--", zorder=0)

    degree = len(basis_fns) - 1
    control_points_x = get_control_points(degree)

    # Plot Control Polygon (dashed line connecting (CPi, 1))
    # This visualizes the influence "pull"
    polygon_y = np.ones_like(control_points_x)
    ax.plot(control_points_x, polygon_y, color="#999999", linestyle="--", linewidth=1.0, zorder=1)

    for i, (B, label, color) in enumerate(zip(basis_fns, labels, COLORS)):
        # Plot the basis function curve
        ax.plot(x, B, color=color, linewidth=2.4, label=label, zorder=3)

        # Draw vertical line from peak of function to x-axis
        peak_idx = np.argmax(B)
        peak_x = x[peak_idx]
        ax.axvline(peak_x, color=color, linestyle=":", linewidth=0.8, alpha=0.6, zorder=2)

        # Plot Control Points (filled circles at y=1)
        # Note: B_i,n is NOT equal to 1 at its control point (except endpoints)
        ax.scatter(
            [control_points_x[i]],
            [1],
            color=color,
            s=70,
            zorder=5,
            edgecolors="white",
            linewidths=1.0,
        )

        # Plot markers on the curve corresponding to control point x-locations
        cp_x = control_points_x[i]
        # Find index in x array closest to cp_x
        cp_idx = (np.abs(x - cp_x)).argmin()
        ax.scatter(
            [cp_x],
            [B[cp_idx]],
            color=color,
            marker="o",
            s=30,
            zorder=4,
            edgecolors="white",
            linewidths=0.5,
            alpha=0.8,
        )

    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-0.1, 1.25)  # Slightly higher y to show CP markers clearly
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

    # Tick marks showing control point locations
    ax.set_xticks(control_points_x)
    if degree == 3:
        ax.set_xticklabels([r"$-1$", r"$-\frac{1}{3}$", r"$\frac{1}{3}$", r"$1$"], fontsize=9)
    else:
        ax.set_xticklabels(
            [str(int(n)) if n == int(n) else str(round(n, 3)) for n in control_points_x], fontsize=9
        )


def main():
    x = np.linspace(-1, 1, 500)
    fig = plt.figure(figsize=(5.5, 10), facecolor=BG_COLOR)
    fig.suptitle(
        "Bezier (Bernstein) Basis Functions\nshowing Control Points ($CP_i$) mapped to $[-1, 1]$",
        fontsize=14,
        fontweight="bold",
        y=0.99,
    )

    gs = gridspec.GridSpec(
        3, 1, figure=fig, top=0.93, bottom=0.1, left=0.13, right=0.97, hspace=0.65
    )

    ax1 = fig.add_subplot(gs[0, 0])
    draw_bezier_panel(
        ax1, x, bernstein_linear(x), "Linear Bezier (2 CPs)", [r"$B_{0,1}$", r"$B_{1,1}$"]
    )

    ax2 = fig.add_subplot(gs[1, 0])
    draw_bezier_panel(
        ax2,
        x,
        bernstein_quadratic(x),
        "Quadratic Bezier (3 CPs)",
        [r"$B_{0,2}$", r"$B_{1,2}$", r"$B_{2,2}$"],
    )

    ax3 = fig.add_subplot(gs[2, 0])
    draw_bezier_panel(
        ax3,
        x,
        bernstein_cubic(x),
        "Cubic Bezier (4 CPs)",
        [r"$B_{0,3}$", r"$B_{1,3}$", r"$B_{2,3}$", r"$B_{3,3}$"],
    )

    out = "bezier.pdf"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"Figure saved → {out}")
    plt.show()


if __name__ == "__main__":
    main()
