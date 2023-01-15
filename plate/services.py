import random


def generate_plate():
    letters = 'АВЕКМНОРСТУХ'
    seria = ''.join(random.choice(letters) for i in range(3))
    register_number = ''.join([str(random.choice(range(10))) for i in range(3)])
    res = seria[0] + register_number + seria[1:]
    return res
