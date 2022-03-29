import re

text = "👷😇👸👹👺👻✍👼👽👾👿💀💁💂"

print(text)
#print(chr(128120))
#print(0x1f000)

match = re.search(r"[\U0001f000-\U00020000]*", text)
print(match.group(0))

for emoji in text:
    print(emoji, ord(emoji), "{:x}".format(ord(emoji)))


