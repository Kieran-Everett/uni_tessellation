import sys
import codecs

if len(sys.argv) > 1:
    f = open(str(sys.argv[1]), "r")
    lines = f.read()
    f.close()
    
    name = sys.argv[1].split(".")[0]
    n = open(name + ".csv", "w")
    output = ",Line,\n1,"
    count = 1
    for char in lines:
        if (hex(ord(char))) != "0xa":
            output += (char)
        else:
            count += 1
            output += (",\n" + str(count) + ",")
    n.write(output + ",")
    n.close()
    """
    for index in range(len(lines)):
        while hex(ord(char)) not "0xa":
            """