import random

stars = []

def insert_value(percentage, star):

    for i in range(percentage):
        stars.append(star)

insert_value(78,3)
insert_value(17,4)
insert_value(4,5)
insert_value(1,6)

def get_random_star():
    random_star = random.choice(stars)
    return random_star