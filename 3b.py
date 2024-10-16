from difflib import SequenceMatcher
s1=input("Enter the first string")
s2=input("Enetr the second string")
print(SequenceMatcher (None,s1,s2).ratio())