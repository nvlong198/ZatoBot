from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def get_gmail():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            # print((creds))

    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
    messages = results.get('messages', [])
    output = []
    for message in messages[:3]:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        msg_from = [ e for e in msg['payload']['headers'] if e['name'] == 'From' ][0]['value']
        msg_date = [ e for e in msg['payload']['headers'] if e['name'] == 'Date' ][0]['value']

        s = "`Người gửi: " + msg_from + '`\n' \
                + "`thời gian: " + msg_date + '`\n' \
                + msg['snippet'] + '\n' # ['snippet']
        output.append(s)
        # for i, e in enumerate(msg['payload']['headers']):
        #     print(i, e)
    return output