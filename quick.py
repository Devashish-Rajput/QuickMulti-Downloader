################ Quick Multi Downloader #####################
a=[]
b=[]

def get():
    from selenium import webdriver
    import time
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    path_to_extension = '/content/drive/MyDrive/3.5.31_0'
    chrome_options.add_argument('load-extension=' + path_to_extension)
    prefs = {'download.default_directory' : '/content/drive/MyDrive/myBot1/'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver =webdriver.Chrome('chromedriver',options=chrome_options)

    with open('urls.txt') as f:
          links = [line.rstrip() for line in f]
    for link in links:
        driver.get(link)
        try:
          x=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#vstr > div.hero-head > div > h1"))).text
          WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#download"))).click()
          try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,"1080p"))).click()
          except:
            try:
              WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,"720p"))).click()
            except:
              WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,"480p"))).click()
          y=driver.current_url
          a.append(y)
          x=x[:-4]
          x=x.replace('RareToonsIndia','OpToonsIndia.com')
          b.append(x)
        except:
          print('N/A')
get()
print('Link Loaded')

import os
os.chdir("/content/drive/MyDrive/myBot/")
i=0
for q in range(0,len(a),1):
  import urllib.request
  p=a[q]
  urllib.request.urlretrieve(a[q], b[q]+p[-4:])
  print(b[q]) 
print('Done')
