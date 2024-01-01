# Brine Task
Created a price alert application that triggers an email when the user’s target price is achieved for BTC/USDT.
## Project Setup
The project is dockerized so just need to build and run the docker container.
Install Docker Desktop for easy GUI on windows. Clone the project and open a terminal.
```
$ docker-compose up --build
```
This will build the container and once completed, the container will be running and visible in the container section of the Docker Desktop.
Even if the terminal is closed, the container can be started/stopped from the GUI.<br><br>
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/2e3a3955-41f8-4f01-ae17-2af69b451090)
<br>This container will run all the resources (redis, postgres, etc) for the project.
<br>We can now access the server at [http://localhost:8000/](http://localhost:8000/).
### Database Setup
To build the database tables, we need to run the migrate command.
- In the integrated terminal of `web` container.
```
$ python manage.py migrate
```
- You can also run the migrate command from the terminal of docker build in the following way
```
$ docker-compose up -d
docker-compose exec web python manage.py migrate
```
### Superuser/Admin Setup
Similar to migrate command, we need to run the `createsuperuser` command to create a admin/super user.
- In the integrated terminal of `web` container.
```
$ python manage.py createsuperuser
```
- You can also run the migrate command from the terminal of docker build in the following way
```
$ docker-compose up -d
docker-compose exec web python manage.py createsuperuser
```
We can now access the admin panel of our project at [http://localhost:8000/admin/](http://localhost:8000/admin/) with the credentials provided while executing the `createsuperuser` command.
### User Creation
In the admin panel, we can create more users from the Users tab by clicking on `ADD USER +` at the top-right of the pannel.
Provide the required details and the user will be created. <br><br>
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/5dd5a66e-4cb3-456d-abef-d2c81458b7c4)
<br>
The email needs to be provided and saved once the User object is created.
- The email is necessary for sending alerts for the user.
- The other details are optional, won't be used anywhere in the project.
- Don't forget to save the object after typing the email. <br><br>
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/5f30ff31-2262-4ca1-bd77-5c4171e4030e)
<br>
This conculdes the basic project setup for running using docker. <br>
## API Endpoints
