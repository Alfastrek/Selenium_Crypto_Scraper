# Selenium_Crypto_Scraper
 
![Screenshot (234)](https://github.com/Alfastrek/Selenium_Crypto_Scraper/assets/93537649/dd3f0d8c-98c3-49fe-a0de-5c88bc2c3866)
![Screenshot (233)](https://github.com/Alfastrek/Selenium_Crypto_Scraper/assets/93537649/726ce40e-6a25-4366-9f92-d73b3fec8a7d)
![Screenshot (232)](https://github.com/Alfastrek/Selenium_Crypto_Scraper/assets/93537649/eda03145-f3bc-48dc-abf9-5cfdeed5d8e2)
![Screenshot (231)](https://github.com/Alfastrek/Selenium_Crypto_Scraper/assets/93537649/51d25679-26e1-4441-abd1-2c062f121159)

Steps to replicate:

1) Download the Repository and unzip the file.
2) initialize the Virtual Environment (venv)
3) Start the Django Server
4) Start Celery Worker
5) Use Postman to test API points-
   
   POST REQUEST TO ASSIGN JOB-
   'localhost/api/taskmanager/start_scraping'

   GET REQUEST TO OBTAIN REQUIRED DETAILES OF THE JOBS-
   'localhost/api/taskmanager/scraping_status/<uuid:job_id>'
  
