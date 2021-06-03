def execute(Command_Helper,*args):
    if args[0].startswith("range"):
        iterations = args[0][(args[0].find('(') + 1):args[0].find(')')]
        if str(range) == "True":
            return
        if str(range).isalnum():
            int(range)