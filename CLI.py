# Command Line interface test setup for the backend to add information to the database
from MySQLconnector import *


def insert_order_chips(full_nameS, amountI, addressS):
    try:
        records_list = [full_nameS, amountI, addressS]
        attributes_list = ['full_name', 'amount', 'address']
        formatted_record_list = str(records_list).replace("[", "").replace("]", "")
        formatted_atk_list = str(attributes_list).replace("'", "").replace("[", "").replace("]", "")
        one_row = "INSERT INTO {} ({}) VALUES ({})".format("chips_ordering", formatted_atk_list, formatted_record_list)
        commands.execute(one_row)
        db_setup.commit()
        print("Record(s) have been inserted successfully")
        input("Press Enter")
    except:
        print("You have entered something wrong")
        input("Press Enter")




while True:

    choice = int(input("Pick a choice between foods\n"
                           "1. Chips\n"
                           "2. Fish\n"
                           "3. Chicken\n"
                           "4. Burgers\n"
                           ": "))

    if choice == 1:
        fullname = str(input("Please enter your full name: "))
        amount = int(input("Please enter the amount you wish to order: "))
        address = str(input("Please enter your full address: "))
        insert_order_chips(fullname, amount, address)
        exit()

    elif choice == 2:
        print("Placeholder for SQL code")
    elif choice == 3:
        print("Placeholder for SQL code")
    elif choice == 4:
        print("Placeholder for SQL code")
    elif choice == 5:
        exit()














