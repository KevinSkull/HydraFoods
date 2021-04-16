# Command Line interface test setup for the backend to add information to the database

# MySql connection to the DB
from MySQLconnector import *
import os
import time

if not os.path.exists('log.txt'):
    with open('log.txt', 'w') as f:
        f.write('0')
with open('log.txt', 'r') as f:
    st = int(f.read())
    st += 1
with open('log.txt', 'w') as f:
    f.write(str(st))

f = open("log.txt", "r")
auto_increment = f.read()


# Function for inserting ordering into the DBMS
def insert_orders(form_id, field_id, user_info):
    try:
        records_list = ["", auto_increment, form_id, field_id, user_info, time.strftime("%Y-%m-%d %H:%M:%S")]
        attributes_list = ['id', 'entry_id', 'form_id', "field_id", "value", "date"]
        formatted_record_list = str(records_list).replace("[", "").replace("]", "")
        formatted_atk_list = str(attributes_list).replace("'", "").replace("[", "").replace("]", "")
        one_row = "INSERT INTO {} ({}) VALUES ({})".format("wp_wpforms_entry_fields", formatted_atk_list, formatted_record_list)
        commands.execute(one_row)
        db_setup.commit()
        print("Order has been recorded")

    except ValueError:
        print("You have entered something wrong")
        input("Press Enter")


# Function to return amount user inputs, to reduce redundant code
def order_setup():

    amount = int(input("Please enter the amount you wish to order: "))

    return amount


# Variables called before entering the loop once

fullname = str(input("Please enter your full name: "))
address = str(input("Please enter your full address: "))

# Loop for users to pick an order type
while True:
    try:

        choice = int(input(" Pick a choice between foods\n"
                               "1. Chips\n"
                               "2. Fish\n"
                               "3. Chicken\n"
                               "4. Burgers\n"
                               "5 or 0 to exit: "))

        if choice == 1:
            amount = order_setup()

            # note form_id is 75 for chip, 78 for fish, 81 for burgers, 83 for Chicken
            # note field_id is 0 for name, 8 for amount, 7 for address
            insert_orders(75, 0, fullname)
            insert_orders(75, 8, amount)
            insert_orders(75, 7, address)
        elif choice == 2:
            amount = order_setup()
            insert_orders(78, 0, fullname)
            insert_orders(78, 8, amount)
            insert_orders(78, 7, address)

        elif choice == 3:
            amount = order_setup()
            insert_orders(81, 0, fullname)
            insert_orders(81, 8, amount)
            insert_orders(81, 7, address)
        elif choice == 4:
            amount = order_setup()
            insert_orders(83, 0, fullname)
            insert_orders(83, 8, amount)
            insert_orders(83, 7, address)
        elif choice == 5 or choice == 0:
            exit()
            break
    except ValueError:
        print("You have entered a wrong value.")
