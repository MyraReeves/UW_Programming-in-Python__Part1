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
