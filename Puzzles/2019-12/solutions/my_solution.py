colors = list("ROGBP")

with open('bulbs.txt') as f:
     lights = f.read()

num_occ = 0
curr_pos = 0
while curr_pos < len(lights)-4: # don't go past the end!
    for i in range(5):
        if lights[curr_pos+i] in colors:
            colors.remove(lights[curr_pos+i])
        else:
            break
    
    if len(colors) == 0:
        num_occ += 1
        curr_pos += 5
    else:
        curr_pos += 1
    
    colors = list("ROGBP")

print(num_occ)

