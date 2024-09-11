def is_isogram(string):
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True

print (is_isogram ("betty"))
print (is_isogram ("tom"))
print (is_isogram ("potato"))
print (is_isogram ("bleach"))
print (is_isogram (""))