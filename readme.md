* wc / wrapcol

	wrappes a the given string (wrapper) around every element in the given column (columno) using "&" as a delimiter. If nofirstline is given the first row wont be wrapped around.
    
	Syntax:
	
		[wc,wrapper,columno]
		[wc,wrapper,columno,nofirstline]
		[wrapcol,wrapper,columno]
		[wrapcol,wrapper,columno,nofirstline]
	Vars:
	
		wrapper : str
		column : int
		nofirstline : bool
        
* wr / wraprow

	wrappes a the given string (wrapper) around every element in the given row (rownno) using "&" as a delimite. If nofirstline is given the first column wont be wrapped around.
    
	Syntax:
	
		[wr,wrapper,rowno]
		[wr,wrapper,rowno,nofirstline]
		[wraprow,wrapper,rowno]
		[wraprow,wrapper,rowno,nofirstline]
	Vars:
	
		wrapper : str
		column : int
		nofirstline : bool
		
* w / wrap

	wrappes a given string (wrapper) around an element specified by row and column
	
	Syntax:
	
		[w,wrapper,row,col]
		[wrap,wrapper,row,col]
	Vars:
	
		wrapper : str
		row : int
		col : int
        
* hl / hline

	prints an hline after the given row 
    
	Syntax:
	
		[hl,row]
		[hline,row]
	Vars:
	
		row : int
		
* hls / hlines

	prints hlines after every row
	
	Syntax:
	
		[hls]
		[hlines]
		
* r / replace

	replaces an element specified by row and column with a given string (newstring)
	
	Syntax:
	
		[r,newstring,row,col]
		[replace,newstring,row,col]
	Vars:
	
		newstring : str
		row : int
		col : int