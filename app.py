"""
app.py - Flask application entry point for Google Cloud Summit 2026
"""

from flask import Flask, render_template, request, jsonify
from data import (
    EVENT,
    SPEAKERS,
    TALKS,
    SCHEDULE,
    CATEGORIES,
    get_speaker_map,
    get_talk_map,
    enrich_talks,
)
import datetime

app = Flask(__name__)


def _build_schedule_items():
    """Build a full schedule list."""
    speaker_map = get_speaker_map()
    talk_map = get_talk_map()
    enriched_talk_map = {t["id"]: t for t in enrich_talks(list(talk_map.values()), speaker_map)}

    items = []
    for entry in SCHEDULE:
        if entry["type"] == "session":
            talk = enriched_talk_map.get(entry["talk_id"], {})
            items.append(
                {
                    "type": "session",
                    "time_start": entry["time_start"],
                    "time_end": entry["time_end"],
                    "talk": talk,
                }
            )
        else:
            items.append(
                {
                    "type": entry["type"],  # break / lunch
                    "label": entry["label"],
                    "time_start": entry["time_start"],
                    "time_end": entry["time_end"],
                }
            )
    return items


@app.route("/")
def index():
    today = datetime.date.today().strftime("%A, %B %d, %Y")
    schedule_items = _build_schedule_items()
    speaker_map = get_speaker_map()
    enriched = enrich_talks(TALKS, speaker_map)
    return render_template(
        "index.html",
        event=EVENT,
        today=today,
        schedule_items=schedule_items,
        talks=enriched,
        speakers=SPEAKERS,
        categories=CATEGORIES,
    )


@app.route("/talk/<talk_id>")
def talk_detail(talk_id):
    speaker_map = get_speaker_map()
    talk_map = get_talk_map()
    talk = talk_map.get(talk_id)
    if not talk:
        return render_template("404.html"), 404
    enriched = enrich_talks([talk], speaker_map)[0]
    return render_template("talk.html", talk=enriched, event=EVENT, categories=CATEGORIES)


@app.route("/api/search")
def api_search():
    """
    JSON search endpoint.
    Query params:
      q        - free-text query (searches title + speaker names)
      category - category id (1 or 2)
    """
    q = request.args.get("q", "").strip().lower()
    cat = request.args.get("category", "").strip()

    speaker_map = get_speaker_map()
    results = enrich_talks(TALKS, speaker_map)

    # Filter by category
    if cat:
        try:
            cat_int = int(cat)
            results = [t for t in results if t["category"] == cat_int]
        except ValueError:
            pass

    # Filter by search query (title, speaker name, description)
    if q:
        filtered = []
        for talk in results:
            speaker_names = " ".join(
                f"{s['first_name']} {s['last_name']}".lower() for s in talk["speakers"]
            )
            if (
                q in talk["title"].lower()
                or q in speaker_names
                or q in talk["description"].lower()
            ):
                filtered.append(talk)
        results = filtered

    # Serialise — remove non-JSON-safe fields
    output = []
    for t in results:
        output.append(
            {
                "id": t["id"],
                "title": t["title"],
                "category": t["category"],
                "category_name": t["category_name"],
                "time_start": t["time_start"],
                "time_end": t["time_end"],
                "room": t["room"],
                "description": t["description"][:200] + "…" if len(t["description"]) > 200 else t["description"],
                "speakers": [
                    {
                        "id": s["id"],
                        "name": f"{s['first_name']} {s['last_name']}",
                        "title": s["title"],
                        "company": s["company"],
                        "linkedin": s["linkedin"],
                        "avatar_initials": s["avatar_initials"],
                        "avatar_color": s["avatar_color"],
                    }
                    for s in t["speakers"]
                ],
            }
        )

    return jsonify({"results": output, "count": len(output)})


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5001)
