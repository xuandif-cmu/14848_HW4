import sys

for line in sys.stdin:
    line = line.strip()
    temperature = int(line[87:92])
    quality = int(line[92])
    date = line[15:23]
    # get valid data
    if(quality == 0 or quality == 1 or quality == 4 or quality == 5 or quality == 9):
	    if ((temperature != 9999) and (temperature != -9999)):
	        print('%s\t%d' % (date, temperature))