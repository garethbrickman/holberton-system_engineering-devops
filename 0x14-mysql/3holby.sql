-- Creates new user, grants replication permission, grants SELECT for mysql.user table
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'root';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'root';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
