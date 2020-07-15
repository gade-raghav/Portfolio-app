# Portfolio-app

A basic django application for dynamic portfolio website

You can change the required variables and host this site from your machine. You can also edit the template to display the content according to your will.

This site shows your public github repos with description and it is required that you add ghub username in variable.py file.(In case there is no description
for a repo, you might run into error. So, disable the description field in ```portfolio/base/views.py``` file.



## Requirements

* [python-3.6](https://www.python.org/downloads/release/python-3611/) 

Make sure you have the above requirement(s) satisified.

* [docker](https://docs.docker.com/engine/install/ubuntu/) (not necessary)


# Usage

First step is to clone the repository
```bash
git clone https://github.com/gadeRaghav/todo-app.git
```

### Edits to be made before hosting

cd into ```portfolio/base``` and edit the variable.py file accordingly.(3 variables are required: Name,github_username,linkedin_username)

cd into ```portfolio/staticfiles/images``` and add your image with name ```dude.jpeg``` 

cd into ```portfolio/base/templates/base/``` and add your personal content in the card.


There are two ways to run this application.

* [Run from ubuntu terminal](#run-from-ubuntu-terminal) 

* [Run using docker](#run-using-docker)


### Run from ubuntu terminal 


Install the requirements from requirements.txt.(django, djangorestframework, django-cors-headers)
```bash
pip3 install -r requirements.txt
```

Switch to portfolio directory and run the server
```bash
cd portfolio
python3.6 manage.py runserver 0.0.0.0:8000
```
and access the app from [http://localhost:8000](http://localhost:8000) !!




**Instead of going through the above steps, you can simply run the app in docker container**

### Run using docker



Run docker build
```bash
docker build --tag <tag-name> . 
```
Run docker image
```bash
docker run --publish 8000:8000 --name <container-name> --detach <tag-name>
```
and access the app from [http://localhost:8000](http://localhost:8000) !!



# Acknowledgement

Thanks to [Github-api](https://developer.github.com/v3/)







