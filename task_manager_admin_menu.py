# ---- FUNCTIONS FOR THE LOGIN ----


# make a function named correct_username, which will check if the argument matches any of the keys in accounts. If it matches a key, it returns the argument, and if it doesn't match any, it repeatedly requests usernames until one does match a key and returns the correct username 
def correct_username(x):
    while (str(x) in accounts) == False:
        x = input('We have not found this username in our database. Please type in a correct username: ')
    if str(x) in accounts:
        y = x
    return y

# make a function named correct_password, which checks if the argument matches the value of the username key in the accounts dictionary. If it matches, it will return the argument, or else it will repeatedly request a password until it does match and return the correct password.
def correct_password(x):
    while (str(accounts[str(username)]).strip('\n') == str(x)) == False:
        x = input('You have not provided the correct password. Please try again: ')
    if accounts[str(username)][:].strip('\n') == str(x):
        y = x
    return y

# ---- FUNCTION FOR CHECKING THE FORMAT OF THE DUE DATE ------

def check_dd(w):
    z = True
    x = w
    while 1 == 1:
        if len(w) != 10:
            z = False
            break
        for y in (str(x[0:1] + x[3:4] + (x[6:9]))):
            while (y in str(1234567890)) == False:
                z = False
                break
            break
        while x[2] != '/' or x[5] != '/':
            z = False
            break
        break
    return z

# ---- BIG FUNCTION TO PRESENT THE MENU ----

# define a function to present the menu, so that the user can return to the menu when he has finished using the relevant option

def present_menu(x):

# The Menu
# request that the user type in one of the options and use a while loop to ensure they provide a valid option
    
    y = input('''\nSelect one of the following options by typing in the appropriate letter(s), with no spaces or punctuation on either side:
    
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()
    while (y in ['r', 'a', 'va', 'vm', 'e']) == False:
        y = input('You have made entered an invalid input. Please try again: ')

# Op 1 -  adding tasks

# if the user chooses a, let them add a task
    if y == 'a':

        # request a username, title, description of the dask, and due date, us
        u = input('Please provide the username of the person performing the task: ')
        u = correct_username(u)
        t = input('Please provide the relevant person\'s title: ')
        d = input('Please provide a description of the task: ')
        dd = str(input('Please provide the due date for the task, in the format dd/mm/yyyy : '))
        while check_dd(dd) == False:
            dd = input('please provide a date with the correct format: ')
        cd = '03/01/2023'
        com = 'n'.upper()
        task = [u, t, d, dd, cd, com]
        task_str = ''
        for x in task[:-1]:
            task_str += (f'{x}, ')
        task_str += str(task[-1] + '\n')
        tasks_file = open("tasks.txt", "a")
        tasks_file.write(task_str)
        tasks_file.close()

# Op 3 -  viewing all tasks

    elif y == 'va':
        # open the tasks file to read
        tasks_file = open("tasks.txt", "r")

        # set a variable 'all tasks' as a template for the display, and another variable to display which task we are iterating
        all_tasks = 'Tasks\n\n'
        task_index = 0
        # iterate through each line in the file, split the line where the text has ', ', and put the relevant strings into the relevant parts of the f-string display 
        for line in tasks_file:
            all_tasks += f'''
Task: {str(task_index)}
Username: {line.split(', ')[0]}
Title: {line.split(', ')[1]}
Task: {line.split(', ')[2]}
Date: {line.split(', ')[3]}
Date Due: {line.split(', ')[4]} 
Completed? {line.split(', ')[5]}   '''
            # increase the task index variable by 1 on each iteration
            task_index += 1
        # at the end of the for loop, print the display and close the file
        print(all_tasks)
        tasks_file.close()




# Op 4 - viewing the user's own tasks
# if the user chooses vm, let them view their tasks
                
    elif y == 'vm':
        # do the same thing as va, but only for those tasks where the username matches the username being used
        tasks_file = open("tasks.txt", "r")
        user_tasks = 'Yours Tasks \n\n'
        task_index = 0
        for line in tasks_file.readlines():
            if line.split(', ')[0] == username:
                user_tasks += f'''
Task: {str(task_index)}
Username: {line.split(', ')[0]}
Title: {line.split(', ')[1]}
Task: {line.split(', ')[2]}
Date: {line.split(', ')[3]}
Date Due: {line.split(', ')[4]} 
Completed? {line.split(', ')[5]}   '''
                task_index +=1
        print(user_tasks)
        tasks_file.close()


#  Op 5 - exit
    
    else:
        print("You have now left. Thank you")

    return y 

# ---- The end of the function 





# ---- FUNCTION TO PRESENT THE ADMIN'S MENU ----



def admin_menu(x):

# The menu - same again, but with the extra options to register users and view statistics
    
    y = input('''Select one of the following options by typing in the appropriate letter(s), with no spaces or punctuation on either side:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    s - view statistics
    e - exit
    : ''').lower()

    while (y in ['r', 'a', 'va', 'vm', 's', 'e']) == False:
        y = input('You have made entered an invalid input. Please try again: ')

# Op 1 -  registering new users

# if the user chooses r, let them register a new user
    if y == 'r':

        # request a username, a password, and a confirmation of the password
        reg_u= input('You have chosen to register a new account. Please type in the username you wish to use, with no spaces or punctuation on either side: ')
        reg_p = input('Please type in the password you would like to use,with no spaces or punctuation on either side: ')
        conf_p = input('And please confirm the password by typing it again, with no spaces or punctuation on either side: ')

        # use a while loop to prevent the user continuing if the passwords don't match 
        while reg_p != conf_p:
            reg_p = input('You have not typed in the password. Please type in your password again, with no spaces or punctuation on either side: ')
            conf_p = input('Please confirm the password: ') 

        # record the new account on a new line in user.txt
        user_file = open("user.txt", "a")
        user_file.write(f'{reg_u}, {reg_p}\n')
        user_file.close()



# Op 2 -  adding tasks - same again

    elif y == 'a':

        # request a username, title, description of the dask, and due date, us
        u = input('Please provide the username of the person performing the task: ')
        u = correct_username(u)
        t = input('Please provide the relevant person\'s title: ')
        d = input('Please provide a description of the task: ')
        dd = str(input('Please provide the due date for the task, in the format dd/mm/yyyy : '))
        while check_dd(dd) == False:
            dd = input('please provide a date with the correct format: ')
        cd = '03/01/2023'
        com = 'n'.upper()
        task = [u, t, d, dd, cd, com]
        task_str = ''
        for x in task[:-1]:
            task_str += (f'{x}, ')
        task_str += str(task[-1] + '\n')
        tasks_file = open("tasks.txt", "a")
        tasks_file.write(task_str)
        tasks_file.close()

# Op 3 -  viewing all tasks - same again

    elif y == 'va':
        tasks_file = open("tasks.txt", "r")
        user_tasks = 'Yours Tasks \n\n'
        task_index = 0
        for line in tasks_file.readlines():
            if line.split(', ')[0] == username:
                user_tasks += f'''
Task: {str(task_index)}
Username: {line.split(', ')[0]}
Title: {line.split(', ')[1]}
Task: {line.split(', ')[2]}
Date: {line.split(', ')[3]}
Date Due: {line.split(', ')[4]} 
Completed? {line.split(', ')[5]}   '''
                task_index +=1
        print(user_tasks)
        tasks_file.close()




# Op 4 - viewing the user's own tasks - same again
        
    elif y == 'vm':
        tasks_file = open("tasks.txt", "r")
        for line in tasks_file.readlines():
            if line.split(', ')[0] == username:
                ind_tasks = f'''
Task: {tasks_file.read()[3]}
Date: {tasks_file.read()[4]}
Date Due: {tasks_file.read()[5]}. 
Completed? {tasks_file.read()[6]}.   '''
                print(ind_tasks)
        tasks_file.close()
    
# op 5 - view statistics 
        
    elif y == 's':
        tasks_file = open("tasks.txt", "r")
        no_tasks = 0
        no_uncompl_tasks = 0
        for line in tasks_file:
            no_tasks += 1
            if line[-1].lower().strip('\n') == 'n':
                no_uncompl_tasks +=1
        tasks_file.close()
        user_file = open("user.txt", "r")
        no_users = 0
        user_already = []
        user_index = -1
        for line in user_file:
            user_already.append(line.split(', ')[0])
            user_index += 1
            if line.split(', ')[0] in user_already[:-1]:
                continue
            no_users += 1
        user_file.close()
        print(f''' 
Number of Tasks: {no_tasks}
Number of Tasks Left: {no_uncompl_tasks}
Number of Users: {no_users}  ''')

#  Op 6 - exit
    
    else:
        print("You have now left. Thank you")

    return y 

# ---- The end of the function 



#  *************** THE PROGRAMME ITSLEF ***************

# **** LOGIN ****

# make an empty dictionary named 'accounts' for usernames and passwords
accounts = {} 

# open user.txt 
user_file = open("user.txt", "r")

# for every line in user.txt, split the line into username and password, and put them into the accounts dictionary as a key: value pair
for line in user_file:
    accounts[str(line.split(', ')[0])] = str(line.split(', ')[1])

# request a username and operate on it with the correct_username function
username = input('Username: ')
# set the username to the result of correct_username 
username = correct_username(username)

# do the same for a password
password = input('Password: ')
password = correct_password(password)
user_file.close()



# **** MENU ****

# if the username is admin, present the admin menu

if username == 'admin':
    menu = admin_menu('x')

    # use a while loop to ask if the user wants to return to the menu, unless they have chosen to exit the programme
    while menu.lower() != 'e':
        to_menu = input('To return to the menu, press any key or press \'e\' to leave the programme. ')
        if to_menu.lower() == 'e':
            menu = 'e'
            print("You have now left. Thank you")
            continue
        menu = admin_menu('x')


# otherwise, present the normal menu

if username != 'admin':
    menu = present_menu('e')
    while menu.lower() != 'e':
        to_menu = input('To return to the menu, press any key, or press \'e\' to leave the programme. ')
        if to_menu.lower() == 'e':
            menu = 'e'
            print("You have now left. Thank you")
            continue
        menu = present_menu('x')


