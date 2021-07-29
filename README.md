# Instagram Simple Unfollowers
This is a Python program that shows the people that are not following you back on Instagram by using instaloader library.

## Installation and Running
As every Python program requires installing python to your computer, you need to do that for this software as well.  If you do not have Python installed on your computer,
you can click [here](https://python.org) and download it. 

After the installation of Python, open the terminal and write the following:
> pip install instaloader

Now, you are good to go. Next thing that you should do is to edit the .py file. You can do that by either using a text editor / IDE or right clicking on the .py file and choosing the
option Edit with IDLE. There are two lines that you have to edit, which are your username and password.

Last step is running the program. You can open the terminal up and reach the directory where the .py file is located, after that you can simply write the following and run the program:
> python InstagramSimpleUnfollowers.py

An alternative way to run the program is to press F5 while you are editing the .py file with IDLE. This will get the program run. 

## Troubleshooting
### Login error: Wrong Password.
If you get that exception by the program, you should review your username and password.

### Login error: Two Factor Authentication.
If you get that expection by the program, you should turn off two-factor authentication future on Instagram. You can do this by following the steps:
> Instagram -> Setting -> Security -> Two-Factor Authentication

Even though this does not look safe, security code that will be sent to you by Instagram, cannot be accessed via the Python console interface. 

### Instagram Login Alert Email
If you receive an email from Instagram that says that new login to Instagram from Chrome on Linux, you do not have to worry about it , It is still you. You can see that login location is same as where you run the program.
