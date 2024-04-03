'''
❓ PROMPT
You are given four arrays representing two lists of operands, one list of operators, and a list of results. For any index, i, your task is to check to see if:

operands1[i] operators[i] operands2[i] = results[i]

For input arrays arrays like:

operands1 = [1, 2]
operators = ['+', '-']
operands2 = [2, 3]
results = [3, 0]

then the result of this function should be [true, false] since 1 + 2 = 3 and 2 - 3 ≠ 0.

The numbers will be integers, and the signs can be "+", "-", "*", "/". Round to the nearest whole number for division.

Example(s)
Given the following:

operands1 = [1, 2]
operators = ['+', '-']
operands2 = [2, 3]
results = [3, 0]

At index 0, we have 1 + 2 = 3. This evaluation is True
At index 1, we have 2 - 3 = 0. This evaluation is False

We should return [True, False] as there are two operands in the input list.

Another Example:
operands1_1 = [1, 5, 2]
operators_1 = ['+', '-', '*']
operands2_1 = [2, 3, 4]
results_1 = [3, 2, 8]

At index 0, we have 1 + 2 = 3. This evaluation is True
At index 1, we have 5 - 3 = 2. This evaluation is True
At index 2 we have 2 * 4 = 8. This evaluation is True

We should return [True, True, True]
'''

operands1 = [1, 2]
operators = ['+', '-']
operands2 = [2, 3]
results = [3, 0]

def interpret(op1, op2, operator):
    match operator:
        case '+':
            return op1 + op2
        case '-':
            return op1 - op2
        case '*':
            return op1 * op2


def calculate(op1, ops, op2, results):
    result = []
    for i in range(len(op1)):
       test_answer = results[i]
       result.append(interpret(op1[i], op2[i], ops[i]) == test_answer)
    return result

# print(calculate(operands1, operators, operands2, results))




operands1 = [1, 5, 2]
operators = ['+', '-', '*']
operands2 = [2, 3, 4]
results = [3, 2, 8]
print(calculate(operands1, operators, operands2, results))