# Phillips-light-control
The best way for a programmer to control their lights. Uses the Phue library with speech recognition software to control your lights just like Google Home and Amazon Alexa!

# Step 1: Installing required libraries.
You will need to install the required libraries to ensure that the code runs. The libraries have all been compiled in a requirements document on the master branch. Open terminal or
your command prompt to the directory where you have stored the "requirements.txt" file and type the following command...
```pip install -r requirements.txt``` or if you are on a Unix based OS run ```pip3 install -r requirements.txt```

# Step 2: Creating a creds.py file.
You will need to create a creds.py file and store any credentials you may want to use within that file. The only required variable that be stored to run the program is
your Phillips Hue Bridge IP.
You can find this by connecting to your Phillips Hue app to your Bridge and finding out the IP. Once this is done you enter the value into the variable and ensure it is consistent
with the calls from other files.

# Step 3: Customize commands and configure to your liking!

I have left the controller.py file relatively open ended such that users can come in and change what they like and improve on the software. Enjoy!
