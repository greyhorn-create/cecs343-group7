from app import app

def test_home_page_shows_tutor_search_form():
    response = app.test_client().get("/")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert 'id="tutor-search-form"' in page
    assert 'name="subject"' in page
    assert 'name="day"' in page
    assert 'name="time"' in page

def test_subject_day_and_time_search_returns_exact_match():
    response = app.test_client().get(
        "/tutors?subject=Mathematics&day=Monday&time=4%3A00+PM"
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "tutors": ["Ana — Mathematics — Monday — 4:00 PM"]
    }

def test_missing_subject_returns_json_error():
    response = app.test_client().get("/tutors?subject=&day=Monday&time=4%3A00+PM")

    assert response.status_code == 400
    assert response.get_json() == {"error": "Enter a subject"}

def test_no_matching_tutors_returns_json_message():
    response = app.test_client().get(
        "/tutors?subject=History&day=Monday&time=4%3A00+PM"
    )

    assert response.status_code == 200
    assert response.get_json() == {
         "message": "No tutors found for History on Monday at 4:00 PM",
         "tutors": []
    }
