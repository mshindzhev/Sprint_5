import random


def generation_email():
    return f"testovich{random.randint(100, 10000)}@gmail.com"

def generation_invalid_email():
    return f"testovich{random.randint(100, 10000)}babail.gnom"

def generation_name_product():
    name_product = [
        "Велосипед",
        "Самокат",
        "Набор Kinder",
        "Советская энциклопедия",
        "Колесо, сам создавал"
    ]

    return f"{random.choice(name_product)}{random.randint(100,10000)}"