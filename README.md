# Web Awards


## Description
Web Awards is a web app that allows users to post their favorite websites for other users to rate `https://web-awards.herokuapp.com/`


## Author


* [**Brian Major**](https://github.com/bryomajor)

## Features


As a user of the web application you will be able to:

1. Sign up and log in
2. View projects posted by other users
3. Post projects
4. Rate a project
5. Edit your profile
6. Generate APIs

## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the app and gets directed to the homepage  | User clicks on a project to review | Directed to the login page | 
If user has no account, they click on `sign up` | User signs up | User is redirected to the log in page |
|  Single projecct loads | User clicks on vote  | Modal appears where they vote |
|  Homepage loads | Click `profile` | User's profile appears | 
| Homepage loads | Click `Submit Project` button | User's redirected to a page where they can upload a project |  
| Homepage loads | User inputs in the search form and presses enter | Searched results show |


## Getting started
### Prerequisites
* python3.6
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/bryomajor/web-awards.git
        $ cd web-awards

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations instagram
        $ python3.6 manage.py migrate 

* To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 manage.py test awards
        
## Technologies Used
* Python3.6
* Django
* HTML
* Bootstrap

This application is developed using [Python3.6](https://www.python.org/doc/), [Django](https://www.djangoproject.com/), [HTML](https://getbootstrap.com/) and [Bootstrap](https://getbootstrap.com/)


## Support and Team
Brian Major


[Slack Me!](https://slack.com/intl/en-ke/)  @bryomajor


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
