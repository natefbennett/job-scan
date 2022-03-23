#! /bin/bash

BASEDIR=$(cd $(dirname $0) && pwd)

echo "!!! WARNING !!! Install script will overwrite db.json and secrets.py! 
Are you sure you want to continue? (Y/n)"

read answer

if [ "$answer" != "${answer#[Yy]}" ] ; then
    echo "{}" > $("${BASEDIR}/db.json")
    echo "G_SHEET_KEY  = 'uxKDH9pj0S4Z9pHeVoPYN4Pv-NCzr9wh2Gyh96BvbN9Xx'
EMAIL        = 'example@gmail.com'
APP_PASSWORD = 'password'
PHONE_NUMBER = '0000000000'
CARRIER      = 'verizon'" > $("${BASEDIR}/secrets.py")
else
    exit
fi

# install python dependencies
pip install -r $("${BASEDIR}/requirements.txt")

# set up a cron job to run scan every day
(crontab -l ; echo "0 9 * * * python ${BASEDIR}/scan.py")| crontab -