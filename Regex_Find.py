import re

"""pattern = re.compile(r'(\w+)@(w+\.\w+)')
match = pattern.search('contact@company.com')

if match:
    print(match.group(0)) #full Match
    print(match.group(1)) #contact
    print(match.group(2)) #company.com"""

pattern = re.compile(r'colou?r') #Match color, or colour
print(pattern.search('color').group())
print(pattern.search('colour').group())
