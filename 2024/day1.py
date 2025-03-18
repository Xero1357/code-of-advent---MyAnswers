with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\data.txt", "r") as file:
    map = file.read()
    A = map.split('\n') 
print(A)

with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\data1.txt", "r") as file:
    map1 = file.read()
    A1 = map1.split('\n')
print(A1)

B = sorted(int(x) for x in A)
B1 = sorted(int(x) for x in A1) # list method
print(B, B1)

difference = []

for i in range(len(B)): # list comprehension
    difference.append(B1[i] - B[i])
total = sum(difference)

print(total, difference)

