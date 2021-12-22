
#A python program to overriding _setitem() and __getitem_()

class MyList:
       def _init_(self,List):
              self.List=List
#overriding _getitem_() method
       def _getitem_(self,index):
              return self.List[index]

       #overriding _setitem_() method
       def _setitem_(self,index,value):
              self.List[index]=value
       def display(self):
              print(self.List)
L=MyList([23,45,56,97])
print("Actual list is:")
L.display()

index=int(input("Enter index:"))
print(L[index])

index=int(input("Enter index:"))
value=int(input("Enter value:"))
(L[index])=value
print("The updated List is:")
L.display()
