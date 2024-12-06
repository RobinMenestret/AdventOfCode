import re
print(sum([10*int(re.findall(r'\d',s)[0])+int(re.findall(r'\d',s)[-1]) for s in open("f", 'r').read().split('\n')]))