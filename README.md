# Bitcoin Price Calculator 💰
A CLI tool that fetches the live Bitcoin price via CoinCap API 
and calculates the USD value for a given quantity.

## Usage
python bitcoin.py <amount>

## Examples
python bitcoin.py 1     → $97,845.0243
python bitcoin.py 2.5   → $244,612.5608
python bitcoin.py 0     → Amount must be greater than 0
python bitcoin.py abc   → Command-line argument is not a number

## Features
- Fetches real-time Bitcoin price via CoinCap REST API
- Input validation with meaningful error messages
- Supports integer and float amounts
- Output formatted to 4 decimal places with comma separators

## Built With
Python 3 | requests | sys
