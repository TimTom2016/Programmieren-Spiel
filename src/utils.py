def checkOperator(self, args):
    try:
        if args[1] == "==":
            if args[0] == args[2]:
                return "True"
        if args[1] == "+=":
            args[0] += args[-2]
            return args[0]
        if args[1] == "-=":
            args[0] -= args[-2]
            return args[0]
        if args[1] == "<=":
            if args[0] <= args[2]:
                return "True"
        if args[1] == "*=":
            args[0] *= args[-2]
            return args[0]
        if args[1] == ">=":
            if args[0] >= args[2]:
                return "True"
        if args[1] == "+":
            return args[0] + args[2]
        if args[1] == "-":
            return args[0] - args[2]
        if args[1] == "=":
            args[0] = args[2]
            return args[0]
        if args[1] == "*":
            return args[0] * args[-2]
        return "False"
    except:
        return "Error"
