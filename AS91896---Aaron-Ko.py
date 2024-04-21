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

# Overall template
class task_management():
    def __init__(self,tasks):
        """
        Initializing any relevant objects in the class.

            Tasks arguement made so that it can be used
            throughout the class.       
        """
        self.tasks = tasks
    
    def add_task(self):
        """
        Creates a new task with all relevant information and adds
        to the tasks dictionary.

            Calls 5 other user input functions and checks if they have 
            returned NoneType(if it does then return add_task with
            nothing).

            Inputs the other function returned values into output dict.

            Presents the options to user to double check if that is 
            really what the user wants.

        Adds to self.tasks dictionary.        
        """
        output_verification = ''
        output = {}
        '''
        Using  list comprehension, it looks through all IDs,
        extracts numeric value and max(), finds the highest one then 
        +1 as it is sequentitally unique.
        '''
        ID = max(int(key[1]) for key in self.tasks.keys()) + 1
        '''
        Adding returned values into variables and then
        checking if any value is returned None(indicating user canceled)
        the exits the function if 'x' or cancel is pressed at anytime.
        '''
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
        
        # Add the task to output.
        output[f'T{ID}'] = { # Making sure the dictionary is consistant.
            'Title': title,
            'Description': description,
            'Assignee': assignee,
            'Priority': priority,
            'Status': status
        }
        
        # Making the verification page look good.
        for id, tasks in output.items():
            output_verification += f'\n{id}\n'
            for task_details, value in tasks.items():
                output_verification += f'{task_details} : {value}\n'

        # Asking for verification.
        verification = easygui.buttonbox(f'Are you sure you would like to\
 add this task?:\n{output_verification}', choices = ['Yes','No'])

        if verification == 'Yes':
            # Adding output to tasks dictionary.
            self.tasks.update(output)
        else:
            return
        output = {} # Reset so that add task can be used again.

    '''
    All the inputs from user through these functions ('user input').
    '''
    def title(self):
        """
        Gets title input from user.
        Returns title.
        """
        title = easygui.enterbox('Please enter your title')
        return title

    def description(self):
        """
        Gets description input from user.
        Returns description.
        """
        description = easygui.enterbox('Please enter your description')
        return description 

    def assignee(self):
        """
        Gets assignee input from user.
        Returns assignee.
        """
        assignee = easygui.choicebox('Please choose your assignees code',
                                     choices = list(team_member.keys()))
        return assignee
    
    def priority(self):
        """
        Gets priority input from user.
        Returns priority.
        """
        priority = easygui.buttonbox('Please choose your priority',
                                     choices = ['1','2','3'])
        return priority

    def status(self):
        """
        Gets title status from user.
        Returns status.
        """
        status = easygui.buttonbox('Please choose your Status', 
            choices = ['Not Started','Blocked','In Progress', 'Completed'])
        return status
    
    def update_task(self):
        """
        Lets the user update any part of any task in the dictionary.

            Calls the user input functions again.

            Calls ID_title function to display with ID and title
            (clarity).

            If the user happens to change status to 'Completed', 
            It deletes that task from the team members task list.

        Updates self.tasks dictionary.  
        """
        task_id = self.ID_title() # Calling.
        if task_id == None: # Checking for None.
            return
        task_section_to_update = easygui.choicebox("What part of the task\
 would you like to update?", choices = ['Title','Description',
                                        'Assignee','Priority','Status'])
        if task_section_to_update == None:  # Checking for None.
            return
        '''
        Calling functions based on what the input form task_section_to
        update then adding them to self.tasks dictionary.
        '''
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
            # Deletes task from the team members Tasks Assigned.
            if status == 'Completed':
                # Get the assignee code.
                assignee_code = self.tasks[task_id]['Assignee']
                '''
                Remove the completed task from the assigned tasks list
                of the team member dictionary.get(key, default_value)x2
                (nested) because for loops take to much code.
                '''
                if task_id in team_member.get(assignee_code, {}).get(
                'Tasks Assigned', []):
                    team_member[assignee_code][
                        'Tasks Assigned'].remove(task_id)
                self.tasks[task_id]['Status'] = status  # Update.
                
    def search(self):
        """
        Allows user to search for any information of tasks or members.

            Calls ID_title() function for clarity (like in update).

            Displays all information form the returned value from 
            ID_title()
        """ 
        options = easygui.buttonbox('What would you like search for?',
                                     choices = ['Task','Team member'])
        
        '''
        Here I am simply using task comprehension to shorted the code.
        The easygui.msgboxes and the lines after just make it look nice 
        by iterating over the dictionarys and connecting list values.
        '''
        if options == 'Task':
            task_id = self.ID_title() # Calling.
            if task_id == None: # Checking None.
                return
            easygui.msgbox('\n'.join( f'{key} : {value}' 
            for id, details in self.tasks.items()
            for key,value in details.items()
            if id == task_id)) # Making it Look good.
        elif options == 'Team member':
            team_member_selected = easygui.choicebox(
            'Please select their code', choices = list(team_member.keys()))
            if team_member_selected == None: # Checking None.
                return
            easygui.msgbox('\n'.join(f'{key} : {value}' 
            for code, details in team_member.items() 
            for key,value in details.items() 
            if code == team_member_selected)) # Making it Look good.
        else:
            return # Checking None.
        
    def ID_title(self):
        """
        Displays a choicebox with the options being the ID AND Title
        for better readablity.

            Returns the user's chosen value.
        """
        # Adding the ID AND title of task for easier navigation.
        tasks_title = [f"{ID} : {details['Title']}" 
        for ID, details in self.tasks.items()]
        task_selected = easygui.choicebox("What task would you like select?",
                                          choices = tasks_title)
        if task_selected == None: # Checking None.
            return
        
        '''
        To Get the task ID from task_selected we split at ':'  and get
        the first value [0] in the list and then strip white space out 
        after.
        '''
        task_id = task_selected.split(':')[0].strip()
        return task_id # Returning the id num.


    def generate_report(self):
        """
        Generates a msgbox report on the number of tasks on each status
        (Completed, In progress... etc.).
        """
        # Initializing a counter.
        status_counts = {
            'Completed': 0,
            'In Progress': 0,
            'Blocked': 0,
            'Not Started':0
        }
        # Through all the task values.
        for task in self.tasks.values():
            # Adding counter to corresponding values in 'status'.
            status_counts[task['Status']] += 1
            # Creates a list of status, count pairs, joins as a str.
        report_text = '\n'.join(f"{status} Tasks: {count}"
        for status, count in status_counts.items())
        easygui.msgbox(report_text)

    def print_all(self):
        """
        Prints both the tasks and team member dictionarys fully 
        and readably.
        """
        output = '' # Initialize variable.
        for ID, task_details in self.tasks.items():
            output += f'\n{ID}\n'# Adding ID
            for attribute, value in task_details.items():
                output += f'{attribute} : {value}\n' # Adding details.
        # Making it look good.
        output += '________________________________________\n\nTeam Members\n'
        # Repeat for team members.
        for code, details in team_member.items():
            output += f'\n{code}\n'
            for information, info in details.items():
                output += f'{information} : {info}\n'
        easygui.msgbox(output)


'''
This is the main menu/loop. 
    Calls every function relevant to the choice of the user.
'''

get = task_management(tasks) # adding template to variable.
while True:
    # Initialize all the options.
    choices = [
        'All Information',
        'Add Task',
        'Update Task',
        'Search',
        'Report',
        'Exit'
    ]
    # Loop the logic.
    choice = easygui.buttonbox('What would you like to do?', 
                               choices = choices)
    if choice == 'All Information':
        get.print_all()
    elif choice == 'Add Task':
        get.add_task()
    elif choice == 'Update Task':
        get.update_task()
    elif choice == 'Search':
        get.search()
    elif choice == 'Report':
        get.generate_report()
    else: 
        break


