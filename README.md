# nsql_app

A flask application with the natural language to sql capability on the Chinook Database.

# How to run

 1. On local env:
        `export FLASK_DEBUG=1`
        `flask run`

 2. On PROD:
        `to be implemented`
#
Docker usage:

1. local env:
   -  Build docker image:
         Use `docker-compose up --build` to build the docker container with the aws secrets
   -  Create Docker Container:
         `docker -p 5000:5000 <docker-image-name>`

2. Ngrok:
   -  Using edge with private endpoint:
      `docker run --net=host -it -e NGROK_AUTHTOKEN=<TOKEN> ngrok/ngrok tunnel --label edge=<edge> 5000`
   -  Using Venilla ngrok with randome endpoint:
      `docker run --net=host -it -e NGROK_AUTHTOKEN=<TOKEN> ngrok/ngrok:latest http 5000`
   
   Generate Token and read more [Here](https://dashboard.ngrok.com/get-started/your-authtoken)

3. Production:
   Using CICD pipeline with github action and AWS ECS.
   
# pages:

- /Home  -> the main page for all the natural language prompts from the end user and responces
- WIP: /admin  -> admin purposes

# Model Features:

- LLM based N-SQL inference setup
- Context based infernece

# Main Development versions:

- python Version 3.12.2
- Flask


## Happy coding...
