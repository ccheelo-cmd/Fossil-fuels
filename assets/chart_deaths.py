"""Slide 4 chart — annual deaths from cooking-smoke vs context.

Action title (lives on the slide, not the chart): "Cooking smoke from biomass
kills ~3.2 million people every year — most in homes without clean fuel."

Sources:
- Household air pollution: WHO Fact Sheet, ~3.2M/year
  https://www.who.int/news-room/fact-sheets/detail/household-air-pollution-and-health
- Ambient (outdoor) air pollution: WHO, ~4.2M/year
- Malaria deaths: WHO World Malaria Report, ~600k/year (context for scale)
"""
import matplotlib.pyplot as plt
from palette import ACCENT, GREY_CTX, TEXT, TEXT_MUTED, apply_style

apply_style(plt)

labels = [
    "Outdoor air pollution",
    "Household air pollution\n(cooking smoke)",
    "Malaria",
]
values = [4.2, 3.2, 0.6]               # millions/year
colors = [GREY_CTX, ACCENT, GREY_CTX]

fig, ax = plt.subplots(figsize=(9, 4.5))
bars = ax.barh(labels, values, color=colors, height=0.55)
ax.invert_yaxis()
ax.set_xlim(0, 5)
ax.set_xticks([])
ax.tick_params(axis="y", length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

for bar, v in zip(bars, values):
    ax.text(v + 0.08, bar.get_y() + bar.get_height() / 2,
            f"{v:.1f}M", va="center", ha="left",
            color=TEXT, fontsize=12, fontweight="bold")

ax.text(0, -1.05, "Annual global deaths, millions  •  Sources: WHO",
        transform=ax.get_yaxis_transform(),
        color=TEXT_MUTED, fontsize=9)

plt.savefig("deaths_per_year.png")
print("wrote deaths_per_year.png")
