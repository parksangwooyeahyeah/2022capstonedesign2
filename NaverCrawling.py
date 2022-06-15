
import time
import os
from time import sleep
from IPython.display import display
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





# 함수 선언
def add_dataframe(name,stars, reviews, cnt):  # 데이터 프레임에 저장
    # 데이터 프레임생성

    df1 = pd.DataFrame(columns=['product_name','stars', 'review'])
    n = 1
    if (cnt > 0):
        for i in range(0, cnt - 1):
            df1.loc[n] = [name, stars[i], reviews[i]]  # 해당 행에 저장
            i += 1
            n += 1
    else:
        df1.loc[n] = ['null', 'null']
        n += 1
    return df1


def save():
    if not os.path.exists('output1.csv'):
        df1.to_csv('output1.csv', encoding='utf-8-sig', mode='w')
    else:
        df1.to_csv('output1.csv', encoding='utf-8-sig', mode='w', header=False)




def WriteCSVFile(CSVFileName, Counts):
    s = Service('/Users/parksangwoo/Documents/chromedriver')
    d = webdriver.Chrome(service=s)
    d.implicitly_wait(3)
    reviews = []
    stars = []
    cnt = 1  # 리뷰index
    page = 1
    link = pd.read_csv(CSVFileName)
    rows = list(link.url)
    while True:
            for i in rows:
                time.sleep(3)
                try:
                    d.get(i)
                    d.find_element(By.XPATH, "//a[@data-nclick='N=a:tab*s.srev']").click()

                    page_number = d.find_elements(By.CSS_SELECTOR, "a[data-nclick^='N=a:rev.page']")
                    page_count = 1
                    product_name_xpath = d.find_elements(By.TAG_NAME, "h2")
                    product_name = product_name_xpath[2].text
                    print(product_name)
                    for page in page_number:


                            print(page_count)
                            review20 = d.find_elements(By.CLASS_NAME, "reviewItems_text__XIsTc")

                            for review in review20:
                                try:
                                    reviews.append(review.text)
                                    print(review.text)
                                    cnt += 1
                                except:
                                    continue

                            star20 = d.find_elements(By.CLASS_NAME, "reviewItems_average__16Ya-")
                            for star in star20:
                                s = star.text
                                s1 = s.replace("평점", "")
                                stars.append(s1)
                                #print(s1)



                            page_count += 1
                            page_index = page_number.index(page)
                            page_number[page_index+1].click()
                            time.sleep(1)
                            #20개를 다 안긁어왔을떄 except 걸어서 리뷰갯수<20일때



                except:
                    print("error")
                df = add_dataframe(product_name, stars, reviews, cnt)
                display(df)
                if cnt >Counts: break
            break

    return df
#WriteCSVFile에다 네이버 상품 링크가 담긴 csv 파일 제목을 입력하세요.
#그리고 리뷰 개수를 총 몇개 뽑을 건지 입력하세요.

a = input("CSV File 이름을 입력하세요 : ")
b = int(input("리뷰를 총 몇개 뽑으실건가요? "))
df1 = WriteCSVFile(a, b)
save()

