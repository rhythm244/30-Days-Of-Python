import math
"""
1. Declare an empty list
2. Declare a list with more than 5 items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7. Print the list using _print()_
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print the list after modifying one of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list."""

exam_list = []
list_more_5 = range(0,8)

for i in list_more_5:
    print(i)
print()
print(len(list_more_5))

lenn = len(list_more_5)

print(list_more_5[0],list_more_5[(lenn+1)//2],list_more_5[-1])

mixed_data_types = ["wasawat",30,175,"maried","65/110 vistavile"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple","IBM","Oracle", "Amazon"]

print(len(it_companies))
it_companies[0] = "Line"

print(it_companies)

new_it = "#".join(it_companies)
print(new_it)

print('Google' in it_companies)

"""
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list
25. Destroy the IT companies list
26. Join the following lists: """

#list.sort(reverse=True)
it_companies.sort(reverse=False)

print(it_companies)
#เอาสามตัวหลังออก
print(it_companies[:-3])
#เอาสามตัวหน้าออก
print(it_companies[:-3])

#ลบโดยที่กระโดดทีละสองตัว
del it_companies[::2]
print(it_companies)

"""
1. The following is a list of 10 students ages:

```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

- Sort the list and find the min and max age
- Add the min age and the max age again to the list
- Find the median age (one middle item or two middle items divided by two)
- Find the average age (sum of all items divided by their number )
- Find the range of the ages (max minus min)
- Compare the value of (min - average) and (max - average), use _abs()_ method
"""

#lesson learn => การ sort ควรใส่ไว้ในฟังก์ชั่น เมื่อทำการ sort เสร็จ แล้ว return กลับออกไป
from numpy import mean
from country import country
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

def thong_sort(li):
    li.sort()
    return li
print(thong_sort(ages))

new_list = thong_sort(ages)

#find min and max
print(max(new_list))
print(min(new_list))

ages_avg = mean(ages)
print(ages_avg)

#import country_list form country.py in this folder
country_list = country()

# print(country_list)

print(len(country_list))

count = 0

"""Divide the countries list into two equal lists if it is even if not one more country for the first half."""

if len(country_list) % 2 == 1:
    print("odd")
    count = 0
    country_first_half = []
    for i in country_list:
        count = count + 1
        #ถ้า len country_list == ครึ่งนึงของ list ทั้งหมด
        if count <= (len(country_list) // 2):
            country_first_half.append(i)
        # """ถ้า count มากกว่าครึ่ง ให้เพิ่ม i ไปอีกตัวนึง i คือ ประเทศอีกประเทศนึง"""
        else:
            country_first_half.append(i)
            print(country_first_half)
            break

else:
    #len(country_list) % 2 == 0
    print("even")
    count = 0
    country_first_half = []
    for i in country_list:
        count = count + 1
        #ถ้า len country_list == ครึ่งนึงของ list ทั้งหมด
        if count <= (len(country_list) // 2):
            country_first_half.append(i)
        # """ถ้า count มากกว่าครึ่ง ให้เพิ่ม i ไปอีกตัวนึง i คือ ประเทศอีกประเทศนึง"""
        else:
            print(country_first_half)
            break