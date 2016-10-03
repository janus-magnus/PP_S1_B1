name = input('Voer naam in:')
bstation = input('Voer beginstation in:')
estation = input('Voer eindstation: ')
codeinput = name+bstation+estation

def code(invoerstring):
    code = ''
    for c in invoerstring:
        enc = ord(c)+3
        code = code + chr(enc)

    print(code)

code(codeinput)
