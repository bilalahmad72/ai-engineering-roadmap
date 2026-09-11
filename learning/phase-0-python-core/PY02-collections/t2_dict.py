response = {
    "id": "msg_01abc",
    "model": "claude-opus-4",
    "stop_reason": "end_turn",
    "content": [{"type": "text", "text": "Salam! Kaise madad karun?"}],
    "usage": {"input_tokens": 12, "output_tokens": 34, "cache_tokens": 100},
}

# print(f"model: {response['model']}")
# print(f"reply: {response['content'][0]['text']}")
# print(f"total tokens: {response['usage']['input_tokens'] + response['usage']['output_tokens']}")

# print(f"error: {response.get('error', 'no error')}")
# print(f"cache tokens: {response.get('usage', {}).get('cache_tokens', 0)}")

# Question two

messages = [
    {"role": "system", "content": "Tum ek Flutter expert ho."},
    {"role": "user", "content": "Riverpod kya hai?"},
    {"role": "assistant", "content": "Riverpod ek state management library hai."},
]

print(messages)

messages.append({"role": "user", "content": "aur BLOC?"})

print(messages)

print(f"total messages: {len(messages)}")
print(f"first role: {messages[0]['role']}")
print(f"last content: {messages[-1]['content']}")
print(f"message 1: {messages[1]['role']} => {messages[1]['content']}")

first = messages[0]

print("role" in first)        # ?
print("system" in first)      # ?
print("system" in first.values())   # ?

last_message = messages[-1]

last_message["timestamp"] = '2026-09-11'

print(messages[-1])

popped_message = last_message.pop("timestamp")

print(f"popped: {popped_message}")