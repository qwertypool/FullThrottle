# FullThrottle

It is deployed at Heroku and, 
the User JSON data can be found at:                https://full-throttle-labs.herokuapp.com/api/user/
  To add more activity periods, we can go to:    https://full-throttle-labs.herokuapp.com/api/activityperiod/



STEPS TO USE THIS REPOSITORY:
-----------------------------
 To use this repository, it can be cloned using -
                     git clone https://github.com/qwertypool/FullThrottle.git
 
 
 Then, please install all the packages from requirements.txt using the following steps: 
            1) cd to the directory where requirements.txt is located.
            2) activate your virtualenv.
            3) run: pip install -r requirements.txt in your shell.


The next step is, you give the command:  1)  py manage.py makemigrations
                                         2)  py manage.py migrate
 
 
 
After that, you can run this using the command:  py manage.py runserver
                                                           OR
                                                 python manage.py runserver         
