# To Run the Dockerfile and the postgress sql
1 -> run this command: docker build -t my-postgres-image .

2 -> run this command: docker run --name my-postgres-container -d -p 5432:5432 my-postgres-image

 # to navigate inside the container 
 run this command docker exec -it my-postgres-container bash

 # to check the postgress sql client
 1 -> download the client management tool https://www.pgadmin.org/

 2 -> lunch the pgadmin

 3 -> click on add new server

 4 -> name: name it anything youwant

 5 -> click on connection

 6 -> hostname: localhost
 	  port: 5432 
      maintaince database: mydb
	  username: myuser
	  password: mypassword

7 -> click save	  

# To Run the Django Api Server (BACKEND)

# step 1
 1 - go to the directory backend/myproject
# step 2
 2 - run the command pyhton3 manage.py runserver
# step 3
 3 - go to your browser and run 127.0.0.1:8000
 4 - you can test also the login post request 127.0.0.1:8000/login

# For Sample HTML Test file
# Path backend/myproject/myapp/templates

# Note: Make sure you have python3 version 3.11.3 downloaded
# Note: Make sure you have django downloaded version 4.2.7 
Link for Django: https://www.djangoproject.com/download/
Command for Django: python3 -m pip install Django