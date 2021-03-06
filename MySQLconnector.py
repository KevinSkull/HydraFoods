import mysql.connector as connector


def user_access_db(hostname, username, password, db_name):
    database_entry = connector.connect(host=hostname, user=username, passwd=password, port="3306",
                                               database=db_name)

    return database_entry


db_access = 0
try:

    if db_access == 0:

        hostname = "localhost"

        username = "customers"

        password = "customer"

        db_name = "food_ordering"
        try:
            db_setup = user_access_db(hostname, username, password, db_name)
            commands = db_setup.cursor()

        except:
            print("\nWrong Values were entered, please restart the program.")
            exit()
    else:
        print("Please restart the program and enter the correct values between 0-1")
        exit(0)


except ValueError:
    print("Please restart the program and enter the correct values between 0-1")
    exit()




