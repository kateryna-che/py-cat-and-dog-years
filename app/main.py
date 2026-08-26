def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    human_age = []

    if cat_age < 15:
        human_age.append(0)
    elif cat_age < 24:
        human_age.append(1)
    else:
        human_age.append(2 + (cat_age - 24) // 4)

    if dog_age < 15:
        human_age.append(0)
    elif dog_age < 24:
        human_age.append(1)
    else:
        human_age.append(2 + (dog_age - 24) // 5)

    return human_age
