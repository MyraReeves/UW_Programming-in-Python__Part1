# Assignment 3: Storing and retrieving data

## Objectives

In this assignment you will learn how to store data and also retrieve data from CSV files.

## Basics

We need to be able to add features to an app to save and load data in a shareable format.
In order to do that, we'll be leveraging [CSV files](https://www.howtogeek.com/348960/what-is-a-csv-file-and-how-do-i-open-it/) with headers.

1. Create a file in a text editor called `questions.csv` that stores the following header and questions.

    ```csv
    question_id,question
    12,What is your phone number?
    10,What is your email?
    ```

1. Create a python program that adds questions to our csv file.
    1. The program starts by reading in all the questions in the `questions.csv` file
    1. Prints them all out to the console, formatted nicely (try playing around with [string formatting](https://stackabuse.com/padding-strings-in-python/#format))
    1. Asks the user for a new question to add to the CSV file
    1. Generates a unique integer id for that question
    1. Appends the new question back into the file

1. Create a file in a text editor called `answers.csv` that stores the following header and questions. Notice that `interviewee` is the same because we are linking it to a set of answers to a user, and the `question_id` field links our answer to a question.

    ```csv
    interviewee,question_id,answer
    Anubhaw,12,(555) 555 - 5555
    Anubhaw,10,arya0@uw.edu
    ```

1. Create a python program that adds answers to our csv file.
    1. The program starts by reading in all the answers in the `answers.csv` file
    1. Asks the interviewee for their name
    1. Reads in all the questions in the `questions.csv` file
    1. Prompts the user with every question and reads in the answer. Be sure to maintain the `question_id` relationship with every answer!
    1. Once all questions have been answered, append those answers back out into the `answers.csv` file

1. Finally, we'll create a python program that prints both questions and answers.
    1. Reads in all questions in the `questions.csv` file
    1. Reads in all answers in the `answers.csv` file
    1. Prints out the questions, one at a time, along with the corresponding set of answers from all interviewees. Format it nicely!
