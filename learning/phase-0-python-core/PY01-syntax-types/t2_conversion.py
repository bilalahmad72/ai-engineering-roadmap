max_token_str = "4096"
temperature_str = "0.7"
timeout_str = "30.5"
model_str = "claude-opus-4"

max_token_int = int(max_token_str)

print(f"max_tokens = {max_token_int} (type : {type(max_token_int).__name__})")

temperature_str_float = float(temperature_str)

print(f"temprature = {temperature_str_float} (type : {type(temperature_str_float).__name__})")

timeout_float = float(timeout_str)
timeout = int(timeout_float)

print(f"timeout = {timeout} (type : {type(timeout).__name__})")

print(f"model = {model_str} (type : {type(model_str).__name__})")

debug_str = "False"
stream_str = "true"
cache_str = ""
number_str = "0"
number_val = 5

is_debug = bool(debug_str)
is_stream = bool(stream_str)
is_cache = bool(cache_str)
is_number = bool(number_str)
is_number_val = bool(number_val)

print(f"debug_str is : {is_debug}")
print(f"stream_str is : {is_stream}")
print(f"cache_str is : {is_cache}")
print(f"number_str is : {is_number}")
print(f"number_val is : {is_number_val}")

age = 30
price = 300.00
x_str = "only string"

age_int = isinstance(age, int)
price_float = isinstance(price, float)
x_int_or_float = isinstance(x_str, (int, float))

print(f"Is age Integer : {age_int}")
print(f"Is price float : {price_float}")
print(f"Is x is integer or float : {x_int_or_float}")

test_values = "4096"
test_decimal = "30.5"
test_text = "claude"

try: 
    value = float(test_values)
    is_test_value_number = True
except ValueError:
    is_test_value_number = False

print(f"{test_values!r} -> isdigit: {(test_values).isdigit()}, float works: {is_test_value_number}")

try: 
    value = float(test_decimal)
    is_test_decimal_float = True
except ValueError:
    is_test_decimal_float = False

print(f"{test_decimal!r} -> isdigit: {(test_decimal).isdigit()}, float works: {is_test_decimal_float}")

try:
    value = float(test_text)
    is_test_text_string = True
except ValueError:
    is_test_text_string = False

print(f"{test_text!r} -> isdigit: {(test_text).isdigit()}, float works: {is_test_text_string}")