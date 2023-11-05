# moving zeros to the end of array and non zero at the beginning of the array
arr = [1,0,4,0,2,8,0,14]
# pointer at the start point
i = 0
j = 0
for j in range(8):
    # checking element is non zero or not
    if(arr[j] != 0):
        arr[i]= arr[j]
        # increment to the pointer i
        i=i+1
# adding remaining places by the zero 
for i in range(i,8):
    arr[i] = 0
print(arr)