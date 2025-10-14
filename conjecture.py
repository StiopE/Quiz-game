import time

number = int(input("Enter a number: "))

while True:
    if number == 1:
        print("You're stuck!")
        break
    elif number %2 ==0:
        print(f"{number}/2 → ", end="", flush=True)
        number = number/2
        number = int(number)
        print(f"{number} ", flush=True)
        time.sleep(0.1)
    elif number%2 != 0:
        print(f"{number} * 3 + 1 → ", end="", flush=True)
        number = (number*3)+1
        number = int(number)
        print(f"{number} ", flush=True)
        time.sleep(0.1)
    


