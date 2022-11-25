"""
# Todo List Exercise

Create an interactive, text-based todo list that has the following features:

- A user can add todos by entering them into the prompt
- A user can complete todos by entering the todo’s corresponding number
- A user can view a help screen by typing ‘h’ or ‘help’
- A user can quit by typing ‘q’ or ‘quit
"""
# https://plum-poppy-0ea.notion.site/Todo-List-Exercise-87d17f24feb74e799086acbb9c875719

print('====== Welcome to My TODO List ====='.upper())
print(""" _____         _
 |_   _|__   __| | ___  ___
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
""")


def display_todos(todos):
    cnt = 1
    for todo in todos:
        print(f'{cnt}) {todo}')
        cnt += 1
    print('*' * 20)


def display_help():
    print("")
    print('TODO LIST HELP')
    print('='*30)
    print("Type 'q' to quit")
    print("""To add a todo to the list, type it and hit enter
To complete a todo enter its number""")


def display_completed_todos(completed):
    print("Today you completed 5 todos:")
    for done in completed:
        print(f"* {done}")


todos = []
completed = []
r = ''

while r != 'q' and r != 'quit':
    r = input("Enter a command. Type 'h' for help: ")
    if r.isnumeric():
        r_int = int(r)

        if r_int > len(todos):
            print("The todo you selected does not exists! Choose another one.")
            display_todos(todos)
            continue
        completed.append(todos[r_int-1])
        todos.pop(r_int-1)
        display_todos(todos)
    elif r.lower() == 'h':  # Display help
        display_help()
    elif r.lower() == 'q':  # Display help
        display_completed_todos(completed)
        break
    else:  # push todo to the list
        todos.append(r)
        display_todos(todos)
    # ask for input
   # r = input("Enter a command. Type 'h' for help: ")
