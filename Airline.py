"""
    @Author: Akshay Palande
    @Date: 2022-06-18 2:05PM
    @Last Modified by: Akshay Palande
    @Last Modified time: None
    @Title : Airline Registartion system
"""


from UC import AirMain

class Bookings():
    
    def __init__(self, first_name, last_name, address, from_city, to_city, seat, phone_number, email):
        """
            Description: Constructor of Bookings Class
            Parametres: Takes class fields
            Retuns: None, Just initialize the values of object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.from_city = from_city
        self.to_city = to_city
        self.seat = seat
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        """
            Description: To return textual content of the Booking class Object
            Parameters: Takes Instance (Object) of class as arguments
            Returns: Returns String Representation of object, understandable by User
        """
        return f"Full Name is {self.first_name} {self.last_name}\ntravelling details are {self.from_city} to {self.to_city}a,{self.seat}\nPhone Number & email is {self.phone_number} and {self.email} respectively"


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
            "Enter \"Y\" for adding more & \"N\" to stop adding: ")
        if (bookings_add_choice.upper() == "N"):
            break
    return booking_list


if __name__ == "__main__":
    booking_list = []
    Storing_bookings_in_list()
    for item in booking_list:
        print(str(item))