'''
Author:Ann mariya tony
Date:22-11-2024
'''
list1=[6,5,25,12,1]
print("First list:",list1)
list2=[2,14,7,20,3]
print("Second list:",list2)
list3=list1+list2
print( "Merged list:",list3)
even=[]
odd=[]
for i in list3:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
sorted_list=even+odd
print("Sorted list:",sorted_list)
