from fabric.api import local

def djangobase():
   local("./manage.py runserver")
