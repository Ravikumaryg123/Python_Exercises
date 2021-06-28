import re

# Your code goes here
find_members = []
key = "find"

for data in dir(re):
    if key in data:
        find_members.append(data)

print(sorted(find_members))