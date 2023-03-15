# Time Scheduler

# Enviroment Set up and Instruction on how to run the program

## Backend: 
```sh

$ python3 -m venv /path/to/new/virtual/environment/CS180

$ source /path/to/venv/bin/activate

Or

$ conda create -n CS180 python=3

$ conda activate CS180
```

Then,

```sh
$ pip install django	

$ pip install mysqlclient	or	$ conda install mysqlclient

$ pip install django-bootstrap-v5 
```
# DataBase Set up

Install MySQL

```sh
$ mysql -u root -p

$ CREATE USER 'cs180'@'localhost' IDENTIFIED WITH mysql_native_password BY 'cs180';

$ create database CS180;

$ GRANT ALL ON CS180.* TO 'cs180'@'localhost';
```

In the virtual environment,

```sh
$ python manage.py makemigrations

$ python manage.py migrate


$ pip install pip install django_rest_framework

$ pip install django-cors-headers

$ pip install drf-yasg
```

## Front Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

