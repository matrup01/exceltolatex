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
excelimport = """loremmm	ipsum	dolor
sit	amet	consectetur
adipisci	velet	1

"""

#insert your own commands here
commands = [["r","Lorem",1,1],
            ["w","\SI{&}{\micro\meter}",3,3],
            ["hl",1],
            ["wr",r"\textbf{&}",1]]

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
data = [list(element.split("\t")) for element in excelimport]

#dict for commandnames

commanddict = {"wc":"column_wrapper",
               "wrapcol":"column_wrapper",
               "wr":"row_wrapper",
               "wraprow":"row_wrapper",
               "hl":"hline",
               "hline":"hline",
               "hls":"hlines",
               "hlines":"hlines",
               "r":"replace",
               "replace":"replace",
               "w":"wrap",
               "wrap":"wrap"}

for element in data:
    element.append(r" \\")

#execute commands

for element in commands:
    func = "funcs." + commanddict[element[0]]
    options = ",".join(['r"'+str(s)+'"' for s in element[1:]])
    func2 = func+"(data,"+options+")"
    
    data = eval(func2)
    
    
length = len(data)
width = len(data[0])

if caption == "":
    caption = "caption"
    
if label == "":
    label = "tab:label"
    
for line in data:  
    line[-2] += line[-1]
    
# print to file

f = open("output.txt","w")

print(r"\begin{table}[!ht]",file=f)

print("\t" + r"\centering",file=f)

print("\t"+r"\caption{"+caption+"}",file=f)

if vspace != "":
    print("\t"+r"\vspace{"+vspace+"}",file=f)
    
l_tabular = r"\begin{tabular}{|" if addleftborder else r"\begin{tabular}{"
r_tabular = "|}" if addrightborder else "}"
if len(celllocation) == 1:
    print("\t"+l_tabular+"".join(celllocation for i in range(width-1))+r_tabular,file=f)
else:
    print("\t"+r"\begin{tabular}{"+celllocation+"}",file=f)
    
if tophline:
    print("\t\t"+r"\hline",file=f)
    
for line in data:
    op = "\t\t" + " & ".join(line[i] for i in range(len(line)-1))
    print(op,file=f)
    
print("\t"+r"\end{tabular}",file=f)

print("\t"+r"\label{"+label+"}",file=f)

print(r"\end{table}",file=f)
    

f.close()