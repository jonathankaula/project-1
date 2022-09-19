from sys import stdin, stdout, stderr 
import json
import re
import numpy as np

class Token():

	def __init__(self, token, value):
		self.token=token
		self.value=value

class Iterator:

	def __init__(self, ls):
		self.ls=ls
		self.len=len(ls)
		self.current_index=0

	def next_token(self):

		if self.current_index==self.len:
			return None

		else:
			self.current_index+=1
			return self.ls[self.current_index-1]

	def peek(self):
		if self.current_index==self.len:
			return None

		else:
			return self.ls[self.current_index]


def is_numeric(char):
	try:
		pass

	except ValueError:
		pass

def scanner(input):
	Number = '[0-9]+'
	Keyword = 'INT'
	Open_braces = '['
	Close_braces=']'
	OP = '='
	O_br='{'
	C_br='}'
	cont='...'

	ls=[]

	iterator=Iterator(input)

	while input:
		char= iterator.peek()

		if char is None:
			return ls

		else:
			char=iterator.next_token()

			if char == Open_braces:
				ls_value = Token('o_braces',char)
				ls.append(ls_value)

			elif char == Close_braces:

				ls_value = Token('c_braces',char)
				ls.append(ls_value)

			elif char == OP:

				ls_value = Token('OP',char)
				ls.append(ls_value)	

			elif char.isdigit():
				digit=True
				integer=''

				while digit:
					integer+=char
					char=iterator.peek()

					if char==None:
						break

					else:
						if not char.isdigit():
							digit=False

						iterator.next_token()
		

				ls_value = Token('integer',integer)
				ls.append(ls_value)	
			elif char==' ':
				pass

			elif char == O_br:
				ls_value = Token('O_br',char)
				ls.append(ls_value)

			elif char == C_br:
				ls_value = Token('C_br',char)
				ls.append(ls_value)

			elif char == '.':
				ls_value = Token('cont','...')
				ls.append(ls_value)
				#iterator.next_token()
				iterator.next_token()
			else:
				print(f"Could not recognize: {char}")




def standard_input():

	for line in stdin: 

		if line.strip() == 'q':
			break

		else:
			ls=scanner(line.strip())
			ls.append(Token('$$',None)) # denotes end of input

			# for obj in ls:
			# 	print(f"{obj.token}:{obj.value}")
			start(ls)

def simple_init_OP(operand,operand_2,operand_3):
	if operand_2>operand:
		print('Cannot insert the element')
	else:
		arr=np.zeros(operand)
		n_arr=np.insert(arr, operand_2, operand_3)
		return n_arr

def Range_init_OP(operand,operand_2,operand_3,operand_4):
	arr=[]

	for i in range(operand):
		if i >= operand_2 and i<operand_3:
			arr=np.insert(arr,i,operand_4)
		else:
			arr=np.insert(arr,i,0)


	return arr


def init(iterator, prev):
	tk=iterator.peek()

	if tk.token == 'integer':
		operand = tk.value
		iterator.next_token()
		tk=iterator.peek()


		if tk.token=='c_braces':
			iterator.next_token()
			tk=iterator.peek()
			if tk.token=='OP':
				iterator.next_token()
				tk=iterator.peek()
				if tk.token=='O_br':
					iterator.next_token()
					tk=iterator.peek()
					if tk.token=='o_braces':
						iterator.next_token()
						tk=iterator.peek()
						if tk.token=='integer':
							operand_2=tk.value
							iterator.next_token()
							tk=iterator.peek()
							if tk.token=='c_braces':
								iterator.next_token()
								tk=iterator.peek()
								if tk.token=='OP':
									iterator.next_token()
									tk=iterator.peek()
									if tk.token=='integer':
										operand_3=tk.value
										iterator.next_token()
										tk=iterator.peek()
										if tk.token=='C_br':
											value = simple_init_OP(int(operand),int(operand_2), int(operand_3))
											

							elif tk.token=='cont':
								iterator.next_token()
								tk=iterator.peek()								
								if tk.token == 'integer':
									operand_3 = tk.value
									iterator.next_token()
									tk=iterator.peek()							

									if tk.token=='c_braces':
										iterator.next_token()
										tk=iterator.peek()
										if tk.token=='OP':
											iterator.next_token()
											tk=iterator.peek()
											if tk.token=='integer':
												operand_4=tk.value
												iterator.next_token()
												tk=iterator.peek()
												if tk.token=='C_br':

													value = Range_init_OP(int(operand),int(operand_2), int(operand_3),int(operand_4))
													json_output(value)
									else:
										print('c_braces not found')
					

		else:
			print('expecting ]} after integer')
			return None



def start(ls):
	iterator=Iterator(ls)
	current_iter = iterator.peek()

	if current_iter.token == 'o_braces':
		iterator.next_token()
		value = init(iterator,current_iter)

	else:
		print('expecting an opening braces')
		return None


def json_output(value):
	y = json.dumps(str(value))
	print(y)

standard_input()

