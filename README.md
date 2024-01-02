<img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>

# Content of project
* [General info](#general-info)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
<details>
<summary>Click here to see general information about <b>Project</b>!</summary>
<b>Sending messages with Docker</b>. This project is a simple example of how to use Django REST framework and Docker to create a web application that allows users to send and receive messages. The backend API is built with Django REST framework, which provides a convenient way to create RESTful web services with Python. The backend are packaged as Docker images, which can be easily deployed and run on any machine that supports Docker. The project also includes a docker-compose file that orchestrates the communication between the two containers and a GitHub workflow that automates the testing and deployment of the application. The project demonstrates how to use Django REST framework and Docker to create a scalable, portable, and maintainable web application.</p>
</details>

## Features
<ul>
<li>Project creation and editing</li>
<li>Send and receive messages</li>
<li>Permissions and authentication</li>
<li>Pagination and filtering</li>
<li>Serializers and validators</li>
</ul>

## Technologies
<div>
<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="50" height="50"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" title="Django" alt="Django" width="60" height="60"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original-wordmark.svg" title="Docker" alt="Docker" width="50" height="50"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original-wordmark.svg" title="postgresql" alt="postgresql" width="50" height="50"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/redis/redis-original-wordmark.svg" title="Redis" alt="Redis" width="50" height="50"/>&nbsp;
</div>

## Setup
<ul>
  <li><h4>Running the application</h4></li>
  <pre><code>$ docker-compose build</code></pre>
  <pre><code>$ docker-compose up</code></pre>
  <li><h4>Create super user</h4></li>
  <pre><code>$ python manage.py createsuperuser</code></pre>
</ul>

