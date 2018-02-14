# Sample Python Django Backend Running in a Docker container
This is a sample Python Django REST application with JSON Web Tokens (JWT) implemented for authentication of specific services. The app is packaged and deployed in a Docker container, along with the supporting applications via the docker-compose file.

THIS REPO IS UNDER CONSTRUCTION AND STILL IN PROGRESS.

Curently, I have only implemented two very basic services, some quick tests, and containerized the app. Up next is the JWT implementation ...

## Host VM
I set up the Vagrantfile to launch an Ubuntu VM that you can run the containers. However, I have NOT set up the Ansible playbook yet to install Docker and Docker Compose, so for now this vm is useless unless you install everything manually.

## Docker Compose
Everything needed to run the sample application is in the `docker-compose.yml` and `Dockerfile` files. This includes the following containers:

* Python Django App (in progress)
* MySQL
* PHPMyAdmin
* Nginx (comming at some point)

The MySQL container is just for development/presentation purposes. Though I did add some persistence via the volume mount, this would not fly for a production situation. Additionally, I have added the MySQL creds via ENV variable and a SQL file. This should be done correctly either via secrets or if you're using Ansible, stored in the vault.

To deploy everything, simply run:

`docker-compose up --build -d`
