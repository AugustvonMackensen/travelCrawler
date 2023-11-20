import attraction_crawling as att


if __name__ == '__main__':
    att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=1')
    att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=2')
    att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=3')
    att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=4')
    att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=5')
    att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=6')
    att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=7')
    att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=8')
    att.crawling('https://www.jeongseon.go.kr/tour/jeongseontour/attractions?pageIndex=9')

    att.export_excel()
