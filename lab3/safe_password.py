import random
import re
import string


def all_conditions_met(conditions_dictionary):
    # print(f'are conditions met:{conditions_dictionary} : {sum(conditions_dictionary.values()) >= 4}')
    return sum(conditions_dictionary.values()) >= 4


# Algorithm assumes that points at which random character will be randomly choose
def generate_safe_password():
    password_length_min = 8
    password_length_max = password_length_min + random.randint(0, 12)
    allowed_letters = string.ascii_letters
    allowed_digits = string.digits
    allowed_special_characters = string.punctuation
    # Currently supported conditions with their counters
    conditions_counters = {
        'min_digits': 0,
        'min_specials': 0,
        'min_uppercase_letters': 0,
        'min_lowercase_letters': 0
    }
    # Just index for dictionary based on numbers
    conditions_index = {
        0: 'min_digits',
        1: 'min_specials',
        2: 'min_uppercase_letters',
        3: 'min_lowercase_letters'
    }
    # Stores dictionaries for each criterion e.g. letters etc.
    password_dictionary = {
        'letters': allowed_letters,
        'digits': allowed_digits,
        'specials': allowed_special_characters
    }

    while True:
        password = ''
        # For each character in password
        for _ in range(password_length_max):
            # Randomly choose criterion to start with
            condition_index_value = random.randint(0, 3)
            # Check if all criteria are already met and if yes just choose randomly new one
            if all_conditions_met(conditions_counters):
                conditions_name = conditions_index[condition_index_value]
                choose_char = random.choice(password_dictionary[conditions_name.split('_')[
                    len(conditions_name.split('_')) - 1]])
                # In case of uppercase and lowercase letters just invoke upper or lower
                if conditions_name == 'min_uppercase_letters':
                    choose_char = choose_char.upper()
                if conditions_name == 'min_lowercase_letters':
                    choose_char = choose_char.lower()
                # Add character to already existing password
                password += choose_char
                # Increase conditions counter for debugging purposes
                conditions_counters[conditions_index[condition_index_value]] += 1
            # Check if current condition is not met e.g. there are no lower character letters in password
            elif conditions_counters[conditions_index[condition_index_value]] == 0:
                conditions_name = conditions_index[condition_index_value]
                choose_char = random.choice(password_dictionary[conditions_name.split('_')[
                    len(conditions_name.split('_')) - 1]])
                if conditions_name == 'min_uppercase_letters':
                    choose_char = choose_char.upper()
                if conditions_name == 'min_lowercase_letters':
                    choose_char = choose_char.lower()
                password += choose_char
                conditions_counters[conditions_index[condition_index_value]] += 1
            else:
                # Check if there is any non met condition using modulo operation
                # This could be extracted as a method etc.
                for i in range(0, 4):
                    if conditions_counters[conditions_index[(condition_index_value + i) % 4]] == 0:
                        conditions_name = conditions_index[condition_index_value]
                        choose_char = random.choice(password_dictionary[conditions_name.split('_')[
                            len(conditions_name.split('_')) - 1]])
                        if conditions_name == 'min_uppercase_letters':
                            choose_char = choose_char.upper()
                        if conditions_name == 'min_lowercase_letters':
                            choose_char = choose_char.lower()
                        password += choose_char
                        conditions_counters[conditions_index[condition_index_value]] += 1
                        break

        # # Extra security. Check if password mets criteria.
        condition_a = len(password) >= 8
        condition_b = any(char.isupper() for char in password)
        condition_c = any(char.isdigit() for char in password)
        condition_d = any(char in password_dictionary['specials'] for char in password)
        # This is tricky but if we want extra validate that case extra library will be needed.
        # Algorithm works by randomly choosing which type of character to choose at which possition so there is very
        # rare possibility of chooosing a word :) 
        condition_e = not re.search(r'\b(?:word1|word2|word3)\b', password, flags=re.IGNORECASE)

        if all([condition_a, condition_b, condition_c, condition_d, condition_e]):
            # print(f'conditions_coutners:{conditions_counters}')
            return password

        # print(f'conditions_coutners:{conditions_counters}')
        # return password


# Example usage
if __name__ == "__main__":
    safe_password = generate_safe_password()
    print("Generated safe password:", safe_password)
