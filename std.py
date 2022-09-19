# from sys import stdin, stdout, stderr 
# import json
# from nltk.tokenize import word_tokenize
# import re


# def standard_input():

# 	for line in stdin: 

# 		if line.strip() == 'q':
# 			break

# 		else:
# 			token_dict=scanner(line.strip())

# def scanner(string):

# 	# Number = re.findall('[0-9]+',string)
# 	# Keyword = 'INT'
#     #Identifier = '\b[a-zA-Z]+\b'
# 	# Open_braces = '['
# 	# Close_braces=']'

# 	# R = Keyword | Identifier | Number | Open_braces | Close_braces

# 	keywords=['INT']
# 	symbols=['...', '[', ']',  '{', '}', ',']
# 	operators=['=']
# 	key_words=keywords+symbols+operators
# 	tokens={}
# 	w_space=' '
# 	lexeme=''
# 	lexemes=[]

# 	for index,char in enumerate(string):
# 		if char !=w_space:
# 			lexeme+=char
# 		if (index+1 < len(string)):

# 			if string[index+1]==w_space or string[index+1] in key_words or lexeme in key_words:
# 				if lexeme !='':
# 					lexemes.append(lexeme)
# 				lexeme=''
# 	lexemes.append(lexeme)
	

# 	for word in lexemes:
# 		if word in keywords:
# 			tokens[word]='keyword'

# 		elif word in symbols:
# 			tokens[word]='symbol'

# 		else:
# 			tokens[word]='identifier'
			
# 	grammar(tokens)







# def standard_output(input_txt):
# 	stdout.write(input_txt)

# def standard_error():
# 	return True

# def grammar(token_dict):

# 	print(token_dict)


# def json_output():
# 	x =  '{ "name":"John", "age":30, "city":"New York"}'

# 	y = json.dumps(x)

# 	print(y)

# standard_input()



string = '[44]' 

for char in string:
	if not char.isdigit():
		print('is number')
	else:
		print('is not number')
