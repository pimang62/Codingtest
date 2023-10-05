for i in range(4, 0, -1):
    print(i)
    
for i in reversed(range(1, 5)):
    print(i)
    
def rotate(array):
    return list(zip(*array[::-1]))

print(rotate(array=[[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]]))

"""
[(7, 4, 1), 
 (8, 5, 2), 
 (9, 6, 3)]
"""