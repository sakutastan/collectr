from . import main
from sys import argv

if len(argv)>1: # if launched with arguments (the domain)
    domain=argv[1]
else:
    domain=input("input domain: ")

main(domain)
