# Trex helper in case you get pwnd
Will send you an SMS after a successful login (and logout).  
Not before, to prevent spamming you on each botnet attempt.  

## But post login is too late if I really got pwnd!
True, but the reasonable alternative is to require a reply SMS to allow login.  
Which, being over 3/4G, is less secure than requiring SSH key, or 2FA (e.g. google-authenticator).  
These are (some of) the tools you should be using to prevent getting owned  
This tool is meant to help you detect in reasonable time the (probably silent) failures should you get compromised.  

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
