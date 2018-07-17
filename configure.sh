#!/bin/bash

echo "sudo password maybe required to installed missing packages if any."

echo "Installing python3..."

command -v python3 >/dev/null 2>&1 || {

if command -v apt 2>&1; then
	sudo apt update && apt install python3
elif command -v dnf 2>&1; then
	sudo dnf update && dnf install python3
elif command -v pacman 2>&1; then
	sudo pacman -S --needed python3
elif command -v slackpkg 2>&1; then
	sudo slackpkg update && slackpkg install python3
else
	echo "[ERROR]: Please install python3 manually"
	exit
fi

}

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
	sudo pacman -S --needed python-pip3
elif command -v slackpkg 2>&1
then
	sudo slackpkg update && slackpkg install python-pip
else
	echo "[ERROR]: Please install python3-pip or pip3 manually"
	exit
fi

}

echo "Installing python dependencies..."
sudo pip3 install requests beautifulsoup4 lxml

if [ $? != 0 ]
then
	printf "\n"
	printf "%0.s*" {1..25}
	printf "\n"
	printf "Configuration FALIED\n"
	printf "requests or beautifulsoup4 modules failed to install"
	printf "%0.s*" {1..25}
	printf "\n"
	exit
fi

printf "\n"
printf "%0.s*" {1..25}
printf "\n"
printf "Configuration SUCCESSFUL\n"
printf "%0.s*" {1..25}
printf "\n"
exit
