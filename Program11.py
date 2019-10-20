# Remove punctuation from the string
# Complexity: E

a= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str = "Hello!!!, he said ---and went."
p= ""
for char in str:
   if char in a and char!=".":  
       p = p+ char
print(p)

