#Enter 2 lists of integers
list1=[10 ,20,30,40,50]
list2=[10,15,20,35,40]
print("list1=",list1)
print("list2=",list2)
# check Whether list are of same length
if len(list1)==len(list2):
    print("list are of same length")
else:
    print("List are not of same length")
    #check whether list sums to same value 
if sum(list1)==sum(list2):
    print("List are same sum")
else:
    print("List are not  same sum")
    #check  whether any value occur in both
list3=[x for x in list1 if x in list2]
if len(list3)<1:
    print("No value occure in both")
else:
    print("common values:",list3)