CREATE TABLE users (
    user_id INT NOT NULL  AUTO_INCREMENT,
    user_name varchar(60),
    user_email varchar(60),
    user_password  varchar(60),
    PRIMARY KEY(user_id)
);