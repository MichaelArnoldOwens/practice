'''
❓ PROMPT
Write a function to simulate the undo operation in a text editor and outputs the final text after applying all of the commands. The editor supports the following three commands:

"append <char>": Append the character <char> to the end.

"backspace": Delete the last character.

"undo": Undo the most recent change to the document.

The "undo" command should revert the most recent change made to the text. Meaning if the most recent command was "append", it should remove that character. If the subsequent command was "backspace", it should add the character back in.

Example(s)
commands = ["append a", "append b", "backspace", "append c", "undo", "append d", "undo", "append e"]

Output: "ae"

Explanation:
* append a: appends "a"
* append b: appends "b"
* backspace: removes "b"
* append c: appends "c"
* undo: removes "c"
* append d: appends "d"
* undo: removes "d"
* append e: appends "e"
'''



def simulate_undo(cmds):
    if len(cmds) == 0:
        return ''
    buffer = []
    last_buffer = []
    for c in cmds:
        split_cmd = c.split(' ')
        cmd = split_cmd[0]
        
        if cmd == 'append':
            buffer.append(split_cmd[1])
            last_buffer.append(('append', None))
        if cmd == 'backspace':
            if len(buffer) > 0:
                new_str = buffer[-1][:-1]
                if len(new_str) == 0:
                    last_buffer.append(('backspace', buffer.pop()))
                else:
                    last_buffer.append(('backspace', buffer[-1][-1]))
                    buffer[-1] = buffer[-1][:-1]
        if cmd == 'undo':
            if len(last_buffer) > 0:
                [undo_cmd, value] = last_buffer[-1]
                if undo_cmd == 'backspace':
                    buffer.append(value)
                    last_buffer.pop()
                if undo_cmd == 'append':
                    buffer.pop()
                    last_buffer.pop()

    return ''.join(buffer)
        
        



commands = ["append a", "append b", "backspace", "append c", "undo", "append d", "undo", "append e"]
print(simulate_undo(commands))
# Test Case 1: Basic operations
commands = ["append a", "append b", "append c", "backspace", "undo"]
result = simulate_undo(commands)
print(result == "abc")

# Test Case 2: Multiple undos
commands = ["append a", "append b", "append c", "backspace", "undo", "undo"]
result = simulate_undo(commands)
print(result == "ab")

# Test Case 3: Empty input
commands = []
result = simulate_undo(commands)
print(result == "")

# Test Case 4: Complex operations
commands = ["append a", "append b", "backspace", "append c", "undo", "append d", "undo", "append e"]
result = simulate_undo(commands)
print(result == "ae")

# Test Case 5: Undo with no history
commands = ["undo"]
result = simulate_undo(commands)
print(result == "")

# Test Case 6: Backspace with empty text
commands = ["backspace"]
result = simulate_undo(commands)
print(result == "")

# Test Case 7: Multiple backspaces
commands = ["append a", "append b", "append c", "backspace", "backspace"]
result = simulate_undo(commands)
print(result == "a")

# Test Case 8: Undo after multiple backspaces
commands = ["append a", "append b", "append c", "backspace", "backspace", "undo", "undo"]
result = simulate_undo(commands)
print(result == "abc")

# Test Case 9: Continuous undos and backspaces
commands = ["append a", "append b", "append c", "undo", "undo", "undo", "backspace", "backspace", "backspace", "append d", "append e", "append f"]
result = simulate_undo(commands)
print(result == "def")
