# 1 - Action Function
# Task - Store application log messages in a file

def write_log(message):
    with open(r'C:\Users\Shashi B Tripathi\OneDrive\Documents\Desktop\UpSkill\Python\Python_Learning\app.log', 'a') as file :
        file.write(message + '\n')

#write_log('App_Started')
#write_log('User logged in')
write_log('App_Stopped')


# 2 - Transformation Function
# Task - Clean an email and split it into user name and domain

def clean_and_split_email(email):
    cl_email = email.strip().lower()
    # shashi@gmail.com
    username, domain = cl_email.split('@')
    return {'username': username,
            'domain': domain}

#print(clean_and_split_email('shashi@gmail.com'))
print(clean_and_split_email('  SHASHI@gmail.com  '))  # Bad data


# 3 - Validation Function
# Task - Check if the password meets the minimum length of 8 characters

def is_valid_password(password):
    return len(password) >= 8

print(is_valid_password('abcd1234'))
print(is_valid_password('ab1234'))
print(is_valid_password(12345678))

# Task - Check if email has a basic valid format

def is_valid_email(email):
    return '@' in email and '.' in email

print(is_valid_email('sbt@gmail.com'))
print(is_valid_email('sbt@gmailcom'))
print(is_valid_email('sbtgmail.com'))

# 4 - Orchestrator Function
# Task - 

# Action Function
def write_log(message):
    with open(r'C:\Users\Shashi B Tripathi\OneDrive\Documents\Desktop\UpSkill\Python\Python_Learning\app.log', 'a') as file :
        file.write(message + '\n')

# Validation Function
def is_valid_email(email):
    return '@' in email and '.' in email

# Transformation Function

def clean_and_split_email(email):
    cl_email = email.strip().lower()
    username, domain = cl_email.split('@')
    return {'username': username,
            'domain': domain}

# Orchestrator Function
def process_user_email(email):
    write_log('Application Started')
    # user we must check if it is valid 
    # if it is not valid we log the problem 
    if not is_valid_email(email):
        write_log(f'Invalid Email Received: {email}')
    # if it is valid, we clean it and store structured info 
    else:
        clean_email = clean_and_split_email(email)
        write_log(f'Processed Email: {clean_email}')
    write_log('Application Stopped')

# We receive an email from a 
email = input('Please Enter Your Email: ')
process_user_email(email)