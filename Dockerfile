# Marakulin Andrey @annndruha
# 2022

# Base image
FROM python:3.10.0

# Create directoris inside container
COPY . /diploma-bot
WORKDIR /diploma-bot

# Install libs from requirements
RUN pip install --no-cache-dir -r requirements.txt

# Specify the port number the container should expose 
EXPOSE 42

# Run the file
CMD ["pwd"]
##===== Example docker Ubuntu command:
# docker run -d --name diploma-bot -v /root/diploma-bot:/diploma-bot IMAGEID
##==== Next, add auth.ini file to /root/diploma-bot
##==== and restart container
# docker stop diploma-bot
# docker start diploma-bot
