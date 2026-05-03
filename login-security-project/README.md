# Login Security Simulation System

## Overview
This project simulates a login system with basic security mechanisms.  
It demonstrates how authentication, logging, and attack detection work.

## Features
- Socket-based login server  
- Brute force simulation client  
- IP-based blocking  
- Time-based detection  
- Username-based detection  
- Logging of login attempts  

## How It Works
The client sends login attempts (username:password) to the server.  
The server authenticates the request, logs activity, and applies detection rules.

## What I Learned
- How login systems handle authentication  
- How brute force attacks work  
- How detection logic (IP, time, username) can be implemented  
- Limitations of simple rule-based security  

## Future Improvements
- Better log analysis  
- Structured logging (JSON)  
- Advanced detection techniques