1. create an ec2 instance(ubuntu)
2. launch server and insstall all deendancies
   # Update packages
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip -y

# Install Git and unzip
sudo apt install git unzip -y

# Clone your repo or prepare a folder
mkdir ~/flask-app

3. add ssh keys in github secrets 
   run :- ssh-keygen
   add your private key in github secrets
4. 
