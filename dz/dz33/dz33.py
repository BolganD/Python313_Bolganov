import json
from random import choice


def gen_person():

    name = ''
    tel = ''

    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letter)

    while len(tel) != 10:
        tel += choice(num)

    person = {
        'name': name,
        'tel': tel
    }
    return person


def write_json(person_dict):
    idd = ''
    d_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(idd) != 11:
        idd += choice(d_num)

    try:
        data = json.load(open('person.json'))
    except FileNotFoundError:
        data = {}

    d = person_dict
    data[idd] = d
    with open('person.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())