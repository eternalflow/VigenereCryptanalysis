def textfromfile(filename):
    with open(filename, "r") as file:
        text = file.read()
    return text

def texttofile(text, filename):
    with open(filename, "w") as file:
        file.write(text)

def MrProper(dirtytext):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cleantext = ""
    for line in dirtytext:
        for s in line:
            if s.lower() in alphabet:
                cleantext += s.lower()
    return cleantext

dirty = textfromfile("big")
clean = MrProper(dirty)
texttofile(clean, "bigclean")