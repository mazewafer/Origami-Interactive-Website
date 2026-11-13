"""My origami pieces, and small helpers to look them up.

For now the pieces live in a plain Python list. Later this could become a
database table (like the to-do app), and only this file would need to change.
"""

# Each piece is a dict. To add a new piece, copy one block and change it.
#   slug   - short name used in the web address, e.g. /pieces/square-twist
#   image  - file inside static/images/ (swap the placeholder for a photo)
#   tags   - words you can filter the gallery by
PIECES = [
    {
        "slug": "square-twist-grid",
        "title": "Square twist grid",
        "year": 2026,
        "paper": "15 cm kami",
        "grid": "32 x 32",
        "tags": ["twist", "square"],
        "image": "square-twist-grid.svg",
        "description": "A field of square twists, all turning the same way.",
    },
    {
        "slug": "hexagonal-twist",
        "title": "Hexagonal twist",
        "year": 2026,
        "paper": "Hexagon cut from 20 cm tant",
        "grid": "Triangle grid, 24 divisions",
        "tags": ["twist", "hexagon"],
        "image": "hexagonal-twist.svg",
        "description": "A single hex twist in the centre of a triangle grid.",
    },
    {
        "slug": "waterbomb-tessellation",
        "title": "Waterbomb base tessellation",
        "year": 2026,
        "paper": "25 cm copy paper",
        "grid": "16 x 16",
        "tags": ["waterbomb", "square"],
        "image": "waterbomb-tessellation.svg",
        "description": "Rows of waterbomb bases that curl the sheet into a shell.",
    },
]


def all_pieces(tag=None):
    """Return every piece, or only the ones that have this tag."""
    if tag is None:
        return PIECES
    return [p for p in PIECES if tag in p["tags"]]


def find(slug):
    """Return the piece with this slug, or None if there isn't one."""
    for p in PIECES:
        if p["slug"] == slug:
            return p
    return None


def all_tags():
    """Every tag used by any piece, sorted A to Z, with no repeats."""
    tags = set()
    for p in PIECES:
        tags.update(p["tags"])
    return sorted(tags)


def neighbours(slug):
    """Return (previous piece, next piece) around this one, wrapping around."""
    slugs = [p["slug"] for p in PIECES]
    i = slugs.index(slug)
    return PIECES[i - 1], PIECES[(i + 1) % len(PIECES)]
