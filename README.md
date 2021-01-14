# Riot Games Data Dump Analyzer
This is a collection of scripts that will help parse the JSON documents you're given when you request data from Riot Games.

*Warning* Currently WIP, no real functionality yet, can calculate league of legends total spend for a user
*Also if you clone this make sure you don't commit your own data to the repository!*

## Instructions

* Clone this repo to your computer `git clone https://github.com/zeke8402/riot-analyzer.git`
* Copy your data directory to the directory you cloned the repo to (by default, `riot-analyzer`)
* Create a new environment with pipenv in the same directory `pipenv --three`
* Install the necessary dependencies `pipenv run pip install -r requirements.txt`
* Run the analyzer `pipenv run python analyze.py`
* Follow the prompt!
