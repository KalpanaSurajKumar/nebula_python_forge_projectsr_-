import argparse

Parser=argparse.ArgumentParser(description="To print the name of the person")
Parser.add_argument("name",type = int, help="A name")

args = Parser.parse_args()

print("The cube of the number is:",args.name*args.name*args.name)
