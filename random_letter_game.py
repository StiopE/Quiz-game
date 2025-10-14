import random

rand_num = random.randint(1,196)
with open("all_countries.txt", 'r') as f:
    for i in range(rand_num):
        country = f.readline()
    
random_country = country.lower() 
random_country = random_country.strip() # a random country that is lowercase and without \n
len_random_country = len(random_country) # take the length of the country just in case
list_random_country = list(random_country) # make my random word into a list

shadow_l = [] # a list for the hidden list_random_country

for i in range(len_random_country):
    shadow_l.append('*') # I fill the shadow_l with * that is the length of the random country
for i in range(25, -1, -1): #Loop 26 times just to guess each letter if needed
    random_letter = input("Enter a random letter: ").strip().lower() #User inputs random letter
    
    if random_letter == random_country:
        # print(f"You have won the game!! The answer was {random_country}")
        shadow_l = list_random_country
        break
    if random_letter in list_random_country: #Check if the random_letter is in the list random country
        print(f"{random_letter} is in my random country") #Say that its in there
        
        for i in range(len(list_random_country)): #Loop through list_random_country
            if list_random_country[i] == random_letter: #checks each letter in list_random country compared to random_letter
                shadow_l[i] = random_letter #Replaces an * with the random letter
                list_random_country[i] = "_" #replace letter in original list with _
        
        
        # index_random_letter = list_random_country.index(random_letter)
        # shadow_l[index_random_letter] = random_letter
        # list_random_country[index_random_letter] = "_"
        print(*shadow_l)
        print()
    else:
        print(f"{random_letter} is not in my random country")
        print(*shadow_l)
        print()
    
if '*' not in shadow_l:
    print(f"You have won the game!! The answer was {random_country}")
else:
    print("You have lost the game :( ")

#This is not ChatGPT btw promise