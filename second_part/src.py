########################################################################## Task 1 #########################################################################

import requests

def http_request():
    url = 'https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=1'
    
    # Headers to specify that we expect a JSON response
    headers = {
        'Accept': 'application/json'
    }
    
    try:
        # Send a GET request to the specified URL with the headers
        response = requests.get(url, headers=headers)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            json_response = response.json()
            
            # Check if the JSON response contains a 'success' message
            if 'success' in json_response:
                return json_response
            else:
                return {'error': 'Expected success message not found in response'}
        else:
            # Return an error message if the response code is not 200
            return {'error': f'Unexpected response code: {response.status_code}'}
    
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        return {'error': f'An error occurred: {str(e)}'}


########################################################################## Task 2 #########################################################################


'curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" \
     -H "Accept: application/json" \
     -H "Content-Type: application/json" \
     -L \
     https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=1'

########################################################################## Task 3 #########################################################################

import datetime
import calendar

def date_formatter(func):
    def wrapper(*args, **kwargs):
        # Call the decorated function to get the date
        date = func(*args, **kwargs)
        
        # Format the date as 'yyyy-mm/d'
        return date.strftime('%Y-%m/%d')
    
    # Return the formatted date
    return wrapper

@date_formatter
def first_day_of_last_week():
    # Get today's date
    today = datetime.date.today()
    year = today.year
    month = today.month
    
    # Find the last day of the current month
    last_day_of_month = calendar.monthrange(year, month)[1]
    
    # Create a date object for the last day of the month
    last_date_of_month = datetime.date(year, month, last_day_of_month)
    
    # Find the first day of the last week of the month
    first_day_of_last_week = last_date_of_month - datetime.timedelta(days=last_date_of_month.weekday())
    
    # Return the first day of the last week
    return first_day_of_last_week

########################################################################## Task 4 #########################################################################

class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap

########################################################################## Task 5 #########################################################################


class NotLoggedInException(Exception):
    pass


class LoginMetaClass(type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and attr_name != "login":
                dct[attr_name] = cls.wrap_method(attr_name, attr_value)
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def wrap_method(method_name, method):
        def wrapped_method(self, *args, **kwargs):
            if not self.logged_in:
                raise NotLoggedInException(f"Cannot call {method_name} when not logged in")
            return method(self, *args, **kwargs)
        return wrapped_method


class AccessWebsite(metaclass=LoginMetaClass):
    logged_in = False

    def login(self, username, password):
        if username == "admin" and password == "admin":
            self.logged_in = True

    def access_website(self):
        return "Success"


# Testing the updated class
if __name__ == "__main__":
    website = AccessWebsite()
    
    try:
        print(website.access_website())  # This should raise an exception
    except NotLoggedInException as e:
        print(e)  # Output: Cannot call access_website when not logged in
    
    website.login("admin", "admin")
    print(website.access_website())  # Output: Success
