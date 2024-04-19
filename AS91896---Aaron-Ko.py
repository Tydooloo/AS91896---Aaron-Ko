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
        self.tasks = tasks
    
    def add_task(self):
        # output will allow the user to double check
        output = {}
        # using and inline for loop, it looks through all IDs, extracts numeric value
        # and max() finds the highest one then +1 as it is sequentially unique
        ID = max(int(key[1]) for key in self.tasks.keys()) + 1

        # adding title
        title = easygui.enterbox('Please enter your title')
        # checking if the user hits 'x' or the cancel button
        if title is None:
            return
        # making sure the dictionary is consistant
        output[f'T{ID}'] = {'Title': title}

        # adding desciption using the same method as the title
        description = easygui.enterbox('Please enter your description')
        if description is None:
            return
        output[f'T{ID}']['Description'] = description
        
        # Add assignee with enterbox
        # While true so that the user can redo if they mess up
        # while True:
        #     assignee = easygui.enterbox('Please enter your assignees code')
        #     assignee = assignee.upper()
              # checking if assignee is found as one of the keys in the team_member dict  
        #     if assignee in team_member.keys():
        #         self.tasks[f'T{ID}']['Assignee'] = assignee
        #         break
        #     else:
        #         easygui.msgbox('Sorry, that code does not exist')

        # adding assignee using choicebox
        choices = list(team_member.keys())
        assignee = easygui.choicebox('Please choose your assignees code', choices = choices)
        if assignee is None:
            return
        output[f'T{ID}']['Assignee'] = assignee

        # adding priority rating using enterbox
        # while True:
              # using Value errors to make sure the code does not break even if the person types in a str or float
        #     try:
        #         priority = int(easygui.enterbox('Please enter your priority rating (1 - 3)'))
                  # This is the Boundary          
        #         if 1 <= priority <= 3:
        #             # Convert to string for consistency in the dictionary
        #             self.tasks[f'T{ID}']['Priority'] = str(priority)  
        #             break
        #         else:
        #             easygui.msgbox('Sorry, that priority is invalid')
        #     except ValueError:
        #         easygui.msgbox('Sorry, invalid input. Please enter a number.')   

        # adding priority rating using buttonbox
        priority = easygui.buttonbox('Please choose your priority', choices = ['1','2','3'])
        if priority is None:
            return
        output[f'T{ID}']['Priority'] = priority

        # adding status
        status = easygui.buttonbox('Please choose your Status', choices = ['Not Started','Blocked','In Progress'])
        if status is None:
            return
        output[f'T{ID}']['Status'] = status

        # making the verification page look good (could have used an inlined forloop up it woudl be too long)
        output_verification = ''
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

    def update_task(self):
        pass

    def search(self):
        pass

    def generate_report(self):
        pass

    def print_all(self):
        output = ''
        for ID, task_details in self.tasks.items():
            output += f'\n{ID}\n'
            for attribute, value in task_details.items():
                output += f'{attribute} : {value}\n'
        easygui.msgbox(output)


# Start
get = task_management(tasks)
get.add_task()
get.print_all()