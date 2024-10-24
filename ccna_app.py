#!/usr/bin/python3

from class_ccna import CCNA
from class_topics import Topics
import ccnadict

while True:
    topics = Topics()
    topics.main_menu()
    response = input('> ')
    if response == '1':
        #  topics.mod1_menu()  Create this
        #  response = input('> ')
        mod1 = CCNA()
        mod1.flash_cards(ccnadict.sbj_mod1td, ccnadict.dict_mod1td)
    elif response == '2':
        mod2 = CCNA()
        mod2.flash_cards(ccnadict.sbj_mod2td, ccnadict.dict_mod2td)
    elif response == '3':
        mod3 = CCNA()
        mod3.flash_cards(ccnadict.sbj_mod3td, ccnadict.dict_mod3td)
    elif response == '4':
        mod4 = CCNA()
        mod4.flash_cards(ccnadict.sbj_core, ccnadict.dict_core)
    elif response == '5':
        mod5 = CCNA()
        mod5.flash_cards(ccnadict.sbj_mod5td, ccnadict.dict_mod5td)
    elif response == '6':
        mod6 = CCNA()
        mod6.flash_cards(ccnadict.sbj_mod6td, ccnadict.dict_mod6td)
    elif response == '7':
        mod7 = CCNA()
        mod7.flash_cards(ccnadict.sbj_mod7td, ccnadict.dict_mod7td)
    elif response == '8':
        mod8 = CCNA()
        mod8.flash_cards(ccnadict.sbj_mod8td, ccnadict.dict_mod8td)
    elif response == '9':
        mod9 = CCNA()
        mod9.flash_cards(ccnadict.sbj_mod9td, ccnadict.dict_mod9td)
    elif response == '10':
        mod10 = CCNA()
        mod10.flash_cards(ccnadict.sbj_mod10td, ccnadict.dict_mod10td)
    elif response == '11':
        mod11 = CCNA()
        mod11.flash_cards(ccnadict.sbj_mod11td, ccnadict.dict_mod11td)
    elif response == '12':
        mod12 = CCNA()
        mod12.flash_cards(ccnadict.sbj_mod12td, ccnadict.dict_mod12td)
    elif response == '13':
        mod13 = CCNA()
        mod13.flash_cards(ccnadict.sbj_mod13td, ccnadict.dict_mod13td)
    elif response == '14':
        mod14 = CCNA()
        mod14.flash_cards(ccnadict.sbj_mod14td, ccnadict.dict_mod14td)
    elif response == '15':
        mod15 = CCNA()
        mod15.flash_cards(ccnadict.sbj_mod15td, ccnadict.dict_mod15td)
    elif response == '16':
        mod16 = CCNA
        mod16.flash_cards(ccnadict.sbj_mod16td, ccnadict.dict_mod16td)
    elif response == '17':
        mod17 = CCNA
        mod17.flash_cards(ccnadict.sbj_mod17td, ccnadict.dict_mod16td)
    else:
        print("Do It Again Tomorrow!!")
        break
