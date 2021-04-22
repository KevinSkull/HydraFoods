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

def make_entry_visible(form_id, fullname, field_id, field_id2, field_id3):

        records_list = [auto_increment, form_id, "0", "1", "", "", "0", "0","{\"{}\":{\"name\":\"Name\",\"value\":\"{}\",\"id\":{},\"type\":\"name\",\"first\":\"\",\"middle\":\"\",\"last\":},\"{}\":{\"name\":\"Amount\",\"value\":\"{}\",\"id\":{},\"type\":\"number\"},\"{}\":{\"name\":\"Address\",\"value\":\"{}\",\"id\":{},\"type\":\"textarea\"}}".format(field_id, fullname, field_id, field_id2, amount, field_id2, field_id3, address, field_id3), "",
                        time.strftime("%Y-%m-%d %H:%M:%S"), time.strftime("%Y-%m-%d %H:%M:%S"), "::1", "", ""]
        attributes_list = ['entry_id', 'form_id',"post_id", "user_id", "status","type", "viewed", "starred",
                           "fields", "meta",
                           "date", "date_modified", "ip_address", "user_agent", "user_uuid"]
        formatted_record_list = str(records_list).replace("[", "").replace("]", "")
        formatted_atk_list = str(attributes_list).replace("'", "").replace("[", "").replace("]", "")
        one_row = "INSERT INTO {} ({}) VALUES ({})".format("wp_wpforms_entries", formatted_atk_list,
                                                           formatted_record_list)
        commands.execute(one_row)
        db_setup.commit()




# Function to return amount user inputs, to reduce redundant code
def order_setup():

    amount = int(input("Please enter the amount you wish to order: "))

    return amount


# Variables called before entering the loop once

fullname = str(input("Please enter your full name: "))
address = str(input("Please enter your full address: "))

# Loop for users to pick an order type
while True:


        choice = int(input(" Pick a choice between foods\n"
                               "1. Chips\n"
                               "2. Fish\n"
                               "3. Chicken\n"
                               "4. Burgers\n"
                               "5 or 0 to exit:"
                           "6 test:  "))

        if choice == 1:
            amount = order_setup()

            # note form_id and field_id is dependent on your DB wpforms_entry_field information
            insert_orders(54, 9, fullname)
            insert_orders(54, 11, amount)
            insert_orders(54, 13, address)
        elif choice == 2:
            amount = order_setup()
            insert_orders(57, 9, fullname)
            insert_orders(57, 14, amount)
            insert_orders(57, 13, address)
            make_entry_visible(57, fullname, 9, 14, 13)
        elif choice == 3:
            amount = order_setup()
            insert_orders(59, 14, fullname)
            insert_orders(59, 15, amount)
            insert_orders(59, 13, address)
        elif choice == 4:
            amount = order_setup()
            insert_orders(58, 9, fullname)
            insert_orders(58, 14, amount)
            insert_orders(58, 13, address)

        elif choice == 5 or choice == 0:
            exit()
            break

