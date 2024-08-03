# Email Unsubscriber

**Email Unsubscriber** is a Python script designed to help users manage unwanted emails by extracting unsubscribe links from Gmail messages and generating an HTML file with clickable unsubscribe buttons. This project leverages the Gmail API to fetch emails from all labels, not just the inbox, and provides a user-friendly way to unsubscribe from unwanted senders.

## Features

- **Fetches Emails from All Labels**: Retrieves messages from all labels in your Gmail account.
- **Extracts Unsubscribe Links**: Finds unsubscribe links from email headers and HTML bodies.
- **Generates HTML File**: Creates a styled HTML file with buttons to unsubscribe from emails.
- **User-Friendly Interface**: Includes Tailwind CSS for a modern and responsive design.

## Requirements

- **Python 3.x**: Ensure you have Python 3 installed on your system.
- **Gmail API Enabled**: Follow the [Gmail API quickstart guide](https://developers.google.com/gmail/api/quickstart/python) to enable the Gmail API and obtain `credentials.json`.

## Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
