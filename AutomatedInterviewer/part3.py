#############
#   Tuple   #
#############

# Redesign the program so that the entire list of questions is stored in one tuple.
# That way all the questions are in one place and it becomes really easy to add one.

questions_and_answers = (
    'What is your name? ',
    'What is your conference ID? ',
    'Which organization do you represent? ',
    'What is your email address? ',
    'State any food preferences: ',
    'Answer with either YES or NO, \nDo you wish to attend "Python for Beginners"? ',
    'Answer with either YES or NO, \nDo you wish to attend "Database Development with Python"? ',
    'Answer with either YES or NO, \nDo you wish to attend "Python for Data Science"? ',
    'Answer with either YES or NO, \nDo you wish to attend "Advanced Python for Application Developers"? ',
)


print("\n🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷 🔶 🔷"
      "\nWELCOME TO THE SEATTLE PYTHON USERS CONFERENCE! \nLet's get you checked in... \n")


for question in questions_and_answers:
    if 'Answer with either YES or NO,' in question:
        yes_no = input(f'{question} \t')
        if yes_no.upper() == 'YES':
            print("Great! I've recorded your interest to attend! \n")
        elif yes_no.upper() == 'NO':
            print("Ok, I've recorded your disinterest in attending \n")
        else:
            print('Invalid response.')
            yes_no = input(f'{question} \t').upper()
            while True:
                if yes_no == 'YES' or yes_no == 'NO':
                    print('Thank you! Your response has been recorded! \n')
                    break
                else:
                    yes_no = input(f'{question} \t').upper()
    else:
        reply = input(f'{question} \t')
        print(f'You answered: {reply} \n')

    #  The above loop is possibly too many lines of code,
    #  depending on what type of response is exactly desired by the hypothetical team leads.
    #  It could be refactored to have less levels of responses when receiving incorrect input
    #  by putting the While loop earlier in it.
    #  I'm leaving it as is for now, as a valid option in case the hypothetical desire
    #  was to allow users multiple chances to get their answering syntax correct.


print("\n___________________________________________________________\n"
      "CHECK-IN COMPLETE! "
      "\n👉 Please proceed to the next station to pick up your name tag from the printer. "
      "\nWe hope you enjoy the conference!")
