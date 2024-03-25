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
    output = {}
    id = 0
    choices = ['Yes','No']
    init = easygui.buttonbox('Would you like to create a new task?\
',choices = choices)
    if init == 'Yes':
        for key in tasks.keys():
            if key > id:
                id = key
        id += 1
        output[id] = {}
        title = easygui.enterbox('What would you like the title to be?')
        output[id]['Title'] = title
 
        description = easygui.enterbox('Please add a desciption to this task')
        output[id]['Desciption'] = description

        assignee = easygui.enterbox('Who would you like to assign this\
 task to? Use their code')
        assignee = assignee.upper()
        while True:
            if assignee in team_member.keys:
                break
            else:
                easygui.msgbox('Code not found, Please Try again')
        output[id]['Assignee'] = assignee

        priority = easygui.integerbox('To what level of priority would\
 you like to make it? From 1 - 3')
        while True:
            if priority in range(1,3):
                break
            else:
                easygui.msgbox('Invalid number, Please Try again')
        tasks[id]['Priority'] = priority

        choices = ['In Progress','Blocked','Not Started']
        status = easygui.buttonbox('To what level of priority would\
 you like to make it?', choices = choices )
        tasks[id]['Status'] = status
        

# just here how show the final deleted movies thing

def update_task():
    '''similar to add just methodically going thorugh each one'''
    output  = ''
    choice = []
    edit_options_choices = []
    for key, value in Movies.items():
        choice.append(key)

    movie_to_edit = easygui.buttonbox('What movie would you like to edit?'\
    , choices = choice, title = 'Movie Update selection')

    for key1, value in Movies[movie_to_edit].items():  
        edit_options_choices.append(key1)

    edit_options = easygui.buttonbox('What part of the movie would\
 you like to edit?', 
    choices = edit_options_choices, title = 'Edit Options')

    for key, value in Movies[movie_to_edit].items():  
        if key == edit_options:
            new_value = easygui.enterbox(f"What would you like to\
 change '{key}' to?")
            Movies[movie_to_edit][key] = new_value



        

        


while True:
    choices = ['Print all', 'Add task','Update task', 'Exit']
    selected_choice = easygui.buttonbox("Welcome to the Tasks database.\
    What would you like to do?", choices=choices)

    if selected_choice == 'Print all':
        print_all()
    elif selected_choice == 'Add task':
        add_task()
    elif selected_choice == 'Update task':
        update_task()
    else:
        break