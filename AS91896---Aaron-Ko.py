import easygui

tasks = {
    1: {
        'Title': 'Design Homepage',
        'Description': 'Create a mockup of the homepage',
        'Assignee': 'JSM',
        'Priority': '3',
        'Status': 'In Progress'
    },
    2: {
        'Title': 'Implement Login page',
        'Description': 'Create the Login page for the website',
        'Assignee': 'JSM',
        'Priority': '3',
        'Status': 'Blocked'
    },
    3: {
        'Title': 'Fix navigation menu',
        'Description': 'Fix the navigation menu to be more user-friendly',
        'Assignee': 'None',
        'Priority': '1',
        'Status': 'Not Started'
    },
    4: {
        'Title': 'Implement payment processing for the website',
        'Description': 'Implement payment processing for the website',
        'Assignee': 'JLO',
        'Priority': '2',
        'Status': 'In Progress'
    },
    5: {
        'Title': 'Create an About Us page',
        'Description': 'Create a page with information about the company',
        'Assignee': 'BDI',
        'Priority': '1',
        'Status': 'Blocked'
    }
}

team_member = {
    'JSM': {
        'Name': 'John Smith',
        'Email': 'John@techvision.com',
        'Tasks Assigned': [1, 2]
    },
    'JLO': {
        'Name': 'Jane Love',
        'Email': 'Jane@techvision.com',
        'Tasks Assigned': [4]
    },
    'BDI': {
        'Name': 'Bob Dillon',
        'Email': 'Bob@techvision.com',
        'Tasks Assigned': [5]
    },
}


def print_all():
    """Prints all tasks with their details."""
    output = ''
    for key, value in tasks.items():
        output += f'{key}\n'
        for aspect, information in value.items():
            output += f'{aspect} : {information}\n'
        output += '\n'
    easygui.msgbox(output)


def add_task():
    """Allows user to add a new task."""
    choices = ['Yes', 'No']
    init = easygui.buttonbox('Would you like to create a new task?', choices=choices)
    if init == 'Yes':
        try:
            id = max(tasks.keys()) + 1
        except ValueError:  # Handles the case when tasks dictionary is empty
            id = 1
        title = easygui.enterbox('What would you like the title to be?')
        tasks[id] = {'Title': title}
    else:
        pass


if __name__ == '__main__':
    while True:
        choices = ['Print all', 'Add task']
        selected_choice = easygui.buttonbox("Welcome to the Tasks database.\
        What would you like to do?", choices=choices)

        if selected_choice == 'Print all':
            print_all()
        elif selected_choice == 'Add task':
            add_task()
        else:
            break
