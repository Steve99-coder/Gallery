# Gallery 

#### Author: [SteveNderitu](https://github.com/Steve99-coder/Gallery)


* Link to live site: [Gallery]()

## Description
This is my photo gallery where the user can be able to view images and also load them using the link.




## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* python3.6
* virtual environment
* pip

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/Steve99-coder/Gallery
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='rdtfyguihjohucbdsjnc'
DEBUG=True
DB_NAME='gallery'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py check
python manage.py makemigrations news
python3.6 manage.py sqlmigrate news 0001
python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)


## Bugs

* There are no known bugs at the moment
## Testing the Application
`python manage.py test gallery`
        
## Built With

* [Python3.6](https://docs.python.org/3/)
* Django 
* Postgresql 
* Boostrap
* HTML

### License

* [[License: MIT]](Licence.md) <stevenderitu99@gmail.com>