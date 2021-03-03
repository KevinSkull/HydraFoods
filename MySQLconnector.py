import mysql.connector as connector
import getpass


def user_access(hostname, username, password):
    database_entry = connector.connect(host=hostname, user=username, passwd=password, port="3306")
    return database_entry


def user_access_db(hostname, username, password, db_name):
    database_entry = connector.connect(host=hostname, user=username, passwd=password, port="3306", database=db_name)
    return database_entry


db_access = 0
try:
    hostname = str(input("Please enter the server IP: "))

    username = str(input("Please enter the username: "))

    password = getpass.getpass(prompt="Please enter the password:", stream=None)

    db_name = str(input("Please enter the database you wish to enter: "))
    try:
        db_setup = user_access_db(hostname, username, password, db_name)
        commands = db_setup.cursor()

    except:
        print("\nWrong Values were entered, please restart the program.")
        exit()


except ValueError:
    print("Please restart the program and enter the correct values between 0-1")
    exit()