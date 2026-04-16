FROM ubuntu:26.04
RUN apt update
RUN apt install iproute2 -y
RUN apt install python3 -y
# RUN apt install python3-pip -y
CMD [ "python3","-u", "/app/server.py" ]
