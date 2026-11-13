import sys
from pathlib import Path

# Let the tests import pieces.py and web.py from the folder above.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pieces import PIECES, all_pieces, all_tags, find, neighbours
from web import app


def test_every_piece_has_an_image_file():
    images = Path(__file__).resolve().parent.parent / "static" / "images"
    for p in PIECES:
        assert (images / p["image"]).exists(), p["image"]


def test_slugs_are_unique():
    slugs = [p["slug"] for p in PIECES]
    assert len(slugs) == len(set(slugs))


def test_filter_by_tag():
    for p in all_pieces("twist"):
        assert "twist" in p["tags"]
    assert all_pieces() == PIECES


def test_find():
    assert find("hexagonal-twist")["title"] == "Hexagonal twist"
    assert find("no-such-piece") is None


def test_tags_sorted_without_repeats():
    tags = all_tags()
    assert tags == sorted(set(tags))


def test_neighbours_wrap_around():
    first, last = PIECES[0], PIECES[-1]
    prev_piece, next_piece = neighbours(first["slug"])
    assert prev_piece == last
    assert next_piece == PIECES[1]


def test_pages_load():
    client = app.test_client()
    assert client.get("/").status_code == 200
    assert client.get("/?tag=twist").status_code == 200
    for p in PIECES:
        assert client.get(f"/pieces/{p['slug']}").status_code == 200
    assert client.get("/pieces/no-such-piece").status_code == 404
