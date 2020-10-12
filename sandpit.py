import random as rn

print(rn.randrange(16))

this_int = 0xEA
this_string = hex(this_int)
that_string = f'{this_int:02x}'

print(this_int, this_string, that_string)