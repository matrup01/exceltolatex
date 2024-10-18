1. cw / colwrap
    wrappes a the given string (add_str) around every element in the given column (columno) using "&" as a delimiter. If nofirstline is given the first row wont be wrapped around.
    
    Syntax:
        [cw,add_str,columno]
        [cw,add_str,columno,nofirstline]
        [colwrap,add_str,columno]
        [colwrap,add_str,columno,nofirstline]
    Vars:
        add_str : str
        column : int
        nofirstline : bool
        
2. rw / rowwrap
    wrappes a the given string (add_str) around every element in the given row (rownno) using "&" as a delimite. If nofirstline is given the first column wont be wrapped around.
    
    Syntax:
        [rw,add_str,rowno]
        [rw,add_str,rowno,nofirstline]
        [rowwrap,add_str,rowno]
        [rowwrap,add_str,rowno,nofirstline]
    Vars:
        add_str : str
        column : int
        nofirstline : bool
        
3. hl / hline
    prints an hline after the given row 
    
    Syntax:
        [hl,row]
        [hline,row]
    Vars:
        row : int