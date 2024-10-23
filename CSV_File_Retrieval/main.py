#########################################################################
# Create a python program that adds questions to the questions.csv file #
#########################################################################

questions_content = []                  # Empty list to hold contents for printing to console

# 1. The program starts by storing in a variable all the questions in the questions.csv file
with open('questions.csv', 'r') as csv_file:
    questions = csv_file.read()         # Stores contents of csv file


# 2. Prints all the questions out to the console, formatted nicely
    questions = questions.split('\n')   # Turns the result into a list
    questions = questions[1:]           # Removes header row
    for i in questions:
        separate = i.split(',')         # Separates the contents into new indexes based upon position relative to comma
        questions_content.append([separate[0], separate[-1]])    # Creates nested list with question id marked as integers
print('The previously existing questions were...')
count = 0
for each_question in questions_content:
    print(f'❓ {questions_content[count][1]}')
    count += 1
# The above automates iterating thru the nested list instead of having to hard code printing each line individually
# For a list of only 2 questions, the syntax without automated interation would be:
# print(f'{questions_content[0][1]}')
# print(f'{questions_content[1][1]}')


# 3. Asks the user for a new question to add to the CSV file
new_question = input("\nPlease add a question: \t")


# 4. Generates a unique integer id for that question
new_id = int(f'{questions_content[-1][0]}')         # Question_id of the last indexed item is turned into an integer
new_id += 5                                         # Increases by 5 to skip over id value 12 earlier in list


# 5. Appends the new question back into the questions file
with open('questions.csv', 'a') as csv_file:
    csv_file.write("\n"+str(new_id)+",")
    csv_file.write(new_question)

print('✔️ Your question has been added to the questions file')


#####################################################################
# Create a python program that adds answers to the answers.csv file #
#####################################################################

# The program starts by reading all the answers in the answers.csv file and storing them in a variable:
answers_content = []
with open('answers.csv', 'r') as requested_file:
    answers = requested_file.read()
    answers = answers.split('\n')  # Turns the result into a list
    answers = answers[1:]  # Removes header row
    for i in answers:
        separate = i.split(',')  # Separates the contents into new indexes based upon position relative to comma
        answers_content.append([separate[0], separate[1], separate[-1]])  # Creates nested list with question id marked as integers

# Asks the interviewee for their name.
interviewee = input("\nWhat is your name?: \t")

# Prints the previously-existing questions and answers:
number = 1                      # Different than id!
question_counter = 0
answer_counter = 0
print(f'\n{interviewee}, you were previously asked: ')
for each_question in questions_content:
    print(f'{number}. {questions_content[question_counter][1]}')
    question_counter += 1
    number += 1
number = 1                      # Needed to be reset so that answer numbers correspond to question numbers
for each_previously_existing_answer in answers_content:
    print(f'➡️ You answered with: {number}. {answers_content[answer_counter][2]}')
    answer_counter += 1
    number += 1

# Prompts the user to answer the newly added question
new_answer = input('\n' + new_question + '\t')

# Once all questions have been answered, append those answers back out into the answers.csv file
with open('answers.csv', 'a') as requested_file:
    requested_file.write('\n'+interviewee+",")
    requested_file.write(str(new_id)+",")
    requested_file.write(new_answer)

print('✔️ Your answer has been recorded')


#####################################################################################
# Create a python program that prints both questions and answers from the csv files #
#####################################################################################

# Stores all questions from the questions.csv file, including the newly added one:
questions_updated_list = []
with open('questions.csv', 'r') as file:
    questions = file.read()         # Stores contents of csv file
    questions = questions.split('\n')   # Turns the result into a list
    questions = questions[1:]           # Removes header row
    for i in questions:
        separate = i.split(',')         # Separates the contents into new indexes based upon position relative to comma
        questions_updated_list.append([separate[0], separate[-1], ''])


# Stores all answers from the answers.csv file, including the newly answered one:
answers_updated_list = []
with open('answers.csv', 'r') as file:
    answers = file.read()
    answers = answers.split('\n')  # Turns the result into a list
    answers = answers[1:]  # Removes header row
    for i in answers:
        separate = i.split(',')  # Separates the contents into new indexes based upon position relative to comma
        answers_updated_list.append([separate[0], separate[1], separate[2]])

# Prints out the questions, one at a time, along with the corresponding set of answers from all interviewees.
print('\n🟡 🟢 🟡 🟢 🟡 🟢 🟡 🟢 🟡 🟢 🟡 🟢 🟡'
      '\nSummary:')

combined = []
combined.append(questions_updated_list)
combined.append(answers_updated_list)

remaining = len(answers_updated_list)

id_index = 0
interviewee_index = 0

for each in combined:
    while remaining > 0:
        print(f'Question ID: {combined[0][id_index][0]} '
              f'\n{combined[0][id_index][1]} '
              f'\n{combined[1][interviewee_index][0]} answered with: '
              f'\n{combined[1][interviewee_index][2]} \n')
        id_index += 1
        interviewee_index += 1
        remaining -= 1
        