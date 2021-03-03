import mysql.connector as connector
import getpass


def user_access(hostname, username, password):
    database_entry = connector.connect(host=hostname, user=username, passwd=password, port="3306")
    return database_entry


def user_access_db(hostname, username, password, db_name):
    database_entry = connector.connect(host=hostname, user=username, passwd=password, port="3306",
                                           database=db_name)
    return database_entry