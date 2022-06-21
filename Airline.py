"""
    @Author: Akshay Palande
    @Date: 2022-06-18 2:05PM
    @Last Modified by: Akshay Palande
    @Last Modified time: None
    @Title : Airline Registartion system
"""


from UC import AirMain
from passenger import Bookings

def Add_booking_from_console():
    """
        Description: Adding Contact Details form Console & returning that details as an object of Contacts Class
        Parameters: None
        Returns: Returns Conatacts class object having all info
    """
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    address = input("Enter the address: ")
    from_city = input("Enter starting city name: ")
    to_city = input("Enter destination city name: ")
    seat = input("Enter seat number: ")
    phone_number = input("Enter phone_number: ")
    email = input("Enter email address: ")
    booking_obj = Bookings(first_name, last_name, address,
                           from_city, to_city, seat, phone_number, email)
    return booking_obj


def Storing_bookings_in_list():
    """
        Description: Adding Contact Details form Console in list
        Parameters: None
        Returns: Returns a list containing objects of Contact Class that is taken form Console i.e. User
    """
    while(True):
        booking_obj = Add_booking_from_console()
        booking_list.append(booking_obj)
        bookings_add_choice = input(
            "Enter \"Yes\" for adding more & \"No\" to stop adding: ")
        if (bookings_add_choice.upper() == "N"):
            break
    return booking_list
    


def updating_bookings(book_list):
    """
        Description: Editing Contact Details form Console i.e. by user choice
        Parameters: None
        Returns: Returns a list containing objects of Contact Class that is taken form Console i.e. User
    """
    updated_or_deleted_person_name = input(
        "Enter the name of person, whom details you want to update or delete(filename): ").upper()
    try:
        for item in book_list:
            if item.first_name.upper() == updated_or_deleted_person_name:
                choice = input(
                    "Enter choice u want to edit:\n 1 : FN,2 : LN,3 : Address,4 : From,5 : To,6 : Seat,7 : Phone,8 : Email")
                if (choice == "1"):
                    fn = input("Enter updated first name: ")
                    item.first_name = fn
                elif (choice == "2"):
                    ln = input("Enter updated last name: ")
                    item.last_name = ln
                elif (choice == "3"):
                    addrs = input("Enter updated address: ")
                    item.address = addrs
                elif (choice == "4"):
                    from_city = input("Enter updated from_city: ")
                    item.from_city = from_city
                elif (choice == "5"):
                    to_city = input("Enter updated to_city: ")
                    item.to_city = to_city
                elif (choice == "6"):
                    seat = input("Enter updated seat number: ")
                    item.seat = seat
                elif (choice == "7"):
                    phn_no = input("Enter updated phone number: ")
                    item.phone_number = phn_no
                elif (choice == "8"):
                    email = input("Enter updated email: ")
                    item.email = email
                elif (choice == "9"):
                    book_list.remove(item)
                else:
                    print("Invalid Choice")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    booking_list = []
    Storing_bookings_in_list()
    user_choice = input("Do u want to update or cancel Bookings \"Yes\" OR \"No\":").upper()
    if (user_choice.upper() == "Yes"):
        updating_bookings(booking_list)
    for item in booking_list:
        print(str(item))