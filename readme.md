# **Report Generator**
I just wanted to know how to deploy a site on heroku and the table is not so important. It can be seen in [https://reportapp-python.herokuapp.com/petroleum_report/]

This app generates the min, max, average for the interval of 5 years. The data has been fetched and added to the database. 

The data is put in three tables: sales, product and year. 

To run the server locally, I have added the 127.0.0.1 as the local host. 
And make sure to run all the modules required in the __requirements.txt__.

### **To run this locally, follow the below steps:**

Knowledge of python is required to run this. 

To install the required modules:

1. Go to folder containing the __requirements.txt__ file. (Use the cmd, powershell, or whatever terminal to do this)
2. Make sure you have installed python of the correct version (written in __runtime.txt__) or above, and is in the __PATH__. Refer to [python](https://www.python.org/) if you have not.
3. `pip install -r requirements.txt` in your terminal or cmd. 

 __Note__: If you want to do this in a virtual environment, make sure you have activated the environment and install the required files in it. (same instructions as above)

And after installation,

1. Make all the migrations by running `python manage.py makemigrations` command from the directory with the manage.py file.
2. Migrate the files using the `python manage.py migrate` command.
3. Run `python manage.py runserver`, if you want to run this app locally.



 

