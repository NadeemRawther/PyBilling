# PyBilling
A billing software that can be used in super markets/hyper markets having following features enabled.
- Barcode scanning, billing and printing
- User management
- Stock management
- Reports generation

This software is developed in python and hosted as a local web application. Just need a Chrome/Firefox browser to get things going.

### System Requirements
- Linux/Windows
- Python >= 2.7
- Postgresql
- Chrome/Firefox

### Setup dev box
Navigate to a directory where you want to work on and get the latest code from git
```sh
cd \home\myApps
git clone https://github.com/HrMn/PyBilling.git
```
Move onto PyBilling folder, create a virtualenv here and install dependencies
```sh
cd PyBilling
#Need to install virtualenv if you don't have one
virtualenv flask 
#Install flask and required dependencies
flask/bin/pip install flask
flask/bin/pip install flask-httpauth
flask/bin/pip install flask-sqlalchemy
flask/bin/pip install psycopg2
```
Now, install and configure postgres
```sh
sudo apt-get -y install postgresql postgresql-contrib
#Create database under postgres user. If you wish to change this, edit PyBilling/app/app.cfg file
sudo su postgres
createdb billing
```


