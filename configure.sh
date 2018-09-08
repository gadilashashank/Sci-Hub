# Configuration script for GNU/LINUX systems
# Should Work for any distro which uses
# apt, dnf, pacman or slackpkg

#!/bin/bash

# User information about need of sudo priviledges
echo "sudo password maybe required to installed missing packages if any."

# User information before installing python3
echo "Installing python3..."

# Check if python3 is already installed or install it.
command -v python3 >/dev/null 2>&1 || {

# For apt based systems
if command -v apt 2>&1; then
	sudo apt update && apt install python3
# For dnf based systems
elif command -v dnf 2>&1; then
	sudo dnf update && dnf install python3
# For pacman based systems
elif command -v pacman 2>&1; then
	sudo pacman -S --needed python3
# For slackpkg based systems
elif command -v slackpkg 2>&1; then
	sudo slackpkg update && slackpkg install python3
# Error message for other systems. :(
# Create a pull request if you want to support your distro
else
	echo "[ERROR]: Please install python3 manually"
	exit
fi

}

# Similar as above for pip3
echo "Installing pip3..."

command -v pip3 > /dev/null 2>&1 || {
if command -v apt 2>&1
then
	sudo apt update && apt install python3-pip
elif command -v dnf 2>&1
then
	sudo dnf update && dnf install python3-pip
elif command -v pacman 2>&1
then
	sudo pacman -S --needed python-pip
elif command -v slackpkg 2>&1
then
	sudo slackpkg update && slackpkg install python-pip
else
	echo "[ERROR]: Please install python3-pip or pip3 manually"
	exit
fi

}

# Run pip3 for installing external python dependencies
echo "Installing python dependencies..."
pip3 install requests beautifulsoup4 lxml

# If exit code NOT 0 then print ERROR
if [ $? != 0 ]
then
	printf "\n"
	printf "%0.s*" {1..60}
	printf "\n"
	printf "Configuration FALIED\n"
	printf "requests or beautifulsoup4 modules failed to install"
	printf "\n"
	printf "%0.s*" {1..60}
	printf "\n"
	exit
fi

# Else success
printf "\n"
printf "%0.s*" {1..25}
printf "\n"
printf "Configuration SUCCESSFUL\n"
printf "%0.s*" {1..25}
printf "\n"
exit
