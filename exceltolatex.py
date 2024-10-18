# -*- coding: utf-8 -*-
"""
@author: mrupp

takes an excel-table and changes it to a latex-readable one

Note:
    commands are taken in the form of a nested list every sublist should have the command type as the first entry (for full docu see readme.md)
    rows and columns are indexed starting with 1
"""

import csv
import funcs

#Variables
###############################################################################

#copy an area from excel and paste it into this docstring
excelimport = """Sieb [mu]	Siebe Tara [g]	AW [g]	AW berichtigt
0	427.4	434.74	7.34
40	262	274.21	12.21
63	229.37	251.56	22.19
100	268.46	300.67	32.21
140	252.95	340.57	87.62
200	221.36	300.53	79.17
315	258.75	265.17	6.42
400	233.25	233.83	0.58
500	244.29	244.45	0.16
630	254.77	254.86	0.09
800	290.88	291.05	0.17"""

#insert your own commands here
commands = [["cw","\SI{&}{\micro\meter}",1,True],
            ["cw","\SI{&}{\gram}",2,True],
            ["cw","\SI{&}{\gram}",3,True],
            ["cw","\SI{&}{\gram}",4,True],
            ["rw","\textbf{&}",1],
            ["hl",1],
            ["hl",12]]

#misc options
caption  = ""
label = ""
celllocation = "c" #if only one character is given, its used for every column
addleftborder = True #draws a vline on the left side of the table
addrightborder = True #draws a vline on the right side of the table
tophline = True 
vspace = "0.3cm" #sets vspace between caption and table (set empty if you dont want any vspace)
###############################################################################


#import excel-data

excelimport = excelimport.splitlines()
data = list(csv.reader(excelimport,delimiter="\t"))

#dict for commandnames

commanddict = {"cw":"funcs.column_wrapper",
               "colwrap":"funcs.column_wrapper",
               "rw":"funcs.row_wrapper",
               "rowwrap":"funcs.row_wrapper",
               "hl":"funcs.hline",
               "hline":"funcs.hline"}

#execute commands

for element in commands:
    func = commanddict[element[0]]
    options = ",".join(['"'+str(s).encode('unicode_escape').decode()+'"' for s in element[1:]])
    func2 = func+"(data,"+options+")"
    
    data = eval(func2)
    
for element in data:
    element[-1] += r"\\"
    
length = len(data)
width = len(data[0])

if caption == "":
    caption = "caption"
    
if label == "":
    label = "tab:label"
    
# print to file

f = open("output.txt","w")

print(r"\begin(table)[!ht]",file=f)

print("\t" + r"\centering",file=f)

print("\t"+r"\caption{"+caption+"}",file=f)

if vspace != "":
    print("\t"+r"\vspace{"+vspace+"}",file=f)
    
l_tabular = r"\begin{tabular}{|" if addleftborder else r"\begin{tabular}{"
r_tabular = "|}" if addrightborder else "}"
if len(celllocation) == 1:
    print("\t"+l_tabular+"".join(celllocation for i in range(width))+r_tabular,file=f)
else:
    print("\t"+r"\begin{tabular}{"+celllocation+"}",file=f)
    
if tophline:
    print("\t\t"+r"\hline",file=f)
    
for line in data:
    op = "\t\t" + " & ".join(element for element in line)
    print(op,file=f)
    
print("\t"+r"\end{tabular}",file=f)

print("\t"+r"\label{"+label+"}",file=f)

print(r"\end{table}",file=f)
    

f.close()