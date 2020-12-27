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






