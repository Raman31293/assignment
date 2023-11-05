matrix = [[1,0,1,1],[1,1,1,1],[1,1,1,1]]
zeroRows = set()
zeroColumns = set()

for i in range (3):
    for j in range(4):
        # getting current value of zero in matrix
        if(matrix[i][j] == 0):
            # store the value in row and column set            
            zeroRows.add(i)
            zeroColumns.add(j)  
#set entire rows and columns to 0 
for i in zeroRows:
    # iterate through whole column
    for j in range(4):
        matrix[i][j] = 0
for j in zeroColumns:
    # iterate through whole row
    for i in range(3):
        matrix[i][j] = 0   
                
print(matrix)