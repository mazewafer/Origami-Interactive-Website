# Origami Interactive Website

A portfolio site for my origami tessellations, built with Python (Flask) and HTML.

## Run it

Once:

    python3 -m pip install -r requirements.txt

Then, from this folder:

    python3 web.py

Open http://127.0.0.1:5000 in a browser. Stop the server with Ctrl+C.

## Run the tests

    python3 -m pytest tests -v

## How it fits together

    web.py            the Flask app: one function per page
    pieces.py         the list of my pieces, plus helpers to filter and look them up
    templates/        the HTML pages (Jinja templates)
      base.html       header and footer shared by every page
      gallery.html    the grid of pieces, with tag filters
      piece.html      one piece's page, with previous/next links
    static/style.css  all the styling
    static/images/    pictures of each piece
    tests/            pytest tests

## Add a piece

1. Put a photo in `static/images/`.
2. Copy one of the blocks in `PIECES` in `pieces.py` and fill it in.
3. Refresh the browser.

The images there now are drawn placeholders; swap them for photos of the real folds.

## Where it's going

1. An interactive gallery of my tessellations (started).
2. A tool that draws crease patterns for tessellations (starting with a grid-based twist-fold generator).
3. A documented catalog of fold sequences.
