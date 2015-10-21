import numpy as np

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

xmin = ymin = 1000000
lines = []

for line in open('scratch.txt', 'r'):
    line = line.split(" ")
    lines.append(line)
    for i in xrange(0, len(line), 2):
        if len(line[i:i+2]) == 2:
            [x,y] = line[i:i+2]
            if (is_number(x) and is_number(y)):
                x = float(x)
                y = float(y)
                xmin = x if x < xmin else xmin
                ymin = y if y < ymin else ymin

print "%s %s translate" % (str(xmin), str(ymin))

for i, line in enumerate(lines):
    command = ""
    for j in xrange(0, len(line), 2):
        if len(line[j:j+2]) == 2:
            [x,y] = line[j:j+2]
            if (is_number(x) and is_number(y)):
                x = str(float(x) - xmin)
                y = str(float(y) - ymin)
            command += "%s %s " % (x, y)
        
    command += lines[i][-1].strip()
    print command
    
