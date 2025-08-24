1. create an ec2 instance(ubuntu)
2. launch server and insstall all deendancies
   # Update packages
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip -y

# Install Git and unzip
sudo apt install git unzip -y

# Clone your repo or prepare a folder
git clone https://github.com/RakeshKanzariya2218/sample-python-app.git  
or 
mkdir ~/flask-app

3. add ssh keys in github secrets 
   run :- ssh-keygen
   add your private key in github secrets
4. cd <git repository>
5. install all dependencies in ec2 server & create venv and active venv 
     apt install python3.12-venv
     # 1. Create virtual environment
          python3 -m venv venv

     # 2. Activate it
          source venv/bin/activate

     # 3. Now install dependencies
          pip install -r requirements.txt
6. run your python app for testing
    python3 app.py
7. create github action workflows
    create file in your repositppry
   .github/workflows/deploy.yml
   {
  name: Deploy Flask App to EC2

on:
  push:
    branches:
      - main

jobs:
  deploy:
    name: Deploy Flask App via SSH
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Set up SSH
      run: |
        mkdir -p ~/.ssh
        echo "${{ secrets.EC2_SSH_KEY }}" > ~/.ssh/id_ed25519
        chmod 600 ~/.ssh/id_ed25519
        ssh-keyscan -H ${{ secrets.EC2_HOST }} >> ~/.ssh/known_hosts

    - name: Deploy to EC2 and restart Flask app
      run: |
        ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no ubuntu@${{ secrets.EC2_HOST }} << 'EOF'
          cd ~/sample-python-app

          # Pull the latest changes
          git pull origin main

          # Activate or create virtual environment
          if [ ! -d "venv" ]; then
            python3 -m venv venv
          fi
          source venv/bin/activate

          # Install/update dependencies
          pip install --upgrade pip
          pip install -r requirements.txt

          # Kill any previous app instance (safely)
          pkill -f "python3 app.py" || true

          # Run the app in background
          nohup python3 app.py > app.log 2>&1 &
        EOF

8. your server public ip:5000 hit in browser running application fine 



