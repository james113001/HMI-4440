import re, string
icd_file = open("icd10cm_codes_2017.txt", "r")
icd_string = icd_file.read()
line_array = re.split(r'\n(?= *[A-Z][0-9\.]{1,5})', icd_string)
dictionary = {}
counter = {}
codearray = []
results_array = []
for thing in line_array:
    thing_match = re.search(r'^ *([A-Z][0-9\.]{1,5}) ?(.+)$', thing)
    if thing_match:
       code = thing_match.group(1)
       term = thing_match.group(2)
       term = re.sub(r'[^a-zA-Z ]',"", term)
       term = term.rstrip()
       code = re.sub(r'\.',"", code)
       dictionary[code] = term
mort_txt = open("mort99us.dat", "r")
for line in mort_txt:
   codesection = line[161:302]
   codesection = re.sub(r' *$', "", codesection)
   codearray = re.split(r' +', codesection)
   for code in codearray:
      code_match = re.search(r'([A-Z][0-9]+)', code)
      if code_match:
         code = code_match.group(1)
      if dictionary.get(code) !=None:
         if counter.get(code) !=None:
            counter[code] = int(counter[code]) + 1
         else:
            counter[code] = 1
mort_txt.close()
out_mort = open("cdc99all.out", "w")
for key,value in counter.items():
   value = str(value)
   value = "000000" + value
   value = value[-6:]
   results_array.append(value + " " + key + " " + dictionary[key])
results_array.sort()
results_array.reverse()
out_mort.write('\n'.join(results_array))
out_mort.close()
exit;