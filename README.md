# PushStocks v1.1 release

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

**PushStocks** *is a self-hosted script* that uses the python-binance wrapper to check crypto prices in Binance and notifies using PushBullet when a price falls under or passes a threshold.

# Requirements:
* [Python3](https://www.python.org)
* [python-binance](https://github.com/sammchardy/python-binance)
* [PushBullet](https://www.pushbullet.com)

# Installation:
1) Install Python3 (Check the box for **add to os environmental variable** for Windows)
2) Download/clone this repo to a directory. *Optional* Clone this repo using git to keep it updated.
3) Navigate to that directory using `cd` and type `pip install -r requirements.txt` in the terminal.
4) Create an account at [PushBullet](https://www.pushbullet.com) and download the app for iOS.
5) At [PushBullet](https://www.pushbullet.com), goto `Settings > Create Access Token` and save the key.
6) Create an account at [Binance](https://www.binance.com), goto `Account Profile > API > API Settings` and save the key and secret.
7) Open config.json and input the keys between the quotes. i.e., `"binance_api_key":"xxxxxxxxxxxx",`
8) Type `python3 pushstocks.py` into the terminal.

# Planned:
* Send messages for fatal errors and close prices.
* Add more exception catching and re-organize code.
