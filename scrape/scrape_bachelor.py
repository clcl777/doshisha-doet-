from selenium import webdriver
from selenium.webdriver.support.select import Select
import os
import time
import requests
import urllib.request
from bs4 import BeautifulSoup
import re
from webdriver_manager.chrome import ChromeDriverManager

# 追加のデータをスクレイプする用　htmlでスクレイプ

def get_table(driver,i):
    content = driver.page_source
    with open("table_riko//table" + str(i) + ".xls", "w", encoding='utf-8') as output:
        output.write(content)

url = 'https://duet.doshisha.ac.jp/kokai/html/fi/fi020/FI02001G.html'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

year = 1
dropdown_year = driver.find_element_by_id('form1:kaikoNendolist')
select_years = Select(dropdown_year)
time.sleep(1)
select_years.select_by_index(year)
text_year = select_years.first_selected_option.text
os.mkdir("tables_new2021//" + text_year)  # 年代のフォルダ作成

for faculty in range(1,20):#学部
    time.sleep(1)
    dropdown_faculty = driver.find_element_by_css_selector('#form1 > div > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > select')
    selects_faculty = Select(dropdown_faculty)
    selects_faculty.select_by_index(faculty)
    text_faculty = selects_faculty.first_selected_option.text
    os.mkdir("tables_new2021//" + text_year + "//" +text_faculty)  #学部のフォルダ作成
    element_enter = driver.find_element_by_css_selector('#form1\:enterDodoZikko')
    element_enter.click()
    i = 1
    while(True):
        time.sleep(0.5)
        content = driver.page_source
        with open("tables_new2021//" + text_year + "//" +text_faculty + "//"+ str(i) + ".html", "w", encoding='utf-8') as output:
            output.write(content)
        i = i + 1
        try:
            element_page = driver.find_element_by_link_text('次のページ')
            tag_page = element_page.tag_name
            print(tag_page)
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'nearest'});", element_page)
            element_page.click()
        except:
            break