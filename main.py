from attraction_crawling import Attraction


if __name__ == '__main__':
    att = Attraction()
    info_list = att.crawling()
    att.export_excel_file(info_list)

