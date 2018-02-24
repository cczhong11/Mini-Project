# Alpine Linux as the base image
FROM ubuntu:latest

# Install packages 
RUN apt update && \
    apt-get upgrade -y && \
    apt install vim-tiny -y &&\
    apt install curl -y  &&\
    apt-get install -y locales python3-pip python3-dev python3-virtualenv &&\
    pip3 install flask &&\
    pip3 install requests
# update pip



EXPOSE 5000
# index.html must be in the current directory
# or must be referred to using an absolute path
ADD playground.py /
ADD site /site
# Define the command which runs when the container starts

#CMD [ "python3","pyService.py" ] 

ENTRYPOINT [ "python3","playground.py" ]