# WOG
devops project  
05/07/2021  
-game application with 3 games and 5 difficulties  
-Main games calls to live  
-live calls selected game with selected difficulty  
~~a win adds to a score file created when with first win~~  
-mysql server stores user score  
-flask server shows live score on the web (/score) or error if no score is detected  
-test folder with selenium test for the flask server  
-both flask server and mysql are built into docker containers using docker-compose
-jenkinsfile: runs on MACos enviorment, checkout>tar.gz>rotate older version using bash>
move the newest version to version control folder  
-jenkinsfile-2e2: checkout>build>test>push to hub 


external libraries used:  
-flask  
-forex_python  
-selenium  
-mysql-connector-python  

