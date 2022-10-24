l = ["Omkar", " Dara", "Kushal"]
t = ("Omkar", " Dara", "Kushal")
s = {"Omkar", " Dara", "Kushal"}


#List 

kushal_name = l[2]
kushal_name = t[2]
#print(kushal_name)
l[0] = "Chaudhari"
#t[0] = "Chaudhari"
print(l)
print(l[-1])

#Indexing
# l[start : end : step_size]

l = [1,2,3,4,5,6,7,8,9]
#print(l[2:5:2])
#print(l[::-1])

#print(dir(l))


# to add elements : append, extend , insert
l.append(10)
#l.append(t)
l.extend([5,10,11,12,13,14,15])
#print(l.count(10))
l.insert(2,5)

# to delete elements : delete, pop
#l.remove(5)
l.pop(5)

#sorting

l = [1,6,3,7,89,223,112,887,221]
#l.sort()
#l.sort(reverse=True)
#l.reverse()
sorted(l)
#print(l)


# tuples are immutable. ie. you cant update or remove items for it.

# sets
# sets are mutable (at base)    
# cannot function with indexing

s = {"Omkar", " Dara", "Kushal"}
#print(dir(s))

s.add("Jan")
#print(s)

s = frozenset(s)
print(dir(s))



