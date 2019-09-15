# official mysql image
FROM mysql:latest
ENV MYSQL_DATABASE DEVOPS_USERS
COPY ./*.sql /docker-entrypoint-initdb.d/
#EXPOSE 3306 -- base image already exposes on this port