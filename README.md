# Trex helper in case you get pwnd
Will send you an SMS after a succesfull login (and logout).  
Not before, to prevent spamming you on each botnet attempt.  

## You will need a Twilio account and number
Or adapt it to your provider.

## Usage
Edit the PAM config file of your service, for example:  
/etc/pam.d/sshd  
Add the following:  
session    optional pam_exec.so /path/to/send_sms.py twilio-account-sid twilio-auth-token +from-phone-number +to-phone-number  

## Future feature
Reply to the SMS to kill the session if it is an intruder.  
(NOT SUPPORTED YET)  
