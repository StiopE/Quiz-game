import random


balance = 0
money_per_win = 200000
flag = False
questions_correct = 0

def user_answer_right():
    global balance
    global questions_correct
    print()
    print("Correct, balance +200,000")
    balance = balance + money_per_win
    questions_correct = questions_correct +1
    print(f"Correct questions so far: {questions_correct}")
    print(f"Current Balance: {balance}")
    print()

def user_answer_wrong():
    global flag
    global balance
    print("Wrong, you have lost the game")
    balance = 0
    print(f"Remaining balance: {balance}")
    flag = True
    
    
def question1():
    global flag
    question_1 = "Who invented the Periodic Table?\n"
    print(question_1)
    print("A: Tesla")
    print("B: Mendeleev")
    print("C: Einstein")
    print("D: LeBron James")
    print("E: Exit")
    
    user_input_01 = input().strip().lower()
    
    if user_input_01 == 'a':
        user_answer_wrong()
    elif user_input_01 == 'b':
        user_answer_right()
    elif user_input_01 == 'c':
        user_answer_wrong()
    elif user_input_01 == 'd':
        user_answer_wrong()
    elif user_input_01 == 'e':
        print("You chose 'Exit'")
        
        print(f"Remaining balance: {balance}")
        flag = True
    else:
        user_answer_wrong()
        
        

def question2():
    global flag
    question_2 = "How do you say 'Hello' in french? \nE to exit"
    print(question_2)
    user_input_02 = input("Input: ").strip().lower()
    if user_input_02 == 'bonjour':
        user_answer_right()
    elif user_input_02 == 'e':
        print("You chose 'Exit'")
        
        print(f"Remaining balance: {balance}")
        flag = True
    else:
        user_answer_wrong()

def question3():
    global flag
    question_3 = "What is the sum of 3*9-3? \nE to exit"
    print(question_3)
    user_input_03 = input("Input: ").strip().lower()
    
    if user_input_03 == '24':
        user_answer_right()
    elif user_input_03 == 'e':
        print("You chose 'Exit'")
        
        print(f"Remaining balance: {balance}")
        flag = True
    else:
        user_answer_wrong()

def question4():
    global flag
    question_4 = "What is the capital of Nigeria? \nE to exit"
    print(question_4)
    user_input_04 = input("Input: ").strip().lower()
    if user_input_04 == 'lagos':
        user_answer_right()
    elif user_input_04 == 'e':
        print("You chose 'Exit'")
        
        print(f"Remaining balance: {balance}")
        flag = True
    else:
        user_answer_wrong()

def question5():
    global flag
    question_5 = "Which flag has 50 stars?"
    print(question_5)
    print("A: Bangladesh")
    print("B: Trinidad and Tobago")
    print("C: United States of America")
    print("D: Bahrain")
    print("E: Exit")
    
    user_input_05 = input("Input: ").lower()
    
    if user_input_05 == 'a':
        user_answer_wrong()
    elif user_input_05 == 'b':
        user_answer_wrong()
    elif user_input_05 == 'c':
        user_answer_right()
    elif user_input_05 == 'd':
        user_answer_wrong()
    elif user_input_05 == 'e':
        
        print("You chose 'Exit'")
        
        print(f"Remaining balance: {balance}")
        flag = True
    else:
        user_answer_wrong()

Q1 = question1
Q2 = question2
Q3 = question3
Q4 = question4
Q5 = question5

all_questions = [Q1, Q2, Q3, Q4, Q5]





print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~   Become a Millionaire    ~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")

#Start of question 1
print("Rules:")
print("1. Five questions")
print("2. Get a question correct, earn $20,000")
print("3. Getting a question wrong will eliminate you instantly")
print("4. In order to keep the money you summed up, quit.")
print()


while flag == False and all_questions:
    current_question = random.choice(all_questions)
    current_question()
    all_questions.remove(current_question)
    
    
    
