# enigma

enigma(old) is a old file that does not work, i have not deleted it because i want to be able to look back on it later.

-------------
problem: i think the machine will work on messages written with this machine, but will not be able to translate messages from the real enigma machine.
this is because the output from one rotor, lets say K in this example, will be the input in the next rotor based on the letter K, not on the position of the rotors relative to each other

for example output from one rotor is K, input into the next rotor will also be K. even tho the next rotor had S next to the output of the first rotor K.
i will still be able to encrypt and decrypt messages from this machine. but i will have to fix this bug to translate messages from the real enigma.
-------------

for now Enigma(NEW) works with the first letter but not after that (this is a bug), and you have to restart between encrypting and decrypting (this is not a bug. you have to reset the enigma settings to decrypt. something i have not implementet yet so the way to reset is to restart the program.)