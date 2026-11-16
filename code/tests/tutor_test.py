from code import app

def test_subject_day_and_time_search_returns_exact_match():
    response = app.test_client().get(
        "/tutors?subject=Mathematics&day=Monday&time=4%3A00+PM"
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "tutors": ["Ana — Mathematics — Monday — 4:00 PM"]
    }
