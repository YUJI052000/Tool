import random
import string
import requests
from bs4 import BeautifulSoup

# List of Boy Names
boy_names = ['John', 'Alex', 'Noah', 'Liam', 'William', 'Mason', 'James', 'Benjamin', 'Jacob', 'Michael']

# List of Girl Names
girl_names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Aria', 'Mia', 'Emily', 'Amelia', 'Abigail']

# List of numbers for temp email
numbers = string.digits

# Generate random email
def generate_random_email():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(5)) + '@temp-mail.org'

# Get Facebook code from temp email
def get_facebook_code(email):
    try:
        # Make a GET request to temp email
        response = requests.get(f'https://temp-mail.org/en/view/{email}/')

        # Parse the response with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the email body
        email_body = soup.find('td', {'class': 'td_mail_body'})

        # Extract the Facebook code
        facebook_code = re.search(r'\d{6}', email_body.text).group()

        return facebook_code
    except:
        return None

# Main function to create a new Facebook account
def create_new_facebook_account(boy_names, girl_names):
    # Generate a random name
    name = random.choice(boy_names + girl_names)

    # Generate a random date of birth
    dob = '01-01-1990' # example

    # Generate a random email
    email = generate_random_email()

    # Create a session with the requests library
    session = requests.Session()

    # Get the Facebook page
    fb_homepage = session.get('https://www.facebook.com/')

    # Parse the Facebook page with BeautifulSoup
    soup = BeautifulSoup(fb_homepage.text, 'html.parser')

    # Get the initial form data from the page
    data = {}
    for input_tag in soup.find_all('input'):
        if input_tag.get('name') is not None:
            data[input_tag.get('name')] = input_tag.get('value')

    # Modify the form data with the random name, dob, and email
    data['firstname'] = name
    data['reg_email__'] = email
    data['month'] = dob.split('-')[0]
    data['day'] = dob.split('-')[1]
    data['year'] = dob.split('-')[2]

    # Make a POST request to the Facebook sign up page
    fb_signup = session.post('https://www.facebook.com/ajax/reg_status/', data=data)

    # Get the Facebook code from the temp email
    facebook_code = get_facebook_code(email)

    if facebook_code is not None:
        # Complete the account creation process
        data['reg_code__'] = facebook_code
        session.post('https://www.facebook.com/ajax/reg_status/', data=data)

        print(f'New Facebook account created: {name} ({email})')
    else:
        print('Failed to get Facebook code from temp email.')

# Call the function to create a new Facebook account
create_new_facebook_account(boy_names, girl_names)
