"""Build the 'Case For Fossil Fuels' .pptx using python-pptx.

Design constraints (Storytelling with Data, Cole Knaflic):
- Action-title sentences on every data slide (the takeaway, not a label)
- Pre-attentive attributes only: one accent colour (#1F4E79), grey context
- No 3D, no gradients, no clip art, no chartjunk
- Speaker notes on every slide
"""
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# ---- Palette ----
ACCENT     = RGBColor(0x1F, 0x4E, 0x79)
TEXT       = RGBColor(0x1F, 0x29, 0x37)
TEXT_MUTED = RGBColor(0x4B, 0x55, 0x63)
GREY_CTX   = RGBColor(0x9C, 0xA3, 0xAF)
GRID       = RGBColor(0xE5, 0xE7, 0xEB)
BG_WHITE   = RGBColor(0xFF, 0xFF, 0xFF)

# ---- Setup ----
HERE = Path(__file__).parent
ASSETS = HERE / "assets"

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]

# ---- Helpers ----
def add_text(slide, left, top, width, height, text, *,
             size=18, bold=False, color=TEXT, align=PP_ALIGN.LEFT,
             anchor=MSO_ANCHOR.TOP, font="Calibri"):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Emu(0)
    tf.margin_top  = tf.margin_bottom = Emu(0)
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font
    return tb, tf

def add_rect(slide, left, top, width, height, fill=ACCENT, line=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
    shp.shadow.inherit = False
    return shp

def add_accent_bar(slide):
    """Thin accent bar across the top of content slides for visual consistency."""
    add_rect(slide, Inches(0), Inches(0), SW, Inches(0.08), fill=ACCENT)

def add_footer(slide, slide_num, total=8):
    add_text(slide, Inches(0.5), Inches(7.05), Inches(8), Inches(0.3),
             "Choolwe  •  The Case For Fossil Fuels  •  Follow-up to “How Climate Change Affects the World We Live In”",
             size=9, color=GREY_CTX)
    add_text(slide, Inches(12.0), Inches(7.05), Inches(1.0), Inches(0.3),
             f"{slide_num} / {total}",
             size=9, color=GREY_CTX, align=PP_ALIGN.RIGHT)

def set_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text

# ============================================================
# Slide 1 — Title
# ============================================================
s = prs.slides.add_slide(BLANK)

# Big accent block on the left
add_rect(s, Inches(0), Inches(0), Inches(4.2), SH, fill=ACCENT)
add_text(s, Inches(0.5), Inches(3.0), Inches(3.5), Inches(1.0),
         "The Case",
         size=44, bold=True, color=BG_WHITE)
add_text(s, Inches(0.5), Inches(3.7), Inches(3.5), Inches(1.0),
         "For Fossil Fuels",
         size=44, bold=True, color=BG_WHITE)
add_text(s, Inches(0.5), Inches(5.0), Inches(3.5), Inches(0.5),
         "A steelman follow-up",
         size=16, color=BG_WHITE)

# Right side: subtitle + presenter
add_text(s, Inches(5.0), Inches(2.4), Inches(7.5), Inches(0.6),
         "Follow-up to:",
         size=14, color=TEXT_MUTED)
add_text(s, Inches(5.0), Inches(2.8), Inches(7.5), Inches(1.5),
         "“How Climate Change Affects the World We Live In”",
         size=22, color=TEXT)
add_text(s, Inches(5.0), Inches(4.8), Inches(7.5), Inches(0.5),
         "Choolwe", size=20, bold=True, color=TEXT)
add_text(s, Inches(5.0), Inches(5.3), Inches(7.5), Inches(0.4),
         "Analytics in Training  •  May 2026",
         size=13, color=TEXT_MUTED)

set_notes(s,
    "(~10 sec) Last week I argued we should cut fossil fuels. "
    "Today I want to make the most honest counter-argument I can — "
    "not because I've changed my mind on climate change, but because "
    "the picture I painted was incomplete.")

# ============================================================
# Slide 2 — Big Idea (Knaflic single-sentence slide)
# ============================================================
s = prs.slides.add_slide(BLANK)
add_accent_bar(s)

# Two-line Big Idea, centred vertically.
tb = s.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(11.0), Inches(3.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = Emu(0)
tf.vertical_anchor = MSO_ANCHOR.TOP

# Para 1 (setup, grey)
p1 = tf.paragraphs[0]
p1.alignment = PP_ALIGN.LEFT
r = p1.add_run()
r.text = ("Africa caused 3% of climate change but pays the highest price — "
          "and pure clean-energy already failed us in last year's drought.")
r.font.size = Pt(30); r.font.color.rgb = TEXT_MUTED; r.font.name = "Calibri"

# Spacer
p_sp = tf.add_paragraph(); p_sp.space_before = Pt(18)
r = p_sp.add_run(); r.text = " "; r.font.size = Pt(12)

# Para 2 (resolution, accent + bold)
p2 = tf.add_paragraph()
p2.alignment = PP_ALIGN.LEFT
r2 = p2.add_run()
r2.text = "The honest path forward is a managed transition, not abandonment."
r2.font.size = Pt(34); r2.font.bold = True
r2.font.color.rgb = ACCENT; r2.font.name = "Calibri"

# Tiny "Big Idea" tag at top
add_text(s, Inches(1.2), Inches(1.3), Inches(3), Inches(0.4),
         "THE BIG IDEA", size=11, bold=True, color=ACCENT)

add_footer(s, 2)
set_notes(s,
    "(~20 sec) This is what I want you to walk out of the room "
    "remembering. Let me show you how I got there.")

# ============================================================
# Slide 3 — Situation (what my last deck said)
# ============================================================
s = prs.slides.add_slide(BLANK)
add_accent_bar(s)

# Action title
add_text(s, Inches(0.6), Inches(0.4), Inches(12.1), Inches(1.2),
         "Last week, the case I made was: fossil fuels drive climate change, "
         "climate change kills, therefore cut fossil fuels.",
         size=22, bold=True, color=TEXT)

# Three thumbnail boxes summarising the original deck
boxes = [
    ("CO₂ at record highs",
     "Fossil fuels = ~90% of human CO₂ emissions."),
    ("Temperature, sea level,\nand disasters all rising",
     "98% chance one of the next five years\nwill be the warmest on record."),
    ("Original conclusion",
     "Reduce emissions and restore forests."),
]
box_w = Inches(3.85); box_h = Inches(3.0); gap = Inches(0.3)
start_x = Inches(0.6); y = Inches(2.4)

for i, (head, body) in enumerate(boxes):
    x = start_x + (box_w + gap) * i
    add_rect(s, x, y, box_w, box_h, fill=RGBColor(0xF3, 0xF4, 0xF6))
    # Accent strip on the top of each
    add_rect(s, x, y, box_w, Inches(0.08), fill=GREY_CTX)
    add_text(s, x + Inches(0.25), y + Inches(0.3), box_w - Inches(0.5), Inches(1.0),
             head, size=16, bold=True, color=TEXT)
    add_text(s, x + Inches(0.25), y + Inches(1.5), box_w - Inches(0.5), Inches(1.5),
             body, size=12, color=TEXT_MUTED)

add_text(s, Inches(0.6), Inches(5.8), Inches(12), Inches(0.4),
         "I stand by the data. What follows is what that deck didn’t show.",
         size=13, color=TEXT_MUTED)

add_footer(s, 3)
set_notes(s,
    "(~30 sec) The climate data hasn’t moved. CO₂ is rising, "
    "temperatures are rising, disasters are increasing. That deck was "
    "honest about half the story. Today I want to show you the other half.")

# ============================================================
# Slide 4 — Complication 1: deaths we don’t count
# ============================================================
s = prs.slides.add_slide(BLANK)
add_accent_bar(s)

add_text(s, Inches(0.6), Inches(0.4), Inches(12.1), Inches(1.3),
         "Cooking smoke from biomass kills ~3.2 million people every year — "
         "most in homes that lack access to clean fuel.",
         size=22, bold=True, color=TEXT)

# Chart image
s.shapes.add_picture(str(ASSETS / "deaths_per_year.png"),
                     Inches(0.6), Inches(1.9),
                     width=Inches(9.0))

# Side commentary
add_text(s, Inches(10.0), Inches(2.3), Inches(3.0), Inches(0.5),
         "What my first deck\nleft out:",
         size=13, color=TEXT_MUTED)
add_text(s, Inches(10.0), Inches(3.2), Inches(3.0), Inches(2.5),
         "Energy poverty has a body count — today, not tomorrow.\n\n"
         "Of those 3.2M deaths, ~815,000 are in sub-Saharan Africa.",
         size=14, color=TEXT)

add_text(s, Inches(0.6), Inches(6.6), Inches(12), Inches(0.3),
         "Sources: WHO Household Air Pollution Fact Sheet; WHO Ambient Air Pollution; WHO World Malaria Report.",
         size=9, color=GREY_CTX)

add_footer(s, 4)
set_notes(s,
    "(~40 sec) My last deck counted future deaths from climate change. "
    "It did not count the 3.2 million people who die EVERY YEAR right now "
    "from cooking on open fires because they have no clean fuel. "
    "In sub-Saharan Africa alone that’s 815,000 deaths a year — "
    "most of them women and children. Energy poverty has a body count today.")

# ============================================================
# Slide 5 — Complication 2: justice asymmetry
# ============================================================
s = prs.slides.add_slide(BLANK)
add_accent_bar(s)

add_text(s, Inches(0.6), Inches(0.4), Inches(12.1), Inches(1.3),
         "Africa hosts 17% of the world’s people, caused under 3% of cumulative "
         "emissions — and is being asked to skip the ladder every wealthy country climbed.",
         size=20, bold=True, color=TEXT)

s.shapes.add_picture(str(ASSETS / "africa_asymmetry.png"),
                     Inches(0.6), Inches(2.0),
                     width=Inches(7.5))

# Commentary box
add_text(s, Inches(8.6), Inches(2.3), Inches(4.4), Inches(0.5),
         "The asymmetry:",
         size=14, bold=True, color=ACCENT)
add_text(s, Inches(8.6), Inches(2.9), Inches(4.4), Inches(3.5),
         "Every wealthy country got rich by burning coal, then oil, then gas.\n\n"
         "The clean-energy supply chain itself — steel, cement, shipping — "
         "still runs on fossil fuels.\n\n"
         "Asking Africa to skip the ladder, today, means asking it to stay poor.",
         size=13, color=TEXT_MUTED)

add_text(s, Inches(0.6), Inches(6.6), Inches(12), Inches(0.3),
         "Sources: UN World Population Prospects; Our World in Data / Energy for Growth Hub.",
         size=9, color=GREY_CTX)

add_footer(s, 5)
set_notes(s,
    "(~40 sec) Look at this asymmetry. Every wealthy country on Earth got rich "
    "by burning coal, then oil, then gas. They are now asking the continent that "
    "contributed least to the problem to skip that ladder — using clean-energy "
    "technology whose OWN supply chain still runs on fossil fuels. That’s not "
    "a climate plan. That’s an injustice with a green sticker on it.")

# ============================================================
# Slide 6 — Complication 3: Zambia lesson
# ============================================================
s = prs.slides.add_slide(BLANK)
add_accent_bar(s)

add_text(s, Inches(0.6), Inches(0.4), Inches(12.1), Inches(1.3),
         "Zambia bet 85% of its grid on “clean” hydropower — "
         "and a climate-driven drought left us in the dark for 21 hours a day.",
         size=21, bold=True, color=TEXT)

s.shapes.add_picture(str(ASSETS / "zambia_mix.png"),
                     Inches(0.6), Inches(1.9),
                     width=Inches(9.0))

# Commentary
add_text(s, Inches(10.0), Inches(2.3), Inches(3.0), Inches(0.5),
         "The lesson:",
         size=14, bold=True, color=ACCENT)
add_text(s, Inches(10.0), Inches(2.9), Inches(3.0), Inches(3.0),
         "Not “burn more coal.”\n\n"
         "Firm, dispatchable power matters — and pretending otherwise is "
         "paid for in dark hospitals and broken cold-chains.",
         size=13, color=TEXT_MUTED)

add_footer(s, 6)
set_notes(s,
    "(~40 sec) We lived this. We did the ‘clean’ thing — "
    "85% of our installed capacity is hydropower. Then the climate broke "
    "our climate solution. ZESCO ran load shedding of up to 21 hours a day. "
    "The lesson is NOT ‘burn more coal.’ The lesson is: firm power matters, "
    "and pretending otherwise is paid for in dark hospitals and empty cold-chains.")

# ============================================================
# Slide 7 — Resolution: managed transition (native shapes)
# ============================================================
s = prs.slides.add_slide(BLANK)
add_accent_bar(s)

add_text(s, Inches(0.6), Inches(0.4), Inches(12.1), Inches(1.3),
         "The honest middle path: gas as a bridge, renewables stacked on top, "
         "firm power kept until storage can carry the load.",
         size=20, bold=True, color=TEXT)

# Three-block diagram horizontally
block_w = Inches(3.8); block_h = Inches(3.3)
ys = Inches(2.4)
xs = [Inches(0.6), Inches(4.75), Inches(8.9)]
labels = [
    ("NOW — BRIDGE",
     "Natural gas",
     "50–60% less CO₂ than coal.\n\n"
     "Africa holds ~13% of\nproven gas reserves.\n\n"
     "Faster to deploy than\nnuclear, firm in a way solar\nalone is not.",
     ACCENT, BG_WHITE, True),
    ("BUILD-OUT",
     "Renewables, aggressively",
     "Solar in Zambia is already\nthe cheapest new capacity.\n\n"
     "Wind, hydro diversification,\nstorage — scaled in parallel,\nnot waited for.",
     RGBColor(0xE5, 0xE7, 0xEB), TEXT, False),
    ("THEN — RETIRE",
     "Phase fossil fuels down",
     "When grids are firm and\nstorage can carry the load,\nretire gas plants.\n\n"
     "Not before. Not as a slogan.\nAs an engineering schedule.",
     RGBColor(0xE5, 0xE7, 0xEB), TEXT, False),
]

for x, (tag, head, body, fill, fg, accent_block) in zip(xs, labels):
    add_rect(s, x, ys, block_w, block_h, fill=fill)
    add_text(s, x + Inches(0.3), ys + Inches(0.25),
             block_w - Inches(0.6), Inches(0.4),
             tag, size=11, bold=True,
             color=BG_WHITE if accent_block else ACCENT)
    add_text(s, x + Inches(0.3), ys + Inches(0.7),
             block_w - Inches(0.6), Inches(0.7),
             head, size=18, bold=True, color=fg)
    add_text(s, x + Inches(0.3), ys + Inches(1.5),
             block_w - Inches(0.6), block_h - Inches(1.7),
             body, size=12,
             color=BG_WHITE if accent_block else TEXT_MUTED)

# Arrows between blocks
for i in range(2):
    ax = xs[i] + block_w
    arrow = s.shapes.add_shape(
        MSO_SHAPE.RIGHT_ARROW, ax, ys + Inches(1.4),
        Inches(0.35), Inches(0.45))
    arrow.fill.solid(); arrow.fill.fore_color.rgb = GREY_CTX
    arrow.line.fill.background(); arrow.shadow.inherit = False

add_text(s, Inches(0.6), Inches(6.4), Inches(12), Inches(0.3),
         "Sources: Atlantic Council, “Natural gas in Africa’s energy transition”; IEA, “Financing Electricity Access in Africa” (2025).",
         size=9, color=GREY_CTX)

add_footer(s, 7)
set_notes(s,
    "(~50 sec) I’m not arguing fossil fuels forever. I’m arguing for "
    "a MANAGED transition. Natural gas as a bridge — emits half what coal "
    "does and Africa holds 13% of global reserves. Renewables scaled aggressively "
    "on top — solar in Zambia is already the cheapest new capacity. And firm "
    "power kept on until storage and grid infrastructure can stand alone. "
    "That’s how we lift the bottom billion while decarbonising the top.")

# ============================================================
# Slide 8 — Honest close
# ============================================================
s = prs.slides.add_slide(BLANK)
add_accent_bar(s)

# Closing one-sentence claim, large
add_text(s, Inches(0.6), Inches(0.5), Inches(3), Inches(0.4),
         "IN CLOSING", size=11, bold=True, color=ACCENT)

add_text(s, Inches(0.6), Inches(1.4), Inches(12.1), Inches(2.5),
         "Counting only future climate deaths and ignoring 3.2 million present-day "
         "energy-poverty deaths is bad arithmetic — and bad ethics.",
         size=28, bold=True, color=TEXT)

# Two-column "what I am / am not saying"
col_w = Inches(5.9); col_h = Inches(2.3); col_y = Inches(4.2)

# NOT saying
add_rect(s, Inches(0.6), col_y, col_w, col_h, fill=RGBColor(0xF3, 0xF4, 0xF6))
add_text(s, Inches(0.85), col_y + Inches(0.25), col_w - Inches(0.5), Inches(0.5),
         "I am NOT saying:", size=14, bold=True, color=TEXT_MUTED)
add_text(s, Inches(0.85), col_y + Inches(0.8), col_w - Inches(0.5), col_h - Inches(1.0),
         "•  Climate change isn’t real\n"
         "•  Renewables don’t work\n"
         "•  Africa should burn more coal",
         size=14, color=TEXT_MUTED)

# AM saying
add_rect(s, Inches(6.85), col_y, col_w, col_h, fill=ACCENT)
add_text(s, Inches(7.1), col_y + Inches(0.25), col_w - Inches(0.5), Inches(0.5),
         "I AM saying:", size=14, bold=True, color=BG_WHITE)
add_text(s, Inches(7.1), col_y + Inches(0.8), col_w - Inches(0.5), col_h - Inches(1.0),
         "•  The honest cost-benefit picture\n"
         "    includes the people dying today\n"
         "    because they have no power, no\n"
         "    gas, no light.",
         size=14, color=BG_WHITE)

add_text(s, Inches(0.6), Inches(6.7), Inches(12), Inches(0.3),
         "Thank you. Questions?",
         size=14, bold=True, color=ACCENT)

add_footer(s, 8)
set_notes(s,
    "(~30 sec) Two columns in the ledger. My first deck only filled out one "
    "of them. The honest case for fossil fuels — really, the honest case "
    "for a managed transition — is the column my first deck left blank. "
    "Thank you. Questions?")

# ---- Save ----
out = HERE / "deliverable" / "case-for-fossil-fuels.pptx"
out.parent.mkdir(exist_ok=True)
prs.save(out)
print(f"wrote {out}")
