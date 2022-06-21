"""
    @Author: Akshay Palande
    @Date: 2022-06-18 2:05PM
    @Last Modified by: Akshay Palande
    @Last Modified time: None
    @Title : Airline Registartion system
"""


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

