import difflib 
def string_similarity(str1, str2): 
result =  difflib.SequenceMatcher(a=str1.lower(), b=str2.lower()) 
return result.ratio() 
str1 = 'Python Exercises' or str1 = input("Enter a sentence: ") 
str2 = 'Python Exercises' or str2 = input("Enter a sentence: ") 
print("Original string:") 
print(str1) 
print(str2) 
print("Similarity between two said strings:") 
print(string_similarity(str1,str2)) 
str1 = 'Python Exercises' or str1 = input("Enter a sentence: ") 
str2 = 'Python Exercise' 
or str2 = input("Enter a sentence: ") 
print("\nOriginal string:") 
print(str1) 
print(str2) 
print("Similarity between two said strings:") 
print(string_similarity(str1,str2)) 
