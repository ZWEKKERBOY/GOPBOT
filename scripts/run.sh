#Runs the server in the background while still displaying output
#Make sure there is a config.json file first
if [ -f config.json ]; then 
node server.js &
disown
else
#Warn the user
echo "\033[0;31mNo config file found! Please create one using the template provided.\033[0m"
fi