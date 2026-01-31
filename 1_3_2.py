def to_lower(s):
    
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':      
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result



def to_upper(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':           
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result



def toggle_case(s):
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':           
            result += chr(ord(ch) + 32)
        elif 'a' <= ch <= 'z':        
            result += chr(ord(ch) - 32)
        else:
            result += ch               
    return result

text = input("Enter a string: ")

print("Lowercase :", to_lower(text))
print("Uppercase :", to_upper(text))
print("Togglecase:", toggle_case(text))
