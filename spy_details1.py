# PROJECT : *****SPY-CHAT***** ! [ ACADVIEW ] ||||| spy_details1.py

from datetime import datetime

# CLASS SPY WHICH CONTAINS ALL THE DETAILS OF THE SPY
class Spy:
    def __init__(self,name,salutation,rating,age):
        self.name = name
        self.salutation = salutation
        self.rating = rating
        self.age = age
        self.chats = []
        self.is_online = True
        self.current_status_message = None

# CLASS TO STORE THE CHATS
class ChatMessage:
    def __init__(self,message,sent_by_me,avg_words):
        self.message = message
        self.sent_by_me = sent_by_me
        self.time = datetime.now()
        if avg_words is not 0:
            self.avg_words = avg_words
        else:
            self.avg_words = 0
spy = Spy('JAYRAJ', 'Mr.' , 4.9,20)

friend_one = Spy('Gaurav', 'Mr.', 4.9, 20)
friend_two = Spy('Harsh', 'Mr.', 4.39, 19)
friend_three = Spy('Aditya', 'Mr.', 4.95, 18)
friends = [friend_one, friend_two, friend_three]

