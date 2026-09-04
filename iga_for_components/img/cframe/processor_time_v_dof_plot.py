"""Regenerate the processor-time-vs-DOF plot for the C-frame table (Table 3-1).

Processor Time (s) = wall-clock Time (s) * core count (#).
"""
import matplotlib.pyplot as plt

# analysis type -> (list of DOF, list of wall-clock times (s), list of core counts)
series = {
    "IGA": {
        "dof": [3_420, 13_332, 69_426, 383_250],
        "time_s": [15, 37, 209, 1_303],
        "cores": [1, 1, 1, 1],
        "color": "#4E9FDB",
    },
    "SSD tet10": {
        "dof": [13_146, 69_234, 382_791, 4_072_959],
        "time_s": [116, 141, 30, 225],
        "cores": [128, 128, 128, 128],
        "color": "#E08030",
    },
    "SSD hex8": {
        "dof": [23_682, 160_059, 1_167_897],
        "time_s": [6, 20, 75],
        "cores": [12, 128, 128],
        "color": "#4FA84F",
    },
}

fig, ax = plt.subplots(figsize=(9, 6.4), dpi=200)

for label, s in series.items():
    proc_time = [t * c for t, c in zip(s["time_s"], s["cores"])]
    ax.plot(
        s["dof"], proc_time,
        marker="o", markersize=8, linewidth=2.5,
        color=s["color"], label=label,
    )
    for x, y in zip(s["dof"], proc_time):
        ax.annotate(
            f"{y:,}", (x, y),
            textcoords="offset points", xytext=(0, 12),
            ha="center", fontsize=11, color=s["color"], fontweight="bold",
        )

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1_000, 10_000_000)
ax.set_ylim(1, 100_000)
ax.set_xlabel("Degree of Freedom (DOF)", fontsize=13)
ax.set_ylabel("Processor Time (s)\n(= wall-clock time × core count)", fontsize=13)
ax.set_title("Processor Time versus Degree of Freedom", fontsize=16)
ax.grid(True, which="major", linewidth=0.6, color="0.85")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=False, fontsize=12)

fig.tight_layout()
fig.savefig("processor_time_v_dof.png", bbox_inches="tight")
print("wrote processor_time_v_dof.png")
