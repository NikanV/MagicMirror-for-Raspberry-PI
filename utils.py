import poplib
from email import parser

pop3server = 'mail.sharif.edu'
username = 'username@sharif.edu'
password = 'password'
pop3server = poplib.POP3_SSL(pop3server)
pop3server.user(username)
pop3server.pass_(password)
messages = [pop3server.retr(i) for i in range(1, len(pop3server.list()[1]) + 1)]
messages = ['\n'.join(map(bytes.decode, msg[1])) for msg in messages]
messages = [parser.Parser().parsestr(msg) for msg in messages]

for message in messages:
    print("subject: " + message['subject'])
    print("from: " + message['from'])
    print("date: " + message['date'])
pop3server.quit()
