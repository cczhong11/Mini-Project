# Alpine Linux as the base image
FROM ubuntu:latest

# Install packages 
RUN apt update && \
    apt-get upgrade -y && \
    apt install vim-tiny -y &&\
    apt install curl -y  &&\
    apt-get install -y locales python3-pip python3-dev python3-virtualenv &&\
    pip3 install flask
# update pip

ENV PYTHONUNBUFFERED=0

EXPOSE 6000
# index.html must be in the current directory
# or must be referred to using an absolute path
ADD pyService.py /
# Define the command which runs when the container starts

#CMD [ "python3","pyService.py" ] 

ENTRYPOINT [ "python3","pyService.py" ]