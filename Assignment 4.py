def getUsername():
    while True:    
        username = str(input("Please enter your name: ")).strip()
        if username == '':
            print("----------\nName cannot be empty.\n----------")
        else:
            return username
            
def getChoice():
    while True:
        choice = input("\nChoose an action: ")
        if choice == '':
            print("----------\nYour choice cannot be empty.\n----------")
        else:
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
    
def displayMenu2():
    print("\n------\na. Add vertex"
          +"\nb. Add edge"
          +"\nc. Remove vertex"
          +"\nd. Remove edge"
          +"\ne. Display vertices with a degree of X or more."
          +"\nf. Return to main menu")


class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedList:
    
  def __init__(self):
    self.head = None
    self.size = 0
    
  def addNode(self,data):
      new_node = Node(data)
      if self.head is None:
           self.head = new_node
           return
       
      last = self.head
      while (last.next):
          
          last = last.next
      last.next = new_node
      
  def displayNodes(self):
      if self.head is None:
          print("\n----------\nThis list is empty. ")
          return
      
      current = self.head
      while current != None:
          print(current.info)
          current = current.next
  
  def removeNode(self,value_to_remove):
      if self.head is None:
          print("\n----------\nThis list is empty. ")
      else:
          current = self.head
          previous = None
          while current is not None:
              if current.info == value_to_remove:
                  print("Removing node with value:", value_to_remove)
                  if previous is None:
                    # The node to be removed is the head
                        self.head = current.next
                        if self.head is None:
                        # If the list becomes empty after removal
                            self.tail = None
                  else:
                      previous.next = current.next
                      if current.next is None:
                        # If the removed node was the last one
                            self.tail = previous

                  self.size -= 1
                  return  # Node found and removed, exit the method

              previous = current
              current = current.next

          print("Value not found in the linked list.")

                 
def isPalindrome():
    s = input("Please enter the string: ")
    stack = []
    queue = []
    for x in s:
        stack.append(x)
        queue.insert(0,x)
        
    if stack == queue:
        print(s," is a Palindrome. ")
    elif stack != queue:
        print(s," is not a Palindrome. ")
    
    
def main():
    ll = LinkedList()
    username = getUsername()
    print("\nWelcome",username)
    displayMenu()
    numeral_choice = int(getChoice())
    while (numeral_choice !=6):
        
        if numeral_choice == 1:
            displayMenu1()
            alphabetic_choice = 'z'
            while (alphabetic_choice != 'd'):
                alphabetic_choice = str(getChoice())
                if alphabetic_choice == 'a':
                    data = int(input("Please enter the number: "))
                    ll.addNode(data)
                elif alphabetic_choice == 'b':
                    ll.displayNodes()
                elif alphabetic_choice == 'c':
                    value_to_remove = int(input("Please enter the value to search for and remove: "))
                    ll.removeNode(value_to_remove)
                elif alphabetic_choice == 'd':
                    break
                else:        
                    print("Please enter a valid letter.")
                
        elif numeral_choice == 2:
            isPalindrome()
        elif numeral_choice == 3:
            pass
        elif numeral_choice == 4:
            pass
        elif numeral_choice == 5:
            displayMenu2()
            alphabetic_choice = 'z'
            while (alphabetic_choice != 'f'):
                alphabetic_choice = str(getChoice())
                if alphabetic_choice == 'a':
                    data = int(input("Please enter the number: "))
                    ll.addNode(data)
                elif alphabetic_choice == 'b':
                    ll.displayNodes()
                elif alphabetic_choice == 'c':
                    value_to_remove = int(input("Please enter the value to search for and remove: "))
                    ll.removeNode(value_to_remove)
                elif alphabetic_choice == 'd':
                    break
                else:        
                    print("Please enter a valid letter.")
        elif numeral_choice != 6:
            print("\n----------\nInvalid action. Try again.\n ")
        
        displayMenu()
        numeral_choice = int(getChoice())
                        
    print("You exited the program. Bye :) ")
    
main()    

    
    
    