# Social Reminder
Get reminders for sending messages to friends, family and others. Very handy if you're forgetful (like me) or just
need an extra hand in helping you out.

* Create a virtual environment
```shell
$ virtualenv venv
$ source ./venv/bin/activate
```
* Install requirements
```shell
$ pip install -r requirements.txt
```
___
##Prepare the project.
We use django-environ to read environment variables from the `.env` file in your root directory
```shell
$ echo "SECRET_KEY=ENTERSOMEVERYSECRETKEYWITHMIN50CHARSHERE" > .env
$ ./manage.py migrate
```
If you want to get up and running with test data, you can run this management command. It will
create 100 entries with related tags:
```shell
$ ./manage.py create_test_data
```
____

##Start the app
```shell
$ ./manage.py runserver
```
