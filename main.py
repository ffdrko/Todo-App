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
            for index, task in enumerate(todo_list):
                print(index, task)
        case 'edit':
            todo_num = int(input("Enter todo number: ")) - 1
            todo_list[todo_num] = input("Enter edited task: ") + "\n"
        case 'exit':
            break