from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import pymongo

def boot_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_news={}
    hem_url=[]

# mars news function
def mars_news():
    browser=boot_browser()
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')
   
    titles = soup.find_all('div',class_='content_title').get_text()
    article = soup.find('div', class_="article_teaser_body").get_text()

    browser.quit()

    return(mars_data)

# JPL Image
def jpl():
    browser=boot_browser()  
    url2 = 'https://www.jpl.nasa.gov/images?search=&category=Mars'
    browser.visit(url2)
    time.sleep(1)

    f_image=browser.links.find_by_partial_text('Mars').click()
    dat_image=browser.links.find_by_partial_text('2021').click()
    cl_image=browser.find_by_tag('button')[1]
    cl_image.click()

    html=browser.html
    soup2=bs(html,'html.parser')
    full_image=soup2.find('img', class_="object-scale-down").get('src')

#Planet Data Table
def mars_table()
    browser=boot_browser() 
    url3='https://space-facts.com/mars/'
    time.sleep(1)
    tables = pd.read_html(url3)
    mars_df=tables[0]
    mars_df.columns= ['', 'Mars']
    mars_df.to_html ('resources/mars_table.html', index=False, classes=['table-stripped'])

#Images of all four hem
def hem_img()
    browser=boot_browser()
    url4='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)
    time.sleep(1)

    links = browser.find_by_css('a.product-item h3')
    img_urls=[]

    for i in range(len(links)):
        hem = {}
        browser.find_by_css('a.product-item h3')[i].click()
        hem['title']=browser.find_by_css('h2.title').text
        hem['img_link']=browser.links.find_by_text('Sample').first['href']
        img_urls.append(hem)
        browser.back()

def scrape()
    scrape={
        'mars_news':mars_news,
        'jpl':jpl,
        'mars_table':mars_table,
        'hem_img':hem
    }

browser.quit()