max_token_str = "4096"
temprature_str = "0.7"
timeout_str = "30.5"
model_str = "claude-opus-4"

max_token_int = int(max_token_str)

print(f"max_tokens = {max_token_int} (type : {type(max_token_int).__name__})")

temprature_str_float = float(temprature_str)

print(f"temprature = {temprature_str_float} (type : {type(temprature_str_float).__name__})")

timeout_str_float = float(timeout_str)
timeout_str_int = int(timeout_str_float)

print(f"timeout = {timeout_str_int} (type : {type(timeout_str_int).__name__})")

print(f"model = {model_str} (type : {type(model_str).__name__})")