"""Shared palette + matplotlib style.

Two-accent system, used thematically:
  • BLUE  (#1F4E79) — the path forward / resolution / what's built
  • AMBER (#D97706) — the cost / stakes / what's being paid right now

Grey for context. White background. No chartjunk."""

BLUE        = "#1F4E79"   # primary — path forward
BLUE_LIGHT  = "#3B6FA0"   # secondary blue tint
AMBER       = "#D97706"   # secondary — cost / stakes
AMBER_LIGHT = "#FBBF24"   # warm tint
TEXT        = "#1F2937"
TEXT_MUTED  = "#4B5563"
GREY_CTX    = "#9CA3AF"
GREY_SOFT   = "#D1D5DB"
GRID        = "#E5E7EB"
SURFACE     = "#F9FAFB"   # soft card background
BG          = "#FFFFFF"

# legacy aliases so old scripts keep working
ACCENT = BLUE

def apply_style(plt):
    plt.rcParams.update({
        "figure.facecolor": BG,
        "axes.facecolor":   BG,
        "axes.edgecolor":   GRID,
        "axes.labelcolor":  TEXT_MUTED,
        "axes.titlecolor":  TEXT,
        "axes.titleweight": "bold",
        "axes.titlesize":   14,
        "axes.titlelocation": "left",
        "axes.titlepad":    16,
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "axes.spines.left":  False,
        "axes.spines.bottom": False,
        "xtick.color":      TEXT_MUTED,
        "ytick.color":      TEXT_MUTED,
        "xtick.labelsize":  11,
        "ytick.labelsize":  11,
        "font.family":      "DejaVu Sans",
        "font.size":        11,
        "savefig.dpi":      220,
        "savefig.facecolor": BG,
        "savefig.bbox":     "tight",
    })
