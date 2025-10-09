# import random
# print("Hello I have some number in my mind from zero to ten")
# guess = int(input("Input: "))

# lives = 3
# random_number = random.randint(0,9)
# while lives != 0:
    
#     if random_number == guess:
#         print("You won!")
#         print(f"You won with {lives} lives left")
#         break
#     else:
#         if (lives-1) == 0:
#             print("You have lost the game")
#             break
#         else:
#             print("Wrong")
#             print(f"You have {lives-1} lives left")
#             lives = lives-1
#             guess = int(input("Input: "))
#             continue







#Ceaser's Cypher

message = input()
rotation = int(input())
message_in_list = []
message_in_list_2 = []
asci_code = 0
normal_code = 0
final_answer = ""
def encoding():
    
    global message_in_list
    global asci_code         
    for i in range(len(message)):
        asci_code = ord(message[i])
        asci_code = asci_code + rotation
        message_in_list.append(chr(asci_code))
    print(*message_in_list)

def decoding():
    global message_in_list_2
    global asci_code
    global normal_code
    for i in range(len(message_in_list)):
        normal_code = ord(message_in_list[i])
        normal_code = normal_code - rotation
        message_in_list_2.append(chr(normal_code))
    print(*message_in_list_2) 

encoding()
decoding() 
        
        
        
    
    


 

    


