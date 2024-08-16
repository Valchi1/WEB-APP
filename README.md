# WEB-APP
Educational Web app for storing course materials.


To run the web app

Navigate to classflow, and make sure any of the virtual environments are activated (class or chi) , class is python 3.10 and chi is python 3.11
 I needed 3.10 to host the web app

Then to run use “python manage.py runserver_plus --cert-file /Users/valchi/SSL-TLSv1/certs/server.crt”

To run normally you use python manage.py runserver but for security reasons I have forced this site to use https, ao the plus is is a link to the ssl/tls certificates .


Users, Passwords and Roles for Testing on Hosted site.
 
 
User	Password	Role	View site
valchi	1234	Admin	https://valchi.pythonanywhere.com/admin/login/?next=/admin/
Paul	Paulpaul1	Support staff/junior admin	https://valchi.pythonanywhere.com/account/login/
ada	Adaada11	student	Same with support staff
temi	Temitemi1	student	Same with support staff
gladys	Gladysgladys1	Teacher	Same with support staff
Table. Users, passwords and their roles on hosted site for testing.

User ‘ada’ uses 2fa , you can use that to test the functionality, but unfortunately you will not be able to log in as you will be unable to get the code . so to test students’ rights, use ‘temi’.
 

For more explanation, this is the link to the screencast  

Link to the screencast:
https://share.vidyard.com/watch/ndLcow7MALZjfu78TH7r6n?
 
This screencast does a little introduction and explains a bit about the code , the live system and how to run it, etc. This is not the official screencast.
 
 
