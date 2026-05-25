import random
import string

def compute_valid_ids():
    total_ids = 26**2 * 10**3
    invalid_ids = 26 * 10
    valid_ids = total_ids - invalid_ids
    return valid_ids

def generate_valid_user_ids(n=5000):
    ids = set()
    while len(ids) < n:
        letters = random.sample(string.ascii_uppercase, 2)
        digits = random.choices('0123456789', k=3)
        if len(set(digits)) == 1:
            continue
        user_id = ''.join(letters) + '-' + ''.join(digits)
        ids.add(user_id)
    return list(ids)

print("Total valid IDs:", compute_valid_ids())
print("Sample valid IDs:", generate_valid_user_ids(10))