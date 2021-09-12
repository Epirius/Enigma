
# Real historical enigma offsets.
e1 = ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
e2 = ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
e3 = ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
e4 = ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
e5 = ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
UKW_A = "EJMZALYXVBWFCRQUONTSPIKHGD"
UKW_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
UKW_C = "FVPJIAOYEDRZXWGCTKUQSBNMHL"


class Rotor:
    def __init__(self, ring_info, offset):
        self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.ring_output = ring_info[0]
        self.turnover = ring_info[1]
        self.R = self.assign_rotor()
        self.offset = offset

    def assign_rotor(self):
        rotor = {}
        for i in range(26):
            rotor.setdefault(self.alpha[i], self.ring_output[i])
        return rotor

    def get_key(self, char, ignore):
        char = char.upper()
        key = ord(char) + self.offset
        if key > 90:
            key = key - 25
        if key < 65:
            key = key + 25
        key = chr(key)
        self.offset += 1
        if self.offset > 26:
            self.offset -= 26
        if ignore == True:
            self.offset -= 1
        print(self.offset - 1)
        return self.R[key]

    def do_turnover(self):
        if self.offset == ord(self.turnover) - 64:
            return True
        else:
            return False


def plug_board(char):
    plug_dict = {}
    # makes the dict 2-way
    plug_dict.update({v: k for k, v in plug_dict.items()})
    if char in plug_dict:
        return plug_dict[char]
    else:
        return char


def reflector(char, version):
    ref_dict = {}
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        ref_dict.setdefault(alpha[i], version[i])
    return ref_dict[char]


def enigma(message, slot1, slot2, slot3, reflector_version):
    message = list(message.upper())
    encrypted = []
    for i in range(len(message)):
        if message[i] not in slot1.alpha:
            encrypted.append(message[i])
        else:
            if slot1.do_turnover() == True:
                print("--------------------------------------")
                slot2.offset += 1
            if slot2.do_turnover() == True:
                slot3.offset += 1

            m = plug_board(message[i])
            m = slot1.get_key(m, False)
            print("-" + m)
            m = slot2.get_key(m, True)
            print("--" + m)
            m = slot3.get_key(m, True)
            print("---" + m)
            m = reflector(m, reflector_version)
            print("------" + m)
            m = slot3.get_key(m, True)
            print("---" + m)
            m = slot2.get_key(m, True)
            print("--" + m)
            m = slot1.get_key(m, True)
            print("-" + m)
            m = plug_board(m)
            encrypted.append(m)
    return "".join(encrypted)


r1 = Rotor(e1, 1)
r2 = Rotor(e2, 1)
r3 = Rotor(e3, 1)

message = "w"  # "LI"

print()
print(enigma(message, r1, r2, r3, UKW_B))

#https://piotte13.github.io/enigma-cipher/