import random as rd
import string as st

pass_size = int(input('What password length do you want? '))
structure = st.ascii_letters + st.digits + '!@#$%&*()-=+_.?'
randomize = rd.SystemRandom()

print(''.join(randomize.choice(structure) for i in range(pass_size)))