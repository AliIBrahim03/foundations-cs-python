def getUsername():
    while True:    
        username = str(input("Please enter your name: ")).strip()
        if username == '':
            print("\nName cannot be empty. Please enter your name: ")
        else:
            return username
            
def getChoice():
    choice = input("\nChoose an action: ")
    return choice

def displayMenu():
    print("----------\n1. Singly Linked List"
          +"\n2. Check if Palindrome"
          +"\n3. Priority Queue"
          +"\n4. Evaluate an Infix Expression"
          +"\n5. Graph"
          +"\n6. Exit\n----------")
    
def displayMenu1():
    print("\n-----\na. Add Node"
          +"\nb. Display Nodes"
          +"\nc. Search for & Delete Node"
          +"\nd. Return to main menu")
    
def main():
    
    username = getUsername()
    print("\nWelcome",username)
    displayMenu()
    choice = int(getChoice())
    while (choice !=6):
        
        if choice == 1:
            displayMenu1()
            choice = getChoice()
            while (choice != 'd'):
                if choice == 'a':
                    pass
                elif choice == 'b':
                    pass
                elif choice == 'c':
                    pass
                elif choice == 'd':
                    break
                else:        
                    print("Please enter a valid letter.")
                
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice != 6:
            print("Invalid action. Try again.\n ")
        
        displayMenu()
        choice = int(getChoice())
                        
    print("You exited the program. Bye :) ")
    
main()    

    
    
    