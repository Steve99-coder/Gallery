# Gallery 

#### Author: [Stephen Nderitu](https://github.com/Steve99-coder/Gallery)


* Link to live site: [Gallery](https://galleria12.herokuapp.com/)

## Description
This is a gallery app that users can be able to view images,search for different categories of photos,copy a link to the photo to share with my friends,view photos based on the location they were taken.




## Setup and installations
* Fork the data .
* git clone the gallery repo.
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`



## Getting started

### Prerequisites
* python3.6
* virtual environment
* pip

#### Clone the Repo 
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
python3 -m venv virtual
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
python3 manage.py check
python manage.py makemigrations gallery
python3 manage.py sqlmigrate gallery 0001
python3 manage.py migrate
```

#### Run the app
```bash
python3 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test gallery`
        
## Technologies Used

* [Python3.8](https://docs.python.org/3/)
* Django 
* Postgresql 
* Boostrap
* HTML

### License

* [[License: MIT]](Licence.md) <stevenderitu99@gmail.com>