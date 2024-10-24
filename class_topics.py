#!/usr/bin/python3

class Topics:
    """Create a class Topics under which to place topic menus"""

    def __init__(self):
        """Constructor Method: Declare and Initialize attributes"""

    def main_menu(self):
        """Function to display main menu for training program"""
        print("_____________________________________________________")
        print("| ================================================== |")
        print("| CCNA ESSENTIALS         |       TRAINING PROGRAM   |")
        print("| ================================================== |")
        print("|____________________________________________________|")
        print("Enter number of topic to train on | (x) to exit")
        print("1)   Module 1 --> Networking Today")
        print("2)   Module 2 --> Switch Config")
        print("3)   Module 3 --> Protocols & Models")
        print("4)   Module 4 --> Physical Layer")
        print("5)   Module 5 --> Number Systems")
        print("6)   Module 6 --> Data Link Layer")
        print("7)   Module 7 --> Ethernet Switching")
        print("8)   Module 8 --> Network Layer")
        print("9)   Module 9 --> Address Resolution")
        print("10)  Module 10 --> Router Config")
        print("11)  Module 11 --> IPv4 Addressing")
        print("12)  Module 12 --> IPv6 Addressing")
        print("13)  Module 13 --> ICMP")
        print("14)  Module 14 --> Transport Layer")
        print("15)  Module 15 --> Application Layer")
        print("16)  Module 16 --> Network Security")
        print("17)  Module 17 --> Build Small Network")

    def mod1_menu(self):
        """Method to display module 1 training topics"""

    def mod2_menu(self):
        """Method to display module 2 training topics"""

    def mod3_menu(self):
        """Method to display module 3 training topics"""
        print("Which module 3 topic to train on? | (x) to Main Menu")
        print("1)   Conversions: binary to decimal")
        print("2)   Conversions: binary to hex")
        print("3)   Conversions: hex to decimal")
        print("4)   Private Addresses")
        print("5)   Reserved Addresses")
        print("6)   Terms and Definitions")
        print("\n Type in number of topic to select it")

    def mod4_menu(self):
        """Method to display module 4 training topics"""
        print("Which module 4 topic to train on? | (x) to Main Menu")
        print("1)   Protocols: Ports & Numbers")
        print("2)   Protocols: Core TCP/IP")
        print("3)   Protocols: General Protocols")

    def mod5_menu(self):
        """Method to display module 5 training topics"""
        print("Which module 5 topic to train on? | (x) to Main Menu")
        print("1)   Ethernet Cable Standards")
        print("2)   Ethernet Fiber Standards")
        print("3)   Twisted Pair Standards")
        print("4)   T568-A pin outs")
        print("5)   T568-B pin outs")
        print("6)   Terms and Definitions")
        print("\n Type in number of topic to select it")
        """response = input('> ')
        if response == '1':
            ethernet_cable_standards()
        elif response == '2':
            ethernet_fiber_standards()
        elif response == '3':
            twisted_pair_standards()
        elif response == '4':
            pin_outs_T568A()
        elif response == '5':
            pin_outs_T568B()
        elif response == '6':
            cabling_terms()
        else:
            print("Back to main menu")"""
    def mod6_menu(self):
        """Method to display module 6 training topics"""
        print("Which module 6 topic to train on? | (x) to Main Menu")
        print("1)   802.11 Standards")
        print("2)   Terms and Definitions")
