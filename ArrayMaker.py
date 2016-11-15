with open('DataSet.txt', 'r') as f:
    read_data = f.read()
    temp = str(read_data)
#Search through text file and make array of str, each str = chars between each [] set. 
#Search through each indicie of array 1 ^^^ and put numeric values and sybmbol into array point
z = len(temp)-1
for x in range(0, z):
    temp1 = temp[x]
    y = str(x)
    if (temp1 == "["):
        print ("Square Bracket Left" + y)
        
        if (temp == "{"):
            print ("Bracket Left" + y)
     
            if (temp == "]"):
                print ("Square Bracket Right" + y)
        
                if (temp == "}"):
                    print ("Bracket Right" + y)