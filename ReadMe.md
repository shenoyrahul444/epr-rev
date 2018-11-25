Sources: https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application

# 1> Building the Application
### Starting the application
    > python manage.py runserver

### To create admin
    > python manage.oy createsuperuser

### To Delete admin 
    > python manage.py shell
    > from django.contrib.auth.models import User
    > User.objects.get(username="rahul",is_superuser = True).delete()

#### To access models/Table in the admin:
    Go to app/admin.py and Register the models for that app
    
 
### Migrations ()
    1> For Models.py
    2> For Admin
    
    
    > python manage.py makemigrations (# To commit changes in models)
    > python manage.py migrate (# To Migrate all the changes)
    
    > python manage.py makemigrations blog (# For a particular app)
    > python manage.py sqlmigration blog 0001
 
    
# 2> Deployment
    
    We'll be dockerizing the Django App so it can take advantage of distributed storage and network
    
    1> Creating Requirements.txt in root
        Django==2.1.3
        gunicorn==19.6.0
    
    # Gunicorn web server is built to handle production levels of traffic, unlike Django's development server(suitable for local development)
    2> Creating Virtual environment 'venv' and activating it
        > python3 -m venv venv
        > source venv/bin/activate
    
    3> Installing the requirements using pip
        > pip install -r requirements.txt    
    
    
    4> Add 'start.sh' bash script to root (Startup script for Docker to execute) 

        #!/bin/bash

        # Start Gunicorn processes
        echo Starting Gunicorn.
        exec gunicorn helloworld.wsgi:application \
            --bind 0.0.0.0:8000 \
            --workers 3
    
    5> Testing if start.sh works
        > chmod +x start.sh
        > cd EPR
        > ../start.sh
        
        # This should run the application on the guinicorn web server

#### Dockerizing the applcation
    6> Create Dockerfile in the root 
        
        # Dockerfile
        
        # FROM directive instructing base image to build upon
        FROM python:2-onbuild
        
        # COPY startup script into known file location in container
        COPY start.sh /start.sh
        
        # EXPOSE port 8000 to allow communication to/from server
        EXPOSE 8000
        
        # CMD specifcies the command to execute to start the server running.
        CMD ["/start.sh"]
        # done!
        
    7> Building and Running the Container
        
        > docker build -t shenoy/epr .
        
        > docker run -it -p 8000:8000 shenoy/epr 