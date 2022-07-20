#!/bin/bash

echo "Installing Runelite..."

sudo apt update
sudo apt install default-jdk

wget https://github.com/runelite/launcher/releases/download/2.4.2/RuneLite.jar

mkdir Runelite
mv RuneLite.jar Runelite
cd Runelite && chmod +x RuneLite.jar

echo "[Desktop Entry]
Name=Runelite
Comment=Old school runescape client!
Exec=java -jar /Runelite/RuneLite.jar
Icon=$HOME/RuneLite/runelite.png
Categories=Game;
Type=Application
Terminal=false" > "$PW_APPS/Runelite.desktop"
