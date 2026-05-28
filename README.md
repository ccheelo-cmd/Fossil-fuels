# The Case For Fossil Fuels

A 5-minute follow-up presentation by **Choolwe** (Analytics in Training, Lusaka, Zambia).

> Steelman counter-argument to my earlier Power BI report *"How Climate Change Affects the World We Live In."* This deck does **not** deny climate change — it argues that abruptly cutting fossil fuels costs more lives today than climate change will tomorrow, and that the honest path is a **managed transition, not abandonment.**

Two deliverables in [`deliverable/`](deliverable/):

| File | What it is | How to view |
|---|---|---|
| [`case-for-fossil-fuels.pptx`](deliverable/case-for-fossil-fuels.pptx) | The presentation deck | Open in PowerPoint |
| [`case-for-fossil-fuels.html`](deliverable/case-for-fossil-fuels.html) | Interactive web version with Plotly charts | Double-click → opens in any browser. Needs internet (Plotly is loaded from CDN). Arrow keys to navigate, **N** for speaker notes, **F** for fullscreen, **P** to print all slides. |

Everything else in this repo is the working that produced them — preserved on purpose for review.

---

## The Big Idea

> **"Africa caused 3% of climate change but pays the highest price — and pure clean-energy already failed us in last year's drought. The honest path forward is a managed transition, not abandonment."**

Built to *Storytelling with Data* (Cole Nussbaumer Knaflic) standards:
- Single-sentence Big Idea on its own slide
- SCR (Situation → Complication → Resolution) structure
- Action-title sentences on every data slide (the takeaway, not the topic)
- **Two-accent palette** used thematically: blue `#1F4E79` = the *path forward / resolution*; amber `#D97706` = the *cost / stakes*. Colour itself tells the story.
- Isotype / waffle / donut charts instead of plain bars
- No 3D, no gradients, no clip art, no chartjunk
- Speaker notes on every slide, timed to ~4 min 20 sec total
- Citations consolidated on a final **Sources** appendix slide rather than per-slide footers

---

## Repo structure

```
case-for-fossil-fuels/
├── README.md                       ← you are here
├── build_deck.py                   ← reproducible python-pptx build script
│
├── research/
│   └── notes.md                    ← all stats with WHO / IEA / Atlantic Council
│                                     / Energy for Growth Hub / Afrobarometer
│                                     citations + a guardrails section
│
├── drafts/
│   ├── story-spine.md              ← 3 Big Idea options, the chosen blend,
│   │                                 3-minute SCR elevator pitch
│   └── storyboard.md               ← slide-by-slide: action title + visual
│                                     + speaker note + time budget
│
├── assets/
│   ├── palette.py                  ← shared matplotlib palette + style
│   ├── chart_deaths.py             → deaths_per_year.png      (Slide 4)
│   ├── chart_asymmetry.py          → africa_asymmetry.png     (Slide 5)
│   └── chart_zambia.py             → zambia_mix.png           (Slide 6)
│
└── deliverable/
    └── case-for-fossil-fuels.pptx  ← the final 8-slide deck
```

## Slide map (9 slides, ~4 min 20 sec budget)

| # | Purpose | Title (action sentence) | Chart |
|---|---|---|---|
| 1 | Title | The Case For Fossil Fuels — follow-up to "How Climate Change Affects the World We Live In" | — |
| 2 | Big Idea | *(the sentence on its own — Knaflic standard)* | — |
| 3 | Situation | Last week's deck argued: fossil fuels drive climate change → therefore cut them. | — |
| 4 | Complication 1 | Cooking smoke kills ~3.2M people every year — most where there's no clean fuel. | Isotype waffle (each dot = 100k lives) |
| 5 | Complication 2 | Africa = 17% of population, <3% of cumulative emissions — yet asked to skip the ladder. | Two-row isotype (100 person icons per row) |
| 6 | Complication 3 | Zambia bet 85% of its grid on "clean" hydropower — drought left us in the dark 21 hrs/day. | 24-hour blackout donut |
| 7 | Bridge | Below ~3,000 kWh/person/year, every extra kWh buys life-years. Zambia sits on the steep part. | Hans-Rosling-style scatter |
| 8 | Resolution | The honest middle path: gas as bridge → renewables stacked → firm power until storage catches up. | Three-block diagram |
| 9 | Sources | Appendix — every statistic, with its citation. | — |

---

## How to rebuild from source

```bash
pip install python-pptx matplotlib

# regenerate the three charts
cd assets
python chart_deaths.py
python chart_asymmetry.py
python chart_zambia.py
cd ..

# rebuild the pptx
python build_deck.py
# → wrote deliverable/case-for-fossil-fuels.pptx
```

The build is deterministic — same inputs, identical output.

---

## Sources

All statistics cited inside the deck are sourced. Full receipts in [`research/notes.md`](research/notes.md). Summary:

- **Cooking-smoke deaths (~3.2M/yr global, ~815k/yr Africa):** [WHO Household Air Pollution Fact Sheet](https://www.who.int/news-room/fact-sheets/detail/household-air-pollution-and-health); [IEA *Universal Access to Clean Cooking in Africa* (2024)](https://www.iea.org/reports/universal-access-to-clean-cooking-in-africa)
- **Africa electricity access (~600M without, sub-Saharan Africa):** [IEA *Financing Electricity Access in Africa* (2025)](https://www.iea.org/reports/financing-electricity-access-in-africa)
- **Africa's share of cumulative CO₂ emissions (<3%):** [Energy for Growth Hub](https://energyforgrowth.org/article/sub-saharan-africa-emits-a-tiny-fraction-of-the-worlds-co2/) (citing Our World in Data)
- **Zambia generation mix (85% hydropower, ~3,986 MW installed):** [Global Legal Insights, *Energy Laws and Regulations 2025: Zambia*](https://www.globallegalinsights.com/practice-areas/energy-laws-and-regulations/zambia/)
- **Zambia 2024 load shedding (up to 21 hrs/day):** [Pulitzer Center reporting](https://pulitzercenter.org/stories/zambias-power-shortages-worsen-drought-deepens); [Afrobarometer AD1178](https://www.afrobarometer.org/publication/ad1178-amid-electricity-crisis-zambians-favour-ending-state-monopoly-investing-in-solar-and-wind-power/)
- **Natural gas as transition fuel (50–60% less CO₂ than coal):** [Atlantic Council](https://www.atlanticcouncil.org/in-depth-research-reports/report/natural-gas-has-a-small-but-important-role-in-africas-energy-transition/)
- **Materials reality (steel/cement footprint in renewables):** [MIT Climate Portal](https://climate.mit.edu/ask-mit/does-steel-and-concrete-needed-build-renewable-energy-cancel-out-benefits)

---

## What the deck deliberately does NOT argue

- ✗ "Climate change isn't real" — it is, my last deck showed the data, and I stand by it.
- ✗ "Renewables don't work" — they do, and their cost is falling faster than predicted.
- ✗ "Africa should burn more coal" — coal-specific. The case is for **gas as a bridge** + accelerated renewables.
- ✗ Cherry-picked or unsourced stats.

## What the deck DOES argue

- ✅ The cost-benefit picture in my original deck was incomplete — it counted future climate deaths but not present energy-poverty deaths.
- ✅ The most climate-vulnerable countries are also the most energy-poor, and the cheapest fastest fix today still includes fossil fuels (specifically gas).
- ✅ A managed transition — gas as bridge, renewables aggressively scaled, firm power retained — saves more lives, present + future, than abrupt shutdown.
- ✅ Zambia is the worked example: hydropower-only failed in a drought; the answer is *more* energy sources, not fewer.
