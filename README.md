# Nittany University Hospital Web Portal

## Overview
This project is a web portal built with Python, Flask, and SQLite that allows hospital staff to add and delete patient records. The application demonstrates front-end (modest html) and back-end integration along with several enhanced features, including:
- **Soft Deletion:** Instead of permanently removing records, patients are marked as inactive.
- **Preservation of Original PIDs:** When a patient is deleted and later re-added, the original PID is reused.
- **Clear Table Feature:** A "Clear Table" button allows marking all patients as inactive.
- **Extra Credit – Bootstrap Integration:** Even though I love GSAP much more than Bootstrap, I decided to use it in this particular assignment. The user interface is enhanced using Bootstrap via CDN links for styling and modals, providing a modern look-and-feel with interactive components.

### What is Soft Deletion?
Instead of permanently deleting records, patients are marked inactive. When a patient is re-added, their original PID is retained. This is also like a history feature to retrieve a record of a patients existence even after they are deleted.

### Why Soft Deletion?
WHen I was testing my app, I found that when I delete a record and readded it, that record was given a new pid and the original pid was unusable/unreachable. This is highly inefficient at scale, so I decided to mark them as inactive so if they choose to register again, they will not have to jump through hoops to get registered again. Similar to pause membership plans. It will exist as a feature as long as database.db is not deleted after initial db population.

- **Extra Credit - Dropdown Menu:** Even though I never used it while testing I implemented a dropdown menu just because for some reason, it is regarded as a complex html feature. This is on the landing page at path [localhost:5000/](http://localhost:5000/)

## Features
- **Add Patient Endpoint:**
  - Adds a new patient unless a duplicate active entry exists.
  - If a patient was previously deleted (marked inactive), reactivation occurs without assigning a new PID.
  - Displays an error alert (Bootstrap alert component) if a duplicate is detected.
  
- **Delete Patient Endpoint:**
  - Deletes (soft deletes) a patient by marking the record inactive.
  - Displays an error alert if the patient does not exist.
  - Includes a "Clear Table" button that marks all patients inactive and shows a success alert.
  
- **Bootstrap Integration:**
  - **CDN Links:** All HTML templates (e.g., `index.html`, `add.html`, and `delete.html`) load Bootstrap CSS and JavaScript via CDN.
  - **Modals:** Confirmation dialogs for adding and deleting patients are implemented using Bootstrap modals. I think it was a nice touch.
  - **Buttons and Alerts:** Bootstrap classes (e.g., `btn`, `alert`) are used to style buttons, alerts, and overall layout. My favorite style in buttons is the enlarge on hover which I always use in any personal project because it adds a layer of interactibility.


## How to Run the Project
0. Unzip the downloaded file, by clicking extract, double clicking the zipped file on MacOS or using the terminal in Linux
  - I think that graduate TAs know how to unzip files.
1. **Double click on Pycharm icon to open the .app or .exe file**
  - In the project side tab, click on Open with an icon that resembles the folder
  - Navigate to the directory where ```Choudhary_UC_WPE``` was extracted
  - On the bottom right of the screen, the 4th icon from the top is the terminal, click on it.
  - Follow the instructions in the next section


2. **Set Up Environment:**
   - Ensure Python is installed.
   - Check by running 
      ```bash
      python --version
      ```
      in the terminal or powershell
   - Create a virtual environment and activate it:
     ```bash
     # For MacOS
     # in ~/.zshrc
     alias python=python3

     # Setting up a virtual environment
     python -m venv venv
     source venv/bin/activate  
    
     # On Windows: 
     ```
     ```bash
      venv\Scripts\activate
      # This may not be required for some Windows Computers
     ```
   - In the virtual environment (if required), install Flask:
     ```bash
     pip install flask
     ```

3. **Run the Application:**
   - From the project root, start the Flask server:
     ```bash
     python app.py
     ```
   - The server will start at `http://127.0.0.1:5000/` as specified in app.py.

4. **Usage:**
   - **Add Patient:** Navigate to the add page, enter a patient's first and last name, and confirm via the Bootstrap modal.  
   - **Delete Patient:** Navigate to the delete page, enter a patient's name to soft-delete them, or use the "Clear Table" button to mark all active patients inactive.

## Code Snippets & Bootstrap Integration

### Bootstrap CDN Links in HTML Templates
In every HTML template (e.g., `index.html`, `add.html`, `delete.html`), Bootstrap is included via CDN links in the `<head>` section:
```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
```
And at the end of the body, the Bootstrap JavaScript libraries are loaded:
```html
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
```

### Example: Bootstrap Modal for Deletion Confirmation
The ```delete``` page (delete.html) includes a Bootstrap modal for confirming patient deletion:
```html
<div class="modal fade" id="confirmDeleteModal" tabindex="-1" role="dialog" aria-labelledby="confirmDeleteModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="confirmDeleteModalLabel">Confirm Deletion</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        Are you sure you want to delete this patient?
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
        <button type="button" class="btn btn-danger" id="confirmDeleteButton">Confirm</button>
      </div>
    </div>
  </div>
</div>
```

<mark>Note: The html templates are just forms, the core backend logic is in</mark> ```app.py```.

### Clear Table Feature in Delete Endpoint
The "Clear Table" button is implemented on the delete page:
```html
<form id="clearTableForm" method="POST" action="/delete/clear" class="mt-4">
  <div class="text-center">
    <button type="submit" class="btn btn-warning action-btn">Clear Table</button>
  </div>
</form>
```
And the endpoint in app.py:
```python
@app.route('/delete/clear', methods=['POST'])
def clear_table():
    connection = get_db_connection()
    connection.execute('UPDATE patients SET active = 0 WHERE active = 1;')
    connection.commit()
    connection.close()
    return redirect('/delete?cleared=1')
```
When this endpoint is triggered, it redirects to the delete page with a query parameter to display a Bootstrap alert indicating the table has been cleared.

## New Features Summary

- **Soft Deletion & PID Preservation:** Instead of permanently deleting records, patients are marked inactive. When a patient is re-added, their original PID is retained. This is also like a history feature to retrieve a record of a patients existence even after they are deleted.
- **Clear Table Functionality:** A dedicated "Clear Table" button marks all active patients as inactive, and a success alert is displayed to confirm the action.
- **Bootstrap Enhancements:**
  - **CDN Integration:** Each HTML file includes HTTP CDN links for Bootstrap CSS and JavaScript for enhanced styling and responsiveness.
  - **Modals:** Bootstrap modals are implemented for confirmation dialogs during deletion operations.
  - **Alerts:** Bootstrap alerts are used to notify users of duplicate entries and successful table clear actions.

## References & Online Sources

- [http://getbootstrap.com/docs/4.4/components/modal/](http://getbootstrap.com/docs/4.4/components/modal/) – For modal dialog usage.
- [Bootstrap CDN Links](http://stackpath.bootstrapcdn.com/bootstrap/4.4.1/) – For styling and responsive design.
- [SQLite Documentation](http://sqlite.org/lang.html) – For database syntax and operations.
- [Flask Documentation](http://flask.palletsprojects.com/) – For guidance on building the web application.
- [GSap website](https://gsap.com/)
