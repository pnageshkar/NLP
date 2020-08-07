import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

#pattern = re.compile(r'\bHa')
#pattern = re.compile(r'start', re.I)
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#pattern = re.compile(r'[89]00.\d{3}.\d{4}')
#pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)

# with open('C:/Data_Science/NLP/code/NLP/Learn/RegExp/data.txt','r') as f:
#    contents = f.read()
#matches = pattern.finditer(contents)
    
for match in matches:
    print(match)
#matches = pattern.search(sentence)
#print(matches)