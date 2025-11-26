## Emails
This script generates personalized emails for students who want to know their final grade. The output consists of an n number of .txt files, where n=number of students, and filename.txt= your students' first names.

- Input: you need a .csv file with your students' first name in a specific column, and their other grades in other columns.
- Variables:
  - **path**: here you put the path to your .csv file.
  - **name**: the student's name (col 1 in my .csv file)
  - **a1, a2, a3**: small assignments whose average (a_av) worth 20% of the grade (cols 4, 7, and 8 in my .csv file)
  - **mt**: midterm grade (30%) (col 9 in my .csv)
  - **exam**: exam grade (50%) (col 10 of my .csv)
  - **path2**: path to the output folder
- The variable **final** stores the calculation of the weighted grades.

## Speech to text

This script uses the SpeechRecognition library. It requires an audio file and yields a .txt file as output. This .txt file can be fed to Praat scripts and/or forced aligners.

Parameters to change:
- Replace "dst.wav" with the name of your audio file.
- The **result** variable uses the Google API, but you can use others (read the library description for more info). You can also specify the language, which in this case was "es-CL" (Chilean Spanish)
- The **text** variable creates a text file (I named mine "transcript.txt").
