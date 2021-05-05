# Command Line interface test setup for the backend to add information to the database

# MySql connection to the DB
from MySQLconnector import *
import time


# Function for inserting ordering into the DBMS
def insert_orders(form_id, field_id, user_info, auto):
    print(auto, "This is insert orders")
    try:
        records_list = ["", auto, form_id, field_id, user_info, time.strftime("%Y-%m-%d %H:%M:%S")]
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

def make_entry_visible(form_id, fullname, field_id, field_id2, field_id3, auto):
    print(auto, "This is entries visible")

    a = "{\""+ str(field_id) +"\":{\"name\":\"Name\",\"value\":\"" \
        + fullname + "\",\"id\":"+ str(field_id) +\
        ",\"type\":\"name\",\"first\":\"\",\"middle\":\"\",\"last\":\"\"},\"" + str(field_id2) + \
        "\":{\"name\":\"Amount\",\"value\":\""+str(amount)+"\",\"id\":"+str(field_id2)+",\"type\":\"number\"},\""\
        +str(field_id3)+"\":{\"name\":\"Address\",\"value\":\""+address+"\",\"id\":"+str(field_id3)+",\"type\":\"textarea\"}}"

    records_list = [auto, form_id, "0", "1", "", "", "0", "0", a, "",
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
                           "5 or 0 to exit:"))

    str_value = open('log.txt', 'r').read()
    value = int(str_value)
    value += 1
    open('log.txt', 'w').write(str(value))

    if choice == 1:
        # note form_id and field_id is dependent on your DB wpforms_entry_field information
        amount = order_setup()
        insert_orders(54, 9, fullname, value)
        insert_orders(54, 11, amount, value)
        insert_orders(54, 13, address, value)
        make_entry_visible(54, fullname, 9, 11, 13, value)
    elif choice == 2:
        amount = order_setup()
        insert_orders(57, 9, fullname, value)
        insert_orders(57, 14, amount, value)
        insert_orders(57, 13, address, value)
        make_entry_visible(57, fullname, 9, 14, 13, value)
    elif choice == 3:
        amount = order_setup()
        insert_orders(59, 14, fullname, value)
        insert_orders(59, 15, amount, value)
        insert_orders(59, 13, address, value)
        make_entry_visible(59, fullname, 14, 15, 13, value)
    elif choice == 4:
        amount = order_setup()
        insert_orders(58, 9, fullname, value)
        insert_orders(58, 14, amount, value)
        insert_orders(58, 13, address, value)
        make_entry_visible(58, fullname, 9, 14, 13, value)
    elif choice == 5 or choice == 0:
        exit()
        break

