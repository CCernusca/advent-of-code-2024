
program = "2,4,1,1,7,5,4,4,1,4,0,3,5,5,3,0"

A = 46337277
B = 0
C = 0

def parse_program(raw_program):
	raw_program = raw_program.split(',')
	instructions = []
	i = 0
	while i < len(raw_program):
		opcode = raw_program[i]
		operator = raw_program[i+1]
		if opcode == '0':
			instructions.append(('adv', int(operator)))
		elif opcode == '1':
			instructions.append(('bxl', int(operator)))
		elif opcode == '2':
			instructions.append(('bst', int(operator)))
		elif opcode == '3':
			instructions.append(('jnz', int(operator)))
		elif opcode == '4':
			instructions.append(('bxc', int(operator)))
		elif opcode == '5':
			instructions.append(('out', int(operator)))
		elif opcode == '6':
			instructions.append(('bdv', int(operator)))
		elif opcode == '7':
			instructions.append(('cdv', int(operator)))
		i += 2
	return instructions

def combo_operator(operator):
	if 0 <= operator <= 3:
		return operator
	elif operator == 4:
		global A
		return A
	elif operator == 5:
		global B
		return B
	elif operator == 6:
		global C
		return C
	else:
		raise ValueError('Invalid operator: ' + operator)

def execute_instruction(instruction, operator, instr_ptr, output):
	global A, B, C
	if instruction == 'adv':
		A = A // (2 ** combo_operator(operator))
	elif instruction == 'bxl':
		B = B ^ operator
	elif instruction == 'bst':
		B = B % 8
	elif instruction == 'jnz':
		if A != 0:
			instr_ptr = operator
			return instr_ptr, output
	elif instruction == 'bxc':
		B = B ^ C
	elif instruction == 'out':
		output.append(combo_operator(operator) % 8)
	elif instruction == 'bdv':
		B = A // (2 ** combo_operator(operator))
	elif instruction == 'cdv':
		C = A // (2 ** combo_operator(operator))
	else:
		raise ValueError('Invalid instruction: ' + instruction)
	instr_ptr += 1
	return instr_ptr, output

def run(instructions):
	instruction_pointer = 0
	output = []
	while True:
		try:
			instruction_pointer, output = execute_instruction(*instructions[instruction_pointer], instruction_pointer, output)
		except IndexError:
			break
	print(','.join([str(o) for o in output]))

instructions = parse_program(program)
print(instructions)

run(instructions)

print(A, B, C)
