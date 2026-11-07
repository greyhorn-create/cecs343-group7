Use case: Find tutors by subject and schedule

Actor: User

Goal: Find a tutor who matches a requested subject, day, and time.

Precondition: A list of tutors with subjects, days, and times exists.

Main success scenario:

The user selects subject-and-schedule matching from the main menu. The user enters a subject, day, and time. 
The system compares the entered subject, day, and time with the tutor list. The system displays tutors who match all three entries.

Extensions:

2a. The user does not enter a subject, day, or time. The comparison does not proceed. 
3a. No tutor matches the entered subject. The system returns no tutors.
3b. Tutors match the subject but not the entered day. The system returns no tutors. 
3c. Tutors match the subject and day but not the entered time. The system returns no tutors.

## Table

|UC-01 step| Where the Step Runs|
| --- | --- |
| 1. The user selects subject-and-schedule matching from the main menu.| User Interface |
| 2. The user enters a subject, day, and time. | User Interface |
| 2a. If the user leaves the subject, day, or time blank, the comparison does not proceed. | Matching Service checks the input; the User Interface can show the result |
| 3. The system compares the entered subject, day, and time with the tutor list. | Matching Service reads tutor records from the Tutor Data Store and performs the comparison |
| 3a. No tutor matches the entered subject; the system returns no tutors. | Matching Service returns an empty result; the User Interface displays it |
| 3b. Tutors match the subject but not the entered day; the system returns no tutors. | Matching Service returns an empty result; the User Interface displays it |
| 3c. Tutors match the subject and day but not the entered time; the system returns no tutors. | Matching Service returns an empty result; the User Interface displays it |
| 4. The system displays tutors who match all three entries. | User Interface displays the results returned by the Matching Service |

 ## Mermaid Diagram:

 <img width="743" height="355" alt="image" src="https://github.com/user-attachments/assets/5be78417-0e04-4a55-8cbe-795980df5677" />

