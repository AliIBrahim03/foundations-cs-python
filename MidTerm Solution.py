#MidTerm Project
################

def openTab():
    Title = input("Please enter the title: ")
    url = input("Please enter the URL: ")
def displayMenu():
    user_name = input("Please enter your name: ")
    print("**********\n"+"Hello",user_name +"\n**********\n"+"1. Open Tab\n"+"2. Close Tab\n"+"3. Switch Tab\n"+
          "4. Display All Tabs\n"+"5. Open Nested Tab\n"+"6. Clear All Tabs\n"+
          "7. Save Tabs\n"+"8. Import Tabs\n"+"9. Exit\n"+"**********")
def main():
    displayMenu()
    your_input = eval(input("Please choose an action: "))
    
main()    