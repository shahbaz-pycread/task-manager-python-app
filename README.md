# Task Manager App

This is a simple command-line task manager application written in Python. It allows users to add, edit, remove tasks, 
and add or edit descriptions for each task. The application displays tasks with their corresponding descriptions and provides an interactive menu for task management.

## Features

- **Add Task**: Add a new task to the task list along with an optional description.
- **Edit Task**: Modify an existing task and its description.
- **Remove Task**: Remove a task from the list.
- **Task Description**: Add or edit descriptions for each task.
- **Display Tasks**: View all tasks and their associated descriptions.

## How It Works

- The program starts by prompting the user to add a task.
- After adding tasks, the user can choose to:
  - Add another task
  - Edit an existing task
  - Remove a task
  - Exit the application
- Tasks are displayed in a numbered list, and descriptions are shown next to each task.
- The app handles invalid input and provides prompts for the user to correct them.

## How to Run

### Requirements
- Python 3.x

### Running the Program
1. Clone the repository or download the script to your local machine:
    ```
    git clone https://github.com/your-username/task-manager.git
    ```

2. Navigate to the directory where the script is saved:
    ```
    cd task-manager
    ```

3. Run the program:
    ```
    python task_manager.py
    ```

4. Follow the prompts in the command line to add, edit, or remove tasks.

## Example Usage

```
  Add task: Buy groceries
  Add description: Purchase fruits, vegetables, and milk
  Your tasks:
    - 1: Buy groceries - Purchase fruits, vegetables, and milk

  Press 'A' to add a task, 'E' to edit a task, 'R' to remove a task or 'F' to quit the application: A
  Add task: Read a book
  Add description: Read "The Great Gatsby"
```
## Project Structure

- `task_manager.py`: The main Python script that runs the application.

## Future Enhancements

- Add persistence by saving tasks to a file (e.g., CSV or JSON) so tasks are not lost when the program ends.
- Implement a search functionality to find tasks by name or description.
- Add a graphical user interface (GUI) using libraries such as `Tkinter` or `PyQt`.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributions

Contributions are welcome! If you find any issues or have ideas for improvements, feel free to open a pull request or submit an issue.


