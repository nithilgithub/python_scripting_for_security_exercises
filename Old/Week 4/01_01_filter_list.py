# Exercise

# stage 1
# Write a program to count the number of strings where the string length is 2 or more
# sample list: ['aaaa', 'a', 'ab', 'abc', ]
# result : 3

# Sample list
sample_list1 = ['aaaa', 'a', 'ab', 'abc']

# Count strings with length 2 or more
count_stage1 = sum(1 for s in sample_list1 if len(s) >= 2)

print("Number of strings with length 2 or more:", count_stage1)




## Stage 2
# Now count the number of strings that have length 2 or more
# AND the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

# Sample list
sample_list2 = ['abc', 'xyz', 'aba', '1221']

# Count strings with length 2 or more and first and last character are the same
count_stage2 = sum(1 for s in sample_list2 if len(s) >= 2 and s[0] == s[-1])

print("Number of strings with length 2 or more and first and last character the same:", count_stage2)


