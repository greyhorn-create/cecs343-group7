from flask import Flask, jsonify, request, render_template

from tutor_matching import match_tutors

app = Flask(__name__)

# Sample tutor records make this slice usable without a database.
TUTORS = [
    {
        "name": "Ana",
        "subjects": ["Mathematics"],
        "days": ["Monday"],
        "times": ["4:00 PM"],
    },
    {
        "name": "Ben",
        "subjects": ["English"],
        "days": ["Monday"],
        "times": ["4:00 PM"],
    },
]

@app.get("/")
def home():
    """show the website's current feature: tutor search."""
    return render_template("index.html")

@app.get("/tutors")
def find_tutors():
    subject = request.args.get("subject", "").strip()
    day = request.args.get("day", "").strip()
    time = request.args.get("time", "").strip()

    if not subject:
        return jsonify({"error": "Enter a subject"}), 400
    if not day:
        return jsonify({"error": "Select a day"}), 400
    if not time:
        return jsonify({"error": "Select a time"}), 400

    matching_tutors = match_tutors(TUTORS, subject, day, time)
    if not matching_tutors:
        return jsonify({
            "message": f"No tutors found for {subject} on {day} at {time}",
            "tutors": [],
        })

    results = []
    for tutor in matching_tutors:
        matched_subject = next(
            value for value in tutor["subjects"] if value.strip().casefold() == subject.casefold()
        )
        matched_day = next(
            value for value in tutor["days"] if value.strip().casefold() == day.casefold()
        )
        matched_time = next(
            value for value in tutor["times"] if value.strip().casefold() == time.casefold()
        )
        results.append(f"{tutor['name']} — {matched_subject} — {matched_day} — {matched_time}")

    return jsonify({"tutors": results})


if __name__ == "__main__":
    app.run(debug=True)
