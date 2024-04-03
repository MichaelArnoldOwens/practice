'''
❓ PROMPT
You will be implementing a function called stringify which will take in a Javascript Object and return the JSON representation of the object as a string. This function is actually built into Javascript as `JSON.stringify(object)` but you have to write yours from scratch!

You may want to take a moment to review the rules for [JSON syntax](https://www.w3schools.com/js/js_json_syntax.asp).

Example(s)
anObj = {"x": 5, "y": "Oliver"}
stringify(anObj)
Output: '{"x": 5, "y": "Oliver"}'

aList = [1, "hello", "null", {"x": 5, "y": "Oliver"}]
stringify(aList)
Output: '[1, "hello", "null", {"x": 5, "y": "Oliver"}]'
'''


def stringify_obj(arg):
    if type(arg) == dict:
        result = "{"
        for i, k in enumerate(arg):
           key_val = f'"{k}": ' 
           val = f'"{arg[k]}"' if type(arg[k]) == str else str(arg[k])
           key_val += f'{val}' 
           result += f'{key_val}, ' if i < len(arg) - 1 else key_val
        result += '}'

        return result
    else:
        return arg


def stringify(arg):
    if type(arg) == list:
        result = '"['
        for idx, i in enumerate(arg):
            if type(i) == dict:
                stringified_obj = stringify_obj(i)
                result += f'{stringified_obj}, ' if idx < len(arg) - 1 else stringified_obj
            elif type(i) == str:
                result += f'"{i}", ' if idx < len(arg) - 1 else f'"{i}"'
            elif type(i) == int or type(i) == float:
                result += f'{i}, ' if idx < len(arg) - 1 else i
        result += ']"'
        return result
    elif type(arg) == dict:
        return f'"{stringify_obj(arg)}"'


print(stringify([1, "hello", "null", {"x": 5, "y": "Oliver"}]))
print(stringify({"x": 5, "y": "Oliver"}))
