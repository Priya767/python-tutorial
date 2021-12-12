word = input("Enter the word: ")
vowels =['a','e','i','o','u','A','E','I','O','U']
list1=[]
for x in word:
    if (x in vowels and x not in list1):
        list1.append(x)
print("Vowels present in given word : ",list1)