# # Most common datastructure operations (Reading, Deletion, Insertion)


# # ---------- Reading from an array ----------

# # initialize myArray
# myArray = [1, 3, 5]
# # access an arbitrary element, where i is the index of the desired value
# print(myArray[0]) # Outputs: 1

# # Traversing through an array O(n)
# for i in range(len(myArray)): # range(5) Outputs: 0, 1, 2, 3, 4
#     print(myArray[i])

# # Or

# i = 0
# while i < len(myArray):
#     print(myArray[i])
#     i += 1


# # ---------- Deleting from an array ----------

# # Remove from the last position in the array if the array
# # is not empty (i.e. length is non-zero)
# def removeEnd(arr, length):
#     if length > 0:
#         # Overwrite last element with some default value.
#         # We would also consider the length to be decreased by 1.
#         arr[length - 1] = 0


# # Remove value at index i before shifting elements to the left.
# # Assuming i is a valid index.
# def removeMiddle(arr, i, length):
#     # Shift starting from i + 1 to end. 
#     for index in range(i + 1, length):
#         arr[index - 1] = arr[index]
#     # No need to 'remove' arr[i], since we already shifted


# # ---------- Inserting in an array ----------

# # Inserting at the end of the array 0(1)
# # Insert n into arr at the next open position.
# # Length is the number of 'real' values in arr, and capacity
# # is the size (aka memory allocated for the fixed size array).
# def insertEnd(arr, n, length, capacity):
#     if length < capacity:
#         arr[length] = n

# # Inserting at the ith index
# # Insert n into index i after shifting elements to the right.
# # Assuming i is a valid index and arr is not full. 
# def insertMiddle(arr, i, n, length):
#     # Shift starting from the end to i.
#     for index in range(length - 1, i - 1, - 1):
#         arr[index + 1] = arr[index]

#     # Insert at i
#     arr[i] = n



# myArray = [1, 2, 3, 4, 5]
# length = len(myArray) 

# removeMiddle(myArray, 1, length)
# print(myArray)
# removeEnd(myArray, length)
# print(myArray)

# myArray = [1, 2, 3, 4, 5, 0]
# length = len(myArray) - 1

# insertEnd(myArray, 10, length, 10)
# print(myArray)

# myArray = [1, 2, 3, 4, 5, 0]
# length = len(myArray) - 1

# insertMiddle(myArray, 2, 69, length)
# print(myArray)



# ---------- Reading from an array ----------
# Initializing array
myArray = [1, 2, 3, 4, 5]
# Traversing the array
for element in myArray:
    pass
    # print(element)
# Or
for index in range(len(myArray)):
    pass
    # print(index) # Outputs: 0, 1, 2, 3, 4
    # print(myArray[index])
# Or
index = 0
while index < len(myArray):
    # print(myArray[index])
    index += 1


# ---------- Deleting from an array ----------
# Deleting from the end of the array
def removeEnd(arr, length):
    if length > 0: # if array is not empty
        arr[length - 1] = None # Overwriting the last element with 0 

myArray = [1, 2, 3, 4, 5, 6]
length = len(myArray)
removeEnd(myArray, length)
print(myArray)

# Deleting at an ith index and shifting
def removeMiddle(arr, i, length):
    for index in range(i + 1, length): # index range is starting at i + 1 and ending but not including length of array
        arr[index - 1] = arr[index] # Replacing the current element with the next element
    
    for i in range(len(arr)):
        if i == len(arr) - 1 and arr[i] > 0:
            arr[i] = None
           
myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(myArray)
removeMiddle(myArray, 3, length)
print(myArray)


# ---------- Inserting in an array ---------- 
# Inserting at the end of the array O(1)
def insertEnd(arr, num, length, capacity):
    if length < capacity: # length is the number of 'real' values in arr (4 and 5 so 2)
        arr[length] = num 

myArray = [4, 5, None]
insertEnd(myArray, 69, 2, 3)
print(myArray)

# Inserting at the ith index 
def insertMiddle(arr, i, num, length):
    for index in range(length - 1, i - 1, -1): # (2, 0, -1)
        arr[index + 1] = arr[index] # shifts the numbers 
    arr[i] = num # Inserting at i
myArray = [4, 5, 6, 7, 8, 9, 0]
length = len(myArray) - 1
insertMiddle(myArray, 2, 69, length)
print(myArray)