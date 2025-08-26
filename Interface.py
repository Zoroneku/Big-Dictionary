from Dictionary import Dictionary
import Handlers
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# colorama lets terminal text be coloured
colorama_init()
dictionary = Dictionary()
done = False

def printList(list):
    for i,item in enumerate(list):
        print(f"{i+1}. {item}")

cmd_info = {"define": {"cmd":"define", "name":"define", "plural":"definitions",
                       "function":dictionary.define},
            "synonym": {"cmd":"syn", "name":"synonym", "plural":"synonyms",
                        "function":dictionary.getSynonyms},
            "antonym": {"cmd":"ant", "name":"antonym", "plural":"antonyms",
                        "function":dictionary.getAntonyms}}


while not done:
    # bit that appears at the start of each line in the terminal
    command_inp = input(f"{Fore.GREEN}wordy> {Style.RESET_ALL}")
    cmd_parts = command_inp.split()

    # if user just presses enter the while loop starts again
    if not cmd_parts:
        continue

    cmd = cmd_parts[0]
    args = cmd_parts[1:]

    match cmd:
        case "define":
            result = Handlers.handleCmd(cmd_info["define"], args)
            if type(result) == str:
                print(result)
            else:
                printList(result)

        case "syn":
            result = Handlers.handleCmd(cmd_info["synonym"], args)
            if type(result) == str:
                print(result)
            else:
                printList(result)

        case "ant":
            result = Handlers.handleCmd(cmd_info["antonym"], args)
            if type(result) == str:
                print(result)
            else:
                printList(result)

        case "all":
            print("ALL")

        case "clear":
            os.system('clear')

        case "exit":
            done = True

        case _:
            print(f"{cmd}: command not found")