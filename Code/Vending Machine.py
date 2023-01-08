#A menu of drinks and snacks presented via the console. The number and range of items is up to you.
#A set of codes that the user can input to select a particular drink or snack.
#A way of capturing the user’s inputted code.
#A way of managing money. The user should be able to input any amount of money and have the correct change returned.
#A message that tells the user that a particular drink or snack has been dispensed.
#A message that tells the user how much change they have received.
#Comments in the code to explain key operations.


import datetime
import os
import time
now = datetime.datetime.now()
t = now.strftime("%A, %B %d %Y")

# Vending machine items, in a dictionary
v1 = {"1": 7, "2": 5, "3": 3, "4": 3, "5": 10}
v2 = {"1": 10, "2": 3, "3": 5, "4": 5, "5": 7}

# Function to return the amount of change
def change(a, b):
    return a % b

print("\n")
# Print date
print(t)
# Print welcoming message + current time.
print("\nHello. I am a vending machine. It is currently", now.strftime("%H:%M."))

# Start of program
while True:
    print("\n-- 1. Comforting Classics --\n-- 2. Futuristic Flavors --\n") # Main menu.

    cat = input("Select your category of choice (1-2, q to quit): ") # Category selection.

    if cat == "1": # First menu.
        print("\n1. Snacker - $", v1["1"], "\n2. KatKat - $", v1["2"], "\n3. Marbles - $", v1["3"], "\n4. Mr. Pepper - $", v1["4"], "\n5. 1up - $", v1["5"], "\n") # Menu no.1.
        ch = input("Enter the number of the item you'd like to purchase (1-5): ") # Ask user to choose item.
        am = int(input("Specify the desired amount: "))    # And the quantity.
        for item in v1.keys():    # Accessing dictionary items.
            item = ch    # Any of the items in the dictionary will be equal to the item chosen by the user.
            val = (v1[item])    # Storing the price of the chosen item.
            tt = val * am    # Total price equals to the price times quantity of the item.
            if ch in v1.keys() and am <= 20:    # Verify the validity of selected item, and limiting the quantity to 20 per purchase.
                print(f"That'll be ${tt} for {am}.")
                money = 0
                for money in range(tt):    # The process of inserting money in a loop.
                    money = int(input("\nPlease insert your money: "))    # Money stored in a variable, to allow for conditions to be used.
                    if money < tt:    # If the money offered is less than the total price.
                        print("Sorry. You did not insert enough funds for this item. Please try again.\n")
                        continue    # Return to the previous prompt
                    else:
                        chn = change(money, val)    # Money accepted, item dispensed and change given.
                        print(f"Thank you. Your item has been dispensed, and you will receive a change of ${chn}.")
                        retry = input("Would you like to make another order? (y-n) ")    # A conditional statement that exits or breaks the loop, which repeats the process
                        if retry == "n":
                            print("Okay. Goodbye.")
                            quit()
                        else:
                            print("Okay. Going back to the main menu...")    # Clears screen, returns back to the very beginning of the loop.
                            time.sleep(2)
                            os.system('cls')
                            break
                break
            else:
                print("Sorry. The item you were looking for is unavailable or in insufficient amounts.")    # If attempting to purchase nonexistent items or items in a quantity exceeding 20
                time.sleep(1)
                os.system('cls')
                break

    elif cat == "2": # Second menu.
        print("\n1. Intergalactic Icecream - $", v2["1"], "\n2. Overnight Oats - $", v2["2"], "\n3. Flavourful Feta Cup - $", v2["3"], "\n4. Cheesy Chips - $", v2["4"], "\n5. Tasty Thing - $", v2["5"], "\n")
        ch = input("Enter the number of the item you'd like to purchase (1-5): ")
        am = int(input("Specify the desired amount: "))
        for item in v2.keys():
            item = ch
            val = (v2[item])
            tt = val * am
            if ch in v2.keys() and am <= 20:
                print(f"That'll be ${tt} for {am}.")
                money = 0
                for money in range(tt):
                    money = int(input("\nPlease insert your money: "))
                    if money < tt:
                        print("Sorry. You did not insert enough funds for this item. Please try again.\n")
                        continue
                    else:
                        chn = change(money, val)
                        print(f"Thank you. Your item has been dispensed, and you will recieve a change of ${chn}.")
                        retry = input("Would you like to make another order? (y-n) ")
                        if retry == "n":
                            print("Okay. Goodbye.")
                            quit()
                        else:
                            print("Okay. Going back to the main menu...")
                            time.sleep(2)
                            os.system('cls')
                            break
                break
            else:
                print("Sorry. The item you were looking for is unavailable or in insufficient amounts.")
                time.sleep(1)
                os.system('cls')
                break
    
    elif cat == "q": # Q to quit.
        print("Have a nice day.")
        quit()
    
    else: # If the user inputs an unspecified answer.
        print("Invalid answer. Please try again.")
        time.sleep(2)
        os.system('cls')
        continue
#

                
                


