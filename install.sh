#! /bin/bash

echo "!!! WARNING !!! Install script will overwrite db.json and secrets.py! 
Are you sure you want to continue? (Y/n)"

read answer

if [ "$answer" != "${answer#[Yy]}" ] ; then
    echo "{}" > db.json
    echo "G_SHEET_KEY  = 'uxKDH9pj0S4Z9pHeVoPYN4Pv-NCzr9wh2Gyh96BvbN9Xx'
EMAIL        = 'example@gmail.com'
APP_PASSWORD = 'password'
PHONE_NUMBER = '0000000000'
CARRIER      = 'verizon'" > secrets.py 
else
    exit
fi