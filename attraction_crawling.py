from selenium import webdriver
import chromedriver_autoinstaller
import openpyxl
from selenium.webdriver.common.by import By

workbook = openpyxl.Workbook()

# 현재 workbook 활성화된 sheet 불러오기
sheet = workbook.active
sheet.title = '정선군 명소정보'

# 딕셔너리 자료형 키 값을 헤더 값으로 설정
sheet.append(['명소명', '분류', '주소', '연락처', '홈페이지', '휴무일', '이용시간', '입장료', '시설사용요금', '소개', '여행가이드'])

def crawling(url):

    # Chrome Driver 설치
    path = chromedriver_autoinstaller.install()

    driver = webdriver.Chrome(path)
    driver.get(url)
    for j in range(1, 13):
        # 링크 클릭
        element = driver.find_element(By.CSS_SELECTOR, '#A-Contents-focus > div.sub_contents > div.category_area '
                                                                   '> ul > li:nth-child(' + str(j) + ') > a')
        element.click()

        title = driver.find_element(By.CSS_SELECTOR,
                                         '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > h4').text
        category = driver.find_element(By.CSS_SELECTOR,
                                            '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(1) > dl > dd').text
        address = driver.find_element(By.CSS_SELECTOR,
                                           '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(2) > dl > dd').text
        tel = driver.find_element(By.CSS_SELECTOR,
                                       '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(3) > dl > dd').text
        link = driver.find_element(By.CSS_SELECTOR,
                                        '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(4) > dl > dd').text
        closed = driver.find_element(By.CSS_SELECTOR,
                                          '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(5) > dl > dd').text
        openTime = driver.find_element(By.CSS_SELECTOR,
                                            '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(6) > dl > dd').text
        entryFee = driver.find_element(By.CSS_SELECTOR,
                                            '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(7) > dl > dd').text
        usingFee = driver.find_element(By.CSS_SELECTOR,
                                            '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(8) > dl > dd').text
        info = driver.find_element(By.CSS_SELECTOR,
                                        '#A-Contents-focus > div.sub_contents > div > div.info_area > div:nth-child(1) > p').text
        guide = driver.find_element(By.CSS_SELECTOR,
                                         '#A-Contents-focus > div.sub_contents > div > div.info_area > div:nth-child(2) > p').text

        sheet.append([title, category, address, tel, link, closed, openTime, entryFee, usingFee, info, guide])

        driver.back()
    driver.close()

def export_excel():
    workbook.save('cite_list.xlsx')

