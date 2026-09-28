# Inbuild String Methods - Single program
s = "  kodNest Technologies 123  "

print("original String:", s) # kodNest Technologies 123

# Case conversion methods
print("upper():", s.upper()) # KODNEST TECHNOLOGIES 123
print("lower():", s.lower()) # kodnest technologies 123
print("capitalize():", s.capitalize()) #  kodnest technologies 123
print("title():", s.title()) #  kodnest Technologies 123
print("swapcase():", s.swapcase()) #  kodNest Technologies 123

# Searching & counting
print("find('Tech'):", s.find("Tech")) # 10
print("count('o'):", s.count("o")) # 3

#Replace
print("replace('123', '2025'):", s.replace("kodNest", "2025")) #  2025 Technologies 123

#Start & End check
print("Startswith('  kod'):", s.startswith("  kod")) # True
print("endswith('123  '):", s.endswith("123  ")) #True

# Split & Join
words = s.split() #
print("split():", words)
print("join():", "-".join(words)) #

# Strip spaces
print("strip():", s.strip()) # kodNest Technologies 123
print("lstrip():", s.lstrip()) # kodNest Technologies 123
print("rstrip():", s.rstrip()) #    kodNest Technologies 123

s = "    "
# Checking methods
print("isalpha():", s.isalpha())# False
print("isdigit():",s.isdigit())# False
print("isspace():", s.isspace())# False
print("isalnum():", s.isalnum())# False
print("Hello".isalnum()) # True

# Length
print("Length of string:", len(s)) # 4
