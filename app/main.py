def get_human_age(cat_age: int, dog_age: int) -> list:
    human_age = [
        (cat_age >= 15)
        + (cat_age >= 24)
        + max(0, (cat_age - 24) // 4),
        (dog_age >= 15)
        + (dog_age >= 24)
        + max(0, (dog_age - 24) // 5)
    ]
    return human_age
