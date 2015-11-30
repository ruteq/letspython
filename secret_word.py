text = "How are you? Eh, ok. Low or Lower? Ohhh."\

def secret(text):
    result = ""
    for ch in text:
        if ch.isupper() == True:
            result += ch
    return result

