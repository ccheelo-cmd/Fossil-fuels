# Storyboard — The Case For Fossil Fuels

**5-minute talk. 8 slides. SCR structure. Accent colour: `#1F4E79` (confident blue). Grey for context.**

Action titles are full sentences (Knaflic's rule — the title is the takeaway, not the topic).

---

## Slide 1 — Title
- **Visual:** Title text, Choolwe's name, AIT, date. No image.
- **Title:** *The Case For Fossil Fuels — a follow-up to "How Climate Change Affects the World We Live In"*
- **Sub:** *Choolwe • Analytics in Training • May 2026*
- **Speaker note (~10 sec):**
  > "Last week I argued we should cut fossil fuels. Today I want to make the most honest counter-argument I can — not because I've changed my mind on climate change, but because the picture I painted was incomplete."

---

## Slide 2 — Big Idea (the Knaflic single-sentence slide)
- **Visual:** The Big Idea on its own, centred, large type, dark grey body, accent-blue emphasis on the words "managed transition" and "abandonment".
- **Title:** *(no title — the sentence IS the slide)*
- **Body:**
  > "Africa caused 3% of climate change but pays the highest price — and pure clean-energy already failed us in last year's drought.
  > **The honest path forward is a managed transition, not abandonment.**"
- **Speaker note (~20 sec):**
  > "This is what I want you to walk out of the room remembering. Let me show you how I got there."

---

## Slide 3 — Situation (what my last deck said)
- **Visual:** Three small grey "thumbnail" boxes summarising my last deck's key claims (CO₂ rising, temperature rising, climate change kills). No chart — minimal text.
- **Action title:** *Last week, the case I made was: fossil fuels drive climate change, climate change kills, therefore cut fossil fuels.*
- **Body bullets (grey, small):**
  - CO₂ at record highs, fossil fuels = ~90% of emissions
  - Temperature, sea-level, disaster frequency all rising
  - Conclusion: reduce emissions, restore forests
- **Speaker note (~30 sec):**
  > "The climate data hasn't moved. That deck was honest about half the story. Today I want to show you the other half."

---

## Slide 4 — Complication 1: The deaths we don't count
- **Visual:** Bar chart. Three horizontal bars, all in grey except the accent-blue "Household air pollution" bar.
  - "Household air pollution (cooking smoke)": **~3.2 million deaths/year (global)**
  - "Outdoor air pollution": ~4.2 million/year (context, grey)
  - "Malaria": ~600 thousand/year (context, grey)
- **Action title:** *Cooking smoke from biomass kills ~3.2 million people every year — most of them in homes that lack access to clean fuel.*
- **Source caption:** WHO Household Air Pollution Fact Sheet
- **Speaker note (~40 sec):**
  > "My last deck counted future deaths from climate change. It did not count the 3.2 million people who die *every year, right now*, from cooking on open fires because they have no clean fuel. In sub-Saharan Africa alone that's 815,000 deaths a year — most of them women and children. Energy poverty has a body count today."

---

## Slide 5 — Complication 2: The justice asymmetry
- **Visual:** Side-by-side bar chart comparing Africa's share of three things:
  - Share of global population: ~17% (grey)
  - Share of cumulative CO₂ emissions: <3% (accent blue, highlighted)
  - Share of climate-vulnerable population: disproportionately high (grey + annotation)
- **Action title:** *Africa hosts 17% of the world's people, caused under 3% of cumulative emissions — and is being asked to skip the energy ladder every wealthy country climbed.*
- **Source caption:** Energy for Growth Hub / Our World in Data
- **Speaker note (~40 sec):**
  > "Look at this asymmetry. Every wealthy country on Earth got rich by burning coal, then oil, then gas. They are now asking the continent that contributed least to the problem to skip that ladder — using clean-energy technology whose *own supply chain* still runs on fossil fuels. That's not a climate plan. That's an injustice with a green sticker on it."

---

## Slide 6 — Complication 3: The Zambia lesson
- **Visual:** Stacked column showing Zambia's installed generation mix — one tall column where 85% is accent-blue (hydropower) and the rest is grey. Annotation: *"21 hours/day of load shedding during 2024 drought."*
- **Action title:** *Zambia bet 85% of its grid on "clean" hydropower — and a climate-driven drought left us in the dark for 21 hours a day.*
- **Source caption:** Global Legal Insights 2025; ZESCO / Pulitzer Center
- **Speaker note (~40 sec):**
  > "We lived this. We did the clean thing — 85% of our installed capacity is hydropower. Then the climate broke our climate solution. ZESCO ran load shedding of up to 21 hours a day. The lesson is NOT 'burn more coal.' The lesson is: firm power matters, and pretending otherwise is paid for in dark hospitals and empty cold-chains."

---

## Slide 7 — Resolution: Managed transition
- **Visual:** Simple three-stack concept graphic — three labelled grey blocks with one (gas) in accent blue:
  - **NOW:** Gas as a bridge (50–60% less CO₂ than coal)
  - **+** Renewables aggressively scaled (solar in Zambia, wind where it works)
  - **THEN:** Firm power retained until storage & grids can carry the load alone
- **Action title:** *The honest middle path is gas as a bridge, renewables stacked on top, and firm power kept until storage can carry the load.*
- **Source caption:** Atlantic Council; IEA
- **Speaker note (~50 sec):**
  > "I'm not arguing fossil fuels forever. I'm arguing for a managed transition. Natural gas as a bridge — emits half what coal does and Africa holds 13% of global reserves. Renewables scaled aggressively on top — solar in Zambia is cheap and getting cheaper. And firm power kept on until storage and grid infrastructure can stand alone. That's how we lift the bottom billion while decarbonising the top."

---

## Slide 8 — Honest close
- **Visual:** Single accent-blue sentence on white, with two small grey "what I'm not saying" tags below.
- **Action title (or really, the closing line):** *Counting only future climate deaths and ignoring 3.2 million present-day energy-poverty deaths is bad arithmetic — and bad ethics.*
- **Body (small grey):**
  - I am NOT saying: climate change isn't real, renewables don't work, or Africa should burn more coal.
  - I AM saying: the honest cost-benefit picture includes the people dying today because they have no power, no gas, no light.
- **Speaker note (~30 sec):**
  > "Two columns in the ledger. My first deck only filled out one of them. The honest case for fossil fuels — really, the honest case for a managed transition — is the column my first deck left blank. Thank you. Questions?"

---

## Time check
- Slide 1: 10 sec
- Slide 2: 20 sec
- Slide 3: 30 sec
- Slide 4: 40 sec
- Slide 5: 40 sec
- Slide 6: 40 sec
- Slide 7: 50 sec
- Slide 8: 30 sec + transition
- **Total: ~4 min 20 sec, leaves ~40 sec slack** for nervous-energy slowdown. Good fit for 5 min.

## Charts to build (Python / matplotlib)
1. `chart_deaths.py` → `deaths_per_year.png` (Slide 4)
2. `chart_asymmetry.py` → `africa_asymmetry.png` (Slide 5)
3. `chart_zambia.py` → `zambia_mix.png` (Slide 6)

Slide 7's three-block graphic will be built natively in python-pptx (shapes), not matplotlib — keeps it crisp.
