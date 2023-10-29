def addMatrices():
    pass
def checkRotation():    
    pass
def invertDictionary():
    pass
def convert_Matrix_D():
    pass
def checkPalindrome():
    pass
def search():
    pass
def displayMenu(): #displaying the options we have

    print("\n1. Add Matrices\n" + "2. Check Rotation\n" + "3. Invert Dictionary\n"
          + "4. Convert Matrix to Dictionary\n" + "5. Check Palindrome\n" + 
          "6. Search for an Element & Merge Sort\n" + "7. Exit")
    
    
    
def main(): #main function

    name = input(print("Please enter your name: "))
    
    print("Welcome", name) 
    
    choice = 10
    limit = 0
    while choice != 7 and limit < 7 :
        displayMenu() 
        choice = eval(input("\nEnter your choice: "))
        if choice == 1:
            addMatrices()
        elif choice == 2:
            checkRotation()
        elif choice == 3:
            invertDictionary()
        elif choice == 4:
            convert_Matrix_D()
        elif choice == 5:
            checkPalindrome()
        elif choice == 6:
            search()
        elif choice != 7:
            print("\nInvalid, try again")
    
    
    
    
main()
