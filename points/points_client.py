import os
import ast
import datetime

def pretty_num(num):
    out = f'{num:,}'
    return out

def send_to_log(message):
    log = open('./points/log.txt', 'r')
    content = log.read()
    log.close()

    log = open('./points/log.txt', 'w')
    log.seek(0,0)
    log.write(message + '\n' + content)
    log.close()

def output(store):

    file = open('README.md', 'w')

    output_str = "# Global Owen Points Rankings\n\n|Ranking|Name|Owen Points|\n| ----------- | ----------- | ----------- |\n"
    
    store = dict(sorted(store.items(), key=lambda item: item[1]))
    store = {k: store[k] for k in reversed(store)}

    for i, item in enumerate(store):
        output_str += f"|{i + 1}.|{list(store)[i]}|{pretty_num(store[item])}|\n"

    output_str += "\n## Report Someone or Request Points [Here](https://forms.gle/cc2Y95JU66t6gKew9).\n"
    output_str += "\n## !! Those Under -500 Owen Points will be [Executed Live](https://www.twitch.tv/will_of_owen) !!\n"
    output_str += "\n## Top Owen Updates Can be Found [Here](./blog).\n\n\n## Owen Points Log:\n"

    log = open('./points/log.txt', 'r')
    lines = log.readlines()
    for i in lines:
        output_str += i + '\n'
    log.close()

    file.write(output_str)
    file.close()
    
def save(store):
    file = open('./points/store.txt', 'w')

    file.write(str(store))

    file.close()

store = open('./points/store.txt', 'r')

scores = ast.literal_eval(store.read())

while True:

    scores = dict(sorted(scores.items(), key=lambda item: item[1]))
    scores = {k: scores[k] for k in reversed(scores)}
    
    for i in scores:
        print(i, ":", scores[i])

    options = ("edit", "add", "namechange", "remove", "exit")
    while True:
        choice = input(f"Input operation {options}: ").strip()
        if choice in options:
            break
        print("Enter valid option.")

    if choice == "exit":
        break
    elif choice == "remove":

        while True:
            remove_choice = input("Input person to remove: ")
            if remove_choice in scores:
                break
            print("Enter Valid option.")

        scores.pop(remove_choice)
        
        send_to_log(f'{datetime.datetime.now()} \| Remove \| {remove_choice}')

    elif choice == "add":

        while True:
            name = input("Input name to add: ")
            if name not in scores:
                break
            print("Person already exists.")
        
        scores[name] = 0
        send_to_log(f'{datetime.datetime.now()} \| Add \| {name}')
    elif choice == "edit":

        while True:
            edit_choice = input("Input person to edit: ")
            if edit_choice in scores:
                break
            print("Person does not exist.")

        while True:
            increment = input("Input points to change by: ").strip()
            try:
                increment = int(increment)
                break
            except ValueError:
                print("Enter an integer.")

        reason = input("Input reason: ")

        scores[edit_choice] += increment

        send_to_log(f'{datetime.datetime.now()} \| Edit Points \| {edit_choice} \| Change: {pretty_num(increment)} \| "{reason}"')
    elif choice == "namechange":

        while True:
            old_name = input("Input person to name change: ")
            if old_name in scores:
                break
            print("Person does not exist.")

        new_name = input("Input new name: ")

        scores[new_name] = scores[old_name]
        scores.pop(old_name)

        send_to_log(f'{datetime.datetime.now()} \| Name Change \| {old_name} \| Changed To: {new_name}')

    
    os.system("cls")

output(scores)
save(scores)

store.close()