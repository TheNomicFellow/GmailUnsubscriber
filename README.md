# Gmail Unsubscriber

**Gmail Unsubscriber** is a Python script designed to help users manage unwanted emails by extracting unsubscribe links from Gmail messages and generating an HTML file with clickable unsubscribe buttons. This project leverages the Gmail API to fetch emails from all labels, not just the inbox, and provides a user-friendly way to unsubscribe from unwanted senders.

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
git clone https://github.com/TheNomicFellow/GmailUnsubscriber.git
cd GmailUnsubscriber
```
### 2. Create and Activate a Virtual Environment (Optional but Recommended)

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
```
### 3. Install dependencies:
  ```bash
    pip install -r requirements.txt
  ```
 
### 4. Add your `credentials.json` file (not included in the repository for security).
 
### 5. Run the script:
  ```bash
    python main.py
  ```
 
 ## Usage
 
 - After running the script, an HTML file named `Unsubscribe_Links.html` will be created in the project directory.
 - Open the HTML file in a web browser to view a table of email senders and clickable "Unsubscribe" buttons.

   ![image](https://github.com/user-attachments/assets/08082a1c-e41d-40b5-89ae-ca557eb20680)

 
 ## Notes
 
 - Ensure that you have configured the Gmail API correctly and have valid credentials.
 - If the script doesn't find any unsubscribe links, check the email content and adjust the script as needed.
 
 ## Contributing
 
 Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
 
 ## License
 
 This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
 
 ## Contact
 
 For any questions or feedback, please open an issue in the repository or contact the project maintainer.
 
 ---
