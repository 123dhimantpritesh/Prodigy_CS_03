import re

def password_strength(password):
    strength = {'length': False, 'uppercase': False, 'lowercase': False, 'numbers': False, 'special': False}
    if len(password) >= 8:
        strength['length'] = True
    if re.search(r'[A-Z]', password):
        strength['uppercase'] = True
    if re.search(r'[a-z]', password):
        strength['lowercase'] = True
    if re.search(r'[0-9]', password):
        strength['numbers'] = True
    if re.search(r'[\W_]', password):
        strength['special'] = True
    return strength

def evaluate_strength(strength):
    criteria = list(strength.values())
    if all(criteria):
        return "Strong"
    elif criteria.count(True) >= 3:
        return "Medium"
    else:
        return "Weak"


password = input("Enter your password: ")
strength = password_strength(password)
feedback = evaluate_strength(strength)
print(f"Your password is {feedback}.")
for key, value in strength.items():
    print(f"Contains {key}: {'Yes' if value else 'No'}")