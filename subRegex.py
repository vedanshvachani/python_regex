import re
replaceRegex = re.compile(r'Agent (\w{4})\w*')
print(replaceRegex.sub(r'pin \1****','Agent vedansh has called Agent shanks'))

