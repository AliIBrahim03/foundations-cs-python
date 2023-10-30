def addMatrices():
    
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix1 = []
    matrix2 = []
    for i in range(rows):
        row = []
        for j in range(columns):
            element = int(input("Enter element " + str(j+1) + " of row " + str(i+1) + " of the first matrix: "))
            row.append(element)
        matrix1.append(row)
        print(matrix1)
    
    for i in range(rows):
        row = []
        for j in range(columns):
            element = int(input("Enter element " + str(j+1) + " of row " + str(i+1) + " of the second matrix: "))
            row.append(element)
        matrix2.append(row)
        print(matrix2)
        
    matrix3 = []
    for i  in range(rows):
        row3 = []
        for j in range(columns):
            element = matrix1[i][j] + matrix2[i][j]
            row3.append(element)
        matrix3.append(row3) 
    print("Matrix 3:",matrix3)
            
    return matrix3     
            
def checkRotation():  
   rows1 = int(input("Enter the number of rows of the 1st matrix: "))
   columns1 = int(input("Enter the number of columns of the first matrix: "))
   matrix1 = []
   for i in range(rows1):
       row = []
       for j in range(columns1):
           element = int(input("Enter element " + str(j+1) + " of row " + str(i+1) + " of the first matrix: "))
           row.append(element)
       matrix1.append(row)
       print(matrix1)
   
   rows2 = int(input("Enter the number of rows of 2nd matrix: "))
   columns2 = int(input("Enter the number of columns of 2nd matrix: "))
   matrix2 = []
   for i in range(rows2):
       row = []
       for j in range(columns2):
           element = int(input("Enter element " + str(j+1) + " of row " + str(i+1) + " of the second matrix: "))
           row.append(element)
       matrix2.append(row)
       print(matrix2)
   

   total_elements_in_matrix1 = sum(len(sublist) for sublist in matrix1)
   total_elements_in_matrix2 = sum(len(sublist) for sublist in matrix2)
    
   if  total_elements_in_matrix1 != total_elements_in_matrix2 :
       print("These matrices are not rotated")
       
       for i in range(len(matrix1)):
           for j in range(len(matrix1[0])):
               if matrix1[i][j] != matrix2[j][i]:
                   print("These matrices are not rotated")
   else:
    print("These matrices are rotated")                
               
               
def invertDictionary():
    lenght = int(input("Please enter the number of elements of this dictionary: "))
    dict = {}
    for i in range(1, lenght + 1):
        key = input("Please enter the key of " + str(i) + ": ").strip()
        value = input("Please enter the value of " + str(i) + ": " ).strip()
        dict[key] = value            
    print("Before inverting:")
    print(dict)
    inverted_dict = {}
    for key, value in dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    print("After inverting:")
    print(inverted_dict)        
    
def convert_Matrix_D():
    
    pass
def checkPalindrome(s): #I assumed the user will input at least one character   
 
    if len(s) <= 1: #Base Case
        return True
    first_letter = s[0]
    last_letter = s[-1]
    if first_letter == last_letter:
        return checkPalindrome(s[1:-1])
    else:
        return False
    
def search():
    user_input = input("Enter a list of elements: ")
    lst = user_input.split()  
    element = input("Please enter the element to look for: ")
    pass
    
def displayMenu(): #displaying the options we have

    print("\n1. Add Matrices\n" + "2. Check Rotation\n" + "3. Invert Dictionary\n"
          + "4. Convert Matrix to Dictionary\n" + "5. Check Palindrome\n" + 
          "6. Search for an Element & Merge Sort\n" + "7. Exit")
    
def sort():
    pass
    
def main(): #main function

    name = input(print("Please enter your name: "))
    
    print("Welcome", name) 
    choice = 10
    while choice != 7:
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
            s = input("Enter a string: ").strip() 
            if checkPalindrome(s):
                print("This string is a Palindrome.")
            else:
                print("This string is not a Palindrome.")
        elif choice == 6:
            search()
        elif choice != 7:
            print("\nInvalid, try again")
    
    
    
    
main()
