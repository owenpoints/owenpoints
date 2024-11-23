import os
import ast
import datetime

user = open('username.txt', 'r')
username = user.read()
user.close()

def show_posts(store):
    for i in store:
        print(i)

def pause():
    input("Press Enter to continue...")

def output(store):

    store = dict(reversed(list(store.items())))

    file = open('README.md', 'w')

    output_str = "# Top Owen Updates\n### [Back](https://owenpoints.github.io) to Owen Points Leaderboard\n"
    
    for i, item in enumerate(store):
        output_str += f'{store[item].split("|")[0] + "|" + store[item].split("|")[1]}| [{item}](./posts/{item}.md)\n\n'
        




    file.write(output_str)
    file.close()
    
def save(store):
    file = open('store.txt', 'w')

    file.write(str(store))

    file.close()

store = open('store.txt', 'r')

posts = ast.literal_eval(store.read())

while True:

    options = ("post", "delete", "list", "read", "exit")
    while True:
        choice = input(f"Input operation {options}: ").strip()
        if choice in options:
            break
        print("Enter valid option.")

    if choice == "exit":
        break
    elif choice == "delete":
        
        show_posts(posts)

        while True:
            remove_choice = input("Input post to remove: ")
            if remove_choice in posts:
                break
            print("Enter Valid option.")

        posts.pop(remove_choice)
        os.remove(f"posts\{remove_choice}.md")

    elif choice == "post":

        while True:
            title = input("Input title of post: ")
            if title not in posts:
                break
            print("That title already exists.")

        while True:
            contents = input("Input post contents: ")
            if not "\|" in contents:
                break
            print("Post cannot contain '\|' (backslash pipeline).")

        posts[title] =  f'{datetime.datetime.now()} \| {username} \| {contents}'

        temp = open(f'posts\{title}.md', 'w')
        temp.write(f'# {title}\n{posts[title]} \n\n Click [Here](../) to Go Back')
        temp.close()

    
    elif choice == "list":
        show_posts(posts)
        pause()
    
    elif choice == "read":
        show_posts(posts)        
        
        while True:
            title = input("Input post title: ")

            if title in posts:
                break
        
            print("Post does not exist.")
        
        print(f"Title: {title}\nContents:\n{posts[title]}")
        pause()

    """
    elif choice == "edit post":
        show_posts(posts)

        while True:
            title = input("Input post title: ")

            if title in posts:
                break
        
            print("Post does not exist.")
        
        new_contents = input("Input new post contents: ")

        posts[title] = f"{new_contents}\n\nEdited {datetime.datetime.now()}\n"
    """

    os.system("cls")

output(posts)
save(posts)

store.close()