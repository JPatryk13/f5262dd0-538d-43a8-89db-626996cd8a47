# Bit By Bit Assessment Project

## Setup

1. Activate virtual environment. E.g. for windows run the below in terminal
```
. vanv/Scripts/activate
```
2. Install requirements
```
pip install -r requirements.txt
```
3. Ensure everything is migrated
```
python src/manage.py makemigrations
python src/manage.py migrate
```
4. Populate database (WIP)
```
python src/manage.py populate
```
5. Register and log in via any tool of choice allowing to interact with APIs
