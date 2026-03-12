matrix = [
          ['a','b','c'],  # Row 0
          ['d','e','f'],  # Row 1
          ['g','h','i']   # Row 2
         ] 

#matrix.remove(['a','b','c'])
#matrix.pop()
#matrix[1].remove('e')
matrix[-1].pop(0)
matrix[0].pop()
print(matrix)