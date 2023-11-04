# Name: Orion R. Gonzales
## CSEC 302: Secure Coding
## Race_Conditions_Demo

### DEMO ASSIGNMENTS
	- The Demo works with docker while using the two race tools python files to set the race conditon
	- Race_tool -> Race Condition tool without using time
	- Race_tool2 -> Race Condition tool using time(0.1) for delay
	- route test -> Testing with the worst vulnerability to a Race Condition (Using time libary to mimic large webite easier for demo)
	- route test_fast -> Testing with a better but still vulnerable to a Race Condition, where some cases a fast function rarely can be tricked 
	- route test_fixed -> Testing with a secure Thread Lock to only allow one request at a time, secured from Race Conditions