import random


def generate_password():
    min_password_length = 8
    conditions = {
        'is_long_enough': False,
        'special_character': False,
        'lowercase': False,
        'uppercase': False,
        'digits': False
    }

    # Initialize password with ascii character from range (33, 125)
    password = chr(random.randint(33, 125))

    while False in conditions.values():
        char = chr(random.randint(33, 125))

        # Ensuring that password does not contain two subsequent letter => it does not contain a dictionary word
        # Not the best solution but fulfills requirements :)
        if password[-1].isalpha() and char.isalpha():
            continue

        if char.isnumeric():
            conditions['digits'] = True
            password += char

        elif char.islower():
            conditions['lowercase'] = True
            password += char

        elif char.isupper():
            conditions['uppercase'] = True
            password += char

        else:
            conditions['special_character'] = True
            password += char

        if len(password) == min_password_length:
            conditions['is_long_enough'] = True

    return password


# Example
print(generate_password())





