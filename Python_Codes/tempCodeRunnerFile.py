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