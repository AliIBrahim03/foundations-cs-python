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
          +"\nd. Return to main menu\n-----")
    
def displayMenu2():
    print("\n------\na. Add vertex"
          +"\nb. Add edge"
          +"\nc. Remove vertex"
          +"\nd. Remove edge"
          +"\ne. Display vertices with a degree of X or more."
          +"\nf. Return to main menu\n------")

def displayMenu3():
    print("\n-----\na.a. Add a student"
          +"\nb. Interview a student"
          +"\nc. Return to main menu")


def isPalindrome():
    s = input("Please enter the string: ")
    stack = []
    queue = []
    for x in s:
        stack.append(x) #append() adds the element to the end of the list
        queue.insert(0,x) #insert() adds the element to the specified index (in this case 0 which is the beginning)
    print("------\n",stack,"\n")
    print("------\n",queue,"\n")    
    if stack == queue:
        print("------\n",s," is a Palindrome.\n------ ")
    elif stack != queue:
        print("------\n",s," is not a Palindrome.\n------ ")

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

                 
class Graph:

  def __init__(self, num_vertices):
    self.num_vertices = num_vertices
    self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    #[[0,0,0,0,0]
    # [0,0,0,0,0]
    # [0,0,0,0,0]
    # [0,0,0,0,0]
    # [0,0,0,0,0]]

  def addVertex(self):
    # automates the process of adding a vertex
    self.num_vertices += 1
    for row in self.adj_matrix:
      row.append(0)
    self.adj_matrix.append([0] * self.num_vertices)
    print("Added vertex", self.num_vertices - 1, "\n")

  def addEdge(self, v1, v2):
    # This method simply adds an edge between vertex 1 and vertex 2
    if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
      # To ensure that both v1 and v2 exist
      self.adj_matrix[v1][v2] = 1
      self.adj_matrix[v2][v1] = 1
      print("Added an edge between vertices", v1, "and", v2, "\n")
      # In our case, the graph is undirected so we added a 1 to make it symmetrical
      # If the graph was directed then you must ONLY add an edge pointing from v1 to v2 or the opposite => either v1 or v2 will be the source and destination.
    elif ((v1 < 0 or v1 >= self.num_vertices)
          and (v2 < 0 or v2 >= self.num_vertices)):
      print("Invalid vertices", v1, "and", v2, "\n")
    elif (v1 < 0 or v1 >= self.num_vertices):
      print("Invalid vertex", v1, "\n")
    else:
      print("Invalid vertex", v2, "\n")

  def removeVertex(self, vertex):
        if 0 <= vertex < self.num_vertices:
            del self.adj_matrix[vertex]
            for row in self.adj_matrix:
                del row[vertex]
            self.num_vertices -= 1
            print("Removed vertex", vertex, "\n")
        else:
            print("Invalid vertex", vertex, "\n")
            
            
  def removeEdge(self, v1, v2):
      if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
          self.adj_matrix[v1][v2] = 0
          self.adj_matrix[v2][v1] = 0
          print("Removed an edge between vertices", v1, "and", v2, "\n")
      else:
          print("Invalid vertices", v1, "and", v2, "\n")          


  def displayGraph(self):
    # simply displays the adjacecny matrix
    if len(self.adj_matrix) == 0:
      print("Graph is empty!\n")
      return  # will break the function
    for row in self.adj_matrix:
      # print(row)
      # Just to make the output look nicer
      print(" ".join(map(str, row)))
    
def main():
    ll = LinkedList()
    graph = Graph(0)
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
            displayMenu3()
        elif numeral_choice == 4:
            pass
        elif numeral_choice == 5:
            displayMenu2()
            alphabetic_choice = 'z'
            while (alphabetic_choice != 'f'):
                alphabetic_choice = str(getChoice())
                if alphabetic_choice == 'a':
                    graph.addVertex()
                elif alphabetic_choice == 'b':
                    v1 = input("PLease enter the first vertex: ")
                    v2 = input("Please enter the second vertex: ")
                    graph.addEdge(v1, v2)
                elif alphabetic_choice == 'c':
                   vtr = int(input("Please enter the vertex to remove: "))
                   graph.removeVertex(vtr)
                elif alphabetic_choice == 'd':
                    v1 = int(input("Enter the first vertex: "))
                    v2 = int(input("Enter the second vertex: "))
                    graph.removeEdge(v1, v2)
                elif alphabetic_choice == 'e':
                    pass
                elif alphabetic_choice == 'f':
                    break
                else:        
                    print("Please enter a valid letter.")
        elif numeral_choice != 6:
            print("\n----------\nInvalid action. Try again.\n ")
        
        displayMenu()
        numeral_choice = int(getChoice())
                        
    print("You exited the program. Bye :) ")
    
main()