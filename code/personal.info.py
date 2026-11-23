profiles = {}


def enter_profile():
    student_id = input("Enter your student ID: ")

    # This inner dictionary stores the student's profile information.
    student_profile = {
        "subjects": input("Enter your subjects: "),
        "courses": input("Enter your courses: "),
        "grade level": input("Enter your grade level: "),
        "academic goals": input(
            "Enter your academic goals (press Enter to leave blank): "
        ),
        "areas of difficulty": input("Enter your areas of difficulty: "),
        "preferred learning methods": input(
            "Enter your preferred learning methods: "
        ),
        "tutoring objectives": input("Enter your tutoring objectives: "),
    }

    # Store the inner dictionary in the outer dictionary using the student ID.
    profiles[student_id] = student_profile
    print("\nYour profile data is stored.")

    return student_id


def view_profile(signed_in_student_id, profile_owner_id):
    # Only let a student view their own profile.
    if signed_in_student_id != profile_owner_id:
        print("Profile unavailable.")
        return

    if profile_owner_id not in profiles:
        print("Profile unavailable.")
        return

    student_profile = profiles[profile_owner_id]

    print("\nYour profile data is stored.")

    if student_profile["academic goals"] == "":
        print("No academic goals are listed.")

    print("\nStudent profile:")
    for field, answer in student_profile.items():
        if answer:
            print(f"{field.title()}: {answer}")
        elif field != "academic goals":
            print(f"{field.title()}: Not provided")


student_id = enter_profile()
view_profile(student_id, student_id)
