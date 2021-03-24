# Importing the module mysql.connector
import mysql.connector as connector


# requires a user to connect to the DB



db_access = 0
# Temp pre-defined names for the local DB
try:
    if db_access == 0:

        hostname = "localhost"

        username = "customers"
        #username = "root"
        password = "customer"
#        password = ""
        db_name = "food_ordering"
 #       db_name = "wordpress_db"


        database_entry = connector.connect(host=hostname,
                                               user=username,
                                               passwd=password,
                                               port="3307",
                                               database=db_name)

        commands = database_entry.cursor()


except ValueError:
    print("Please restart the program and enter the correct values between 0-1")

exit()

