"""
PY01 · Topic 1 — Variables aur types.

Bilal ka practice file. Sawal 1 aur 2 ka hal.
"""

full_name = "Bilal Ahmad"
experience_years = 5
hourly_rate = 20.0
is_learning_ai = True

print(f"full_name = {full_name} (type: {type(full_name).__name__})")
print(f"experience_years = {experience_years} (type: {type(experience_years).__name__})")
print(f"hourly_rate = {hourly_rate} (type: {type(hourly_rate).__name__})")
print(f"is_learning_ai = {is_learning_ai} (type: {type(is_learning_ai).__name__})")

# Sawal 2 — format specs
hours_per_month = 120
total_earnings = hourly_rate * hours_per_month

print(
    f"{hourly_rate:.2f}/hour x {hours_per_month} hours "
    f"= {total_earnings:,.2f} per month"
)
