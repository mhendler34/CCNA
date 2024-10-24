#!/usr/bin/python3

# File for all dictionaries in class_networking_app.py
# ABSOLUTE PATH
# '/home/mitchell/Code/projects/networking/text_files/mod1_terms.txt', 'r'
# MODULE 1
dictionary_1 = {}
with open('text_files/module01.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_1[key] = value

sbj_mod1td = "Module 1: Networking Today"
dict_mod1td = dictionary_1

# MODULE 2
dictionary_2 = {}
with open('text_files/module02.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_2[key] = value

sbj_mod2td = "Module 2: Switch Configuration"
dict_mod2td = dictionary_2


# MODULE 3
dictionary_3 = {}
with open('text_files/module03.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_3[key] = value

sbj_mod3td = "Module 3: Protocols & Models"
dict_mod3td = dictionary_3

# MODULE 4
dictionary_4a = {}
with open('text_files/module04.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_4a[key] = value

sbj_core = "Module 4: Physical Layer"
dict_core = dictionary_4a


# MODULE 5
dictionary_5 = {}
with open('text_files/module05.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_5[key] = value

sbj_mod5td = "Module 5: Number Systems"
dict_mod5td = dictionary_5


# MODULE 6
dictionary_6a = {}
with open('text_files/module06.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_6a[key] = value

sbj_mod6td = "Module 6: Data Link Layer"
dict_mod6td = dictionary_6a

# MODULE 7
dictionary_7 = {}
with open('text_files/module07.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_7[key] = value

sbj_mod7td = "Module 7: Ethernet Switching"
dict_mod7td = dictionary_7


# MODULE 8
dictionary_8 = {}
with open('text_files/module08.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_8[key] = value

sbj_mod8td = "Module 8: Network Layer"
dict_mod8td = dictionary_8

"""
# MODULE 9
dictionary_9 = {}
with open('text_files/module09.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_9[key] = value

sbj_mod9td = "Module 9: Address Resolution"
dict_mod9td = dictionary_9

# MODULE 10
dictionary_10 = {}
with open('text_files/module10.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_10[key] = value

sbj_mod10td = "Module 10: Router Configuration"
dict_mod10td = dictionary_10

# MODULE 11
dictionary_11 = {}
with open('text_files/module11.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_11[key] = value

sbj_mod11td = "Module 11: IPv4 Addressing"
dict_mod11td = dictionary_11

# MODULE 12
dictionary_12 = {}
with open('text_files/module12.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_12[key] = value

sbj_mod12td = "Module 12: IPv6 Addressing"
dict_mod12td = dictionary_12

# MODULE 13
dictionary_13 = {}
with open('text_files/module13.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_13[key] = value

sbj_mod13td = "Module 13: ICMP"
dict_mod13td = dictionary_13

# MODULE 14
dictionary_14 = {}
with open('text_files/module14.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_14[key] = value

sbj_mod14td = "Module 14: Transport Layer"
dict_mod14td = dictionary_14

# MODULE 15
dictionary_15 = {}
with open('text_files/module15.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_15[key] = value

sbj_mod15td = "Module 15: Application Layer"
dict_mod15td = dictionary_15

# MODULE 16
dictionary_16 = {}
with open('text_files/module16.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_16[key] = value

sbj_mod16td = "Module 16: Network Security"
dict_mod16td = dictionary_16

# MODULE 17
dictionary_17 = {}
with open('text_files/module17.txt', 'r') as m:
    lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        dictionary_17[key] = value

sbj_mod17td = "Module 17: Build Small Network"
dict_mod17td = dictionary_17

"""
