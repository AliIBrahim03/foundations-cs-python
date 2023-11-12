#MidTerm Project
################


from urllib.request import urlopen
import json
#import requests
#from bs4 import BeautifulSoup #https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-2/


#this function will check if the list that keeps the tabs is empty
def isTabsEmpty():
    return len(tabs) == 0
#####################################################################
#this function asks the user for the title of the Tab
#####################################################################
def getTitle(): #O(1)
    Title = input("Please enter the Title: ")
    return Title
#####################################################################
#this function asks the user for the URL of the Tab
#####################################################################
def getURL(): #O(1)
    URL = input("Please enter the URL: ")
    return URL
#####################################################################
#this function will first get the Title and URL and then add them to a new tab that will get appended to the empty "tabs" list to keep track
def addTab(): #O(1)
    Title = getTitle()
    URL = getURL()
    new_tab = {"Title": Title , "URL": URL}
    tabs.append(new_tab)
    print(Title, "with the URL:",URL, "was added")
#####################################################################


#this function asks the user for an the index of a tab and deletes it using the pop() function   
def closeTab():
    if isTabsEmpty():
        print("There are no tabs to close.")
    else:
        index = str(input("Enter the index of the Tab you want to close: "))
        #check if the user doesn't enter an index
        if index == '':
            tabs.pop() #https://www.w3schools.com/python/ref_list_pop.asp 
                       #this function removes the element at the specified index inside the list, and since we didn't specify the index it will automatically remove the last item in the list.
                       #O(n)
            
            print("The last tab was closed.")
        else:
            index = int(index)
            if index < len(tabs) and index >= 0:
                closed_tab = tabs.pop(index)
                print("Tab", index, "with the Title", closed_tab["Title"],
                     "and URL", closed_tab["URL"], "was closed")

            else:
                print("This tab does not exist")
#####################################################################

#this function asks the user for the index of the tab he wishes to switch to
def switchTab():
    if isTabsEmpty():
        print("There are no tabs to switch to.")
    else:
        index = input("Please enter the index of the Tab you want to switch to: ")
        if index == '':
            switched_tab = tabs[len(tabs)-1]
            print(switched_tab)
            HTML_content = switched_tab.get('HTML', '')
            print(HTML_content)
        else:
            index = int(index)
            URL = tabs[index]["URL"]
            switched_tab = tabs[index]          #https://realpython.com/python-web-scraping-practical-introduction/
            page = urlopen(URL)                 #https://realpython.com/python-web-scraping-practical-introduction/
            html_bytes = page.read()            #https://realpython.com/python-web-scraping-practical-introduction/
            HTML = html_bytes.decode("utf-8")   #https://realpython.com/python-web-scraping-practical-introduction/
            print(switched_tab)                 #this snippet takes the urlopen(),read() and .decode() functions in order to get the HTML code of the page we get from the URL 
            print(HTML)
#####################################################################
#this function prints the titles of all the open tabs including the nested ones
def displayTabs(): #O(n)
    if isTabsEmpty():
       print("There are no tabs to display.")
    else:
        print("The open Tabs are: \n")
        for index in range(len(tabs)):#O(n)
            displayed_tab = tabs[index]['Title']
            print(displayed_tab)
            nested_tabs = tabs[index].get('Nested', [])
            if nested_tabs:
                for nested_tab in nested_tabs:
                    print("  ", nested_tab['Title'])
#####################################################################
#this function asks user for the index of a tab and creates a child tab (nested tab) inside it                        
def openTab(): #O(1)
     if isTabsEmpty():
        print("There are no parent tabs.")
     else:
         parent_tab_index = int(input("Please enter the index of the parent tab: "))
         if parent_tab_index > len(tabs):
             print("Parent tab does not exist")
         else:
             parent_tab = tabs[parent_tab_index]
             parent_tab["Nested"] = []
             Title = getTitle()
             URL = getURL()
             new_child_tab = {"Title": Title, "URL": URL}
             parent_tab["Nested"].append(new_child_tab)
             print("Nested tab",Title," was created.")
#####################################################################
                     
def clearTabs():
    if isTabsEmpty():
       print("There are no tabs to clear.")
    else:
        for i in range(len(tabs)):
            tabs.pop()
        print("All tabs have been cleared.")
#####################################################################

def saveTabs(): 
    file_path = input("Please enter the file path to save the"
                      " current state of open tabs: ")
    
    saved_tabs = {"tabs": tabs}
    with open(file_path, "w") as save_file:
         json.dump(saved_tabs, save_file, indent=6)
    print("The current state of the tabs is saved to", file_path)
     
#####################################################################    
def importTabs(): #https://www.geeksforgeeks.org/read-json-file-using-python/
                  #open() function
                  #snippet of code written by user Tejashwi5
    
    file_path = str(input("Please enter the file path to your file: "))
    f = open(file_path)
    data = json.load(f)
    for i in data['emp_details']:
        print(i)
#####################################################################
#this function asks for the user's name    
def inputName():
    user_name = input("Please enter your name: ")
    return user_name
#####################################################################
#this functions displays the main meny that the user will interact with        
def displayMenu(user_name):
    
    
    print("**********\n"+"Hello",user_name +"\n**********\n"+"1. Open Tab\n"+"2. Close Tab\n"+"3. Switch Tab\n"+
          "4. Display All Tabs\n"+"5. Open Nested Tab\n"+"6. Clear All Tabs\n"+
          "7. Save Tabs\n"+"8. Import Tabs\n"+"9. Exit\n"+"**********")
#####################################################################
#this is the main function where all the functions come along and get executed    
def main():
    user_name = inputName()
    displayMenu(user_name)
    your_input = 0
    while ( your_input != 9):
        your_input = int(input("\nPlease choose an action: "))
        if  your_input == 1:
            addTab()   
        elif your_input == 2:
            closeTab()
        elif your_input == 3:
            switchTab()
        elif your_input == 4:
            displayTabs()
        elif your_input == 5:
            openTab()
        elif your_input == 6:
            clearTabs()
        elif your_input == 7:
            saveTabs()
        elif your_input == 8:
            importTabs()
        elif your_input != 9:
            print("Error, pick a valid number.")
            
    print("\nYou exited the Program.")
    
tabs = [] #this empty list is used to keep the tabs in order   
main()    #calling the main function    