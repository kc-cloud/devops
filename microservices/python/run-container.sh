docker run -d -p 5000:5000 \
    -e db_username=root \
    -e db_password=welcome1 \
    -e db_name=DEVOPS_USERS \
    -e db_host=172.17.0.2 \
    --name devops-python \
    devops-python