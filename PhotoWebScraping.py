import re, time, os, csv
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request


# Get the number of pages to extract information
pages_number=int(input('How many pages ? '))
tic = time.time()

# Configure chromedriver
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

# Create a folder to save downloaded HTML pages
dirName = 'PhotosFolder'
try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

# Loop through the website's pages
for page in range(1,pages_number+1):
   
    # Get Link and Change page number - Edit if necessary !
    #link = 'https://collections.lib.uwm.edu/digital/collection/ags_south/search/searchterm/Fortaleza/field/citypl/mode/exact/conn/and/page/'+str(page)
    link='https://collections.lib.uwm.edu/digital/collection/ags_south/search/searchterm/Cear%C3%A1%20(state)/field/statep/mode/exact/conn/and/page/'+str(page)   
    driver.get(link)
    time.sleep(2)
    data = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup_complete_source = BeautifulSoup(data.encode('utf-8'), "lxml")
    
    soup = soup_complete_source.find(class_='Search-mainContent col-sm-8 col-lg-9')    
    
    for line in soup.findAll(class_="SearchResult-container shared-search-box shared-box row SearchResult cdm-item-card"):
        name=line.text
        tags=str(line)
        endereco=tags[315:352]
        link_photo='https://collections.lib.uwm.edu'+endereco[:9]+'download/'+endereco[9:]+'/size/full'
        print(link_photo)
        try:
            urllib.request.urlretrieve(link_photo, dirName+'//'+name+'.jpg')
        except:
            ano=name.find('19')
            ano=ano+4
            urllib.request.urlretrieve(link_photo, dirName+'//'+name[:ano]+'.jpg')

driver.quit()