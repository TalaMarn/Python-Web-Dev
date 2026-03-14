# Django app - Student app
# step 1. create project - python manage.py startproject myproject
# step 2. python manage.py startapp student - create app
# step 3. Register App in settings.py
# step 4. Create model in models.py
# step 5. Run migrations
'''
    1. python manage.py makemigrations - create migration files
    2. python manage.py migrate - apply migrations to the database
'''
# step 6. register model in admin.py
# step 7. Create superuser - python manage.py createsuperuser
# step 8. Run server - python manage.py runserver - http://127.0.0.1:8000/admin/ - admin panel
# step 9. show student on website - student/views.py
# step 10. Create template - student/templates/student.html
# step 11. add urls - student/urls.py and myproject/urls.py - http://127.0.0.1:8000/ - show student list on homepage