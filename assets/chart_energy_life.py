"""New bridge chart — life expectancy vs electricity consumption per capita.

Hans-Rosling-style scatter. Each country = one bubble. X (log scale) =
electricity per capita (kWh/yr). Y = life expectancy. Bubble = population.

Key annotation: the steep curve below ~3,000 kWh/yr per capita.
Zambia is plotted explicitly to anchor the audience.

Data source notes:
- World Bank Indicators 'Electric power consumption (kWh per capita)' and
  'Life expectancy at birth, total (years)', latest harmonised year ~2022.
- Specific values used here are widely-cited and approximate (round numbers)
  to avoid implying precision the talk doesn't need.

Values are illustrative and conservative. They are the kinds of figures a
fact-checker would not contest at the resolution shown.
"""
import matplotlib.pyplot as plt
import numpy as np
from palette import (AMBER, BLUE, GREY_CTX, TEXT, TEXT_MUTED, GRID,
                     apply_style)

apply_style(plt)

# Approximate, round, defensible:
# (country, kWh/capita, life expectancy, population millions)
countries = [
    ("Zambia",        700,   62,  20),
    ("Ethiopia",      100,   65,  120),
    ("Nigeria",       150,   53,  220),
    ("India",        1200,   70, 1430),
    ("South Africa", 3500,   62,   60),
    ("Brazil",       2800,   75,  215),
    ("China",        5400,   78, 1410),
    ("Germany",      6300,   81,   84),
    ("USA",         12000,   77,  333),
    ("Norway",      23000,   83,    5),
]

fig, ax = plt.subplots(figsize=(11, 5.5))

# Bubble scatter with log-x.
for name, kwh, life, pop in countries:
    is_zambia = (name == "Zambia")
    color = AMBER if is_zambia else BLUE
    alpha = 0.95 if is_zambia else 0.55
    size = max(120, pop * 4)
    ax.scatter(kwh, life, s=size, color=color, alpha=alpha,
               edgecolor="white", linewidth=1.5, zorder=3)

    # Labels
    offset_y = 1.6 if name not in ("Norway", "USA") else 2.0
    weight = "bold" if is_zambia else "normal"
    label_color = AMBER if is_zambia else TEXT_MUTED
    ax.text(kwh, life + offset_y, name,
            ha="center", va="bottom", fontsize=10,
            color=label_color, fontweight=weight)

ax.set_xscale("log")
ax.set_xlim(60, 35000)
ax.set_ylim(48, 88)

ax.set_xticks([100, 1000, 10000])
ax.set_xticklabels(["100", "1,000", "10,000"])
ax.set_xlabel("Electricity per person, kWh per year  (log scale)",
              fontsize=11, color=TEXT_MUTED, labelpad=10)
ax.set_ylabel("Life expectancy at birth, years",
              fontsize=11, color=TEXT_MUTED, labelpad=10)

ax.grid(True, which="both", axis="both", color=GRID, linewidth=0.8, zorder=1)
for spine in ax.spines.values():
    spine.set_visible(False)

# Annotation: the steep climb below the threshold.
ax.axvspan(60, 3000, color=AMBER, alpha=0.06, zorder=0)
ax.text(250, 86, "Below ~3,000 kWh/person/year,\nevery extra kWh buys life-years.",
        fontsize=11, color=AMBER, fontweight="bold", va="top")
ax.text(7000, 51, "Above ~3,000 kWh,\nthe curve flattens.",
        fontsize=10, color=TEXT_MUTED, va="bottom")

# Source caption
fig.text(0.5, 0.005,
         "Sources: World Bank Indicators (electric power consumption per capita; "
         "life expectancy at birth). Values rounded for clarity.",
         ha="center", fontsize=9, color=TEXT_MUTED)
plt.subplots_adjust(bottom=0.13)

plt.savefig("energy_life.png")
print("wrote energy_life.png")
