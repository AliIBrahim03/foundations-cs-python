#MidTerm Project
################
tabs = [] #this empty list is used to keep the tabs in order
def addTab():
    title = input("Please enter the title: ")
    URL = input("Please enter the URL: ")
    new_tab = {"title": title , "URL": URL}
    tabs.append(new_tab)
    print("Tab added successfully.")
def closeTab(): 
    if len(tabs) == 0:
        print("There are no tabs to close.")
    else:
        index = input("Enter the index of the Tab you want to close: ")
        if index == '':
            tabs.pop() #https://www.w3schools.com/python/ref_list_pop.asp 
                       #this function removes a the element at the specified position, and since we didn't specify the index it will automatically remove the last item in the list.
            
            
            else:
                if index == len(tabs)
        
    
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
            addTab()   
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