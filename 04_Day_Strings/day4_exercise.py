"""
1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
3. Declare a variable named company and assign it to an initial value "Coding For All"."""
# 1
print('Thirty', 'Days', 'Of', 'Python')

print('Coding', 'For' , 'All')

company = "coding For All"
print(company)

"""
4. Print the variable company using _print()_.
5. Print the length of the company string using _len()_ method and _print()_.
6. Change all the characters to capital letters using _upper()_ method.
7. Change all the characters to lowercase letters using _lower()_ method."""

# 4
print(len(company))

print(company.upper())
print(company.lower())

"""
8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
9. Cut(slice) out the first word of _Coding For All_ string.
10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
11. Replace the word coding in the string 'Coding For All' to Python."""


print(company.capitalize())
print(company.title()+"test")
print(company.swapcase())

print(company[1:])

if 'coding' in company:
    new_com = company.replace('coding','Codeing')
    print(new_com)

"""
12. Change Python for Everyone to Python for All using the replace method or other methods.
13. Split the string 'Coding For All' using space as the separator (split()) .
14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
15. What is the character at index 0 in the string _Coding For All_.
16. What is the last index of the string _Coding For All_."""

#split จะเป็นตัวหาว่ามีตัวที่เรากำหนดว่าอะไร แล้วมันจะทำการแยกคำตามนั้น
print('Coding For All'.split(" "))

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

#15
print("_Coding For All"[0])
print("_Coding For All"[-1])

"""
17. What character is at index 10 in "Coding For All" string.
18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
19. Create an acronym or an abbreviation for the name 'Coding For All'.
20. Use index to determine the position of the first occurrence of C in Coding For All."""

print("Coding For All"[10])

code = "Codeing For All"
print(code.find('C'))


""" 21. Use index to determine the position of the first occurrence of F in Coding For All.
22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'"""


print(code.find('F'))
print(len("Coding For All People"))
print("Coding For All People".rfind('l'))

bec = 'You cannot end a sentence with because because because is a conjunction'
rebec = []
new_bec = bec.split(' ')
for s in new_bec:
    if s != 'because':
        rebec.append(s)
        reebec = " ".join(rebec)
print(reebec)

"""
26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
28. Does '\'Coding For All' start with a substring _Coding_?
29. Does 'Coding For All' end with a substring _coding_?
30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
31. Which one of the following variables return True when we use the method isidentifier():
    - 30DaysOfPython
    - thirty_days_of_python"""

#28
print(code.startswith("\\"))
print(code.endswith("coding"))

def check(test):
    a = test.isidentifier()
    return a

strr = "30DaysOfPython"
strr2 = "thirty_days_of_python"

#จะได้ false เพราะ isidentifier ถ้าตัวแรกขึ้นตัวด้วยตัวเลข จะเป็น false
print(check(strr))
print(check(strr2))

"""
32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
33. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
34. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
35. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
36. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
37. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
38. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string."""

program = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print(" # ".join(program))

"""
40. Use the new line escape sequence to separate the following sentences.
    ```py
    I am enjoying this challenge.
    I just wonder what is next.
    ```
41. Use a tab escape sequence to write the following lines.
    ```py
    Name      Age     Country
    Asabeneh  250     Finland
    ```
42. Use the string formating method to display the following:

```sh
radius = 10
area = 3.14 * radius ** 2
The area of a cricle with radius 10 is 314 meters square.
```"""
radius = float(input("Your radius : "))
area = 3.14 * radius * 2 
print(f"The area of a circle with radius {radius:.1f} is {area:.2f} meter sq.")

"""
36. Make the following using string formating methods:

```sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""












