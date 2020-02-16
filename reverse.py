print("hello little project")

arr = [1,2,3,4,5]

new = slice(2,5)
newobj = arr[new]
newobj.extend([1,2])

print(arr)
print(newobj)



