def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return set(s.lower()) >= alphabet

str = input("Enter the sentence: ")
if(is_pangram(str)):
    print("It is a pangram")
else:
    print("It is not a pangram")
