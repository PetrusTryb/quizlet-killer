import requests
import sys
import os
import _thread as thread
import random
import asyncio
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
requests.packages.urllib3.disable_warnings()
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def join(code,name,driver):
	wait = WebDriverWait(driver, 10)
	driver.execute_script("window.onbeforeunload = function() {};window.alert = function() {};")
	driver.get("https://quizlet.com/live")
	try:
		wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"LiveGameTarget\"]/div/div/form/div[2]/div/div/div/div[1]/label[1]/div/input")))
		driver.find_element_by_xpath("//*[@id=\"LiveGameTarget\"]/div/div/form/div[2]/div/div/div/div[1]/label[1]/div/input").send_keys(str(code) + Keys.RETURN)
	except:
		wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"LiveGameTarget\"]/div/div/form/div[2]/div/div/div/div[1]/label[1]/div/input")))
		driver.find_element_by_xpath("//*[@id=\"LiveGameTarget\"]/div/div/form/div[2]/div/div/div/div[1]/label[1]/div/input").send_keys(str(code) + Keys.RETURN)
	try:
		wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"LiveGameTarget\"]/div/div/form/div[2]/div/label/div/input")))
		driver.find_element_by_xpath("//*[@id=\"LiveGameTarget\"]/div/div/form/div[2]/div/label/div/input").send_keys(name + Keys.RETURN)
	except:
		print(colors.FAIL,"[x]Could not join this game. Your code is probably invalid. Ask Your teacher or use brute-force.",colors.ENDC)
		os._exit(1)
	finally:
		wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"StudentInstructionsView")))
		print(colors.OKGREEN,"[+]Joined game",code,"with random fake name.",colors.ENDC)
		driver.close()
def loop():
	options = webdriver.ChromeOptions()
	options.add_argument("--incognito")
	options.add_argument('--disable-notifications')
	options.add_argument('--disable-extensions')
	options.add_argument('--headless')
	options.add_argument('--log-level=3')
	for i in range (1000):
		join(code,"Quizlet killer by PT #"+str(random.randint(0,10000)),webdriver.Chrome("chromedriver.exe",options=options))
print(colors.HEADER,"[i]Welcome to Quizlet Killer! Enter game code:",colors.ENDC)
code=input()
print(colors.HEADER,"[i]Please enter number of attack threads (too high number may freeze your machine)",colors.ENDC)
threads=int(input())
print(colors.HEADER,"[i]Quizlet killer attack is in progress. Press CTRL+C to stop.",colors.ENDC)
sys.tracebacklimit = 0
for i in range(threads):
	thread.start_new_thread(loop,())
while(1):
	pass