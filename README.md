# Sorting Server Log File Data Using Python
Program description:
1. clear the log file of unnecessary data (RequestMethod / Version, StatusCode, URL)
2. clean the log file from search engine robots
   1. identify robots based on access to the robots.txt file (URL)
   1. identify robots based on the User-Agent (Agent) field
3. create a UnixTime variable
4. identify users based on IP address and User-Agent field
5. create a Length variable based on User_ID and 60 min. STT.
6. identify sessions based on the Reference Length method (use value for navigation page share: 40%)
7. fill in the missing requirements for certain sessions
