import math

lastAnswer = 0.0
memory = 0.0

print("Type 'exit' to stop, 'help' for help")

while True:
	inp = input(":> ")

	if inp == "exit":	
		break

	num1 = ""
	numSet = False
	num2 = ""
	op = ""
	if inp == "help":
		print("You can add onto the last answer given, by typing '<operator><Number or value>'\nSupported operators:\n\t+\n\t-\n\t*\n\t/\nUsing pi or memory:\n\tto use pi, type p.\n\tTo set memory, type m after it gives the answer you want in memory. To acces memory type m in a calculation")
	elif inp != "m":
		for x in inp:
			if x == "+" or x == "-" or x == "/" or x=="*":
				op = x
				if num1 == "":
					num1 = str(lastAnswer)
					if inp[1] == "m":
						num2 = memory
					elif inp[1] =="p":
						num2 = 3.14159
					else:
						num2 = inp[1:]
					break
				else:
					numSet = True
			else:
				if numSet == False:
					if x == "p":
						num1 = 3.14159
						continue
					if x == "m":
						num1 = memory
						continue
					num1 = num1+x
				else:
					if x == "p":
						num2 = 3.14159
						continue
					if x == "m":
						num2 = memory
						continue
					num2 = num2+x
		if op == "+":
			lastAnswer = float(num1) + float(num2)
			print(lastAnswer)
		elif op == "-":
			lastAnswer = float(num1) - float(num2)
			print(lastAnswer)
		elif op == "/":
			lastAnswer = float(num1) / float(num2)
			print(lastAnswer)
		elif op == "*":
			lastAnswer = float(num1) * float(num2)
			print(lastAnswer)
		else:
			print("Invalid operator")
	else:
		memory = lastAnswer

	