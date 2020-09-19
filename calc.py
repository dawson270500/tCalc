lastAnswer = 0.0
memory = 0.0

print("Type 'exit' to stop, 'help' for help")

def numGet(token):
	if token == "m":
		return memory
	elif token == "p":
		return 3.14159
	else:
		return token

while True:
	inp = input(":> ").replace(" ", "")
	
	if inp == "exit":	
		break

	elif inp == "help":
		print("You can add onto the last answer given, by typing '<operator><Number or value>'\nSupported operators:\n\t+\n\t-\n\t*\n\t/\nUsing pi or memory:\n\tto use pi, type p.\n\tTo set memory, type m after it gives the answer you want in memory. To acces memory type m in a calculation")
		continue

	elif inp == "m":
		memory = lastAnswer	
		continue
	
	else: 
		if "+" in inp:
			if "+" == inp[0]:
				try:
					lastAnswer = lastAnswer + float(numGet(inp[1:]))
				except:
					print("Invalid value")
					continue

			else:
				vals = inp.split("+")
				lastAnswer = float(numGet(vals[0])) + float(numGet(vals[1]))

			print(lastAnswer)
			continue
		elif "-" in inp:
			if "-" == inp[0]:
				try:
					lastAnswer = lastAnswer - float(numGet(inp[1:]))
				except:
					print("Invalid value")
					continue

			else:
				vals = inp.split("-")
				lastAnswer = float(numGet(vals[0])) - float(numGet(vals[1]))

			print(lastAnswer)	
			continue
		elif "*" in inp:
			if "*" == inp[0]:
				try:
					lastAnswer = lastAnswer * float(numGet(inp[1:]))
				except:
					print("Invalid value")
					continue

			else:
				vals = inp.split("*")
				lastAnswer = float(numGet(vals[0])) * float(numGet(vals[1]))

			print(lastAnswer)
			continue
		elif "/" in inp:
			if "/" == inp[0]:
				try:
					lastAnswer = lastAnswer / float(numGet(inp[1:]))
				except:
					print("Invalid value")
					continue

			else:
				vals = inp.split("/")
				lastAnswer = float(numGet(vals[0])) / float(numGet(vals[1]))

			print(lastAnswer)
			continue
		else:
			print("Invalid operator")
			continue