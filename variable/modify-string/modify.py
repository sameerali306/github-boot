# upper case method
a="hello i am sameer ali"
# print(a.upper())
ab="sameer ali"
print(ab.upper())
b="i ma from gilgit baltistan"
print(b.upper())
# lower case method
a="SAmeer alli Ypouathhxbbjxbjh"
ba="PAKISTAN"
print(ba.lower())
print(a.lower())
b="SAMEER ALI YPNARE "
print(b.lower())

# remove the white space
a="hello i am from gilgit baltistan"
print(a.strip())
text = "   Hello, World!   "
print(text)
clean_text = text.strip()
print(f"'{clean_text}'")


# replace method
a="hello"
text = "Hello, World!"
print(text)
no_spaces = text.replace(" ", "")
print(no_spaces)
word="hello , i am sameer ali"
print(word)
# " ","" this line mean remove white string with empty string
ans=word.replace(" ","")
print(ans)
# print(a.replace("hell","kil"))
b="hello"
print(b.split(","))


# splits method
# the split method remove the white space and divide each word into indivical component
words=" hello ! , i ma  sameer    ali  "
# print(words.split())
word=words.split()
ans=" ".join(word)
print(ans)
