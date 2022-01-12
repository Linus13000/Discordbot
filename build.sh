#!/bin/bash
python -m venv venv
source venv/bin/activate
venv/bin/python -m pip install --upgrade pip
pip install -r requirements.txt
echo
echo
echo
read -p "Token: " token
echo That worked!
destfile=token.txt
touch $destfile
if [ -f "$destfile" ]
then
    echo "$token" > "$destfile"
fi
echo Now you can start your bot
