"""Slide 6 chart — Zambia's electricity mix is dominated by hydropower.

Action title (on slide): "Zambia bet 85% of its grid on 'clean' hydropower —
and a climate-driven drought left us in the dark for 21 hours a day."

Source: Global Legal Insights, Energy Laws and Regulations 2025 (Zambia).
Total installed capacity ~3,986 MW; ~85% hydropower.
Load shedding figure: Pulitzer Center reporting on 2024 drought.
"""
import matplotlib.pyplot as plt
from palette import ACCENT, GREY_CTX, TEXT, TEXT_MUTED, apply_style

apply_style(plt)

fig, ax = plt.subplots(figsize=(9, 5))

# Single stacked column on the LEFT half of the chart.
bar_x = 0.25
bar_w = 0.18
ax.bar(bar_x, 85, bottom=0, width=bar_w, color=ACCENT)
ax.bar(bar_x, 15, bottom=85, width=bar_w, color=GREY_CTX)

# In-bar labels.
ax.text(bar_x, 42.5, "Hydropower\n85%",
        ha="center", va="center", color="white",
        fontsize=14, fontweight="bold")
ax.text(bar_x, 92.5, "Other  15%",
        ha="center", va="center", color=TEXT,
        fontsize=11)

# Callout annotation on the RIGHT half pointing at the hydropower bar.
ax.annotate(
    "2024 drought collapsed reservoirs.\n"
    "ZESCO load shedding reached\n"
    "up to 21 hours per day.",
    xy=(bar_x + bar_w / 2, 55),
    xytext=(0.62, 55),
    fontsize=12, color=TEXT, ha="left", va="center",
    arrowprops=dict(arrowstyle="-", color=TEXT_MUTED, lw=1.2),
)

# Axes cleanup.
ax.set_xlim(0, 1)
ax.set_ylim(0, 105)
ax.set_xticks([bar_x])
ax.set_xticklabels(["Zambia installed\ngeneration capacity"], fontsize=12)
ax.set_yticks([])
ax.tick_params(axis="x", length=0, pad=10)
for spine in ax.spines.values():
    spine.set_visible(False)

fig.text(0.5, 0.02,
         "Share of installed capacity, %  •  Sources: Global Legal Insights 2025; Pulitzer Center",
         ha="center", color=TEXT_MUTED, fontsize=9)

plt.subplots_adjust(bottom=0.18)
plt.savefig("zambia_mix.png")
print("wrote zambia_mix.png")
