import re

pattern = re.compile(r'(\w+)@(\w+\.\w+)')
match = pattern.search('contact@company.com')

if match:
    print(match.group(0)) #Full Match
    print(match.group(1)) #contact
    print(match.group(2)) #company.com


pattern = re.compile(r'colou?r') #Match color or colour
print(pattern.search('color').group())
print(pattern.search('colour').group())


text = "Emails: info@example.com, support@example.com"
emails = re.findall(r'\b[\w.%+]+@[\w-]+\.[a-zA-Z]{2,}\b',text)
print(emails)


pattern = re.compile(r'[aeiou]') #Matches all vowels
print(pattern.findall('hello world'))



phone = "123-456-789"
if re.match(r'^\d{3}-\d{3}-\d{4}$', phone):
    print("Valid")
else:
    print("Invalid")
    

text = "<p>First</p><p>Second</p>"
greedy = re.compile(r'<p>.*</p>')

non_greedy = re.compile(r'<p>.*?</p>')

print(greedy.findall(text))

print(non_greedy.findall(text))


text = "Hello WORLD"

print(re.sub(r'world','Python',text,flags=re.IGNORECASE))