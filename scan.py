import json
import secrets as s
from collections import defaultdict
import pandas
from pathlib import Path
import requests
import sms

base_path = Path(__file__).parent
db_path = (base_path / "./db.json").resolve()

# read in database file to runtime memory
with open(db_path, 'r') as db_file:
    prev_scan_data = json.load(db_file)

db = defaultdict(int, prev_scan_data) # set to 0 initially by calling int

# get google sheet
url = f'https://docs.google.com/spreadsheets/d/{s.G_SHEET_KEY}/export?gid=0&format=csv'
df = pandas.read_csv(url, on_bad_lines='skip') # yields pandas DataFrame

changes_found = False

# loop though companies
for company in df.itertuples(index=False):

    # get length of site content
    content_len = len(requests.get(company.Link).content)

    # check if new entry (career page link added after last scan)
    if company.Name not in db:

        # send text to user that site has been added
        print(f'{company.Name} added! Sending text...')
        sms.send(f'{company.Name} added to database! Click the link to view!\n{company.Link}')

        db[company.Name] = content_len

    # if career page length different from last time
    # default dict will create if entry does not exist with length of 0
    elif db[company.Name] != content_len:
        
        changes_found = True
        print(f'{company.Name} has changed! Sending text...')

        # send text to user that site has changed
        sms.send(f'Alert: {company.Name} career page has changed. Click the link to view!\n{company.Link}')

        # update database with new length for that page
        db[company.Name] = content_len

if changes_found:
    # replace database file with runtime memory
    with open(db_path, 'w') as db_file:
        json.dump(db, db_file, indent=4)
else:
    sms.send(f'I scanned {len(db.keys())} career pages and there are no job updates to report! Have a nice day :)')
