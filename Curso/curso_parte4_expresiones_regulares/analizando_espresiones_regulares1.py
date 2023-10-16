import re

text = "The quic brown fox jumps over the lazy dogs"

x = re.search("^The.*dogs", text)
print(x)

if x:
    print("SI")
else:
    print("NO")
