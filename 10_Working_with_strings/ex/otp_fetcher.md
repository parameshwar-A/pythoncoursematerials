# OTP fetcher

## Requirements
- You are given with the text message. The objective is to get the four digit otp from the text.
- The otp position can be in random places. But it always starts with a pattern.
- pattern: G-xxxx
- See G- is denotes the next four digit is the otp.
- Your taks is to process the entire message and finally print out the 4 digit otp.

## Steps
- get the input string from user
- Find a way to locate the G- pattern
- once that is found, proceed to cut out the otp
- Print the final output

## Example
input: "Your google otp is G-1000 and it is valid for 10 mins"

output: 1000 

