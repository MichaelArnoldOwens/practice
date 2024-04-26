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



def editor(cmds):
    if len(cmds) == 0:
        return ''
    buffer = []
    last_buffer = []
    for c in cmds:
        print(last_buffer)
        print(buffer)
        split_cmd = c.split(' ')
        cmd = split_cmd[0]
        print(cmd)
        
        if cmd == 'append':
            buffer.append(split_cmd[1])
            last_buffer.append(('append', None))
        if cmd == 'backspace':
            if len(buffer) > 0:
                new_str = buffer[-1][:-1]
                print('new_str:', new_str)
                if len(new_str) == 0:
                    last_buffer.append(('backspace', buffer.pop()))
                else:
                    last_buffer.append(('backspace', buffer[-1][-1]))
                    buffer[-1] = buffer[-1][:-1]
        if cmd == 'undo':
            [undo_cmd, value] = last_buffer[-1]
            if undo_cmd == 'backspace':
                buffer.append(value)
                last_buffer.pop()
            if undo_cmd == 'append':
                buffer.pop()
                last_buffer.pop()

    return ''.join(buffer)
        
        



commands = ["append a", "append b", "backspace", "append c", "undo", "append d", "undo", "append e"]
print(editor(commands))
