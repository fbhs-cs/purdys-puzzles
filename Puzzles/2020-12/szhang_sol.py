# Submitted by Samuel Zhang 12/22/2020

directions = "N.W$WNNN$XPX..$NW;SP;P$;.;$P.W.PWE$SNPEW;NN;EN.PXS;XSP$NSPS.SNNX.;ESW$NXSXXS;EXX;PESSXWX$PWPXXN$$$X......"
distance = 0
far_distance = 0
x = 0
y = 0
i = 0
while (i < len(directions)):
    if i == len(directions)-1:
        if directions[i] == ";":
            distance += (x**2+y**2)**0.5
            x = 0
            y = 0
        elif directions[i] == "N":
            distance += 100
            y += 100
        elif directions[i] == "E":
            distance += 100
            x += 100
        elif directions[i] == "S":
            distance += 100
            y -= 100
        elif directions[i] == "W":
            distance += 100
            x -= 100
        distance += (x**2+y**2)**0.5
        if ((x**2+y**2)**0.5 > far_distance):
                far_distance = (x**2+y**2)**0.5
        break
    if directions[i] == ";":
        distance += (x**2+y**2)**0.5
        if ((x**2+y**2)**0.5 > far_distance):
                far_distance = (x**2+y**2)**0.5
        x = 0
        y = 0
    elif directions[i] == "N":
        distance += 100
        y += 100
    elif directions[i] == "E":
        distance += 100
        x += 100
    elif directions[i] == "S":
        distance += 100
        y -= 100
    elif directions[i] == "W":
        distance += 100
        x -= 100
    i += 1
print(far_distance/1760)
print(distance/1760)
