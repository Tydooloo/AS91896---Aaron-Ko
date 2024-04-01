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
def print_all(tasks):
    """prints all tasks with their details"""
    output = ''
    for key, value in tasks.items():
        output += f'{key}\n'
        for aspect, information in value.items():
            output += f'{aspect} : {information}\n'
        output += '\n'
    easygui.msgbox(output)
def print_report(tasks):
    """Shows the number of tasks for each status"""
    # all needed variabled initialized 
    output = ''
    in_progress = ''
    blocked = ''
    not_started = ''
    # Iterate over tasks keys that we can extract the statuses from each one
    for key in tasks.keys():
        if tasks[key]['Status'] == 'In Progress':
            in_progress += f'Task {str(key)}, '
        elif tasks[key]['Status'] == 'Blocked':
            blocked += f'Task {str(key)}, '
        elif tasks[key]['Status'] == 'Not Started':
            not_started += f'Task {str(key)}, '
    # finalizing by inputting into output variable
    output += f'Tasks in progress:{in_progress}\n'
    output += f'Tasks blocked:{blocked}\n'
    output += f'Tasks not started:{not_started}\n'
    easygui.msgbox(output)  
def add_task(tasks, team_member):
    """add a new task."""
    output = {}
    # taking the highest value in the tasks dict keys and adding one for the new id (so that it is chronological
    id = max(tasks.keys()) + 1 if tasks else 1 # checking if the tasks dict is empty or not
    # Procceding to add all the necessery values in one by one
    title = easygui.enterbox('What would you like the title to be?')
    output[id] = {'Title': title}

    description = easygui.enterbox('Please add a description to this task')
    output[id]['Description'] = description

    # comfort for the user so that they do not have to redo the whole function again if they make a mistake
    while True:
        assignee = easygui.enterbox('Who would you like to assign this task to? Use their code')
        # these Nonetype if statements are everywhere to ensure the code does not break when exited
        if assignee == None:
            break
        # case sensitivity
        assignee = assignee.upper()
        # checking 
        if assignee in team_member:
            # Update the 'Tasks Assigned' list for the corresponding team member
            team_member[assignee]['Tasks Assigned'].append(id)
            break
        else:
            easygui.msgbox('Code not found, Please Try again')
    output[id]['Assignee'] = assignee
    while True:
        priority = easygui.integerbox('To what level of priority would you like to make it? From 1 - 3')
        if priority == None:
            break
        # valid inside of boundary
        if priority in range(1, 4):
            break
        else:
            easygui.msgbox('Invalid number, Please Try again')
    output[id]['Priority'] = priority
    choices = ['In Progress', 'Blocked', 'Not Started']
    status = easygui.buttonbox('To what status would you like to make it?', choices=choices)
    output[id]['Status'] = status
    # double checking with user
    authorization = easygui.buttonbox(f'Would you like to create the following new task?:\n{output}', choices=['Yes', 'No'])
    if authorization == 'Yes':
        # function to add it to the dictionary easily
        tasks.update(output)
    else:
        easygui.msgbox('This task will be deleted')
    # depended of the conditional statement right before, it will return a changed task dict or unchanged
    return tasks, team_member
def update_task(tasks, team_member):
    """update a task"""
    # for loop to append all the task ids into choices (task id to clarify)
    choices = [f'Task ID: {key}' for key in tasks.keys()]
    # get the selected task ID from the user
    task_to_edit = easygui.choicebox('Which task would you like to edit?', choices=choices, title='Task Update Selection')
    # in case the user pressed cancel
    if task_to_edit is not None:
        for i in task_to_edit: 
            # Attempt to get rid of the Task ID str
            try:
                task_to_edit = int(i)
            except ValueError:
                # everytime a letter comes up
                pass
    # If user exits and NoneType appears
    if not task_to_edit:
        easygui.msgbox('No tasks to update')
        return tasks, team_member
    # getting the keys in the nested dictionary
    edit_options_choices = list(tasks[task_to_edit].keys())
    edit_options = easygui.buttonbox('What part of the task would you like to edit? (please do not exit)', choices=edit_options_choices,
                                     title='Edit Options')
    # if the user attempts to exit
    if edit_options == None:
        pass
    else:
        new_value = easygui.enterbox(f"What would you like to change '{edit_options}' to?")
    # If assignee is changed, update team_member dictionary
    if edit_options == 'Assignee':
        # ensure that it is case sensitive by using upper()
        new_value = new_value.upper()
        old_assignee = tasks[task_to_edit][edit_options]
        if old_assignee != new_value:
            team_member[new_value]['Tasks Assigned'].append(task_to_edit)
            team_member[old_assignee]['Tasks Assigned'].remove(task_to_edit)
    elif edit_options == None:
        pass
    else:
        # adding the new_value into the 'edit_options' section of the nested dictionary
        tasks[task_to_edit][edit_options] = new_value
    # the new tasks and team member dictionaries are returned to their callers (variable in the main loop)
    return tasks, team_member
def search(tasks):
    criteria = easygui.enterbox("Search by criteria (title, assignee, priority, status)")
    if criteria is not None:
     # Check if the criteria is a valid key in the nested dictionary keys using the first task as an example
        if criteria.capitalize() not in tasks[1].keys():
            easygui.msgbox("Invalid criteria. Please try again.")
            return
        # specify the search value
        search_value = easygui.enterbox(f"Enter the {criteria.capitalize()} to search for:")
        # Initialize a flag to indicate if any matches were found
        found = False
        # Iterate over the tasks and print those matching the search criteria
        output = ''
        for task_id, task in tasks.items():
            if str(task.get(criteria.capitalize(), '')).lower() == str(search_value).lower():
                output += f'Task ID: {task_id}\n'
                for aspect, information in task.items():
                    output += f'{aspect} : {information}\n'
                output += '\n'
                found = True
        # if no matches were found, display a message
        if not found:
            easygui.msgbox("No tasks found matching the search criteria")
        else:
            easygui.msgbox(output)
while True:
    choices = ['Print all','Print report', 'Add task', 'Update task', 'Search', 'Exit']
    selected_choice = easygui.buttonbox("Welcome to the Tasks database. What would you like to do?", choices=choices)
    if selected_choice == 'Print all':
        print_all(tasks)
    elif selected_choice == 'Print report':
        print_report(tasks)
    elif selected_choice == 'Add task':
        # added these variables to the caller because the user makes real changes to the actually dictionaries 
        tasks, team_member = add_task(tasks, team_member)
    elif selected_choice == 'Update task':
        tasks, team_member = update_task(tasks, team_member)
    elif selected_choice == 'Search':
        search(tasks)
    else:
        break