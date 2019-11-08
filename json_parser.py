import json

test_str = '{"a":123, "b":"xyz", "c":0.01}'

def json_read(json_input, key) -> (str, str):
    py_input = json.loads(json_input)
    out = py_input[key]
    return str(out)

def json_add(json_input, key, value) -> (str, str, str):
    py_input=json.loads(json_input)
    py_input[key]=value
    out=json.dumps(py_input)
    return out

if __name__ == "__main__":
    print (test_str)
    print (json_read(test_str, "a"))
    print (json_add(test_str,"d",666))
    print (test_str)