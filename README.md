# Project Name

Description of the project.

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
    - python -m venv myenv
    - myenv\Scripts\activate.bat (Windows)
    - source myenv/bin/activate (Linux)
3. Install the requirements by running `pip install -r requirements.txt`.
4. Run the migrations by running `python manage.py migrate`.

## Usage
1. Run the server by running `python manage.py runserver`.
2. Access the website at `http://localhost:8000/`.
    
You can navegate through the app and do all the actions there, but if
you prefer you can access the following urls in any program like Postman
to make the requests.
 
## Requests:

- Access Admin panel

    First you will have to create a superuser, for that use the command `python manage.py createsuperuser`.

    Follow the prompts to enter a username, email, and password for the superuser account.

    Then make the request to the admin url
    ```
    GET http://localhost:8000/admin/
    ```
    Enter the username and password for the superuser account to log in to the admin panel.

- Access the Collaborator List 
    ```
    GET http://localhost:8000/collaborators/
    ```
- Access the Departments List 
    ```
    GET http://localhost:8000/departments/
    ```
- Create Department
    ```
    POST http://localhost:8000/departments/add/
    ```

    Will open a form to create the Department

- Create Collaborator
    ```
    POST http://localhost:8000/collaborator/add/
    ```
    
    Will open a form to create the Collaborator

- Delete Department
    ```
    POST http://localhost:8000/departments/<int:pk>/remove/
    ```
    Obs: replace `<int:pk>` on the url to the key of the Department that you want to delete 

- Delete Collaborator
    ```
    POST http://localhost:8000/collaborator/<int:pk>/remove/
    ```
    Obs: replace `<int:pk>` on the url to the key of the Collaborator that you want to delete 