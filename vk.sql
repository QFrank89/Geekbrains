DROP database IF exists VK;
create database VK;
USE VK;

create table users(
	id bigint unsigned not null auto_increment primary key,
	firstname varchar(100),
    lastname varchar(100),
    email varchar(100) unique,
    phone bigint unsigned unique
);
