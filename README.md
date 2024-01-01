# Brine/tanX Task
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
- Don't forget to save the object after typing the email. <br>
<!--alignment fix comment-->
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/5f30ff31-2262-4ca1-bd77-5c4171e4030e)
This conculdes the basic project setup for running using docker.
## API Endpoints
### Postman collection
For the project the following postman collection can be used for easy API  setup.
- It can be accessed using this [Postman Collection Link](https://api.postman.com/collections/18099512-d616d445-f405-4adc-a450-c1497b24dcc4?access_key=PMAT-01HK3CF7SVG4SPHKEXG547S8XH).
- The Collection contains example responses for all the possible cases of all APIs. Please refer to those for any clarification on sample response.  <br><br>
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/579365c9-794c-4388-a5b5-9e38f39473d7)
### Access Token (JWT)
Authentication for all Alerts APIs has been implemented using JWT tokens. To generate/get a token for any user, use the `Get User by ID` API in the Users Folder.
- User Id need to be passed the the endpoint. The endpoint for the API is
```
/api/users/{user_id}/
```
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/3407fd31-ab37-4ec9-b70b-45a240e1cdff)
- Use the access token from the response for authentication.
- Copy and Paste the access token in the current_value for the Variable `AUTH_TOKEN` of the collection or your enviornment. <br>
<!--alignment fix comment-->
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/3f61de13-6064-41a2-92b1-2fc7594a57d7)
<br>
- Without the token, No Alert API can be run as the user is get from the token only.
- Once the token value has been pasted in the `AUTH_TOKEN`, we can move on to Alerts APIs.
### Create Alert
To create an Alert, we can use the `Create Alert` request of the collection.
- It is a `POST` request where the `price` at which the alert is to be triggered needs to be passed. `price` can be a decimal value.
- The endpoint is
```
/api/alerts/create/
```
- Sample Request Body
```
{
    "price": 42810
}
```
- This creates an object for the UserAlert and returns the `id`, `status` and `price` in response <br>
<!--alignment fix comment-->
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/66b58ad8-263c-4a9a-851b-bf0d4af9ae73)
### Delete Alert
To delete an Alert, we can use the `Delete Alert` request of the collection.
- It is a `DELETE` request where the `alert_id` of the alert needs to be passed in the endpoint.
- The endpoint is
```
/api/alerts/delete/{alert_id}/
```
- This deletes the object for the UserAlert and returns the a confirmation message in response. <br>
<!--alignment fix comment-->
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/4a1015ac-b819-48e7-9094-7fbe3d253851)
### Get Specific Alert
To get the details of any specific alert, we can use the `Get Alert by ID` request of the collection.
- It is `GET` request where the `alert_id` needs to be passed in the endpoint.
- The endpoint is
```
/api/alerts/{alert_id}/
```
- This retrieves the details of the particular alert. <br>
<!--alignment fix comment-->
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/6faefc20-bb1a-4158-b6e1-64199036a245)
### Get Alerts List
To List out all the alerts of a User, we can use the `Get Alerts` request of the collection.
- It is a `GET` request that reetrives all the alerts of the user.
- The endpoint is
```
/api/alerts/?page=1
```
- The query param `page` is optional and specifies the page number for the paginated response.
- This gets the list of all alerts of a user in order of `Created`, `Triggered` and then `Deleted`. <br>
<!--alignment fix comment-->
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/61090deb-3ee3-450d-9984-3067969cd99a)
- The results are Cached for a duration of `60 seconds`.
### Filters
- The Alerts for any user can be filtered on their current status.
- This is implemented in the `Get Alerts` request of the collection.
- An optional query parameter called `status` needs to be passed with one of the following values - `created`, `triggered` or `deleted`.
- The endpoint is
```
/api/alerts/?page=1&status={status_value}
```
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/e13f1d4d-1c53-47f0-a15f-66373d0b67c9)
- The results are Cached for a duration of `60 seconds`.
## Project Soltuion
### Price Fetch
- For Live Price of BTC/USDT, I've used the <b>Binance WebSocket</b>. I've used the <b>[trade websocket stream](https://binance-docs.github.io/apidocs/spot/en/#trade-streams)<b> among all the websocket streams.
- I created a utility class in `core/utils.py` file of the project. I've used [websockets](https://pypi.org/project/websockets/) library for connection.
- The websocket is automatically started with app initialization on `runserver` in a seperate thread.
- The data is served in the `on_messaged` method.
- I'm extracting the current price at which the trade happened and checking if any `UserAlert` object exists.
- If any object exists, I'm sending the user's email list and price to a task which runs asynchronously using `celery` and `redis` as broker.
### Email Trigger
- Once the task recieves any email list, it sends a mail to those users from my personal email. <br>
<!--alignment fix comment-->
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/620ed7ac-d64d-423e-be4f-6cc9a9a52614)
- It prints the same mail content/statement on the console as well.
- The print output can be found in the logs of the `celery` container of the docker container.
- The `celery` container is the once which runs the celery worker. <br>
<!--alignment fix comment-->
![image](https://github.com/Jain-Ayush-11/Brine-Task/assets/76158814/41dac6bf-f6f5-4e88-b043-357475a5b463)
### Caching Alerts List
- I've used `Redis` for creating a cache layer.
- The result for `Get Alerts` and `Get Alerts with Filter` are stored seperately based on two different keys.  <br>
### Development Practices
- Used sqlite3 for initial development ad shifted to PostgresQL during end stages and dockerize.
- I've used `safedelete` models and admin for soft delete functionality. ([See Package](https://pypi.org/project/django-safedelete/))
- The status of any alert is assumed to be one of the following
    - `created`: The alert hasn't yet been triggered.
    - `triggered`: The price set by user was reached and alert has been triggered.
    - `deleted`: The alert was deleted. (doesn't matter if it was triggered or not)
- Used `JWT` for authentication.
- Used `PageNumberPagination` from the `rest_framework` pagination class.
- Used `redis` as broker and result-backend for `celery` to implement background/async processing.
- Used `redis` as backend/location for `caching`.
## Resources Used:
- [Binance trade stream documentation](binance-docs.github.io/apidocs/spot/en/#trade-streams)
- [Celery Documentation for Django](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#using-celery-with-django)
- [Django Rest Framework Documentation for Pagination](https://www.django-rest-framework.org/api-guide/pagination/)
- [Stackoverflow](https://stackoverflow.com/)
