from attraction_crawling import Attraction


if __name__ == '__main__':
    att = Attraction()
    info_list1 = att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=1')
    info_list2 = att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=2')
    info_list3 = att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=3')
    info_list4 = att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=4')
    info_list5 = att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=5')
    info_list6 = att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=6')
    info_list7 = att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=7')
    info_list8 = att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=8')
    info_list9 = att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=9')

    info_list = info_list1 + info_list2 + info_list3 + info_list4 + info_list5 + info_list6 + info_list7 + info_list8 + info_list9

    att.export_excel_file(info_list)

