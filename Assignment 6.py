import re, string
in_file = open("Mort99us.dat")
count = 0
whitecount = 0
blackcount = 0
whitearter = 0
blackarter = 0
for line in in_file:
   count = count + 1
   codesection = line[161:301]
   race = line[59:61]
   if race == "01":
      whitecount = whitecount + 1
   if race == "02":
      blackcount = blackcount + 1
   codematch = re.search(r'I25', codesection) #arteriosclerosis of heart (artery clogged or stiffened)
   
   if codematch:
      if race == "01":
         whitearter = whitearter + 1
      if race == "02":
         blackarter = blackarter + 1
in_file.close()
whiteartfrac = str(100 * (float(whitearter) / whitecount))
blackartfrac = str(100 * (float(blackarter) / blackcount))
print("Total records in file is " + str(count))
print("Total African-Americans in file is " + str(blackcount))
print("Total Whites in file is " + str(whitecount))
print("Total African-Americans with atherosclerosis is " + str(blackarter))
print("Total Whites with atherosclerosis is " + str(whitearter))
print("Percent African-Americans with atherosclerosis is " + blackartfrac[0:4])
print("Percent Whites with atherosclerosis is " + whiteartfrac[0:4])
exit