"""Slide 5 — Alberta Jan 2024 cold snap: capacity =/= reliability when it's coldest.

A two-bar comparison: Alberta's installed wind+solar capacity (6,131 MW)
versus what it delivered at the Jan 13, 2024 evening demand peak — when
solar had set and wind was calm, and the grid fell to 10 MW of reserves.

Blue  = capacity that exists on paper (the "path forward" we're told to trust).
Amber = what actually showed up when survival was on the line (the stakes).

Sources: AESO / Alberta MSA "January and April 2024 Event Report";
CBC News (record demand 12,384 MW; reserves to 10 MW).
"""
import matplotlib.pyplot as plt
from palette import AMBER, BLUE, TEXT, TEXT_MUTED, apply_style

apply_style(plt)

fig, ax = plt.subplots(figsize=(10, 5.2))

labels = ["Installed\nwind + solar", "Delivered at the\ncold-snap peak"]
y = [1, 0]
installed = 6131
delivered_visual = 110   # drawn as a sliver only; labelled "almost nothing" (no number implied)

ax.barh(y[0], installed, height=0.52, color=BLUE)
ax.barh(y[1], delivered_visual, height=0.52, color=AMBER)

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=13, color=TEXT)
ax.set_xticks([])
ax.set_xlim(0, 7400)
ax.set_ylim(-1.35, 1.7)

# value labels at the bar ends
ax.text(installed + 130, y[0], "6,131 MW", va="center", ha="left",
        fontsize=17, fontweight="bold", color=BLUE)
ax.text(delivered_visual + 130, y[1], "almost nothing", va="center", ha="left",
        fontsize=17, fontweight="bold", color=AMBER)

ax.set_title("Alberta had 6,131 MW of wind & solar — and at the\n"
             "January 2024 cold-snap peak, it delivered almost none",
             fontsize=15)

# Context line below the chart
ax.text(0, -1.05,
        "Jan 13, 2024:  -40 deg cold,  record demand 12,384 MW,  grid reserves down to 10 MW.\n"
        "Solar had set and the wind was calm. Gas-fired power carried the province.",
        fontsize=11, color=TEXT_MUTED, ha="left", va="center")

plt.savefig("cold_climate.png")
print("wrote cold_climate.png")
