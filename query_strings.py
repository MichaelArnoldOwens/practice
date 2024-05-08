'''
Build a query string parser. This problem should be presented in 4 stages. Move on to the next stage after completing the previous one without breaking any functionality.

1. Build a query string parser.
2. If there is no value for a key specified in the query string, we should treat that value as a boolean true.
3. Keys can be used multiple times. The resulting value for that key should be an array of all 
4. Build the inverse function.

Use built-in functions from Python's urllib or Javascript's decodeURIComponent and encodeURIComponent to simplify interpreting the strings.
 

EXAMPLE(S)
Input: ?foo=hello&bar=world
Output: { foo: "hello", bar: "world" }
 

FUNCTION SIGNATURE
function parseQueryString(query) { /* returns object */ }
def parse_query_string(query: str) -> dict:
'''

def parse_query_string(query: str) -> dict:
  amp_split_list = query[1:].split('&')
  result = {}
  for key_val_pair in amp_split_list:
    if '=' in key_val_pair:
      [key, value] = key_val_pair.split('=')
      if key in result:
        if type(result[key]) == list:
          result[key].append(value)  
        else:
          result[key] = [result[key], value]
      else:
        result[key] = value
    else:
      result[key_val_pair] = True

  return result

def generate_query_string(arg):
  result = '?'
  for key in arg:
    if type(arg[key]) == bool:
      result += f'{key}&'
    elif type(arg[key]) == list:
      for val in arg[key]:
        result+= f'{key}={val}&'
    else:
      result += f'{key}={arg[key]}&'
  return result[:-1]
    

print(generate_query_string({'foo': ['hello', 'big'], 'bar': 'world', 'pizza': True}))
print(generate_query_string({ 'foo': 'hello', 'bar': 'hello', 'baz': True }))
# print(parse_query_string('?foo=hello&bar=world&foo=big&pizza'))
# print(parse_query_string('?foo'))

