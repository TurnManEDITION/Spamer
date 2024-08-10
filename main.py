import pyautogui as pag
import random as rand
import time as t
import os


while True:
    try:
        x1_num = int(input("Enter first number  : "))
        if x1_num > 0:
            break
    except ValueError:
        os.system("cls")
while True:
    try:
        x2_num = int(input("Enter second number : "))
        if x2_num >= x1_num:
            break
    except ValueError:
        os.system("cls")
        print(f"Enter first number  : {x1_num}")

while True:
    try:
        num = int(input("Enter number  : "))
        if num > 0:
            break
    except ValueError:
        os.system("cls")
        print(f"Enter first number  : {x1_num}")
        print(f"Enter second number : {x2_num}")

nums_list = ["0","1","2","3","4","5","6","7","8","9"]
chrs_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
             "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

while True:
    try:
        mode = int(input("Enter mode(def-0, num-1, chr-2) : "))
        if -1 < mode < 3:
            break
        else:
            os.system("cls")
            print(f"Enter first number  : {x1_num}")
            print(f"Enter second number : {x2_num}")
            print(f"Enter number  : {num}")
    except ValueError:
        os.system("cls")
        print(f"Enter first number  : {x1_num}")
        print(f"Enter second number : {x2_num}")
        print(f"Enter number  : {num}")

if mode == 0:
    sym = "numbers + chars"
if mode == 1:
    sym = "numbers"
if mode == 2:
    sym = "chars"

t.sleep(10)
i = 0
x = 0
text = ""

start_time = t.time()
while not num == i:
    # t.sleep(0.5)
    os.system("cls")
    print(f"message : {i}")

    end_time = t.time()
    time = end_time - start_time

    print(f"Time    : {round(time, 3)}")
    x_num = rand.randint(x1_num, x2_num)
    while not x == x_num:
        if mode == 0 and not x == x_num:
            lists = nums_list + chrs_list
            text += rand.choice(lists)
            x += 1
        if mode == 1 and not x == x_num:
            lists = nums_list
            text += rand.choice(lists)
            x += 1
        if mode == 2 and not x == x_num:
            lists = chrs_list
            text += rand.choice(lists)
            x += 1
    pag.write(text)
    pag.hotkey("Enter")
    x = 0
    i += 1
    text = ""
end_time = t.time()

time = end_time - start_time

os.system("cls")
print(f"  Info:\nTime: {round(time, 3)}\nFrom: {x1_num}, To: {x2_num}\nSymbols: {sym}")
print(f"Finish code: 0\nmessage:     {num}")
os.system("pause")

