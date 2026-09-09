nums = [3, 1, 2]

nums.sort() # ager hum ye call kar latay hain to nums print karnay per hume sorted list he mile ge

# print(nums)

nums.reverse()

# print(nums)

nums.sort(reverse=True)

# print(nums)


sorted_nums = sorted(nums) # ager sorted list ko kisi variable me store karna he phir hum sorted funtion use kartay hain us list k against

# print(sorted_nums)

# First Question

messages = []

messages.append("user: salam")

# print(messages)

messages.append("assistant: walaikum salam")
messages.append("user: python sikhao")

# print(messages)
# print(f"count: {len(messages)}")

first = messages[0]

# print(f"first: {first}")

last = messages[-1]

# print(f"last: {last}")

last_two = messages[-2:]

# print(f"last two: {last_two}")

# Second Question

history = [
    "user: salam",
    "assistant: walaikum salam",
    "user: python sikhao",
    "assistant: zaroor, kahan se shuru karein?",
    "user: list se",
    "assistant: theek hai",
]

history.append("user: aur batao")
history.extend(["assistant: ji", "user: shukriya"])

# print(history)

trimmed_history = history[-4:]

# print(len(history))
# print(trimmed_history)
# print(len(trimmed_history))

# Third question

original = ["a", "b", "c"]
backup = original

original.append("d")

print("original:", original)
print("backup:  ", backup)

original2 = ["a", "b", "c"]
backup2 = original2.copy()

original2.append("d")

print("original2:", original2)
print("backup2:  ", backup2)

print(id(original) == id(backup))      # ?
print(id(original2) == id(backup2))    # ?

print(original is backup)              # ?
print(original2 is backup2)            # ?