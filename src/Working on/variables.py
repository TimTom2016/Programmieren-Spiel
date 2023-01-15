import string
variables = {}
def execute(Command_Helper,args):
    if Command_Helper.Controller.Command_Identifier.identify(args[0],"Get_module"):
        return "Function"
    try:
        if args[2] in variables:
            args[2] = variables[args[2]]
        for i in string.ascii_uppercase:
            if args[0] == i:
                if args[1] == "=":
                    variables[i] = args[2]
                args[0] = variables[i]
        for i in string.ascii_lowercase:
            if args[0] == i:
                if args[1] == "=":
                    variables[i] = args[2]
                args[0] = variables[i]
        for i in string.digits:
            if args[0] == i:
                break
        if Command_Helper.Check_Operators(args) == "True":
            print("Got True")
            return "True"
        elif Command_Helper.Check_Operators(args) == "False":
            print("Could'nt Find Operator")
            return "False"
        else:
            print(Command_Helper.Check_Operators(args))
            return Command_Helper.Check_Operators(args)
    except:
        for i in string.ascii_uppercase:
            if args[0] == i:
                if args[1] == "=":
                    variables[i] = args[2]
                args[0] = variables[i]
        for i in string.ascii_lowercase:
            if args[0] == i:
                if args[1] == "=":
                    variables[i] = args[2]
                args[0] = variables[i]
        for i in string.digits:
            if args[0] == i:
                break
        if Command_Helper.Check_Operators(args) == "True":
            print("Got True")
            return "True"
        elif Command_Helper.Check_Operators(args) == "False":
            print("Could'nt Find Operator")
            return "False"
        else:
            print(Command_Helper.Check_Operators(args))
            return Command_Helper.Check_Operators(args)
def check_if_line_variable(Command_Helper,args):
    for i in string.ascii_uppercase:
        if args.startswith(i):
            args = args.split(" ")

    #for i in string.ascii_lowercase:
    #for i in string.digits:
