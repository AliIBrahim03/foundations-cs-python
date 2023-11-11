#MidTerm Project
################
import requests
from bs4 import BeautifulSoup #https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-2/

tabs = [] #this empty list is used to keep the tabs in order

def getTitle():
    Title = input("Please enter the Title: ")
    return Title

def getURL():
    URL = input("Please enter the URL: ")
    return URL

def addTab():
    Title = getTitle()
    URL = getURL()
    new_tab = {"Title": Title , "URL": URL}
    tabs.append(new_tab)
    print(Title +" with the URL:",URL," was added")
    
def closeTab(): 
    if len(tabs) == 0:
        print("There are no tabs to close.")
    else:
        index = int(input("Enter the index of the Tab you want to close: "))
        if index == '':
            tabs.pop() #https://www.w3schools.com/python/ref_list_pop.asp 
                       #this function removes a the element at the specified position, and since we didn't specify the index it will automatically remove the last item in the list.
            
            
        else:
            if index < len(tabs) and index >= 0:
                closed_tab = tabs.pop(index)
                print("Tab", index, "with the Title", closed_tab["Title"],
                      "and URL", closed_tab["URL"], "was closed")

            else:
                print("This tab does not exist")

def switchTab():
    if len(tabs) == 0:
        print("There are no tabs to switch to.")
    else:
        index = int(input("Please enter the index of the Tab you want to switch to: "))
        if index == '':
            print(tabs[len(tabs)-1])
            HTML_content = switched_tab.get('HTML', '')
        else:
            switched_tab = tabs[index]
            print(switched_tab)

            
        
def displayTabs():
    if len(tabs) == 0:
        print("There are no tabs to display.")
    else:
        for index in range(len(tabs)):
            displayed_tab = tabs[index]
            print(displayed_tab)
            
def clearTabs():
    for i in range(len(tabs)):
        tabs.pop()
    
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
            closeTab()
        elif your_input == 3:
            switchTab()
        elif your_input == 4:
            displayTabs()
        elif your_input == 5:
            pass
        elif your_input == 6:
            clearTabs()
        elif your_input == 7:
            pass
        elif your_input == 8:
            pass
        elif your_input != 9:
            print("Error, pick a valid number.")
            
    print("\nYou exited the Program.")
   
main()    