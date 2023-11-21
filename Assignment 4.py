def getUsername():
    while True:    
        username = str(input("Please enter your name: ")).strip()
        if username == '':
            print("\nName cannot be empty. Please enter your name: ")
        else:
            return username
            
def getChoice():
    choice = int(input("\nChoose an action: \n"))
    return choice

def displayMenu():
    print("1. Singly Linked List"
          +"\n2. Check if Palindrome"
          +"\n3. Priority Queue"
          +"\n4. Evaluate an Infix Expression"
          +"\n5. Graph"
          +"\n6. Exit")

def main():
    
    username = getUsername()
    print("\nWelcome",username)
    displayMenu()
    choice = getChoice()
    while choice != 6:
        
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
        elif choice != 6:
            print("Please choose a valid action.\n")
        displayMenu()
        getChoice()
            
    print("You exited the program. Bye")
    
main()    

    
    
    