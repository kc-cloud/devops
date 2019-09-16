CREATE TABLE users (
    user_id INT NOT NULL  AUTO_INCREMENT,
    user_name varchar(60),
    user_email varchar(60),
    user_password  varchar(60),
    PRIMARY KEY(user_id)
);

insert into users (user_name, user_email, user_password) VALUES('kannan', 'abcd@gmail.com', 'welcome1');
