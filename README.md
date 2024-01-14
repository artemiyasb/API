# Project name
API Time and Cities

## Description
This repository consists from code for creating API that give us the current time in New-York and then give us the list of ten biggest cities of Armenia

## Installing and launch of app
1. Clone this repository in your PC
2. Install all the required dependencies, completing the command *pip install -r requirements.txt.*
3. Launch the app completing the command *python main.py*
   
## Usage

## Get the current time in New-York
- Request method: **GET**
- Path: **/time**

Will be returned in response the current time in New-York

### Get the list of biggest cities of Armenia
Request method: **GET**
Path: **/cities**

Will be returned the list of ten biggest cities in Armenia in *JSON* format that sorted by population

## Dependencies
- Python 3.6 or more
- Flask
- pytz

## Author

*Artem Vtyurin* - [vtyurin.artem@bk.ru]
