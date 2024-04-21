class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head = new_node
    def add_end(self,data):
        new_node=node(data)
        if self.head is None:
            print("it is the first node..")
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,after_node):
        n=self.head
        while n is not None:
            if n.data==after_node:
                break
            n=n.ref
        if n is None:
            print("Node not found..")
        else:
            new_node=node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,add_before):
        if self.head is None:
            print("linked list is empty..")
            return
        elif add_before==self.head.data:
            l.add_begin(data)
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==add_before:
                break
            n=n.ref
        if n.ref is None:
            print("node not found..")
        else:
            new_node=node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def if_empty(self,data):
        if self.head is None:
            new_node=node(data)
            self.head=new_node
        else:
            print("linked list is not empty..")
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty..")
            return
        self.head=self.head.ref
    def delete_end(self):
        if self.head is None:
            print("linked list is empty..")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def delete_node(self,x):
        if self.head is None:
            print("linkedlist is empty..")
        elif self.head==x:
            self.head=self.head.ref
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("node not found..")
        else:
            n.ref=n.ref.ref


l=linkedlist()
while True:
    print("1.traverse 2.add_begin 3.add_end 4.Insert_at_middle 6.to_insert_firstnode 8.delete_end 9.delete_node 7.delete_firstnode 5.exit")
    choice = input("entre your choice:")

    if choice == "1":
        l.traversal()

    elif choice == '2':
        d = input("entre data you want in linkedlist:")
        l.add_begin(d)
    elif choice=='3':
        d = input("entre data you want in linkedlist:")
        l.add_end(d)

    elif choice=='4':
        print("lease choose where we have to insert 1.Afternode 2.Beforenode")
        choice=input("entre your choice:")
        if choice=='1':
            d=input("entre data you want to entre:")
            a=input("after node:")
            l.add_after(d,a)
        elif choice=='2':
            d=input("entre data to be inserted:")
            b=input("before data:")
            l.add_before(d,b)

        else:
            print(" insert node at middle.entre correct choice..")
    elif choice=='5':
        break
    elif choice=='6':
        d=input("entre data to insert:")
        l.if_empty(d)
    elif choice=='7':
        l.delete_begin()
    elif choice=='8':
        l.delete_end()
    elif choice=='9':
        d=input("entre node to be deleted:")
        l.delete_node(d)
    else:
        print("entre correct choice...")










