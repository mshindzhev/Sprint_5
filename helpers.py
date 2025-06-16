import random


def generation_email():
    return f"testovich{random.randint(100, 10000)}@gmail.com"

def generation_invalid_email():
    return f"testovich{random.randint(100, 10000)}babail.gnom"