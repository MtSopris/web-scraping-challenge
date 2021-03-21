from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import pymongo


mars_data={}
mars_data1={}
mars_data2={}
mars_data3={}
# hem_url=[]

# mars news function
def mars_news(browser):
    # browser=boot_browser()
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
    time.sleep(1)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


    html = browser.html
    soup = bs(html, 'html.parser')
   
    pointer = soup.select_one("ul.item_list li.slide")
    news_title = pointer.find("div", class_="content_title").get_text()
    news_p = pointer.find("div", class_="article_teaser_body").get_text()

    # browser.quit()
    mars_data["title"] = news_title
    mars_data["para"] = news_p
    return mars_data

# JPL Image
def jpl(browser):
    # browser=boot_browser()  
    url2 = 'https://www.jpl.nasa.gov/images?search=&category=Mars'
    browser.visit(url2)
    time.sleep(1)
    browser.is_element_present_by_text("About JPL", wait_time=1)

    f_image=browser.links.find_by_partial_text('Mars').click()
    time.sleep(2)
    # dat_image=browser.links.find_by_partial_text('2021').click()
    # time.sleep(2)
    cl_image=browser.find_by_tag('button')[1]
    cl_image.click()
    time.sleep(2)

    html=browser.html
    soup2=bs(html,'html.parser')
    full_image=soup2.find('img', class_="object-scale-down").get('src')

    mars_data["img_url"] = full_image
    return mars_data

#Planet Data Table
def mars_table():
    # browser=boot_browser() 
    url3='https://space-facts.com/mars/'
    time.sleep(1)

    tables = pd.read_html(url3)
    mars_df=tables[0]
    mars_df.columns= ['', 'Mars']
    # mars_df.to_html ('resources/mars_table.html', index=False, classes=['table-stripped'])
    # mars_table_html=pd.read_html('Resources/mars_table.html')
    mars_table_html=mars_df.to_html(index=False, classes=['table-stripped'])
    mars_data["facts"] =mars_table_html
    return mars_data

#Images of all four hem
def hem_img(browser):
    # browser=boot_browser()
    url4='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)
    time.sleep(1)
    browser.is_element_present_by_text("USGS Astrogeology Science Center", wait_time=1)

    links = browser.find_by_css('a.product-item h3')
    img_urls=[]

    for i in range(len(links)):
        hem = {}
        browser.find_by_css('a.product-item h3')[i].click()
        hem['title']=browser.find_by_css('h2.title').text
        hem['img_link']=browser.links.find_by_text('Sample').first['href']
        img_urls.append(hem)
        browser.back()

    mars_data["hemispheres"] = img_urls
    return mars_data

def scrape_all():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    scrape={
        'mars_news':mars_news(browser),
        'jpl':jpl(browser),
        'mars_table':mars_table(),
        'hem_img':hem_img(browser)
    }
    
    browser.quit()
    return mars_data