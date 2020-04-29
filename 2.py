def choice():
    
    front=0
    rear=0
    print('''Operations Available:
               1.Stack
               2.Queue
               3.Linkedlist''')
    a=input("Enter the choice you need to perform: ")
    items=[]
    front=0
    rear=0
    
    if a=='1':
        Stack()
    elif a=='2':
        Queue()
    elif a=='3':
        Linkedlist()
    else:
        print("Invalid Input,Enter the correct choice")
        choice()
def Stack():
        while True:
            print(''' The Stack operations:
                1.push
                2.pop
                3.add
                4.remove
                5.exit''')
        #    break
        while True:
            try:
                b = input("Enter your choice which you need to perform: ")
            except:
                print("Enter the valid input")
            if b == '1':
                while True:
                    try:
                        Val = int(input("Enter the value to push: "))
                        break
                    except:
                        print("enter the valid input to push")
                if is_full():
                    print("Stack is full")
                else:
                    push(int(Val))
            elif b == '2':
                if is_empty():
                    print("Stack is empty")
                else:
                    pop()
            elif b == '3':
                while True:
                    try:
                        Val = int(input("Enter the value to push: "))
                        break
                    except:
                        print("Enter valid value: ")
                if is_full():
                    print("Stack is full")
                else:
                    add(int(Val))
            elif b == '4':
                while True:
                    try:
                        Val = int(input("Enter the value to remove: "))
                        break
                    except:
                        print("Enter valid value to remove")
                if is_empty():
                    print("Stack is empty, not able to remove")
                else:
                    remove(int(Val))
            elif b == '5':
                return choice()
                
            else:
                print("Invalid Input,Enter valid input: ")
                return Stack()
      
def push(data):
    items.append(data)
    print("Stack memory allocation:",items)
def pop():
    items.pop()
    print("Popped items from Stack: ",items.pop())
def add(data):
    items.append(data)
    print("Stack memory allocation:",items)
def remove(b):
    items.remove(b)
    print("Stack memory allocation:",items)
def is_empty():
    return items==[]
def is_full():
    if(maxlength==len(items)):
        return True
    else:
        return False

def Queue():
    front=0
    rear=0
    while True:
        print('''The Queue operations are:
                    1.Enqueue
                    2.Dequeue
                    3.Insert
                    4.Delete
                    5.Quit''')
        while True:
            try:
                b = input("Enter your choice which you need to perform: ")
            except:
                print("Enter the valid input")
        if b == '1':
                while True:
                    try:
                        Val = int(input("Enter the value to Enqueue: "))
                        break
                    except:
                        print("enter the valid input to Enqueue")
                if is_full():
                    print("Queue is full")
                else:
                    Enqueue(int(Val))
                    rear=rear+1      #If queue is not full,increment rear and add element
        elif b == '2':
                if is_empty():
                    print("Queue is empty")
                else:
                    pop(front) #dequeue takes place at front,so pop(front). If queue is not empty dequeue takes at front
                    front=front+1 #so front is incremented to 1
        elif b == '3':
                while True:
                    try:
                        Val = int(input("Enter the value to push: "))
                        break
                    except:
                        print("Enter valid value: ")
                if is_full():
                    print("Queue is full")
                else:
                    insert(int(Val))
                    rear=rear+1
        elif b == '4':
                while True:
                    try:
                        Val = int(input("Enter the value to remove: "))
                    except:
                        print("Enter valid value to remove")
                if is_empty():
                    print("Queue is empty, not able to remove")
                else:
                    delete(int(Val))
        elif b == '5':
                return choice()
                
        else:
                print("Invalid Input,Enter valid input: ")
                return queue()
def Enqueue(data):
    items.append(data)
    print("Queue memory allocation:",items)
def Dequeue():
    items.pop(front)
    print("Popped items from Stack: ",items)
def insert(data):
    items.append(data)
    print("Queue memory allocation:",items)
def delete(b):
    items.delete(b)
    print("Queue memory allocation:",items)
def is_empty():
    return items==[]
def is_full():
    if(maxlength==len(items)):
        return True
    else:
        return False
def Linkedlist():
    head=0
    while True:
        print('''The Linkedlist operations are:
                    1.Insertion
                    2.Deletion
                    3.Find
                    4.Quit''')
        while True:
            try:
                b = input("Enter your choice which you need to perform: ")
                break
            except:
                print("Enter the valid input")
        if b == '1':
            print('''Insertion operation available:
                  1.Start
                  2.End
                  ''')
            c = input("Enter the available insertion operation : ")
            #Starting position
            if c == '1':
                while True:
                    try:
                        val = int(input("Enter the value to insert to list : "))
                        break
                    except:
                        print("Enter the valid value to insert")             
                items.insert(0,Val)
                head = head + 1
                print("Linked list Memory Allocation : ",items)
            # At end position
            if c == '2':
                while True:
                    try:
                        val = int(input("Enter the value to insert to list : "))
                        break
                    except:
                        print("Enter the valid value to insert")             
                items.insert(-1,Val)
                head = head + 1
                print("Linked list Memory Allocation : ",items)
        elif b == '2':
                while True:
                    try:
                        Val = int(input("Enter the value to delete: "))
                    except:
                        print("Enter valid value to delete")
                if is_empty():
                    print("Linkedlist is empty, not able to delete")
                else:
                    delete(int(Val))
                    head=head-1
        elif b == '3':
            while True:
                try:
                    value = int(input("Enter the value to find from Linkedlist : "))
                    break
                except:
                    print("Enter the valid value to find")
            find(value)
        elif b=='4':
            print("Quit")
            return choice()
        else:
            print("Invalid Input")
            return Linkedlist()
            

def Insertion(head,Val):
    items.insert(head,Val)
    print("Linked list Memory Allocation : ",items)

#Defining Deletion operation
def Deletion(Val):
        items.remove(Val)
        print("Linked list Memory Allocation : ",items)
def find(Value):
    if Value in items:
        print("Value is available in items")
    else:
        print("Value is not available in items")


        
while True:
    try:
        maxlength = int(input("Allocate memory for storing data: "))
        break
    except:
        print("\nEnter valid input")
        
front=0
rear=0
head=0
items = []
choice()
    
            
            
            




















