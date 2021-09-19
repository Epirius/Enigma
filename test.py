rotor = {1:"a", 2:"b", 3:"c"}
print(rotor)
reverse_rotor={}
reverse_rotor.update({v: k for k, v in rotor.items()})

print(reverse_rotor)