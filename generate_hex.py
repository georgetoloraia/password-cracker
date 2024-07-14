import random

# characters for random generate hex
char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

def generate_random_hex(length):
    return ''.join(random.choice(char) for _ in range(length))