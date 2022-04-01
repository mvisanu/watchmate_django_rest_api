# watchmate_django_rest_api

Create a Django Rest Framework API for Movie IMDB

1.  Create the project directory and virtual environment folder
mkdir drf-project
cd drf-project

2.  Create a virtual environment to isolate our package dependencies locally and actvate the environment
python -m venv menv
menv\Scripts\activate

3. Check for any install packages
pip freeze

4. install django
pip install Django==latest
pip install Django==4.0.3

5. update pip
python -m pip install --upgrade pip

6. create project inside the virtual environment folder
django-admin startproject watchmate

7. VS Code extensions
- Python Extension Packs
- Tabnine Autocoplete

8. create app inside the folder watchmate in cmd after it's activate
python manage.py startapp watchlist_app

9. start the app
python manage.py runserver

10. Add "watch_list in watchmate/settings.py

11. Migration -- python manage.py migrate

12. Create Superuser -- python manage.py createsuperuser
user: mvisanu
email:
password: password

13. run the server again: python manage.py runserver
http://127.0.0.1:8000/admin/login/?next=/admin/

14. after adding a Model need to: 
- python manage.py makemigrations
- python maage.py migrate

15 make change to admin.py to register model we created
- from watchlist.models import Movie
- admin.site.register
