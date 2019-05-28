import re

s = 'A B C D'
pattern1 = re.compile('\w+\s+\w+')
print(pattern1.findall(s))
pattern2 = re.compile('(\w+)\s+\w+')
print(pattern2.findall(s))
pattern3 = re.compile('(\w+)\s+(\w+)')
print(pattern3.findall(s))
