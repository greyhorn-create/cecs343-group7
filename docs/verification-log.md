Requested: ChatGPT Work, intro to spiral process

Generated: 3 problems, the worst risk, 1 hypothetical experiment

Claimed: product will fail due to a lack of tutors or students

Verified: Nothing, no code to run, experiment hypothetical only

Not verified: Nothing, no code to run, experiment hypothetical only

##

Requested: CHatGPT Luna 6, to generate a Mermaid Diagram about our issue on Tutor_based_Matching

Generated: an image of diagram

Claimed: to keep track of all the thing our system keeps track of

Verified: Does keep track of some of our things

Not Verified: what input goes to where
##
Requested: CHatGPT Luna 6, to create a Mermaid Diagram based on our main code file for now

Generated: an image of a diagram
<img width="1154" height="1512" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/51d45553-f6b6-4a72-8546-fb6cbe0f88d0" />

Claimed: keeps track of what each class fields and methods. showing if one class keep another 

Verified: Some of the classes are kept.

Not Verified: If these are the only classes that we'll truly need.

##
Requested: CHatGPT Luna 6, to create a table to see how many files/projects every code imports and to rank them

Generated: a table:
<img width="593" height="233" alt="image" src="https://github.com/user-attachments/assets/c0ba6946-6652-4293-975b-ec244728f643" />

Claimed: The two test files tie for second place; neither is imported by another project file. 
Filenames weren’t included, so it identified them by their pasted code.

Verified: the application file imports no project files, and that each pasted test file imports app with import app as app_module

##
Requested: ChatGPT 6 Luna, check our most important file, and to describe it's symptoms as well as a potential fix

Generated:  a symptom in a paragraph, and a solution in a paragraph 

Claimed: Symptom: find_tutors() in app.py handles the Flask request, validates the subject, filters the sample tutor list, and builds the JSON response in one function. A solution it proposed is that we could create a different file to handle all the filtering of the tutors so that if more filters were to get added later on we  without needing to change the main file.

Verified: That adding another file would be better in order to better implement changes if needed later on to the filtering. 

Not Verified: How long the file would be 

Not Verified: the actual filenames, whether the two identical test excerpts are separate files, 
or whether there are other project files or imports beyond what you pasted


