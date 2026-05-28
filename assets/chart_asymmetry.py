"""Slide 5 chart — Africa's share of population vs share of cumulative emissions.

Action title (on slide): "Africa hosts 17% of the world's people, caused under
3% of cumulative emissions — and is being asked to skip the energy ladder every
wealthy country climbed."

Sources:
- Population: UN World Population Prospects (~17% of global population, 2024)
- Cumulative CO2 emissions since 1750: Our World in Data / Energy for Growth Hub
  Africa <3%; Sub-Saharan Africa ~0.55%
  https://energyforgrowth.org/article/sub-saharan-africa-emits-a-tiny-fraction-of-the-worlds-co2/
"""
import matplotlib.pyplot as plt
from palette import ACCENT, GREY_CTX, TEXT, TEXT_MUTED, apply_style

apply_style(plt)

labels = ["Share of global\npopulation", "Share of cumulative\nCO₂ emissions"]
values = [17, 3]
colors = [GREY_CTX, ACCENT]

fig, ax = plt.subplots(figsize=(8, 4.5))
bars = ax.bar(labels, values, color=colors, width=0.55)
ax.set_ylim(0, 22)
ax.set_yticks([])
ax.tick_params(axis="x", length=0, labelsize=12)
for spine in ax.spines.values():
    spine.set_visible(False)

for bar, v in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, v + 0.6,
            f"{v}%", ha="center", va="bottom",
            color=TEXT, fontsize=18, fontweight="bold")

ax.text(0.5, -0.18,
        "Africa, % of global total  •  Sources: UN WPP, Our World in Data",
        ha="center", transform=ax.transAxes,
        color=TEXT_MUTED, fontsize=9)

plt.savefig("africa_asymmetry.png")
print("wrote africa_asymmetry.png")
