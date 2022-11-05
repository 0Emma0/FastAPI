#Lists
list_example = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"List {list_example}")
print(list_example[-1]) # print the last element of the list
print(list_example[4:]) # print from position 4 to last
print(len(list_example)) # Count elements of the list
print(80*"-")
##List methods
list_example.append("DevOps") #add elements to the end of the list
print(list_example)
list_example.insert(2,3) #add the value 3 in the position 2
print(list_example)
list_example.extend([1,2,3]) #add elements to final 
print(list_example)
print(list_example.count("Monday")) #Count 
print(list_example.pop()) #delete elements of the list
list_example.remove()
list_example.reverse()
list_example.sort(reverse=True)

print(80*"-")
#Tuples
tuple_example = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(f"Tuple {tuple_example}")
print(tuple_example[0]) # print the first element of the tuple
print(tuple_example[:4]) # print from position 0 to 4
print(len(tuple_example)) # Count elements of the tuple

#Set
#Dictionaries
