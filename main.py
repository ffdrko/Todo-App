print('--- Home ---')
print("""1- Add Todo
2- show Todo
3- Edit Todo
4- Complete Todo
5- Exit""")
print("-----------------")

todo_list = []

while True:
    user_action = input("Enter your option: ").strip()

    match user_action:
        case 'add':
            todo_task = input("Enter a Todo task: ") + '\n'
            todo_list.append(todo_task)
            print("Task is added in the list.")
        case 'show':
            for task in todo_list:
                print(task)
        case 'exit':
            break