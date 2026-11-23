"""Pure tutor-matching rules, supporting both original records and time ranges."""

from datetime import datetime


def parse_search_time(value):
    value = value.strip().upper()
    for pattern in ("%I:%M %p", "%H:%M"):
        try:
            return datetime.strptime(value, pattern).strftime("%H:%M")
        except ValueError:
            pass
    return None


def display_time(value):
    return datetime.strptime(value, "%H:%M").strftime("%I:%M %p").lstrip("0")


def match_tutors(tutors, subject, day, time):
    """Match all criteria in the same slot; leave input records unchanged.

    A range includes its start and excludes its end. Original records with
    separate days/times lists retain their original exact-text matching rules.
    """
    requested = tuple(value.strip().casefold() for value in (subject, day, time))
    if not all(requested):
        return []

    requested_time = parse_search_time(time)
    matches = []

    for tutor in tutors:
        if not any(
            requested[0] == value.strip().casefold()
            for value in tutor["subjects"]
        ):
            continue

        if "availability" in tutor:
            available = requested_time is not None and any(
                requested[1] == slot["day"].strip().casefold()
                and slot["start_time"] <= requested_time < slot["end_time"]
                for slot in tutor["availability"]
            )
        else:
            available = (
                any(
                    requested[1] == value.strip().casefold()
                    for value in tutor["days"]
                )
                and any(
                    requested[2] == value.strip().casefold()
                    for value in tutor["times"]
                )
            )

        if available:
            matches.append(tutor)

    return matches
