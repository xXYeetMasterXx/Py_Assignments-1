# input how many arrays
num_arrays = int(input("How many arrays do you want to find the average of?"))

#Hint:
for x in range(0,num_arrays):
 a = input("Enter your array:").split()
 a = [int(x) for x in a]
 l = sum(a) / (len(a))
 print('The average is:',l)
