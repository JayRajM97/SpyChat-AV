# PROJECT : *****SPY-CHAT***** ! [ ACADVIEW ] ||||| spy_chat.py

'''
We are Importing The files from spy_details here in spy_chat
spy and Chat Message Class
'''
from spy_details1 import spy,Spy,friends,ChatMessage
from steganography.steganography import Steganography
from datetime import datetime


# These are some default status messages , Used in add_status()
STATUS_MESSAGE = ['Sherlock Holmes takes my breath away!' , 'There\'s only one truth' , 'CONCERNED BUT NOT CONSUMED', 'The case called for plain, old-fashioned police leg work!']


'''
Function Used To Add A Friend To The Spy-Chat !
'''
def add_friend():
    new_friend = Spy('','',0.00,0)
    print("\n Enter details of your new friend : ")
    new_friend.name = raw_input("\nEnter the name of your friend : ")
    new_friend.salutation = raw_input("\nAre they Mr. or Ms.? : ")
    new_friend.age = int(raw_input("\nEnter their age : "))
    new_friend.rating = float(raw_input("\nEnter their rating : "))

    pass_name = new_friend.name
    pass_age = new_friend.age

    #Check The Validation Of Name & Age !
    if name_valid(pass_name) is True and age_valid(pass_age) is True :
        friends.append(new_friend)
        print("\nYour friend has been added.")
    else:
        print("Wrong Entry!\tWe can't add the spy with the details you provided.")

    return len(friends)


'''
Function Used To Check The Name !
'''
def name_valid(nme):
    # strip() checks if the string is empty or not and then proceeds
    if nme.strip():
        return True
    else:
        return False


'''
Function Used To Check The Age !
'''
def age_valid(no):

    if no > 12 and no <= 50:
        return True
    else:
        return False


'''
Funtion To Select A Friend
From The List Of Friends
'''
def select_friend():
    try:
        print "\nChose one friend from the list below : "
        x=0
        for friend in friends:
            print"\n%d. %s %s of rating : %.2f and age: %d ." %(x+1 , friend.salutation , friend.name,friend.rating,friend.age)
            x += 1

        friend_selection = int(raw_input("\nEnter your choice : "))
        friend_selection -= 1
        if(len(friends) >= friend_selection):
            print("\nYou selected %s %s ") %(friends[friend_selection].salutation , friends[friend_selection].name)
        else:
            print("WRONG SELECTION! SELECT A VALID OPTION!")

        return (friend_selection)
    except ValueError:
        print("Please enter a correct value for the input!! ")
        return (False)


'''
Funtion To Send Messages
i.e. Encrypted In A Image
'''
def send_message():

        friend_select = select_friend()
        if friend_select is not False:
            input_path = raw_input("Enter the full path of the image : ")
            output_path = raw_input("Enter path where you want to store the output image : ")
            text = raw_input("Enter secret text that you want to encode : ")

            if name_valid(text) is True:
                if len(text.split()) > 100 :
                    print "You're speaking a lot, this is Intolerable!!\nYou're banished from the chat!! "
                    del friends[friend_select]
                elif len(text.split()) == 0 :
                    print "*****DON'T WASTE TIME OF YOUR FRIEND SPY !"
                else:
                    Steganography.encode(input_path , output_path , text)

                    # VARIABLE TO STORE THE DETAILS OF THE NEW CHAT DATA

                    new_chat = ChatMessage(text,True,0)
                    friends[friend_select].chats.append(new_chat)

                    if text == "SOS" or text == "SAVE ME" or text == "Vatican Cameos" or text == "HELP ME" :
                        print " *****THE MESSAGE IS FORWARDED TO ALL THE SPY'S ! THE NEAREST ONE WILL CONTACT YOU , SIT TIGHT !***** "

                    print("Your secret image is ready !")


            else:
                print " You haven't entered any secret message. Please try again!"




'''
Funtion To Read Messages
i.e. Decrypt From The Image
'''
def read_message():


        sender = select_friend()
        if sender is not False:
            words_spoken = None
            orig_image = raw_input("Enter the full path of the image to be decoded: ")
            secret_text = Steganography.decode(orig_image)
            # No. of words (from message) send by SPY
            for word in friends[sender].chats:
                words_spoken = word.avg_words + len(secret_text.split())

            new_chat = ChatMessage(secret_text,False,words_spoken)
            friends[sender].chats.append(new_chat)
            print secret_text
            print"Your secret message has been decoded and saved!"


'''
Funtion To See The Chat History
'''
def read_chat_history():
    read_from = select_friend()
    for i in friends[read_from].chats:
        if i.sent_by_me is True:
            print("\033[1;34m    [%s]   \033[1m    \033[1;31m   You said : \033[1m   %s ") % (i.time.strftime("%H:%M  %d %B %Y"), i.message)
        else:
            print("\033[1;34m   [%s]    \033[1m \033[1;31m  %s  said :    \033[1m  %s ") % ( i.time.strftime("%H:%M %d %B %Y"), friends[read_from].name, i.message)


'''
Funtion To Set A Status Message
'''
def add_status():
    updated_status_message = None
    if spy.current_status_message!=None:
        print("\nYour current status message is :%s") %(spy.current_status_message)
    else:
        print "\nYou don't have any status message set."

    choice = raw_input("Do you want to proceed with the current status message or you want to change it? (Y/N) : ")
    if choice.upper() == 'Y':
        STATUS_MESSAGE.append(spy.current_status_message)
        updated_status_message = spy.current_status_message
    elif choice.upper() == 'N':
        default = raw_input("\nDo you want to select a status message from older status messages? (Y/N): ")
        if default.upper() == 'Y':

            print "\nChoose one of the status from the list below : "
            for i in range(len(STATUS_MESSAGE)):
                print(str(i + 1) + ". " + STATUS_MESSAGE[i] + "\n")
            select_message = int(raw_input("Enter your choice : "))

            if len(STATUS_MESSAGE) >= select_message:
                select_message -= 1
                updated_status_message = STATUS_MESSAGE[select_message]
            else:
                print"\nKindly select a valid input!"


        elif default.upper() == 'N':
            get_message = raw_input("\nEnter your status message : ")
            STATUS_MESSAGE.append(get_message)
            updated_status_message = get_message

        else:
            print " WRONG CHOICE INPUT! \n KINDLY SELECT (Y/N) ?  "

    else:
        print " WRONG CHOICE INPUT! \n KINDLY SELECT (Y/N)"

    if updated_status_message != None:

        print("\nYour current status message is : %s") % (updated_status_message)
    else:
        print " You currently don't have any status message set."


'''
Function To Start The Chat
Using WHILE LOOP , It Calls The Menu Again & Again
'''
def start_chat(spy):
    spy.current_status_message = None

    spy.name = spy.salutation+" "+spy.name
    if spy.age > 12 and spy.age < 50:
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.name) + " and rating of: " + str(
            spy.rating) + " Proud to have you onboard"

        show_menu = True
        while show_menu:
                menu_choice = raw_input("\nWhat do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n")
                if name_valid(menu_choice) is True:
                    menu_choice = int(menu_choice)
                    if menu_choice == 1:
                        print("You chose to update the status.")
                        add_status()
                    elif menu_choice == 2:
                        no_of_friends = add_friend()
                        print("\nYou've %d number of friends in total.") %(no_of_friends)
                    elif menu_choice == 3:
                        send_message()
                    elif menu_choice == 4:
                        read_message()
                    elif menu_choice == 5:
                        read_chat_history()

                    elif menu_choice == 6:
                        show_menu = False
                    else:
                        print "Invalid choice input!"
                        show_menu = False

    elif spy.age < 12:
        print "Sorry ! You are too KIDDO to be an Spy !"
    else:
        print "Sorry ! You are too OLD to be an Spy !"


'''
Starting Of The Project
'''
print "                                                                                   Hey There ! \n                                                                        ***** Welcome To Spy-Chat *****"
question = raw_input(('Do you want to continue as ') + spy.salutation+" "+spy.name + ('( Y/N: ?)'))

if question.upper() == 'Y':
    start_chat(spy)

elif question.upper() == 'N':

    spy = Spy('','',0.00,0)

    spy.name=raw_input("Welcome to spy chat, you must tell me your spy name first:")

    if name_valid(spy.name) is True:
        spy.salutation = raw_input("What should we call you (Mr. or Mrs.)")
        spy.name = spy.salutation + " " + spy.name
        print("Welcome "+spy.name+" to SpyChat")
        spy.age = int(raw_input("Enter the age of your spy :"))
        if age_valid(spy.age) is True:
            spy.rating = float(raw_input("Enter Spy Rating :"))
            if spy.rating >= 5:
                print "You'r an Elite Spy ! "
            elif spy.rating < 5 and spy.rating >= 4:
                print "You'r a Excellent Spy ! "
            elif spy.rating < 4 and spy.rating >= 3.5:
                print "You'r a Good Spy , Yet could do better ! "
            else:
                print "You have to much ! We'll help "

            spy.is_online = True
            print 'Authentication completed! Welcome ' +spy.name + " age:" + str(spy.age) + " with Rating :" + str(spy.rating)
            start_chat(spy)
        else:
            print("Sorry!! You are not eligible to be a spy kiddo!")
    else:
        print('Invalid Input!!')

else:
    print("Please provide a valid input (Y/N)")
