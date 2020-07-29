FROM python:3-alpine

LABEL "com.github.actions.name"="update auth0 web origin"
LABEL "com.github.actions.description"="Github action to update auth0 web origin update auth0 web origin"
LABEL "com.github.actions.repository"="https://github.com/dhanvi/update-auth0-web-origin"
LABEL "com.github.actions.maintainer"="Tummala Dhanvi <dhanvicse@gmail.com>"
LABEL "com.github.actions.icon"="shield"
LABEL "com.github.actions.color"="white"

ADD main.py .

ENTRYPOINT ["python3","/main.py"]
