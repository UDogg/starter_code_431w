# Nittany University Hospital Web Portal

## Overview
This project is a web portal for Nittany University Hospital that allows hospital staff to add and delete patient records from a SQLite database. The portal is built using Python with the Flask framework and uses HTML, CSS, and JavaScript on the front-end. It incorporates advanced UI features such as GSAP animations, CSS hover effects, Bootstrap modals for confirmation, and provides dual navigation via buttons and a drop-down menu.

## Features
- **Main Landing Page:** 
  - Displays a clear heading with navigation options.
  - Provides two navigation methods: buttons and a drop-down menu.
  - Implements GSAP animations on page load.
  - Buttons have hover effects (20% larger and darker when hovered).

- **Add Patient Page:**
  - Contains a form for entering the patient's first and last name.
  - Uses a Bootstrap modal to confirm the addition of a new patient.
  - Automatically generates a unique PID (using SQLite AUTOINCREMENT).
  - Displays all patient records in an HTML table.

- **Delete Patient Page:**
  - Contains a form for entering the patient’s first and last name for deletion.
  - Uses a Bootstrap modal to confirm deletion.
  - Displays updated patient records in an HTML table after deletion.

## Project Organization
- **app.py:** Main Flask application with routes for the landing page, adding patients, and deleting patients. It also initializes the SQLite database.
- **index.html:** Main landing page that offers both button and drop-down navigation.
- **add.html:** Page for adding a patient record. Includes the form, Bootstrap modal confirmation, and a table displaying current patient records.
- **delete.html:** Page for deleting a patient record. Includes the form, Bootstrap modal confirmation, and a table displaying updated patient records.
- **database.db:** SQLite database file storing patient records.
- **README.md:** This file with instructions, context, features, and citations.

## Instructions to Run the Project
1. **Setup Environment:**
   - Ensure that Python is installed.
   - Install Flask using pip:
     ```
     pip install flask
     ```
   - Since only Flask is being used it is not worth it making a ```requirements.txt``` file
   - If using PyCharm Professional, open the project folder and configure the Python interpreter.

2. **Run the Application:**
   - Open a terminal in the project directory.
   - Run the Flask application:
     ```
     python app.py
     ```
   - Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. **Usage:**
   - On the landing page, choose to navigate via the buttons or the drop-down menu.
   - On the **Add Patient** page, enter the patient's first and last names and click the **Add** button. Confirm the addition in the modal dialog.
   - On the **Delete Patient** page, enter the patient's first and last names and click the **Delete** button. Confirm the deletion in the modal dialog.

## Online Sources and Citations
- HTML and Form Elements:
  - W3Schools, "HTML Input Types" 
  - W3Schools, "HTML Select Tag" 
- SQL Commands:
  - W3Schools, "SQL INSERT INTO" 
  - W3Schools, "SQL DELETE" 
- Bootstrap Modals:
  - Bootstrap, "Modal Component" 
- SQLite Syntax:
  - SQLite, "Language Reference"
- GSAP Animations:
  - GreenSock, "GSAP Animation Platform" [https://greensock.com/gsap/]

## Assumptions and Clarifications
- The project uses SQLite as specified in the starter code.
- Each patient record is uniquely identified by an auto-incremented PID.
- The delete functionality removes all records matching the provided first and last names.
- Both buttons and drop-down navigation are implemented to demonstrate varied UI techniques.
- GSAP is used for smooth animation effects, and CSS is used to achieve responsive hover effects.

## Conclusion
This web portal demonstrates a complete solution for managing patient records using Flask and SQLite while incorporating modern front-end techniques such as GSAP animations, Bootstrap modals, and interactive hover effects. This project meets all assignment requirements and includes bonus enhancements to showcase multiple approaches for user interaction.

