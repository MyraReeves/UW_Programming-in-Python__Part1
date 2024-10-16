#############
#   Lists   #
#############

# Consult the documentation on lists, and rewrite the program so that a simple change
# to the question is all that is needed to record all the relevant answers.

initial_questions = [
    'your name',
    'your conference ID',
    'the organization you represent',
    'your email address',
    'your food preference for the banquet dinner'
]

available_workshops = [
    'Python for Beginners',
    'Database Development with Python',
    'Python for Data Science',
    'Advanced Python for Application Developers',
]


print("\n🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷"
      "\nWELCOME TO THE SEATTLE PYTHON USERS CONFERENCE! \nLet's get you checked in... \n")

# Iterating thru the initial questions list:
for question in initial_questions:
        reply = input(f'What is {question}? \t')
        print(f'You answered: {reply} \n')

print("Thank you!  You are almost done checking in."
      "\nAll that remains is for you to sign up for the interactive workshop(s) you plan on attending...\n")

# Iterating thru the list of workshop sessions:
for workshop in available_workshops:
    while True:
        attendance = input(f'Would you like to attend: {workshop}? \nPlease answer with: YES or NO \t')
        if attendance.upper() == 'YES' or attendance.upper() == 'NO':
            break
        else:
            print('YES or NO?')

    if attendance.upper() == 'YES':
        print(f'Great! I\'ve signed you up to attend {workshop}! \n')

    else:
        print(f'Thank you for letting us know that you do NOT plan on attending {workshop} \n')


print("\n\n___________________________________________________________\n"
      "CHECK-IN COMPLETE! "
      "\n👉 Please proceed to the next station to pick up your name tag from the printer. "
      "\nWe hope you enjoy the conference!")

