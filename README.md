mitmproxy -s response.py --> Start the mitm proxy
./LT.exe --user {username} --key {acess_key} --proxy-port 8080 -v --shared-tunnel --proxy-host localhost --ingress-only --mitm
python proxy1.py ------> 
File gets created in ----------> api_responses.json
