"""Shared palette + matplotlib style for all charts.
Confident blue accent on warm-neutral greys. White background. No chartjunk."""

ACCENT      = "#1F4E79"   # confident blue — used to direct attention
TEXT        = "#1F2937"   # near-black for titles/axis text
TEXT_MUTED  = "#4B5563"   # secondary text
GREY_CTX    = "#9CA3AF"   # context bars / de-emphasized
GRID        = "#E5E7EB"   # subtle gridlines
BG          = "#FFFFFF"

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
        "xtick.color":      TEXT_MUTED,
        "ytick.color":      TEXT_MUTED,
        "xtick.labelsize":  11,
        "ytick.labelsize":  11,
        "font.family":      "DejaVu Sans",
        "font.size":        11,
        "savefig.dpi":      200,
        "savefig.facecolor": BG,
        "savefig.bbox":     "tight",
    })
