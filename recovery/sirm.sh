echo [+] SIRM Stock Image Recovery Mode
echo Make sure that git, python3 and termcolor is installed
echo WARNING! ENTERING SIRM MODE MAY DOWNGRADE YOUR VERSION, IF THE HEXROID SYSTEM IS CORRUTED, DOWNLOAD THE SYSTEM ON OFFICIAL GITHUB PAGE, PRESS CTRL+C TO CANCEL THIS OPERATION
sleep 2
echo [+] Flashing new system... DO NOT PRESS CTRL + C WHILE INSTALLING THE HEXRAIL SYSTEM! THIS MAY ABORT THE INSTALLATION COMPLETELY!
git clone https://github.com/createlineageos1/hexrail
cd hexrail
echo The main Hexrail directory located at:
pwd
echo [+] Installation finished, booting to Hexrail system...
python3 main.py
