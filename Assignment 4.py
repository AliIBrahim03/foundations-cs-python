def getUsername():
    while True:    
        username = str(input("Please enter your name: ")).strip()
        if username == '':
            print("\nName cannot be empty. Please enter your name: ")
        else:
            return username
            
def getChoice():
    choice = int(input("\nChoose an action: "))
    return choice

def displayMenu():
    print("1. Singly Linked List"
          +"\n2. Check if Palindrome"
          +"\n3. Priority Queue"
          +"\n4. Evaluate an Infix Expression"
          +"\n5. Graph"
          +"\n6. Exit")

def main():
    limit = 0
    username = getUsername()
    print("\nWelcome",username)
    while True:
        displayMenu()
        choice = getChoice()
        
        if 1 <= choice <= 5:
            if choice == 1:
                pass
            elif choice == 2 :
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
        else:
            limit += 1
            print("\nError limit is at 4, you're currently at:", limit, "\n")
            if limit >= 4:
                print("\nLimit reached.")
                break
            print("\nPlease choose a valid action.\n")
            
    print("\nYou exited the program. Bye :)")

main()