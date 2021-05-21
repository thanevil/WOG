# WOG
devops project  
05/07/2021  
-game application with 3 games and 5 difficulties  
-Main games calls to live  
-live calls selected game with selected difficulty  
-a win adds to a score file created when with first win  
-score file is deleted when done playing (if application crashes, when app starts it checks for the file and deletes it)  
-flask server shows live score on the web (/score) or error if no score is detected  
-a win adds to a score file created when the application starts  
-test folder with selenium test for the flask server  

external libraries used:  
-flask  
-forex_python  
-selenium  