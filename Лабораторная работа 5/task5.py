from random import sample
from string import ascii_letters, digits


def get_random_password(n=8) -> str:
    str_ = ascii_letters + digits
    return "".join(sample(str_, n))


print(get_random_password())
# end
