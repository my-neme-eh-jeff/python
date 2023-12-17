list1=[10,20,30]
print("Original List ",list1)
list1.append(50)
print("List after appending",list1)
list2=[111,333]
print("Original List ",list1)
list1.extend(list2)
print("List after extending",list1)
print("Original List ",list1)
list1.insert(2,15)
print("List after inserting",list1)
print("Original List ",list1)
list1.pop(1)
print("List after Popping",list1)
print("Original List ",list1)
list3=list1.copy()
print("List after copying",list3)
print("Original List ",list1)
list3=list1.clear()
print("List after clearing",list3)
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list_union = set(list1 + list2)
print(f"List Union: {list_union}")
list_intersection = set(list1).intersection(set(list2))
print(f"List Intersection: {list_intersection}")
list_difference = set(list1).difference(set(list2))
print(f"List Difference: {list_difference}")

tuple1=(10,40,20,25,80,90,30,25)
print("Original tuple ",tuple1)
print("Length of tuple ",len(tuple1))
print("Count of 25 in tuple",tuple1.count(25))
print("Index of 25 in tuple",tuple1.index(20))
print("Sorting in tuple ",sorted(tuple1))
print("Min in tuple ",min(tuple1))
print("Max in tuple ",max(tuple1))
print("Sum of tuple ",sum(tuple1))
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
tuple_union = set(tuple1 + tuple2)
print(f"Tuple Union: {tuple_union}")
tuple_intersection = set(tuple1).intersection(set(tuple2))
print(f"Tuple Intersection: {tuple_intersection}")
tuple_difference = set(tuple1).difference(set(tuple2))
print(f"Tuple Difference: {tuple_difference}")

set1={'a','b','c','d','e'}
set1.add('f')
print("Set after adding element",set1)
set1.discard('e')
print("Set after dicarding element",set1)
set1.remove('a')
print("Set after removing element",set1)
set1.pop()
print("Set after popping element",set1)
set1.clear()
print("Set after clearing element",set1)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set_union = set1.union(set2)
print(f"Set Union: {set_union}")
set_intersection = set1.intersection(set2)
print(f"Set Intersection: {set_intersection}")
set_difference = set1.difference(set2)
print(f"Set Difference: {set_difference}")


dict1 = {'1':'One','2':'Two','3':'Three'}
print("Original dictionary:",dict1)
seq=('1','2','3')
print(dict1.fromkeys(seq, None))
dict2 = dict1.copy()
print("Copied dictionary:",dict2)
dict1.clear()
print("The dictionary after clearing:",dict1)
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'd': 4, 'e': 5}
dict_union = {**dict1, **dict2}
print(f"Dictionary Union: {dict_union}")
dict_intersection = set(dict1.keys()).intersection(set(dict2.keys()))
print(f"Dictionary Intersection: {dict_intersection}")
dict_difference = set(dict1.keys()).difference(set(dict2.keys()))
print(f"Dictionary Difference: {dict_difference}")


def histogram(l):
    s= list(set(l))
    count_s=[]
    for i in s:
        count_s.append((i,l.count(i)))
    hist=sorted(count_s,key=lambda x: x[1])
    return hist
print("Histogram :",histogram([13,12,14,15,11,13,7,12,7,13,14,12]))    

def armstrong(a):
    a = str(a)
    n = len(a)
    sum = 0
    for i in a:
        sum += int(i)**n
        
    if sum == int(a):
        print('yes')
    else:
        print('no')
a=int(input('Enter a number:'))
armstrong(a)

def perfect(n):
    sum = 0 
    for i in range(1, n-1):
        if n % i == 0: 
            sum += i               
    if n == sum:
        return True
    else:
        return False
print(f"\nperfect number check : ",perfect(6))

print("\nTower of Hanoi : ")
def hanoi (disks, source, auxiliary, target):
    if disks ==1:
        print('Move disk 1 from peg{} to peg{}'.format(source, target))
        return
    hanoi(disks -1, source, target, auxiliary) 
    print('Moves disk{} from peg{} to peg{}'.format(disks,source, target))
    hanoi(disks - 1, auxiliary, source, target)
disks = int(input("Enter number of disks:"))
hanoi(disks, 'A', 'B', 'C')

print("\nLamda Function : ")
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
maximum = lambda a,b : a if a>b else b
print(f"Maximum btw {a},{b} is {maximum(a,b)}")

n = int(input("Enter the number of fibonacci : "))
if n <=0: print("Error : (--)")
else:
    l = [0,1]
    for i in range(1,n-1):
        l.append(l[-1]+l[-2])
    print(l)
    
x=int(input("Enter number "))
fact = 1
if x <0:
   print("error 6000")
else:
   for i in range(1,x+1):
      fact *= i
print(f"Factorial of {x} is {fact}")
