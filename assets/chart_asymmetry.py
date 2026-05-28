"""Slide 5 — two-row isotype showing 17% vs 3%.

Row 1: 100 person icons. 17 amber (Africa population).
Row 2: 100 person icons. 3 amber (Africa cumulative CO2 emissions).

The visual shock: the amber stripe is dramatically shorter in row 2.

Sources: UN World Population Prospects; Our World in Data / Energy for Growth Hub.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from palette import AMBER, GREY_SOFT, TEXT, TEXT_MUTED, apply_style

apply_style(plt)


def person(ax, cx, cy, color, h=0.7):
    """A tiny stylised person icon: circle head + tapered body."""
    # head
    ax.add_patch(patches.Circle((cx, cy + h * 0.32), h * 0.13,
                                color=color, zorder=3))
    # body — slim trapezoid
    body = patches.FancyBboxPatch(
        (cx - h * 0.16, cy - h * 0.30), h * 0.32, h * 0.55,
        boxstyle="round,pad=0,rounding_size=0.06",
        linewidth=0, facecolor=color, zorder=3,
    )
    ax.add_patch(body)


def draw_row(ax, y, n_total, n_highlight, gap=0.42):
    for i in range(n_total):
        cx = 0.4 + i * gap
        color = AMBER if i < n_highlight else GREY_SOFT
        person(ax, cx, y, color)


fig, ax = plt.subplots(figsize=(13, 5.8))
ax.set_xlim(-0.5, 43)
ax.set_ylim(-1.8, 6)
ax.set_aspect("equal")
ax.axis("off")

# Row 1 — population (17 of 100 amber)
ax.text(-0.5, 4.3, "Share of global population",
        fontsize=13, color=TEXT, fontweight="bold", ha="left")
ax.text(43, 4.3, "17%",
        fontsize=22, color=AMBER, fontweight="bold", ha="right")
draw_row(ax, 3.3, 100, 17)

# Row 2 — cumulative CO2 emissions (3 of 100 amber)
ax.text(-0.5, 1.6, "Share of cumulative CO₂ emissions",
        fontsize=13, color=TEXT, fontweight="bold", ha="left")
ax.text(43, 1.6, "<3%",
        fontsize=22, color=AMBER, fontweight="bold", ha="right")
draw_row(ax, 0.6, 100, 3)

ax.text(-0.5, -1.4, "Each figure represents 1% of the global total.  "
                    "Africa, all data.",
        fontsize=10, color=TEXT_MUTED, style="italic")

plt.savefig("africa_asymmetry.png")
print("wrote africa_asymmetry.png")
