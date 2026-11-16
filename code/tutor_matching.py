"""Pure tutor-matching rules."""


def match_tutors(tutors, subject, day, time):
    """Return tutors matching subject, day, and time without changing records."""
    requested = tuple(value.strip().casefold() for value in (subject, day, time))
    if not all(requested):
        return []

    return [
        tutor
        for tutor in tutors
        if any(
            requested[0] == taught_subject.strip().casefold()
            for taught_subject in tutor["subjects"]
        )
        and any(
            requested[1] == available_day.strip().casefold()
            for available_day in tutor["days"]
        )
        and any(
            requested[2] == available_time.strip().casefold()
            for available_time in tutor["times"]
        )
    ]
