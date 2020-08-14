import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
	
with open("sample2.txt", "r+") as file_object:
    # Move read cursor to the start of file.
    file_object.seek(0)
    # If file is not empty then append '\n'
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    # Append text at the end of file
    for f in files:
    	if ".jpg" in str(f):
    		print(f)
	    #file_object.write("\n")
	    #file_object.write("<img src=\""+f+"\" alt=\""+f+"\">")
	    #print("<img src=\""+f+"\" alt=\""+f+"\">")
    
