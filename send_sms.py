#!/usr/bin/python

from twilio.rest import Client
import sys
import os
import socket

default = 'unknown'

#TODO: use argparse
account_sid = default if len(sys.argv) < 2 else sys.argv[1]
auth_token = default if len(sys.argv) < 3 else sys.argv[2]
from_ = default if len(sys.argv) < 4 else sys.argv[3]
to = default if len(sys.argv) < 5 else sys.argv[4]

client = Client(account_sid, auth_token)

user = os.environ.get('PAM_USER', default)
rhost = os.environ.get('PAM_RHOST', default)
host = socket.gethostname()
service = os.environ.get('PAM_SERVICE', default)

message = client.messages \
                .create(
                     body= user + " logged in from " + rhost + " to " + host + " via " +service + ".",
                     from_= from_,
                     to= to,
                 )

print(message.sid)
