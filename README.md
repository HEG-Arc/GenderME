# GenderME
API to genderify your data

This app was designed to support the design of ETL processes during a datawarehouse course.

## Usage

Usage is quite simple

GET
http://genderme.xyz/api?surname=luc

RESPONSE 200
{"surname": "luc", "gender": "male", "language": "fr"}

RESPONSE 404
Sorry, we don't know this surname :-(

RESPONSE 403
Quota exceeded! See you tomorrow...
