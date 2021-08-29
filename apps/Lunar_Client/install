#!/bin/bash
#Script created by oxmc
#Made for Lunar-Client by gl91306

#install modprobe if not already installed
if ! command -v modprobe >/dev/null;then
  
  if [ -f /usr/bin/apt ];then
    sudo apt update
    sudo apt install -y modprobe || echo "Failed to install modprobe."
  else
    error "Failed to find any package manager to install modprobe."
  fi
fi

#Run modprobe fuse
sudo modprobe fuse

cd
#Download client
wget https://github.com/gl91306/lunar/raw/master/lunarclient-2.7.3c-armv7l.AppImage
if [ ! -d ~/lwjgl3arm32 ]; then
    mkdir ~/lwjgl3arm32
fi
if [ ! -d ~/lwjgl2arm32 ]; then
    mkdir ~/lwjgl2arm32
fi
if [ ! -f jdk-8u251-linux-arm32-vfp-hflt.tar.gz ]; then
    wget https://github.com/mikehooper/Minecraft/raw/main/jdk-8u251-linux-arm32-vfp-hflt.tar.gz
fi
if [ ! -f jdk-16.0.1+9-jre.tar.gz ]; then
    wget https://github.com/gl91306/lunar/raw/master/jdk-16.0.1%2B9-jre.tar.gz
fi
if [ ! -f lwjgl3arm32.tar.gz ]; then
    wget https://github.com/mikehooper/Minecraft/raw/main/lwjgl3arm32.tar.gz
fi
if [ ! -f lwjgl2arm32.tar.gz ]; then
    wget https://github.com/mikehooper/Minecraft/raw/main/lwjgl2arm32.tar.gz
fi
if [ ! -d /opt/jdk ]; then
    sudo mkdir /opt/jdk
fi
sudo tar -zxf jdk-8u251-linux-arm32-vfp-hflt.tar.gz -C /opt/jdk
sudo tar -zxf jdk-16.0.1+9-jre.tar.gz -C /opt/jdk
tar -zxf lwjgl3arm32.tar.gz -C ~/lwjgl3arm32
tar -zxf lwjgl2arm32.tar.gz -C ~/lwjgl2arm32
sudo update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.8.0_251/bin/java 0
sudo update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk1.8.0_251/bin/javac 0
sudo update-alternatives --set java /opt/jdk/jdk1.8.0_251/bin/java
sudo update-alternatives --set javac /opt/jdk/jdk1.8.0_251/bin/javac
cd lwjgl2arm32
wget https://github.com/gl91306/lunar/raw/master/libwebp-imageio32.so
wget https://github.com/gl91306/lunar/raw/master/libgstreamer-lite.so
wget https://github.com/gl91306/lunar/raw/master/libjfxmedia.so
cd
cd lwjgl3arm32
wget https://github.com/gl91306/lunar/raw/master/libwebp-imageio32.so
wget https://github.com/gl91306/lunar/raw/master/libgstreamer-lite.so
wget https://github.com/gl91306/lunar/raw/master/libjfxmedia.so
cd
cd /opt/jdk/opt/jdk
sudo cp -r jdk-16.0.1+9-jre /opt/jdk
cd /opt/jdk
sudo rm -rf opt
cd
cd /opt/jdk/jdk1.8.0_251
sudo rm -rf jre
echo please wait a bit, as this step takes a bit
sudo apt-get install subversion
sudo svn checkout https://github.com/gl91306/lunar/trunk/jre
cd
sudo apt-get install unzip
wget https://github.com/gl91306/lunar/raw/master/javafx-sdk-17.zip
mkdir lunarassets
unzip javafx-sdk-17.zip -d $HOME/lunarassets
cd lunarassets
cd javafx-sdk-17
cd lib
rm -rf libjfxwebkit.so
wget https://github.com/gl91306/lunar/raw/master/libjfxwebkit.so
cd
#Change perms of Launcher
sudo chmod +x $HOME/lunarclient-2.7.3c-armv7l.AppImage

#Run launcher
cd
rm -rf jdk-8u251-linux-arm32-vfp-hflt.tar.gz
rm -rf jdk-16.0.1+9-jre.tar.gz
rm -rf javafx-sdk-17.zip
rm -rf lwjgl2arm32.tar.gz
rm -rf lwjgl3arm32.tar.gz
cd
cd lwjgl2arm32
rm -rf libopenal.so
cd
cp lwjgl3arm32/libopenal.so $HOME/lwjgl2arm32

#Add icon
cd
cd lunarassets
wget https://github.com/gl91306/lunar/raw/master/lunarclient.png
cd

#Then make menu button & desktop icon
echo "Creating a desktop entry for Lunar-Client..."
echo "[Desktop Entry]
Name=Lunar Client
Comment=Lunar Client for Rpi made by PiKATchu on Discord.
Exec=$HOME/lunarclient-2.7.3c-armv7l.AppImage
Icon=$HOME/lunarassets/lunarclient.png
Categories=Game;
Type=Application
Terminal=false" > "$HOME/.local/share/applications/Lunar-Client.desktop"

echo "[Desktop Entry]
Name=Lunar Client
Comment=Lunar Client for Rpi made by PiKATchu on Discord.
Exec=$HOME/lunarclient-2.7.3c-armv7l.AppImage
Icon=$HOME/lunarassets/lunarclient.png
Categories=Game;
Type=Application
Terminal=false" > "$HOME/Desktop/Lunar Client"

$HOME/lunarclient-2.7.3c-armv7l.AppImage
