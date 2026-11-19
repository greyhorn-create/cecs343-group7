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

------------------------------------------------------------------
 User Case: A Website where the student will find all of the feature we'll implement. 

 Actor: User

 Goal: A User is able to open up the website where they'll be able to use it's functions

 Main Success Scenario:

 The user is able to open up the website and see the bars where they can input the Subject, Time, and Day. Then the website loads and returns a list
 of potential tutors using the match_tutor function. 

 Extensions:

 - The user enters nothing in the boxes
 - If no tutors were found the website will return a "No Tutors Match" message
 - User can see their profile if one was created

## Table 

| UC-Step | Where it runs |
| --- | --- |
| 1. The user enters the website | User's browser |
| 2. The browser requests the main page | Browser sends a request to the website |
| 3. The website returns the main page with the tutor search options | Website's home-page route and page|
| 4. The browser displays the main page to the user | User's Browser | 
| 5. The user selects "Find a Tutor" | Main-page interface; this starts the seprate tutor-search use case|

## Mermaid Diagram
<img width="1618" height="964" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/76b02c76-cb31-4096-8ca3-fcfda55a1d62" />


