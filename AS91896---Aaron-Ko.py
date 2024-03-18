tasks = {
    1: {
    'Title':'Design Homepage',
    'Desciption':'Create a mockup of the homepage', 
    'Assignee':'JSM',
    'Priotiy': '3',
    'status':'In Progress'
    },

    2: {
    'Title':'Implement Login page',
    'Desciption':'Create the Login page for the website', 
    'Assignee':'JSM',
    'Priotiy': '3',
    'status':'Blocked'
    }, 

    3: {
    'Title':'Fix navigation menu',
    'Desciption':'Fix the navigation menu to be more user-friendly', 
    'Assignee':'None',
    'Priotiy': '1',
    'status':'Not Started'
    },

    4: {
    'Title':'Implement payment processing for the website',
    'Desciption':'Implement payment processing for the website', 
    'Assignee':'JLO',
    'Priotiy': '2',
    'status':'In Progress'
    },

    5: {
    'Title':'Create an About Us page',
    'Desciption':'Create a page with information about the company', 
    'Assignee':'BDI',
    'Priotiy': '1',
    'status':'Blocked'
    }
}

team_member = {
    'JSM': {
        'Name':'John Smith',
        'Email':'John@techvision.com',
        'Tasks Assigned': [1,2]
    },
    'JLO': {
        'Name':'Jane Love',
        'Email':'Jane@techvision.com',
        'Tasks Assigned': [4]
    },
    'BDI': {
        'Name':'Bob Dillon',
        'Email':'Bob@techvision.com',
        'Tasks Assigned': [5]
    },
}

import easygui 



def print_all():
    '''literally just go through everything and print all'''
    output = ''
    # I will do this thing alot
    for key,value in tasks.items():
        output += f'{key}\n'
        for aspect, information in value.items():
            output += f'{aspect} : {information}\n'
        output += '\n'
    easygui.msgbox(output)

def add_task():
    output = ''
    choices = ['Yes','No']
    init = easygui.buttonbox('Would you like to create a new task?\
',choices = choices)
    if init == 'Yes': 
        id = 10
        title = easygui.enterbox('What would you like the title to be?')
        tasks[id]['Title'] = title
    else:
        pass

def add():
    pass

def delete():
    pass

def update():
    pass

def exit():
    pass


if __name__ == '__main__':
    while True:
        choices = [
            'Print all',
            'add task'
            ]
        selected_choice = easygui.buttonbox("Welcome to the Tasks database.\
        What would you like to do?", choices=choices)

        if selected_choice == 'Print all':
            print_all()
        elif selected_choice == 'add task':
            add_task()
        else:
            break
    
    




