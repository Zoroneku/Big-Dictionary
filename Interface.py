from Dictionary import Dictionary
import Handlers
import os

dictionary = Dictionary()
done = False

def printList(list):
    for i,item in enumerate(list):
        print(f"{i+1}. {item}")


while not done:
    command_inp = input("wordy> ")
    cmd_parts = command_inp.split()
    # if user just presses enter the while loop starts again
    if not cmd_parts:
        continue

    cmd = cmd_parts[0]
    args = cmd_parts[1:]

    match cmd:
        case "define":
            definitions = Handlers.handleDefine(dictionary,args)
            match definitions:
                case -1:
                    print("Usage: define [WORD]")
                case -2:
                    print(f"No definitions found for {args[0]}")

        case "syn":
            if not args:
                print("Usage: syn [WORD]")
            else:
                synonyms = dictionary.getSynonyms(args[0])
                if not synonyms:
                    print(f"No synonyms found for {args[0]}")
                else:
                    if len(synonyms) > 10:
                        printList(synonyms[:11])
                    else:
                        printList(synonyms)

        case "ant":
            if not args:
                print("Usage: ant [WORD]")
            else:
                antonyms = dictionary.getAntonyms(args[0])
                if not antonyms:
                    print(f"No antonyms found for {args[0]}")
                else:
                    printList(antonyms)

        case "all":
            print("ALL")

        case "clear":
            os.system('clear')

        case "exit":
            done = True

        case _:
            print(f"{cmd}: command not found")