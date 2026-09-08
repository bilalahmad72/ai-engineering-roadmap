model_a = "claude-opus-4"
tokens_a = 15234
cost_a = 0.2285

model_b = "claude-haiku-4"
tokens_b = 892450
cost_b = 0.7139

model_heading = "MODEL"
tokens_heading = "TOKENS"
cost_heading = "COST"

print(f"{model_heading:<16} {tokens_heading:<11} {cost_heading}")
print(f"{model_a:<16} {tokens_a:<11,} ${cost_a:.4f}")
print(f"{model_b:<16} {tokens_b:<11,} ${cost_b:.4f}")

print(f"{tokens_a=}")
print(f"{cost_a * 2 = }")