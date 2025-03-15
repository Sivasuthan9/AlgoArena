# class Dog:
#     def __init__(self,color,name):
#         self.color=color
#         self.name=name

#     def show_color(self): #instant method
#         print(self.color)

# d1=Dog("blue","mike")
# d1.show_color() # Vs Dog.show_color()
# x=d1
# x.color="black"
# d1.show_color()


# class Cal:
#     two=2

#     @classmethod
#     def devide_by_2(cls,num):
#         print(num/cls.two)

# Cal.devide_by_2(5)

# class Node:
#     def __init__(self,data,ref=None):
#         self.data=data
#         self.ref=ref
        
# class SingleLinked:
#     def __init__(self,head=None):
#         self.head=head
     
#     def add_at_end(self,data):
#         new_node=Node(data)
#         if not self.head:
#             self.head=new_node
#             return
#         temp=self.head
#         while temp.ref:
#             temp=temp.ref
#         # print(new_node.data)
#         temp.ref=new_node

#     def display(self):
#         tem=self.head
#         while tem:
#             print(tem.data,end="->")
#             tem=tem.ref
#         print(None)

# ssl=SingleLinked()
# ssl.display()
# ssl.add_at_end(2)
# ssl.display()
# ssl.add_at_end(4)
# ssl.add_at_end(-5)
# ssl.display()

