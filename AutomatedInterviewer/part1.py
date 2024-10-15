# Assignment 2
"""
 Automated interviewer: The purpose of this Python program is to operate in a welcome booth at the Seattle Python Users conference.
 All delegates will be expected to line up at one of the many terminals and enter their details into the program you are going to write.
"""

#########
#   1   #
#########
print("\n🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷"
      "\nWELCOME TO THE SEATTLE PYTHON USERS CONFERENCE! \nLet's get you checked in... \n")

# The program should ask for the delegate's name:
attendee_name = input("What name would you like printed on your name tag? \t")

#  Display the user's answer:
print("Thank you! Your name tag will read: ", attendee_name, "\n")

# The program should ask:  "What is your conference ID?"
attendee_ID = input("Please help me to locate your registration information.  What is your conference ID? \t")

#  Display the user's answer:
print("🗸 Okay, I have found the conference registration records for:", attendee_ID + ".\n")

# The program should ask which organization the delegate represents:
attendee_org = input("Which organization are you associated with? \t")

#  Display the user's answer:
print('Thank you. I will print " ', attendee_org, ' " on the line underneath', attendee_name, 'on your name tag. \n')

# The program should ask for the attendee's email address:
print("Please help us to reach you in case of lost & found items, schedule changes, emergencies, etc.")
attendee_phone = input("If we need to reach you by text, what phone number should we use? \t")
attendee_email = input("What email address would you like conference information to be sent to? \t")

#  Display the user's answer:
print("Thank you! If necessary during the conference, we will contact you at: ", attendee_email, " or ", attendee_phone, "\n")

# The program should ask about any food preferences:
attendee_food_choice = input("Your registration included tickets to the Saturday night banquet."
                             "\nWhich do you prefer for your entree:  chicken, fish, or vegetarian? \t")

#  Display the user's answer:
print("Thanks! I have made a note in the catering system that your dining preference is: ", attendee_food_choice)


#########
#   2   #
#########

