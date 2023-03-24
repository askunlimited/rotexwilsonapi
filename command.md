# Commands

-https://www.markdownguide.org/basic-syntax/#:~:text=Headings,e.g.%2C%20%23%23%23%20My%20Header%20.

1. **python3 -m venv env** : _to create a virtual environment_
2. **source env/bin/activate** : _to activate the virtual environment_
3. **pip install django** : _to install Django_
4. **django-admin startproject project .** : _To create project in the parent folder_
5. **python manage.py (./manage.py) runserver** : _Will run the server_
6. **from django.core.management.utils import get_random_secret_key** : _To be executed in the python shell to enable generating secret key_
7. **print(get_random_secret_key())** : \*To print the secret key
8. **type python or python manage.py shell to prompt the interactive shell and Ctrl + D to quit from the python shell**
9. **pip freeze > requirements.txt** : _to log the packages on the project_
10. **pip install -r requirements.txt** : _To install all packages in the txt file_
11. **Django Treebrad and Django mptt**: \_Used for creating deeply nested categories. _to install \_pip install django-mptt_
12. **Django API Documentation with swagger and drf-spectacular**: *install df-spectacular*
13. **manage.py spectacular --file schema.yml**: *To create the documentation schema for the applications models that will be used to generate the documentation*
14. **To identify areas of testing use coverage "pip install coverage".** *run coverage using "coverage run -m pytest" and "coverage run html" to generate html file*
15. **Alternatively we can "pip install pytest-cov" and run "pytest-cov"**
16. **Usung Factory Boy for Testing: Install pytest-factoryboy and create factories and contest files in the test folder**

# Packages Installed

django
python-dotenv 0.21.0
djangorestframework==3.14.0
pytest==7.2.0
DJANGO treebeard
Django mptt
drf-spectacular
coverage
pytest-cov
pytest-factoryboy
