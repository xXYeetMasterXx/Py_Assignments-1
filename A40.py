word = input("In: ")
count = 0
word1 = word.replace('a','')
word2 = word1.replace('e','')
word3 = word2.replace('i','')
word4 = word3.replace('o','')
word5 = word4.replace('u','')
for letter in word5:
  count += 1
print(count)
