# Devin Schwartz
file=open("bulbs.txt","r")
lights=file.read()
i=0
count=0
while i+4<len(lights):
    section=lights[i:i+5]
    if len(set(section))==5:
        i+=5
        count+=1
    else:
        i+=1
print(count)