# 0x1A. Application server

### This project in the System engineering & DevOps series is about:

 * How to serve a Flask Application with Gunicorn and Nginx on Ubuntu 14.04
 * Web Server
 * Server
 * Web stack debugging

## General
 * A README.md file, at the root of the folder of the project, is mandatory
 * Everything Python-related must be done using python3
 * All config files must have comments

## Bash Scripts
 * All your files will be interpreted on Ubuntu 14.04 LTS
 * All your files should end with a new line
 * All your Bash script files must be executable
 * Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
 * The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
 * The second line of all your Bash scripts should be a comment explaining what is the script doing

---
File|Task
---|---
0-welcome_gunicorn-upstart_config | an Upstart script that starts a Gunicorn instance to serve web_flask/0-hello_route.py
0-welcome_gunicorn-nginx_config | set Nginx up so that the route /airbnb-onepage/ points to your Gunicorn instance
1-pass_parameter-upstart_config | an Upstart script that starts a Gunicorn instance to serve web_flask/6-number_odd_or_even.py
1-pass_parameter-nginx_config | set Nginx up so that the route/airbnb-dynamic/ points to your Gunicorn instance
3-complete_webapp-upstart_config | an Upstart script that starts a Gunicorn instance to serve web_dynamic/2-hbnb.py
3-complete_webapp-nginx_config | set Nginx up so that the route / points to your Gunicorn instance

## Author
Leine Valente
