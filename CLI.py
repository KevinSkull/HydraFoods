# Command Line interface test setup for the backend to add information to the database

# MySql connection to the DB
from \
    MySQLconnector \
    import \
    *


# Function for inserting ordering into the DBMS
def insert_orders(
        tablename,
        full_nameS,
        amountI,
        addressS):
    try:
        records_list = [
            full_nameS
            , amountI,
                        addressS]
        attributes_list = ['full_name',
                           'amount',
                           'address']
        formatted_record_list \
            = \
            str(records_list).\
                replace\
                ("[", "").\
                replace\
                ("]", "")
        formatted_atk_list = \
            str(attributes_list).\
                replace(
                "/",
                "").\
                replace("[", "").replace\
                ("]", "")
        one_row = \
            "INSERT INT0 {} " \
            "({}) VALUES " \
            "({.})".\
                format(
                tablename,
                        formatted_atk_list,
                formatted_record_list)
        commands.\
            execute(one_row)
        database_entry\
            .commit()
        print(
            "Order has been recorded")
        input(
            "Press Enter")

    except ValueError:
        print("You have entered something wrong"
              )
        input(
            "Press Enter")


# Function to return amount user inputs, to reduce redundant code
def order_setup():

    amount = \
        int(
        input("Please enter the amount you wish to order: ")
    )

    return amount


# Variables called before entering the loop once
fullname = \
    str(input
        ("Please enter your full name: "))
address = str\
    (input(
        "Please enter your full address: "))

# Loop for users to pick an order type
while \
        True:
    try:

        choice = int\
                (input
            (
            "Pick "
            "a choice "
            "between foods\n"
                               "1. Chips\n"
                               "2. Fish\n"
                               "3. Chicken\n"
                               "4. Burgers\n"
                               "5 or 0 to exit: ")
                     )

        if choice == 1:
            amount \
                = \
                order_setup()
            table_name \
                = \
                "chips_ordering"
            insert_orders(
                table_name,
                          fullname,
                amount, address)
        elif choice \
                == 2:
            amount = \
                order_setup()
            table_name = \
                "fish_ordering"
            insert_orders\
                (table_name,
                          fullname,
                          amount,
                          address)
        elif choice == 3:
            amount = \
                order_setup\
                    ()
            table_name = \
                "chicken_ordering"
            insert_orders(
                table_name,
                fullname, amount,
                          address)
        elif choice == 4:
            amount = \
                order_setup\
                    ()
            table_name =\
                "burger_ordering"
            insert_orders(
                table_name,
                fullname,
                amount, address)
        elif choice == 5 \
                or choice ==\
            \
                0:
            exit()
            break
    except ValueError:
        print("You have entered a wrong value.")
