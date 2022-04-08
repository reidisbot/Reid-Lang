def comp():
    ff = fr.replace("print(", "prnt(")
    ff = ff.replace("def", "deff")
    ff = ff.replace("=", "")
    ff = ff.replace("", "")
    ff = ff.replace("write ", "print('")
    ff = ff.replace(".", "')")
    ff = ff.replace("", "")
    with open('output.o', 'w') as t:
        t.write(ff)
        exec(ff)

while True:
    intt = input()
    intt = intt.replace("run ", "")
    if intt == 'End' or intt == 'end' or intt == 'exit' or intt == 'Exit':
        print("Exited(Maybe error)")
        exit()
    fs = None
    try:
        fs = open(intt, 'r')
    except:
        pass
    if fs == None:
        print("That is not a valid file name!")
        continue
    fr = fs.read()
    comp()