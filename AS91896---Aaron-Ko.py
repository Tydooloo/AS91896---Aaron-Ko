import easygui
tasks = {
    'T1': {
        'Title': 'Design Homepage',
        'Description': 'Create a mockup of the homepage',
        'Assignee': 'JSM',
        'Priority': '3',
        'Status': 'In Progress'
    },
    'T2': {
        'Title': 'Implement Login page',
        'Description': 'Create the Login page for the website',
        'Assignee': 'JSM',
        'Priority': '3',
        'Status': 'Blocked'
    },
    'T3': {
        'Title': 'Fix navigation menu',
        'Description': 'Fix the navigation menu to be more user-friendly',
        'Assignee': 'None',
        'Priority': '1',
        'Status': 'Not Started'
    },
    'T4': {
        'Title': 'Implement payment processing for the website',
        'Description': 'Implement payment processing for the website',
        'Assignee': 'JLO',
        'Priority': '2',
        'Status': 'In Progress'
    },
    'T5': {
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
        'Tasks Assigned': ['T1', 'T2']
    },
    'JLO': {
        'Name': 'Jane Love',
        'Email': 'Jane@techvision.com',
        'Tasks Assigned': ['T4']
    },
    'BDI': {
        'Name': 'Bob Dillon',
        'Email': 'Bob@techvision.com',
        'Tasks Assigned': ['T5']
    },
}

class task_management():
    def __init__(self, tasks):
        # making tasks a global object within the class
        self.tasks = tasks
        # output will allow the user to double check
    
    def add_task(self):
        output_verification = ''
        output = {}
        # using  list comprehension, it looks through all IDs, extracts numeric value
        # and max() finds the highest one then +1 as it is sequentially unique
        ID = max(int(key[1]) for key in self.tasks.keys()) + 1

        # adding returned values into variables
        # Check if any field is None (indicating user canceled)
        # exits the function if 'x' or cancel is pressed at anytime
        title = self.title()
        if title is None:
            return
        description = self.description()
        if description is None:
            return
        assignee = self.assignee()
        if assignee is None:
            return
        priority = self.priority()
        if priority is None:
            return
        status = self.status()
        if status is None:
            return
        
        # Add the task to output
        output[f'T{ID}'] = {
            'Title': title,
            'Description': description,
            'Assignee': assignee,
            'Priority': priority,
            'Status': status
        }
        
        # making the verification page look good (could have used an inlined for loop up it would be too long)
        for id, tasks in output.items():
            output_verification += f'\n{id}\n'
            for task_details, value in tasks.items():
                output_verification += f'{task_details} : {value}\n'

        # asking for verification
        verification = easygui.buttonbox(f'Are you sure you would like to add this task?:\n{output_verification}', choices = ['Yes','No'])

        if verification == 'Yes':
            # to add the output to the tasks dictionary we use update() function
            self.tasks.update(output)
        else:
            return
        # reset so that add task can be used again
        output = {}

    # make these in functions so that I dont have to reuse them for update function 
    def title(self):
        title = easygui.enterbox('Please enter your title')
        # making sure the dictionary is consistant
        return title

    def description(self):
        # adding desciption using the same method as the title
        description = easygui.enterbox('Please enter your description')
        return description 

    def assignee(self):
        # adding assignee using choicebox
        assignee = easygui.choicebox('Please choose your assignees code', choices = list(team_member.keys()))
        return assignee
    
    def priority(self):
        # adding priority rating using buttonbox
        priority = easygui.buttonbox('Please choose your priority', choices = ['1','2','3'])
        return priority

    def status(self):
        # adding status
        status = easygui.buttonbox('Please choose your Status', choices = ['Not Started','Blocked','In Progress', 'Completed'])
        return status

    def update_task(self):
        # adding the ID AND title of task for easier navigation
        choices = []
        info = ''
        for ID, details in tasks.items():
            # adding ID of given iteration
            info += ID
            for key, value in details.items():
                # this will add the actual title(value) into info
                if key == 'Title':
                    info += f' : {value}'
            choices.append(info)
            # resetting info to avoid tasks stacking up in one value of list
            info = ''
    
        task_to_update = easygui.choicebox("What task would you like to Update", choices = choices)
        # makes sure that the any NoneTypes can't cause errors
        if task_to_update == None:
            return
        task_section_to_update = easygui.choicebox("What part of the task would you like to update?", choices = ['Title','Description','Assignee','Priority','Status'])
        if task_section_to_update == None:
            return
        # get the task ID from task_to_update 
        # split at ':' get the first value [0] in the list and then strip white space out after
        task_id = task_to_update.split(':')[0].strip()


        # calling all functions based of task_section_to_update
        if task_section_to_update == 'Title':
            title = self.title()
            self.tasks[task_id]['Title'] = title

        if task_section_to_update == 'Description':
            description = self.description()
            self.tasks[task_id]['Description'] = description

        if task_section_to_update == 'Assignee':
            assignee = self.assignee()
            self.tasks[task_id]['Assignee'] = assignee

        if task_section_to_update == 'Priority':
            priority = self.priority()
            self.tasks[task_id]['Priority'] = priority

        if task_section_to_update == 'Status':
            status = self.status()
            # makes this task dissappear from the team members Tasks Assigned
            if status == 'Completed':
                # get the assignee code
                assignee_code = self.tasks[task_id]['Assignee']
                # remove the completed task from the assigned tasks list of the team member
                # dictionary.get(key, default_value)x2 (nested) for loops take to much code
                if task_id in team_member.get(assignee_code, {}).get('Tasks Assigned', []):
                    team_member[assignee_code]['Tasks Assigned'].remove(task_id)
                # Update the task status
                self.tasks[task_id]['Status'] = status
                

        

        

    def search(self):
        pass


    def generate_report(self):
        # initializing a counter 
        status_counts = {'Completed': 0, 'In Progress': 0, 'Blocked': 0, 'Not Started':0}
        # through all the task values
        for task in self.tasks.values():
            # adding counter to corresponding values in 'status'
            status_counts[task['Status']] += 1
            # creates a list (list comprehension) of status, count pairs and joins em as a str
        report_text = '\n'.join(f"{status} Tasks: {count}" for status, count in status_counts.items())
        easygui.msgbox(report_text)



    def print_all(self):
        output = ''
        for ID, task_details in self.tasks.items():
            output += f'\n{ID}\n'
            for attribute, value in task_details.items():
                output += f'{attribute} : {value}\n'
        output += '___________________________________________\n\nTeam Members\n'
        for code, details in team_member.items():
            output += f'\n{code}\n'
            for information, info in details.items():
                output += f'{information} : {info}\n'
        easygui.msgbox(output)



# Start
get = task_management(tasks)
get.add_task()
get.update_task()
get.print_all()