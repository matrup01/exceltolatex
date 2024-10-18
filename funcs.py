# -*- coding: utf-8 -*-
"""
@author: mrupp

functions for the exceltolatex-script
"""


def column_wrapper(data,wrapper,columno,nofirstline=False):
    """
    

    Parameters
    ----------
    data : list
        list creatted from an excel-file
    wrapper : str
        str that should be wrapped around each element of the column, where the location of the element should be marked with "&". e.g. add_str="textbf{&}"
    columno : int
        specifies which column should be changed
    nofirstline : bool
        if set to true it leaves the first element unchanged

    Returns
    -------
    updated data-list with a wrapped column

    """
    
    nofirstline = bool(nofirstline)
    columno = int(columno)
    #if type(nofirstline) != bool:
     #   nofirstline = True
    
    columno -= 1
    #adder = add_str.encode('unicode_escape').decode()
    adder = wrapper.split("&")
    
    for line in range(len(data)):
        for column in range(len(data[line][:-1])):
            
            if column == columno and not (nofirstline == True and line == 0):
                
                data[line][column] = adder[0] + data[line][column] + adder[1]
                
    return data


def row_wrapper(data,wrapper,rowno,nofirstline=False):
    """
    

    Parameters
    ----------
    data : list
        list creatted from an excel-file
    wrapper : str
        str that should be wrapped around each element of the row, where the location of the element should be marked with "&". e.g. add_str="textbf{&}"
    columno : int
        specifies which row should be changed
    nofirstline : bool
        if set to true it leaves the first element unchanged

    Returns
    -------
    updated data-list with a wrapped row

    """
    
    rowno = int(rowno)
    #if type(nofirstline) != bool:
     #   nofirstline = True
    nofirstline = bool(nofirstline)
    
    rowno -= 1
    #adder = add_str.encode('unicode_escape').decode()
    adder = wrapper.split("&")
    
    for line in range(len(data)):
        
        appender = data[line][-1]
        
        if line == rowno and nofirstline:
            
            data[line] = [adder[0]+data[line][column]+adder[1] if column != 0 else data[line][column] for column in range(len(data[line][:-1]))]
            data[line].append(appender)
            
        elif line == rowno and not nofirstline:
            
            data[line] = [adder[0]+data[line][column]+adder[1] for column in range(len(data[line][:-1]))]
            data[line].append(appender)
            
    return data


def hline(data,loc):
    """
    

    Parameters
    ----------
    data : list
        list created from excel file
    loc : int
        rownumber after which the hline should be drawn

    Returns
    -------
    updated data list with hline

    """
    
    loc = int(loc)
    loc -= 1
    
    data[loc][-1] += r" \hline"
    
    return data


def hlines(data):
    """
    

    Parameters
    ----------
    data : list
        list created from excel file

    Returns
    -------
    updated data list with all hlines

    """
    
    for i in range(len(data)):
        data[i][-1] += r"\hline"
        
    return data


def replace(data,newstring,row,col):
    """
    

    Parameters
    ----------
    data : list
        list created from excel file
    newstring : str
        string that should replace the old one
    row : int
        row-locator to decide which element should be replaced
    col : int
        column-locator to decide which element should be replaced

        
    Returns
    -------
    updated data list with replaced element

    """
    
    row = int(row)
    col = int(col)
    
    row -= 1
    col -= 1
    
    data[row][col] = newstring
    
    return data


def wrap(data,wrapper,row,col):
    """
    

    Parameters
    ----------
    data : list
        list created from excel file
    wrapper : str
        str that should be wrapped around the element, using "&" as a delimiter
    row : int
        row-locator to decide which element should get wrapped
    col : int
        col-locator to decide which element should get wrapped


    Returns
    -------
    updated data list with wrapped element

    """
    
    row = int(row)
    col = int(col)
    
    row -= 1
    col -= 1
    
    adder = wrapper.split("&")
    
    data[row][col] = adder[0] + data[row][col] + adder[1]
    
    return data