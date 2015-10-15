import re
from kivy.uix.popup import Popup

def parseFace(text):
	#creates a pattern to identify various operations within a string and use it to split the text into a list
	
	ptn=re.compile('([\-\+\d\.]+?|[\d]\.\d+)([\*,\-,\+,/])([\-\+\d\.].*)')
	if re.match(ptn,text):
					v_op_vList=re.split(ptn,text)
					
					return v_op_vList 			
					 
	else:
					return False
				
