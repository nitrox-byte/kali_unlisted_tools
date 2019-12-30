#! /bin/bash
apt-get install libc6
apt-get install libcaca0
echo "For normal install requiere toilet-fonts"
echo "Download toilet-fonts..."
wget http://ftp.br.debian.org/debian/pool/main/t/toilet/toilet-fonts_0.3-1.2_all.deb
echo "Download toilet-fonts...OK"
echo "Install toilet-fonts..."
dpkg -i toilet-fonts_0.3-1.2_all.deb
echo "Install toilet-fonts...OK"
echo "Install base part.. OK"
echo "Download toilet..."
wget http://ftp.br.debian.org/debian/pool/main/t/toilet/toilet_0.3-1.2_amd64.deb
echo "Download toilet... OK"
echo "Download figlet..."
wget http://ftp.br.debian.org/debian/pool/main/f/figlet/figlet_2.2.5-3_amd64.deb
echo "Download figlet...OK"
echo "Install toilet..."
dpkg -i toilet_0.3-1.2_amd64.deb
echo "Install toilet...OK"
echo "Install figlet..."
dpkg -i figlet_2.2.5-3_amd64.deb
echo "Install figlet...OK"
echo "Installed all of them.. SUCCESS"
