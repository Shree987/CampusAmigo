# CampusAmigo

## Installation
### Cloning repository
Clone the repository to download the project
```
>> git clone https://github.com/Shree987/CampusAmigo.git
>> cd CampusAmigo/Project
```
OR
Update the repository if already downloaded
```
>> cd CampusAmigo
>> git pull origin master
>> cd Project
```

### Creating Virtual Environment
Create a virtual envionment for the project (only if it is not present)
#### Windows
Install the virtual environment
```
>> pip3 install virtualenv
```
Create an instance
```
>> virtualenv -p python env
```
Activate the virtual environment
```
>> env\Scripts\activate
```

#### Ubuntu
Install the virtual environment
```
>> pip3 install virtualenv
```
Create an instance
```
>> virtualenv -p python env
```
Activate the virtual environment
```
>> source env/bin/activate
```
### Install Django
Install Django for the project. Ignore if it is already downloaded.
```
>> pip install django
```

### Migrations
Apply the migrations to create the tables in database.
```
>> cd campus_amigo
>> python manage.py makemigrations
>> python manage.py migrate
```
*NOTE: Ignore the warning messages regarding URL*
### Server
Run the server to run project.
```
>> python manage.py runserver
```
