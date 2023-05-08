# About

This application is comprised of a React frontend created using the Material UI component library and a stub API created using Django with view functions returning JsonResponse objects.

Upon page load, the application obtains a list of floors via API call, which it uses to dynamically populate the floor select dropdown. When the user selects a floor, another API call is made that returns the control panels on that floor and displays them. Another call is made when the user requests a floor by pressing a button, sending a request which returns the most appropriate elevator, along with its new position which is displayed.

![A screenshot of the application displaying a floor with 3 control panels](https://i.imgur.com/e9I0O4U.png)

# Issues / Limitations

* At present, the application only addresses the process of calling elevators to the user's current floor upon receiving a button-press request 

* There is no simulated delay when calling an elevator - the elevator's current floor is immediately set to the floor the user is on

* If the user is on floor x, the button for floor x is disabled. However, this is currently not handled in the backend

* If the user in on floor X, the corresponding button for floor X is disabled on the frontend, however this is not currently addressed on the backend


# Setup

First, clone the repository from https://github.com/nt294/Elevator-Task.git

## React frontend

To run the React frontend, the following steps need to be taken on a machine with a valid npm installation:

1. Navigate to the React frontend folder (where the `package.json` file is located)

2. Install the required dependencies:
   * $ npm install

3. Start the React development server:
   * $ npm start

The React development server should now be running on [http://localhost:3000](http://localhost:3000).
 

## Django backend

To run the backend on the Django development server, the following steps need to be taken on a machine with a valid Python 3 installation. Please note that the frontend is expecting this to be run on port 8000, which is the default. This will also create an admin account with the username `admin` and password `AdminPassword` for the admin panel:

1. (Recommended) Create and activate a Python virtual environment

2. Navigate to the backend directory containing the `manage.py` file and run the following commands:
   * $ pip install -r requirements.txt
   * $ python manage.py makemigrations
   * $ python manage.py migrate

3. Import the admin account and pre-configured database:
   * $ python manage.py loaddata admin_account.json
   * $ python manage.py loaddata db.json
 
4. Start the development server:
   * $ python manage.py runserver
  
The Django development server should now be running on http://localhost:8000.  


