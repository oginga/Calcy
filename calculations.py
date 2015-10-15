

def operation(v_op_vList):
	Res=None
	
	for i in v_op_vList:
						if i=='':
							v_op_vList.remove('') in v_op_vList
						print v_op_vList
	
	try:		
		
						if v_op_vList[1] == '+':
							#Res=lambda:v_op_vList[0] + v_op_vList[2]
							Res=addition(v_op_vList[0],v_op_vList[2])			
						if v_op_vList[1] == '-':
							Res=subtraction(v_op_vList[0],v_op_vList[2])
						if v_op_vList[1] == '/':
							Res=division(v_op_vList[0],v_op_vList[2])
						if v_op_vList[1] == '*':
							Res=product(v_op_vList[0],v_op_vList[2])
						return Res
	except:return False 
						
	

def addition(Num1,Num2):

			return str( float(Num1) + float(Num2))
			
def subtraction(Num1,Num2):
			
			return str( float(Num1) - float(Num2))
		
def product(Num1,Num2):
			
			return str( float(Num1) * float(Num2))
			
def division(Num1,Num2):
			
			return str( float(Num1) / float(Num2))
