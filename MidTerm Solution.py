#MidTerm Project
################
def addTab(title,url):
    title = input("Please enter the title: ")
    URL = input("Please enter the URL: ")
    new_tab = {"title": title , "URL":link}
    tabs.append(new_tab)
def closeTab():
    if len(tabs) == 0:
        print("There are no tabs to close.")
    else:
        index = input("Enter the index of the Tab you want to close: ")
        
    
def inputName():
    user_name = input("Please enter your name: ")
    return user_name
def openTab():
    Title = input("Please enter the title: ")
    url = input("Please enter the URL: ")
def displayMenu(user_name):
    print("**********\n"+"Hello",user_name +"\n**********\n"+"1. Open Tab\n"+"2. Close Tab\n"+"3. Switch Tab\n"+
          "4. Display All Tabs\n"+"5. Open Nested Tab\n"+"6. Clear All Tabs\n"+
          "7. Save Tabs\n"+"8. Import Tabs\n"+"9. Exit\n"+"**********")
def main():
    user_name = inputName()
    displayMenu(user_name)
    your_input = 0
    while ( your_input != 9):
        your_input = int(input("Please choose an action: "))
        if  your_input == 1:
            pass
        elif your_input == 2:
            pass
        elif your_input == 3:
            pass
        elif your_input == 4:
            pass
        elif your_input == 5:
            pass
        elif your_input == 6:
            pass
        elif your_input == 7:
            pass
        elif your_input == 8:
            pass
        elif your_input != 9:
            print("Error, pick a valid number.")
            
    print("\nYou exited the Program.")
   
            
        
            
    
            
        
            
    
main()    