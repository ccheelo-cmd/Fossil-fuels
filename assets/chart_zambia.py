"""Slide 6 — 24-hour blackout clock for Zambia 2024.

A 24-hour donut. 21 hours dark (amber for "stakes" — blackout).
3 hours of power (blue for "what little path forward we had").
Large central number: 21 / 24.

This is the moment of the deck most likely to land emotionally with a
Zambian audience: they lived it.

Source: ZESCO / Pulitzer Center reporting on the 2024 drought.
Capacity mix annotation: 85% hydropower (Global Legal Insights 2025).
"""
import matplotlib.pyplot as plt
from palette import AMBER, BLUE, TEXT, TEXT_MUTED, GREY_CTX, apply_style

apply_style(plt)

fig, ax = plt.subplots(figsize=(10, 6.2), subplot_kw=dict(aspect="equal"))

dark_hours = 21
light_hours = 3
sizes = [dark_hours, light_hours]
colors = [AMBER, BLUE]
labels = [f"Dark\n{dark_hours} hrs", f"Power\n{light_hours} hrs"]

wedges, _ = ax.pie(
    sizes,
    colors=colors,
    startangle=90,
    counterclock=False,
    wedgeprops=dict(width=0.32, edgecolor="white", linewidth=3),
)

# Center label — the headline
ax.text(0, 0.15, "21",
        fontsize=68, color=AMBER, fontweight="bold",
        ha="center", va="center")
ax.text(0, -0.20, "hours dark, per day",
        fontsize=14, color=TEXT, ha="center", va="center")
ax.text(0, -0.32, "during the 2024 drought",
        fontsize=11, color=TEXT_MUTED, ha="center", va="center")

# Outer ring legends with leader lines
ax.text(1.35, 0.75, "Power\n3 hrs", fontsize=12, color=BLUE,
        fontweight="bold", ha="left", va="center")
ax.text(-1.35, -0.4, "No power\n21 hrs", fontsize=12, color=AMBER,
        fontweight="bold", ha="right", va="center")

# Context: the bet that failed
ax.text(0, -1.45,
        "Zambia's grid is ~85% hydropower.\n"
        "The 2024 drought collapsed reservoir levels.",
        fontsize=11, color=TEXT_MUTED, ha="center", va="center")

plt.savefig("zambia_mix.png")
print("wrote zambia_mix.png")
