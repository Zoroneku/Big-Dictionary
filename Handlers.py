def handleDefine(dictionary,args):
    if not args:
        return -1
    else:
        definitions = dictionary.define(args[0])
        if not definitions:
            -2
        else:
            return definitions