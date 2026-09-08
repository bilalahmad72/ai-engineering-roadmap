raw_line = "   ANTHROPIC_API_KEY = sk-ant-api03-xyz123456789   \n"

raw_line_strip = raw_line.strip()

print(raw_line_strip)

raw_line_strip_parts = raw_line_strip.split("=", 1)

print(raw_line_strip_parts)

first_item = raw_line_strip_parts[0]
second_item = raw_line_strip_parts[1]

print(first_item)
print(second_item)

key = first_item.rstrip()
value = second_item.lstrip()

print(f"key = {key!r}")
print(f"value = {value!r}")

prefix  = value[:7]
postfix = value[-4:]

print(f"Using API Key: {prefix}...{postfix}")

key_validation = key.endswith('_API_KEY')

print(f"Key ends with _API_KEY : {key_validation}")

value_validation = value.startswith('sk-ant-')
value_length = len(value)

print(f"value start with sk-ant- : {value_validation}")
print(f"value length > 20 : {value_length > 20}")