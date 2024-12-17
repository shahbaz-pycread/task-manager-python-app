print('Task Manager App')
print('**********')
#1. Add a task
#2. Remove task
#3. Edit task
#4. Edit description
#5. Add description

# Create a function 'addTask' and pass a list of tasks that already 
# have been created by users as argument.

#Initial task list
tasks = []

# Create an empty dictionary for adding 'description'

descriptions = {}

# Auxiliary function => to display the task => Task displayer function
def displayTasks(all_tasks, descriptions):
    print('\nYour tasks: ')
    if len(all_tasks) <= 0:
        print('No Tasks yet..!!')
    else:
        for index, task in enumerate(all_tasks):
            print(f'{index+1} : {task} - {descriptions[task]}')

# Choose operation to perform
def newOperation(all_tasks, descriptions):
    operation = input("\nPress 'A' to add a task, 'E' to edit a task, 'R' to remove a task or 'F' to quit the application: ")
    if operation == 'A':
        addTask(all_tasks, descriptions)
    elif operation == 'E':
        editTask(all_tasks, descriptions)
    elif operation == 'R':
        removeTask(all_tasks, descriptions)
    elif operation == 'F':
        return
    else:
        newOperation(all_tasks, descriptions)
        
# Validate User Input
# Function to validate task number

def validTaskNumber(all_tasks,operation):
    task_number = input(f"Enter the task's number you want to {operation}: ")
    
    valid = False
    while not valid:
        try:
            number = int(task_number)
            valid = True
        except:
            task_number = input("Please enter valid task number: ")
    if not(0 < number <= len(all_tasks)):
        print("Task not found")
        validTaskNumber(all_tasks, operation)
    else:
        return number

# OPERATIONS      

# Add description
def addDescription(task, descriptions):
    description = input("Add description: ")
    descriptions[task] = description # description is the value for 'task' key.
    return descriptions
    
  
# Edit a task
def editTask(all_tasks, descriptions):
    task_number = validTaskNumber(all_tasks, 'edit')
    new_task = input('Edit task: ')
    
    all_tasks[task_number-1] = new_task
    addDescription(new_task, descriptions)
    print(f'Item with {task_number} has been edited.!')
    
    displayTasks(all_tasks, descriptions)
    newOperation(all_tasks, descriptions)

# Remove a task
def removeTask(all_tasks, descriptions):
    task_number = validTaskNumber(all_tasks, 'remove')
    #delete the description with the task number
    del descriptions[all_tasks[int(task_number)-1]]
    all_tasks.remove(all_tasks[int(task_number)-1])
    
    print(f'Item with task number {task_number} has been removed from the task list.')
    
    displayTasks(all_tasks, descriptions)
    newOperation(all_tasks, descriptions)

# Add a task
def addTask(all_tasks, descriptions):
    new_task = input('Add task: ')
    all_tasks.append(new_task)
    new_description = addDescription(new_task, descriptions)
    
    # print tasks
    displayTasks(all_tasks, new_description)
    
    
    newOperation(all_tasks, descriptions) # Ask for the new operation

# Start Application        
addTask(tasks, descriptions)     

