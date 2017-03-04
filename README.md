# Django Core Training
A Udemy training app from Django Core Course, implementing Two Scoops of Django File Structure. This project is made in Django 1.10.6

### Requirements:
We've implemented several requirements files. Command for using requirements is:
* `pip installl -r requirements/[file_to_use.txt]`

### Settings:
Remember to create a copy of env.example as .env in the **src/settings** changing the fields needed for the project and leaving blank for the ones that aren't needed.
Command to use specific settings file is:
* `python manage.py runserver --settings=src.settings.[settings_to_use]`

### Testing / Coverage:
If needed to check whether or not tests are working or what needs testing, run:
* `coverage run`
* `coverage report` --to view testing reports
