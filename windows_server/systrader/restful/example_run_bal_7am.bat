rem You get curl if you install windows version of git and select the option "add git to PATH".

call activate.bat
python wait7am.py
sleep 120
curl --header "Content-Type: application/json" --data {\"accno\":\"1234567890\"} http://localhost:5000/balance
