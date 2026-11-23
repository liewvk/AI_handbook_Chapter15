import re

text = "AI helps students learn."
tokens = re.findall(r"\w+|[^\w\s]", text)
print("Tokens:", tokens)
print("Token count:", len(tokens))

