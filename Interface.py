from Dictionary import Dictionary
import Handlers
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import readline

# colorama lets terminal text be coloured
colorama_init()

# initialises dictionary
dictionary = Dictionary()

def printList(list):
    for i,item in enumerate(list):
        print(f"{i+1}. {item}")

cmd_info = {"define": {"cmd":"define", "name":"define", "plural":"definitions",
                       "function":dictionary.define},
            "synonym": {"cmd":"syn", "name":"synonym", "plural":"synonyms",
                        "function":dictionary.getSynonyms},
            "antonym": {"cmd":"ant", "name":"antonym", "plural":"antonyms",
                        "function":dictionary.getAntonyms}}

done = False

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
        # defines a given word
        case "define":
            result = Handlers.handleCmd(cmd_info["define"], args)
            if type(result) == str:
                print(result)
            else:
                printList(result)

        # finds synonyms for a given word
        case "syn":
            result = Handlers.handleCmd(cmd_info["synonym"], args)
            if type(result) == str:
                print(result)
            else:
                printList(result)

        # finds antonyms for a given word
        case "ant":
            result = Handlers.handleCmd(cmd_info["antonym"], args)
            if type(result) == str:
                print(result)
            else:
                printList(result)

        # shows definitions, synonyms and antonyms
        case "all":
            print("Definitions:")
            result = Handlers.handleCmd(cmd_info["define"], args)
            if type(result) == str:
                print(result)
            else:
                printList(result)

            print("\nSynonyms: ")
            result = Handlers.handleCmd(cmd_info["synonym"], args)
            if type(result) == str:
                print(result)
            else:
                printList(result)

            print("\nAntonyms: ")
            result = Handlers.handleCmd(cmd_info["antonym"], args)
            if type(result) == str:
                print(result)
            else:
                printList(result)

        case "clear":
            os.system('clear')

        case "help":
            print("Type 'help' to see this list")
            print("type 'help name' to learn more about the function 'name'\n")
            print("define [WORD] [OPTION]...")
            print("syn [WORD] [OPTION]...")
            print("ant [WORD] [OPTION]...")
            print("all [WORD] [OPTION]...")
            print("clear")
            print("exit")

        case "exit":
            done = True

        case _:
            print(f"{cmd}: command not found")