FROM debian:buster

ARG DEBIAN_FRONTEND="noninteractive"
ARG DEBCONF_NOWARNINGS="yes"

RUN apt-get update && \
    apt-get install --yes nginx

COPY ./srcs/default /etc/nginx/sites-enabled/default

EXPOSE	8080

CMD ["nginx", "-g" ,"daemon off;"]