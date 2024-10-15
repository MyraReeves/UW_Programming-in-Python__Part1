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
print("Thank you! Your name tag will read: ", attendee_name.upper(), "\n")

# The program should ask which organization the delegate represents:
attendee_org = input("Which organization are you associated with? \t")

#  Display the user's answer:
print('Thank you. I will print "' + attendee_org.title() + '" on the line underneath', attendee_name,
      'on your name tag. \n')

# The program should ask:  "What is your conference ID?"
attendee_ID = input("Please help me to locate your registration information.  What is your conference ID? \t")

#  Display the user's answer:
print("🗸 Okay, I have found the conference registration records for:", attendee_ID + ".\n")

# The program should ask for the attendee's email address:
print("Please help us to reach you in case of lost & found items, schedule changes, emergencies, etc.")
attendee_phone = input("If we need to reach you by text, what phone number should we use? \t")
attendee_email = input("What email address would you like conference information to be sent to? \t")

#  Display the user's answer:
print("Thank you! If necessary during the conference, we will contact you at: ", attendee_email, " or ", attendee_phone,
      "\n")

# The program should ask about any food preferences:
attendee_food_choice = input("During registration, you purchased a ticket for the Saturday night banquet!"
                             "\nWhich do you prefer for your entree:  chicken, fish, or vegetarian? \t")
while attendee_food_choice.strip().lower() != "chicken":
    if attendee_food_choice.strip().lower() == "fish":
        print("Thanks! I have made a note in the catering system that your dining preference is: fish \n")
        break
    elif attendee_food_choice.strip().lower() == "vegetarian":
        print("Thanks! I have made a note in the catering system that your dining preference is: vegetarian \n")
        break
    else:
        attendee_food_choice = input("INVALID RESPONSE. There are only 3 available options."
                                     "\nPlease type one of the following choices: \t\t chicken \t\t fish \t\t vegetarian \t")
else:
    # Display the user's answer:
    print("Thanks! I have made a note in the catering system that your dining preference is: chicken \n")


#########
#   2   #
#########
# The program should then prompt the user if they wish to attend the following sessions:
print("You are almost done checking in."
      "\nAll that remains is for you to sign up for the interactive workshop(s) you plan on attending...\n")

# Python for Beginners
py_beginners = "Python for Beginners"
attend_py_beginners = input("1. Will you be attending " + py_beginners.upper() + "? \nPlease answer with: YES or NO \t")
while attend_py_beginners.strip().upper() != "YES":
    if attend_py_beginners.strip().upper() == "NO":
        break
    else:
        attend_py_beginners = input("You entered an invalid answer! Please answer with either YES or NO"
                                    "\nWill you be attending " + py_beginners.upper() + "? \t")

# Database Development with Python
db_dev = "Database Development with Python"
attend_db_dev = input("\n2. Will you be attending " + db_dev.upper() + "? \nPlease answer with: YES or NO \t")
while attend_db_dev.strip().upper() != "YES":
    if attend_db_dev.strip().upper() == "NO":
        break
    else:
        attend_db_dev = input("You entered an invalid answer! Please answer with either YES or NO"
                              "\nWill you be attending " + db_dev.upper() + "? \t")

# Python for Data Science
py_data_science = "Python for Data Science"
attend_py_data_science = input(
    "\n3. Will you be attending " + py_data_science.upper() + "? \nPlease answer with: YES or NO \t")
while attend_py_data_science.strip().upper() != "YES":
    if attend_py_data_science.strip().upper() == "NO":
        break
    else:
        attend_py_data_science = input("You entered an invalid answer! Please answer with either YES or NO"
                                       "\nWill you be attending " + py_data_science.upper() + "? \t")

# Advanced Python for Application Developers
py_app = "Advanced Python for Application Developers"
attend_py_app = input("\n4. Will you be attending " + py_app.upper() + "? \nPlease answer with: YES or NO \t")
while attend_py_app.strip().upper() != "YES":
    if attend_py_app.strip().upper() == "NO":
        break
    else:
        attend_py_app = input("You entered an invalid answer! Please answer with either YES or NO"
                              "\nWill you be attending " + py_app.upper() + "? \t")

# For improved viewing of the output, I inserted a break before confirming their choices:
confirmation = input("\nPress any key to view what you chose..... ")

# Using conditionals, print back out confirmation of their choices:
print("\n\nYou have signed up to ATTEND the following workshops:")
if attend_py_beginners.strip().upper() == "YES":
    print("✔️ ", py_beginners)

if attend_db_dev.strip().upper() == "YES":
    print("✔️ ", db_dev)

if attend_py_data_science.strip().upper() == "YES":
    print("✔️ ", py_data_science)

if attend_py_app.strip().upper() == "YES":
    print("✔️ ", py_app)

print("\n\nYou DECLINED the following workshops:")
if attend_py_beginners.strip().upper() == "NO":
    print("❌ ", py_beginners)

if attend_db_dev.strip().upper() == "NO":
    print("❌ ", db_dev)

if attend_py_data_science.strip().upper() == "NO":
    print("❌ ", py_data_science)

if attend_py_app.strip().upper() == "NO":
    print("❌ ", py_app)

print("\n\n___________________________________________________________\n"
      "\aCHECK-IN COMPLETE! "
      "\n👉 Please proceed to the next station to pick up your name tag from the printer. "
      "\nWe hope you enjoy the conference!")
