import os
import pickle
import re
from base64 import urlsafe_b64decode
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Define the scope for accessing Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    """
    Authenticates the user and creates the Gmail API service object.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

def decode_base64_url(base64_url):
    """
    Decodes a base64 URL encoded string.
    """
    base64_str = base64_url.replace('-', '+').replace('_', '/')
    padding = len(base64_str) % 4
    if padding:
        base64_str += '=' * (4 - padding)
    return urlsafe_b64decode(base64_str).decode('utf-8')

def get_all_labels(service, user_id='me'):
    """
    Retrieves all labels for the user.
    """
    labels_response = service.users().labels().list(userId=user_id).execute()
    return [label['id'] for label in labels_response.get('labels', [])]

def find_unsubscribe_links(service, user_id='me', max_results=10):
    """
    Finds emails with unsubscribe links from all labels and extracts those links.
    """
    labels = get_all_labels(service)
    unsubscribe_links = {}

    for label in labels:
        print(f"Fetching messages from label: {label}")
        messages = service.users().messages().list(userId=user_id, labelIds=[label], maxResults=max_results).execute().get('messages', [])

        for message in messages:
            msg = service.users().messages().get(userId=user_id, id=message['id'], format='full').execute()
            msg_payload = msg.get('payload', {})
            
            # Extract email sender
            sender = next((header['value'] for header in msg_payload.get('headers', []) if header['name'] == 'From'), 'Unknown Sender')

            # Check for "List-Unsubscribe" header
            headers = msg_payload.get('headers', [])
            for header in headers:
                if header['name'].lower() == 'list-unsubscribe':
                    unsubscribe_url = header['value']
                    if "<" in unsubscribe_url and ">" in unsubscribe_url:
                        unsubscribe_url = unsubscribe_url.split("<")[1].split(">")[0]
                    unsubscribe_links[ sender ] = unsubscribe_url

            # Check for unsubscribe links in the HTML body
            parts = msg_payload.get('parts', [])
            for part in parts:
                if part['mimeType'] == 'text/html':
                    body = decode_base64_url(part['body']['data'])
                    matches = re.findall(r'href="([^"]*unsubscribe[^"]*)"', body, re.IGNORECASE)
                    for match in matches:
                        unsubscribe_links[ sender ] = match

    return unsubscribe_links

def create_html_file(unsubscribe_links, filename='Unsubscribe_Links.html'):
    """
    Creates an HTML file with a table of unsubscribe links styled with Tailwind CSS and buttons.
    """
    with open(filename, 'w') as file:
        file.write('<!DOCTYPE html>\n<html>\n<head>\n')
        file.write('<title>Unsubscribe Links</title>\n')
        file.write('<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">\n')
        file.write('</head>\n<body class="bg-gray-100 p-8">\n')
        file.write('<div class="container mx-auto bg-white p-6 rounded-lg shadow-lg">\n')
        file.write('<h1 class="text-3xl font-bold mb-4 text-gray-900">Unsubscribe Links</h1>\n')
        file.write('<table class="min-w-full bg-white border border-gray-200 rounded-lg overflow-hidden">\n')
        file.write('<thead class="bg-gray-800 text-white">\n<tr>\n<th class="py-3 px-4 text-left">Email Sender</th>\n<th class="py-3 px-4 text-left">Unsubscribe Link</th>\n</tr>\n</thead>\n')
        file.write('<tbody>\n')

        for sender, link in unsubscribe_links.items():
            file.write(f'<tr class="border-b border-gray-200">\n')
            file.write(f'<td class="py-3 px-4">{sender}</td>\n')
            file.write(f'<td class="py-3 px-4"><button onclick="window.open(\'{link}\', \'_blank\' )" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Unsubscribe</button></td>\n')
            file.write('</tr>\n')

        file.write('</tbody>\n</table>\n</div>\n')
        file.write('</body>\n</html>\n')

    print(f"HTML file saved as {filename}")

def main():
    # Step 1: Authenticate and create the Gmail API service
    service = authenticate_gmail()
    
    # Step 2: Fetch emails with unsubscribe links from all labels
    print("Fetching emails with unsubscribe links from all labels...")
    unsubscribe_links = find_unsubscribe_links(service)

    # Step 3: Create HTML file with unsubscribe links
    if unsubscribe_links:
        create_html_file(unsubscribe_links)
    else:
        print("No unsubscribe links found.")

if __name__ == '__main__':
    main()
