from flask import Flask, abort, render_template, request

from pieces import all_pieces, all_tags, find, neighbours

app = Flask(__name__)


@app.route("/")
def gallery():
    # ?tag=twist in the address shows only pieces tagged "twist"
    tag = request.args.get("tag")
    return render_template(
        "gallery.html",
        pieces=all_pieces(tag),
        tags=all_tags(),
        current_tag=tag,
    )


@app.route("/pieces/<slug>")
def piece(slug):
    p = find(slug)
    if p is None:
        abort(404)   # "Not Found" page
    prev_piece, next_piece = neighbours(slug)
    return render_template(
        "piece.html",
        piece=p,
        prev_piece=prev_piece,
        next_piece=next_piece,
    )


if __name__ == "__main__":
    app.run(debug=True)
