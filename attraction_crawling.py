from selenium import webdriver
import chromedriver_autoinstaller
import openpyxl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Attraction:

    def __init__(self):
        self.title = ''
        self.category = ''
        self.address = ''
        self.tel = ''
        self.link = ''
        self.closed = ''
        self.openTime = ''
        self.entryFee = ''
        self.usingFee = ''
        self.info = ''
        self.guide = ''

    def crawling(self):
        info_list = []
        info_dict = {}

        # Chrome Driver 설치
        path = chromedriver_autoinstaller.install()

        driver = webdriver.Chrome(path)
        for i in range(1, 10):
            driver.get('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=' + str(i))
            for j in range(1, 12):
                # 링크 클릭
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                              '#A-Contents-focus > div.sub_contents > div.category_area '
                                              '> ul > li:nth-child(' + str(j)+') > a'))).click()
                self.title = driver.find_element(By.CSS_SELECTOR,
                                                 '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > h4').text
                self.category = driver.find_element(By.CSS_SELECTOR,
                                                    '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(1) > dl > dd').text
                self.address = driver.find_element(By.CSS_SELECTOR,
                                                   '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(2) > dl > dd').text
                self.tel = driver.find_element(By.CSS_SELECTOR,
                                               '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(3) > dl > dd').text
                self.link = driver.find_element(By.CSS_SELECTOR,
                                                '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(4) > dl > dd').text
                self.closed = driver.find_element(By.CSS_SELECTOR,
                                                  '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(5) > dl > dd').text
                self.openTime = driver.find_element(By.CSS_SELECTOR,
                                                    '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(6) > dl > dd').text
                self.entryFee = driver.find_element(By.CSS_SELECTOR,
                                                    '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(7) > dl > dd').text
                self.usingFee = driver.find_element(By.CSS_SELECTOR,
                                                    '#A-Contents-focus > div.sub_contents > div > div.summary_area > div > div > div.txt_box > ul > li:nth-child(8) > dl > dd').text
                self.info = driver.find_element(By.CSS_SELECTOR,
                                                '#A-Contents-focus > div.sub_contents > div > div.info_area > div:nth-child(1) > p').text
                self.guide = driver.find_element(By.CSS_SELECTOR,
                                                 '#A-Contents-focus > div.sub_contents > div > div.info_area > div:nth-child(2) > p').text

                info_dict['명소명'] = self.title
                info_dict['분류'] = self.category
                info_dict['주소'] = self.address
                info_dict['연락처'] = self.tel
                info_dict['홈페이지'] = self.link
                info_dict['휴무일'] = self.closed
                info_dict['이용시간'] = self.openTime
                info_dict['입장료'] = self.entryFee
                info_dict['시설사용요금'] = self.usingFee
                info_dict['소개'] = self.info
                info_dict['여행가이드'] = self.guide
                print("명소 정보 : ", info_dict)
                self.add_list(info_list, info_dict)
                driver.back()
        driver.close()
        print("리스트 정보 : ", info_list)
        return info_list

    def add_list(self, info_list, dict):
        info_list.append(dict)

    def export_excel_file(self, info_list):
        # 현재 엑셀 workbook 생성
        workbook = openpyxl.Workbook()

        # 현재 workbook 활성화된 sheet 불러오기
        sheet = workbook.active
        sheet.title = '정선군 명소정보'

        # 딕셔너리 자료형 키 값을 헤더 값으로 설정
        sheet.append(list(info_list[0].keys()))

        for item in info_list:
            sheet.append(list(item.values()))

        sheet.save('정선군_명소리스트')
