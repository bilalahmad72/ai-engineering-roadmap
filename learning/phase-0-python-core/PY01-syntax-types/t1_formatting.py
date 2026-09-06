input_tokens = 15432
cost_per_million = 15.0
success_rate = 0.8567

print(f"Tokens: {input_tokens:,}")

cost = input_tokens * cost_per_million / 1_000_000

print(f"Cost: ${cost:.6f}")

print(f"Success: {success_rate:.1%}")
print(f"Success: {success_rate:.2%}")

print(f"{input_tokens:,} tokens = ${cost:.6f} ({success_rate:.1%} success)")