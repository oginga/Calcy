"""
This is a simple calculator app that I created while learning to use the Kivy framework in Python
It computes the basic mathematical operations(+-*/) on both positive/negative floats/integers
Requires:Kivy 1.9.0

Copyright 2015 Oginga Steven <stevilley@gmail.com>
github:oginga

"""
import re
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
#from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import *
from parser import *
from calculations import operation

'''
This class overrides the insert_text method of the parent class to allow entry of digits,dot(.) and mathematical operators
pat:string of pattern used to match text from CalcFace
'''
class FaceInput(TextInput):
	pat='[^0-9\*\.\+\-/]'
	
	def insert_text(self,substring,from_undo=False):
			pat=self.pat
			s=re.sub(pat,'',substring)
			return super(FaceInput,self).insert_text(s,from_undo=from_undo)
			
'''
This class overrides the insert_text method of the parent class to allow entry of floats and a single dot(.)
'''			
class FloatInput(TextInput):
	pat='[^0-9\-\+]'
	
	def insert_text(self,substring,from_undo=False):
		pat=self.pat
		if '.' in self.text:
			s=re.sub(pat,'',substring)
		else:
			s='.'.join([re.sub(pat,'',s) for s in substring.split('.',1)])
		return super(FloatInput,self).insert_text(s,from_undo=from_undo)


class ThreeFace(FloatLayout):
	def __init__(self,**kwargs):
		super(ThreeFace,self).__init__(**kwargs)
		
		def calculate(instance):
			v_op_vList=[Num1_In.text,instance.text,Num2_In.text]
			print v_op_vList
			Res=operation(v_op_vList)
			Results_In.text=Res
			
		
		Num1_Lbl=Label(text="Integer 1",size_hint=(None,None),height=30,width=60,pos_hint={'x':.4,"top":.9})
		Num2_Lbl=Label(text="Integer 2",size_hint=(None,None),height=30,width=60,pos_hint={'x':.4,"top":.8})
		Results_Lbl=Label(text="Results",size_hint=(None,None),height=30,width=60,pos_hint={'x':.4,"top":.7})

		Num1_In=FloatInput(size_hint=(None,None),height=30,width=150,multiline=False,pos_hint={'x':.5,"top":.9})
		Num2_In=FloatInput(size_hint=(None,None),height=30,width=150,multiline=False,pos_hint={'x':.5,"top":.8})
		Results_In=FloatInput(size_hint=(None,None),height=30,width=150,multiline=False,pos_hint={'x':.5,"top":.7})
				
		self.add_widget(Num1_Lbl)
		self.add_widget(Num1_In)
		self.add_widget(Num2_Lbl)
		self.add_widget(Num2_In)
		self.add_widget(Results_Lbl)
		self.add_widget(Results_In)
		
		PlusBtn=Button(text='+',font_size=20,size_hint=(None,None),height=30,width=60,pos_hint={'x':.51,"y":.5})
		PlusBtn.bind(on_press=calculate)
		
		MinusBtn=Button(text='-',font_size=20,size_hint=(None,None),height=30,width=60,pos_hint={'x':.62,"y":.4})
		MinusBtn.bind(on_press=calculate)
		
		DivBtn=Button(text='/',font_size=20,size_hint=(None,None),height=30,width=60,pos_hint={'x':.4,"y":.4})
		DivBtn.bind(on_press=calculate)

		MultBtn=Button(text='*',font_size=20,size_hint=(None,None),height=30,width=60,pos_hint={'x':.51,"y":.3})
		MultBtn.bind(on_press=calculate)		
		
		self.add_widget(PlusBtn)
		self.add_widget(MinusBtn)
		self.add_widget(DivBtn)
		self.add_widget(MultBtn)

class OneFace(FloatLayout):
	def __init__(self,**kwargs):
		super(OneFace,self).__init__(**kwargs)
		
		
		def add_text(instance):
			CalcFace.insert_text(instance.text)
			
		def clearFace(instance):
			CalcFace.text=''
		def calculate(instance):
			parsed=parseFace(CalcFace.text)
			
			if parsed:
				Res=operation(parsed)
				if Res:
					CalcFace.text=Res
				else:
					popup=Popup(title='Syntax Error',content=Label(text=''.join(s for s in parsed)),title_color=[1,0,0,1],size_hint=(None,None),size=(200,150))
					popup.open()
					
			else:
				popup=Popup(title='Syntax Error',content=Label(text='Empty/Invalid Syntax'),title_color=[1,0,0,1],size_hint=(None,None),size=(200,150))
				popup.open()
			
		
		CalcFace=FaceInput(multiline=False,pos=(300,500),size_hint=(None,None),height=30,width=240)
		
		
		Clear=Button(text='CLEAR',font_size=16,size_hint=(None,None),height=30,width=60,pos=(480.5,440))
		Clear.bind(on_press=clearFace)
		
		Div=Button(text='/',font_size=20,size_hint=(None,None),height=30,width=60,pos=(480.5,410))
		Div.bind(on_press=add_text)
		
		Mul=Button(text='*',font_size=20,size_hint=(None,None),height=30,width=60,pos=(480.5,380))
		Mul.bind(on_press=add_text)
		
		Sub=Button(text='-',font_size=20,size_hint=(None,None),height=30,width=60,pos=(480.5,350))
		Sub.bind(on_press=add_text)
		
		Plus=Button(text='+',font_size=20,size_hint=(None,None),height=30,width=60,pos=(480.5,320))
		Plus.bind(on_press=add_text)
		
		_7=Button(text='7',font_size=20,size_hint=(None,None),height=30,width=60,pos=(300,410))
		_7.bind(on_press=add_text)
		
		_8=Button(text='8',font_size=20,size_hint=(None,None),height=30,width=60,pos=(360.5,410))
		_8.bind(on_press=add_text)
		
		_9=Button(text='9',font_size=20,size_hint=(None,None),height=30,width=60,pos=(420.5,410))
		_9.bind(on_press=add_text)
		
		_4=Button(text='4',font_size=20,size_hint=(None,None),height=30,width=60,pos=(300,380))
		_4.bind(on_press=add_text)
		
		_5=Button(text='5',font_size=20,size_hint=(None,None),height=30,width=60,pos=(360.5,380))
		_5.bind(on_press=add_text)
		
		_6=Button(text='6',font_size=20,size_hint=(None,None),height=30,width=60,pos=(420.5,380))
		_6.bind(on_press=add_text)
		
		_1=Button(text='1',font_size=20,size_hint=(None,None),height=30,width=60,pos=(300,350))
		_1.bind(on_press=add_text)
		
		_2=Button(text='2',font_size=20,size_hint=(None,None),height=30,width=60,pos=(360.5,350))
		_2.bind(on_press=add_text)
		
		_3=Button(text='3',font_size=20,size_hint=(None,None),height=30,width=60,pos=(420.5,350))
		_3.bind(on_press=add_text)
		
		_dot=Button(text='.',font_size=20,size_hint=(None,None),height=30,width=60,pos=(300,320))
		_dot.bind(on_press=add_text)
		
		_0=Button(text='0',font_size=20,size_hint=(None,None),height=30,width=60,pos=(360.5,320))
		_0.bind(on_press=add_text)
		
		_eq=Button(text='=',font_size=20,size_hint=(None,None),height=30,width=60,pos=(420.5,320))
		_eq.bind(on_press=calculate)
			
		self.add_widget(CalcFace)
		self.add_widget(Clear)
		self.add_widget(_7)
		self.add_widget(_4)
		self.add_widget(_1)		
		self.add_widget(_dot)
		self.add_widget(_8)
		self.add_widget(_5)
		self.add_widget(_2)
		self.add_widget(_0)
		self.add_widget(_9)
		self.add_widget(_6)
		self.add_widget(_3)
		self.add_widget(_eq)
		self.add_widget(Div)
		self.add_widget(Mul)
		self.add_widget(Sub)
		self.add_widget(Plus)	


class MainWidget(TabbedPanel):
	def __init__(self,**Kwargs):
		super(MainWidget,self).__init__(**Kwargs)
		
		tp=TabbedPanel()
		oneTh=TabbedPanelHeader(text='ONE FACE')
		threeTh=TabbedPanelHeader(text='THREE FACE')
		self.add_widget(oneTh)
		self.add_widget(threeTh)
		threeTh.content=ThreeFace()
		oneTh.content=OneFace()
		
		self.do_default_tab=False
		
class CalcApp(App):
	def build(self):
		
		return MainWidget();
		
		
if __name__ == '__main__':
	CalcApp().run()
