# FakeNewsDetector
The purpose of this project is to determine whether an article found online is presenting truthful information. It makes use of python's multitude of machine learning libraries as well as gui frameworks. It also makes use of a mySQL database so that people can see what has been checked recently and what the program decided was real or fake. Here are the steps on how this can be run on your Windows machine.

1) Clone this Repository

To start with, you'll need to clone this repository into some directory on your machine. If you have git installed on your machine, you can simply create a new folder somewhere convenient, then open it with command prompt and run "git clone https://github.com/Lestyn5053/FakeNewsDetector.git". Git will download the entire repository into that folder for you. If you do not have git installed, you can simply download the zip file and extract it into a new folder.

2) Install Python 3.8.5

I used Python 3.8.5 for this program. While any version of Python 3.8 should work fine, I cannot guarantee this as I developed it in 3.8.5 specifically. If you already have this version of Python installed, you can skip this step. Otherwise, you'll need to head over to "https://www.python.org/downloads/release/python-385/" and download Python. I personally used the "Windows x86-64 executable installer", but you can install using any method you like. If you are using the installer, make sure you have the option checked to add Python to your system's PATH.

2 1/2) Ensure Python & Pip Installed Correctly/At All

Just to make sure everything installed correctly, open up Command Prompt and run python --version. It should return Python 3.8.5. If this does not happen, go into the start menu and type "env". The first option should be "Edit the system environment variables". That's what you're looking for. You will then want to click on the button that says "Environment Variables" towards the bottom of the window. Under "System Variables", scroll down until you find "Path". Click on that and then click the "Edit" button. Confirm that the python directory is there. For me, that directory is "C:\Users\lbrooks\AppData\Local\Programs\Python\Python38". Additionally, that same directory with "\Scripts" at the end of it should be there. If they are not, add them, restart Command Prompt and try running python --version again. It should work now. You'll also want to run python -m pip install --upgrade pip to make sure you have the latest version of pip.

3) Install MySQL Server

This program also makes use of a MySQL Server. For simplicity's sake, the program uses a local database (although it could be expanded to use a remote database in the future if I decide I want to). For this, we'll need to install mySQL Server. If you already have this installed, you can skip this step. Otherwise, you'll need to head over to "dev.mysql.com/downloads". I personally chose to use the "MySQL Installer for Windows" as I had other things besides the server that I wanted to install, but you can also just download the "MySQL Community Server" if you prefer. However, the remaining instructions for this step will assume you chose the Windows Installer. When you get to the screen asking which products you want to install on your computer, select the latest version of MySQL Server 8.0. It will also ask you to set up a username and password for the server. You'll want to set both to "root", as that is what is specified in the code. Aside from that, the default settings can be left unchanged, although you may want to consider unchecking the "Start Server at System Startup" option unless you are okay with the server always running.

4) Install Python Libraries

This software makes use of many python libraries that will need to be installed for it to run. Open up Command Prompt and go to the project's directory. From there, all of the libraries required can be installed in this one line: "pip3 install requests kivy newspaper3k mysql-connector-python pandas numpy matplotlib seaborn scikit-learn". This may take a few minutes.

5) Build the Machine Learning Model

Before we can fact check articles, we need a model for the program to work with. For this reason, once all of the python libraries are installed, run "python buildModel.py". This will take a few moments, but will build the model and create the file "final_model.sav" within the program directory. 

6) Finally, Run the Program

To run this program, all you need to do is run "python main.py" within the command line from the program's directory. You should see the GUI pop open!