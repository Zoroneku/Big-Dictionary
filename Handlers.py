from Dictionary import Dictionary


# returns -1 for command with no args
# returns -2 for command with no results
# if there is a nonsense argument it returns the first one
# if nothing is wrong it returns a list of items fitting the given options
def handleRequest(request, args):
    if not args:
        return -1
    else:
        items = request(args[0])
        if not items:
            return -2
        
        aFlag = False
        eFlag = False
        for arg in args[1:]:
            if arg == "-a":
                aFlag = True
            elif arg == "-e" and request == Dictionary.define:
                eFlag = True
            else:
                return arg

        if not aFlag:
            items = items[:3]
        
        return items


# returns a string to be printed to the terminal, or a list of results to be printed later
def handleCmd(cmd_info, args):
    results = handleRequest(cmd_info['function'], args)
    if results == -1:
        return f"Usage: {cmd_info['cmd']} [WORD] [OPTION]..."
    
    elif results == -2:
        return f"No {cmd_info['plural']} found for {args[0]}"
    
    elif type(results) == str:
        if results.startswith("-"):
            return f"{cmd_info['cmd']}: invalid option -- '{results[1:]}'"
        else:
            return f"Usage: {cmd_info['cmd']} [WORD] [OPTION]..."

    else:
        return results