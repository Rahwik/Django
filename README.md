Django Setup and Usage Guide

1\. Set-Up:
===========

1.  Install Python:
    ---------------
    
    Install Python in the system.
    
2.  Create Local Folder:
    --------------------
    
    Make a local folder in the disk (e.g., Django).
    
3.  Open Command Prompt:
    --------------------
    
    Open the folder in the command prompt by typing cmd in the address bar.
    
4.  Install Virtual Environment:
    ----------------------------
    
    Install virtual environment in the folder. (pip install virtualenv)
    
5.  Activate Virtual Environment:
    -----------------------------
    
    Activate the virtual environment by navigating to scripts.
    
    1.  cd env
    2.  cd scripts
    3.  activate
6.  Install Django:
    ---------------
    
    Install Django in the virtual environment (pip install Django).
    
7.  Check Django Installation:
    --------------------------
    
    Check if Django is successfully installed.
    
    1.  Write in the command palate. (python)
    2.  Import Django
    3.  django.\_\_version\_\_
    4.  To exit, press (Ctrl + Z)

2\. Project Creation In Django:
===============================

1.  Create Project:
    ---------------
    
    Run `django-admin startproject |core|`.
    
2.  Navigate to Project:
    --------------------
    
    Navigate to the project folder.
    
    1.  cd core
3.  Open Project in VS Code:
    ------------------------
    
    Open VS Code to view the project.
    
    1.  code .

3\. App Creation In Django:
===========================

1.  Create App:
    -----------
    
    Run `python manage.py startapp |home|`.
    

4\. Run the Server:
===================

1.  Start Server:
    -------------
    
    Run `python manage.py runserver`.
    
2.  Custom Port Execution:
    ----------------------
    
    Run `python manage.py runserver 0.0.0.0:5000`.
    

5\. Views and URLs:
===================

A. HttpResponse (from the apps):
--------------------------------

1.  ### Open Views:
    
    Open the views.py in the app created to add the attributes.
    
2.  ### Import HttpResponse:
    
    Import HttpResponse from django.http.
    
3.  ### Create Functions:
    
    Create functions to add the tags of HTML to display content.
    
4.  ### Add Paths in URLs:
    
    In the main directory open the urls.py to add the path of the view just created.
    
5.  ### Import Views:
    
    Import the views from the app in the urls.py.
    
6.  ### Add Paths:
    
    Add the path of the function which is created in the urls.py.
    
    1.  `path('',home,name="home"),`
    2.  `path('success_page/',success_page,name="success_page"),`
    3.  **NOTE:** don't forget the comma at the last.

B. HTML response (from the apps):
---------------------------------

1.  ### Create Templates Folder:
    
    Create a templates folder in the apps folder (e.g., core/home/templates).
    
2.  ### Create HTML Files:
    
    Create `index.html` in the templates folder previously created.
    
3.  ### Create Render Function:
    
    Create a render function for the `index.html`.
    
4.  ### Use Templates:
    
    If more than one folder is inside the templates folder, add the proper path of the HTML file.
    

6\. Template Engine:
====================

A. Dynamic Data Manipulation:
-----------------------------

### Passing A List:

1.  #### Create a List:
    
    Create a list of dictionaries within the views.py.
    
2.  #### Declare the List:
    
    Declare the new list in the `return render` in the views.py.
    
3.  #### Ways to Add Dynamic Data:
    
    Ways to add the Dynamic data to the `index.html`.
    
    1.  Simply displaying the data.
    2.  Dynamically adding the data using the tables in the HTML.
    3.  Using Dynamic Data for Other Operations (if...else).
