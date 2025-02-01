# Importing Libraries
import selenium 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


# Inter your username and password
UserName = "*******"
PassWord = "*******"

# PREPARING THE DATE IN PANDAS #
df = pd.read_excel(r"D:\Creation\Creation.xlsx")
Outputs = []


## OPINGING WORKDAY ##

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Workday login page
driver.get("https://www.myworkday.com/***/d/home.htmld")
time.sleep(5)

# pass the first page 
page = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/ul/li[1]/div") # used the full XPATH # It's to pass the first page before the login page
page.click()

# Wait until the login page is fully loaded
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "username")))

# Enter Username
username = driver.find_element(By.ID, "username")
username.send_keys(UserName)
username.send_keys(Keys.RETURN)

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "passwordInput")))

# Enter Password
password = driver.find_element(By.ID , "passwordInput")
password.send_keys(PassWord)
password.send_keys(Keys.RETURN)

# Wait for 30 sec to inter dou 
time.sleep(30)

# Hitting the skip Button

    #WAIT FOR IT TO SHOW
        #it has to be sleep time bc if it's not it's gonna cause an error once different page appear


skip = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]")
skip.click()
time.sleep(10)



# click 'creat Prospect'

Create_prospect = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[3]/div[2]/div/div[4]/div[1]/ol/li[1]/div")
Create_prospect.click()

# Western Script Check

Check = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/ul/li/div[2]/div/div/div")
Check.click()



# Filling Out 
try:
    for index , row in df.iterrows():
      First_Name = row['First Name']
      Last_Name = row['Last Name']
      Family_Name = row['Family Name']
      Phone_Number = row['Phone Number']
      Email = row['E-mail']
      Source = row['Source']
      Evergreen = row['Evergreen']
      
                 
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/ul/li[3]/div[2]/div/div"))).send_keys(Phone_Number)
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div/ul/li[4]/div[2]"))).send_keys(First_Name)
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div/ul/li[5]/div[2]"))).send_keys(Last_Name)
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div/ul/li[6]/div[2]"))).send_keys(Family_Name)
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/ul/li[1]/div[2]"))).send_keys(Email)

      Ok_1 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/section/div[2]/div[2]/div[3]/button[1]")
      Ok_1.click()

      # chooseing 'Mobile' from dropdown list 
      dropdown_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , "/html/body/div[3]/div[2]/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/ul/li[1]/div[2]/div[1]/div/div/div/div[1]/span")))
      select = select(dropdown_element)
      select.select_by_visible_text('Mobile') # we can her choose to wright 'Mobile' then time.sleep(1) then .send_Keys(Keys.RETURN) if it didn't work


      fill_source = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div/div/div/div[1]/div/div[2]/div/ul/li[1]/div[2]/div[1]/div/div/div/div/div/input")))
      fill_source.send_keys(Source)

      time.sleep(1)
      fill_source.send_keys(Keys.RETURN)

      time.sleep(1)
      fill_source.send_keys(Keys.RETURN)

      Ok_2 = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[1]/section/div[2]/div[1]/div[1]/button[1]")
      Ok_2.click()

      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "relatedActionsButton"))).click()
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div/div/div/div/div[5]/div[2]/div/ul/li[3]/div/div"))).click()

      fill_evergreen = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/ul/li[2]/div[2]/div/div/div/div/div/div/input"))).send_keys(Evergreen)
      fill_evergreen.send_keys(Keys.RETURN)


      Ok_3 = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div[1]/section/div[2]/div[2]/div[3]/button[1]")
      Ok_3.click()

      Ok_4 = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/section/div[2]/div[1]/div[1]/button[1]")
      Ok_4.click()

      # adding the code in the df
      
      output_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "workerProfileDetailsPanelName"))).text
      Outputs.append(output_text)

      df['Code'] = Outputs
     # back to home page to repete 
        
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[6]/div[1]/div[2]/button"))).click()

      WebDriverWait(driver,10).untill(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/ul/li/div[2]/div/div/div"))).click()


finally:
    driver.quit()
