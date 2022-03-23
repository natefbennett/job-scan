# Job Scan

Are you tired of checking company career webpages every day/week to see if new jobs have been added? Have you wished that you could simply receive a text when the webpage changes? Look no further, this python script will automate the process for you! 

## Getting Started

### You Will Need
- Gmail Account (creating a new account is recommended)
- Raspberry Pi (or any system you can run continuously)

### Setting Up the Google Account

So first lets set up a new Gmail account. It will be responsible for sending the texts to your phone. It does NOT use the unofficial [Google Voice Python API](https://pypi.org/project/googlevoice/) as it is slightly broken at the time of writing this. Instead the code connects to the Gmail Account via SMTP and sends an email to the users gateway address. A gateway address is available for most popular mobile carriers and allows short messages to be sent via email and received by the target as an SMS text. A list of carrier domains can be viewed [here](https://www.fbbbrown.com/garmin-connect-iq/help-faq/app-help/runsafe/list-of-mobile-carrier-gateway-addresses/) or [here](https://avtech.com/articles/138/list-of-email-to-sms-addresses/).

1. Create a new Gmail Account. If you need help go [here](https://support.google.com/mail/answer/56256).
2. Enable 2-step verification, steps can be found [here](https://support.google.com/accounts/answer/185839). This will allow for you to generate an App Password.
3. Make an App Password for this program, for more information click [here](https://support.google.com/accounts/answer/185833).

### Populating the Google Sheet

Job Scan is designed to be utilize a Google Sheet to know what company career pages to track. This allows users to easily add/remove tracked URLs without having to directly connect with the Raspberry Pi. This Google Sheet MUST follow the format specified below or the program will not work.

Note: The column description cells at the top ("Name" and "Link") are case sensitive and must appear exactly as shown. Site names and links can be added beneath the corresponding "Name" and "Link" headers.

| Name            | Link                    |
|  -              | -                       |
| Example Company | www.example.com/careers |
| ...             |...                      |

This Google Sheet must be [public](https://support.google.com/docs/answer/183965) so that the Pi can access it without having to log in. This means we don't have to use the account we created earlier. It is recommended to use whatever account makes modifying the sheet easiest (I used my personal account).

### Setting up the Raspberry Pi

I will not go into too much detail on this part as there are already a lot of great guides out there. If you have never used a Raspberry Pi before go ahead and read the [docs to set it up](https://www.raspberrypi.com/documentation/computers/getting-started.html). If you know what you are doing and don't want to deal with a mouse and keyboard, check out [how to make the Pi headless](https://www.raspberrypi.com/documentation/computers/configuration.html#setting-up-a-headless-raspberry-pi).

### Getting the Code to Work

Open a terminal on the Pi and download the code for this project.

```
git clone https://github.com/natefbennett/job-scan.git
```

Navigate to the root directory of the repo:

```
cd job-scan
```

Run the setup shell script. This initializes two files that you will need for the code to work: db.json and secrets.py. It also invokes pip to install required python modules and adds a cron job to run the script once a day at 9:00 AM.

```
./install.sh
```

Once the script has finished creating the files, open secrets.py and fill in the placeholder values with your own details. 

The G_SHEET_KEY can be obtained from the URL of your publicly shared Google Sheet. For example if the link to the spreadsheet is `https://docs.google.com/spreadsheets/d/uxKDH9pj0S4Z9pHeVoPYN4Pv-NCzr9wh2Gyh96BvbN9Xx/edit#gid=0`, the G_SHEET_KEY would be this part: `uxKDH9pj0S4Z9pHeVoPYN4Pv-NCzr9wh2Gyh96BvbN9Xx`. The EMAIL is the Gmail account we set up earlier and used to generate the App Password.

### Configuring a Different Schedule with Cron (Optional)

Since the Pi is (usually) running a Linux operating system, we can use the popular scheduling utility: cron. The install script already set up a job for you, but if you would like to change it, run the command below.

```
crontab -e
```

Select your editor of choice for modifying the crontab file. Find the crontab line that looks like: `0 9 * * * python /home/pi/job-scan/scan.py`. This is the line that you want to modify. Refer to the [Wikipedia page](https://en.wikipedia.org/wiki/Cron) for more info on what values to set. 

### Congratulations!

Sit back, relax and enjoy peace of mind :)

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.