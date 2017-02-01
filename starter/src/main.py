import sys
from premier import estPremier

userInput = input('Choisissez un nombre : ')

try:
    n = int(userInput)
except ValueError:
    print("Oops ! Ceci n'est pas un nombre...")
    sys.exit()

if estPremier(n) :
    print("{} est un nombre premier".format(n))
else :
    print("{} n'est pas un nombre premier".format(n))
