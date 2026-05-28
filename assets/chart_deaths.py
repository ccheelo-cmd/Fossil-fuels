"""Slide 4 — deaths waffle (isotype).

Each dot = 100,000 deaths per year. 32 amber dots = 3.2M from household air
pollution. 42 grey dots = 4.2M from outdoor air pollution (context).
6 small dots = 600k malaria deaths.

The visual point: cooking smoke is on the same order as the things we DO
talk about, but it gets none of the attention.

Sources: WHO Household Air Pollution; WHO Ambient Air Pollution; WHO Malaria.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from palette import AMBER, GREY_CTX, GREY_SOFT, TEXT, TEXT_MUTED, apply_style

apply_style(plt)


def draw_dot_row(ax, x0, y, n, color, dot_r=0.18, gap=0.50):
    """Draw n dots from (x0, y) to the right."""
    for i in range(n):
        cx = x0 + i * gap
        ax.add_patch(patches.Circle((cx, y), dot_r, color=color, zorder=3))


fig, ax = plt.subplots(figsize=(11, 5.2))
ax.set_xlim(0, 22)
ax.set_ylim(-0.5, 5.5)
ax.set_aspect("equal")
ax.axis("off")

# Row 1: outdoor air pollution (4.2M = 42 dots), grey
ax.text(0, 4.6, "Outdoor air pollution",
        fontsize=12, color=TEXT_MUTED, ha="left", va="bottom")
ax.text(22, 4.6, "4.2M",
        fontsize=14, color=TEXT, ha="right", va="bottom", fontweight="bold")
draw_dot_row(ax, 0.3, 4.1, 42, GREY_CTX)

# Row 2: household air pollution (3.2M = 32 dots), AMBER — the point
ax.text(0, 2.6, "Household air pollution  (cooking smoke)",
        fontsize=12, color=TEXT, ha="left", va="bottom", fontweight="bold")
ax.text(22, 2.6, "3.2M",
        fontsize=14, color=AMBER, ha="right", va="bottom", fontweight="bold")
draw_dot_row(ax, 0.3, 2.1, 32, AMBER)

# Row 3: malaria (0.6M = 6 dots), grey-soft
ax.text(0, 0.6, "Malaria",
        fontsize=12, color=TEXT_MUTED, ha="left", va="bottom")
ax.text(22, 0.6, "0.6M",
        fontsize=14, color=TEXT, ha="right", va="bottom", fontweight="bold")
draw_dot_row(ax, 0.3, 0.1, 6, GREY_SOFT)

# Legend
ax.text(0, -0.4, "Each dot = 100,000 lives per year",
        fontsize=10, color=TEXT_MUTED, style="italic")

plt.savefig("deaths_per_year.png")
print("wrote deaths_per_year.png")
