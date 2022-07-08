import codecs
pnc = [".", ",", "?", "-", ",|", "s", "and"]
newlines = []
f = codecs.open('final.txt', 'r', "utf-8")
lines = f.readlines()
raw = [lin for lin in lines]
print("cleaning...")
for dirtyline in raw:
    splittedline = dirtyline.split(" ")
    listed = [word for word in splittedline]
    ist = listed[0]
    for p in pnc:
        if ist == p:
            listed.remove(ist)         
    cleanline  = " ".join(listed)
    newlines.append(cleanline+"\n") 
print("done cleaning")
print("deleting short lines...") 

filtered_lines = [line for line in newlines if len(line) > 19]

f = codecs.open('product.txt', 'w', 'utf-8')
for lne in filtered_lines:
    f.write(lne)
        
print("done")