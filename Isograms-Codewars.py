def is_isogram(string):
    seen = set()
    # iteratinig over each character and converting to each to lowercase for processing regardless of case
    for char in string.lower():
        # if a character is repeated in the set False is returned
        if char in seen:
            return False
        seen.add(char)
    # if characters do not repeat returns true
    return True

print (is_isogram ("betty"))
print (is_isogram ("tom"))
print (is_isogram ("potato"))
print (is_isogram ("bleach"))
print (is_isogram (""))
print (is_isogram ("MoMma"))