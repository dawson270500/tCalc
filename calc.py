import math
import random
import sys

lastAnswer = 0.0
memory = 0.0

print("-- tCalc V1.2 -- Programmed by Bailey Dawson --")

def numGet(token):#get the number out of the string
	if token == "m":
		return memory
	if token =="r":
		return random.random()
	if token == "p":
		return math.pi
	if str(token).isnumeric():
		return token
	return "ERROR"

def getAnswer(inp):#Take in a string, convert it to a answer
	if "+" in inp:
			if "+" == inp[0]:
				try:
					num = numGet(inp[1:])
					if num != "ERROR": return lastAnswer + float(num)
					else: 
						print("Invalid value | Code 1.1")
						return "ERROR"
				except:
					print("Invalid value | Code 1.2")
					return "ERROR"

			else:
				vals = inp.split("+")
				return float(numGet(vals[0])) + float(numGet(vals[1]))
	elif "-" in inp:
		if "-" == inp[0]:
			try:
				num = numGet(inp[1:])
				if num != "ERROR": return lastAnswer - float(num)
				else: 
					print("Invalid value | Code 2.1")
					return "ERROR"
			except:
				print("Invalid value | Code 2.2")
				return "ERROR"

		else:
			vals = inp.split("-")
			return float(numGet(vals[0])) - float(numGet(vals[1]))
	elif "*" in inp:
		if "*" == inp[0]:
			try:
				num = numGet(inp[1:])
				if num != "ERROR": return lastAnswer * float(num)
				else:
					print("Invalid value | Code 3.1") 
					return "ERROR"
			except:
				print("Invalid value | Code 3.2")
				return "ERROR"

		else:
			vals = inp.split("*")
			return float(numGet(vals[0])) * float(numGet(vals[1]))
	elif "/" in inp:
		if "/" == inp[0]:
			try:
				num = numGet(inp[1:])
				if num != "ERROR": return lastAnswer / float(num)
				else: 
					print("Invalid value | Code 4.1")
					return "ERROR"		
			except:
				print("Invalid value | Code 4.2")
				return "ERROR"

		else:
			vals = inp.split("/")
			return float(numGet(vals[0])) / float(numGet(vals[1]))
	elif "cos(" in inp:
		vals = inp.split("(")
		if vals[1] != "":
			vals[1] = vals[1].replace(")", "")
			num = numGet(vals[1])
			if num != "ERROR": return math.cos(float(num))
	elif "tan(" in inp:
		vals = inp.split("(")
		if vals[1] != "":
			vals[1] = vals[1].replace(")", "")
			num = numGet(vals[1])
			if num != "ERROR": return math.tan(float(num))
	elif "sin(" in inp:
		vals = inp.split("(")
		if vals[1] != "":
			vals[1] = vals[1].replace(")", "")
			num = numGet(vals[1])
			if num != "ERROR": return math.sin(float(num))
	return "Invalid Input | Code 0.2"

if len(sys.argv) > 1:
	del sys.argv[0]
	for x in sys.argv:
		lastAnswer = getAnswer(x)
		print(lastAnswer)
	sys.exit()

print("Type 'exit' to stop, 'help' for help")

while True:
	inp = input(":> ").replace(" ", "")
	
	if inp == "exit":	#Stop
		break

	elif inp == "help": # Help
		print("You can add onto the last answer given, by typing '<operator><Number or value>'\nSupported operators:\n\t+\n\t-\n\t*\n\t/\n\tcos(<val>)\n\tsin(<val>)\n\ttan(<val>)\nUsing pi or memory:\n\tto use pi, type p.\n\tTo set memory, type m after it gives the answer you want in memory. To acces memory type m in a calculation")
		continue

	elif inp == "m": #Put last into memory
		memory = lastAnswer	
		continue
	
	else: #Calculation
		lastAnswer = getAnswer(inp)
		if lastAnswer != "ERROR": 
			print(lastAnswer)
			continue
		print("ERROR")
		continue
	print("Invalid Input | Code 0.1")
	print("ERROR")
			