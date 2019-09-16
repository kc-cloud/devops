#docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=welcome1 --name devops-mysql -v /my/own/datadir:/var/lib/mysql devops-mysql
docker run -h devops-mysql -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=welcome1 --name devops-mysql devops-mysql
