file = open("input.txt", "r")

lines = file.readlines()

#part 1
def result_rec(result, equation_parts, curr_operator, operators):
	if curr_operator == len(operators):
		res = equation_parts[0]
		for i in range(1, len(equation_parts)):
			if operators[i-1] == 1:
				res *= equation_parts[i]
			else:
				res += equation_parts[i]
		#print(result, equation_parts, res)
		return res == result

	operators_alternative = operators.copy()
	operators_alternative[curr_operator] = 1
	return result_rec(result, equation_parts, curr_operator+1, operators) or result_rec(result, equation_parts, curr_operator+1, operators_alternative)

total = 0
wrong_lines = []

for line in lines:
	result, equation = line.split(": ")
	result = int(result)
	equation_parts = list(map(int, equation.split()))
	operators = [0 for i in range(len(equation_parts)-1)]
	is_valid = result_rec(result, equation_parts, 0, operators)
	#print(is_valid)
	if is_valid:
		total += result
	else:
		wrong_lines.append(line)
print(total)


#part 2
def result_rec2(result, equation_parts, curr_operator, operators):
	if curr_operator == len(operators):
		res = equation_parts[0]
		for i in range(1, len(equation_parts)):
			if operators[i-1] == 1:
				res *= equation_parts[i]
			elif operators[i-1] == 2:
				res = int(str(res) + str(equation_parts[i]))
			else:
				res += equation_parts[i]
		
		#print(result, equation_parts, res)
		return res == result

	operators_alternative = operators.copy()
	operators_alternative[curr_operator] = 1
	operators_alternative2 = operators.copy()
	operators_alternative2[curr_operator] = 2
	return result_rec2(result, equation_parts, curr_operator+1, operators) or result_rec2(result, equation_parts, curr_operator+1, operators_alternative) or result_rec2(result, equation_parts, curr_operator+1, operators_alternative2)

#print(len(wrong_lines))
total2 = 0
for k, line in enumerate(wrong_lines):
	#print(k)
	result, equation = line.split(": ")
	result = int(result)
	equation_parts = list(map(int, equation.split()))
	operators = [0 for i in range(len(equation_parts)-1)]
	is_valid = result_rec2(result, equation_parts, 0, operators)
	if is_valid:
		total2 += result
#print(total2)
print(total + total2)