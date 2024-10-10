import string

def evaluate_password_strength(password):
    # Initialize strength factors
    length_valid = len(password) >= 8
    upper_valid = any(c.isupper() for c in password)
    lower_valid = any(c.islower() for c in password)
    digit_valid = any(c.isdigit() for c in password)
    special_valid = any(c in string.punctuation for c in password)

    # Determine overall strength
    strength_criteria = [length_valid, upper_valid, lower_valid, digit_valid, special_valid]
    strength_score = sum(strength_criteria)

    # Evaluate strength based on the score
    if strength_score == 5:
        return "Very Strong"
    elif strength_score == 4:
        return "Strong"
    elif strength_score == 3:
        return "Moderate"
    elif strength_score == 2:
        return "Weak"
    else:
        return "Very Weak"

# Example usage:
password = input("Enter a password to evaluate its strength: ")
strength = evaluate_password_strength(password)
print(f"The strength of your password is: {strength}")
