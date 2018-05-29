#For each case, determine whether or not it is possible to produce the third number
def numberFun(a, b, c):
  # insert your logic here
  if a-b == c or b-a == c or a*b == c or a/b == c or b/a == c or a+b == c:
    return True
  else:
    return False
  
  
# Test cases. Don't modify  
print(1,numberFun(1, 2, 3))	     # Possible
print(2,numberFun(4, 5, 1))	   	 # Possible
print(3,numberFun(10, 2, 4))	     # Impossible	
print(4,numberFun(9, 2, 18))	     
print(5,numberFun(9, 5, 14))	   	
print(6,numberFun(90, 25, 65))	   
print(7,numberFun(288, 16, 18))
print(8,numberFun(56, 5, 260))
print(9,numberFun(4, 65, 260))
