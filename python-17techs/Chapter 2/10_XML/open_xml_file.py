# 다음 코드 실행을 위해서는 lxml 모듈이 필요하다. pip install lxml

from lxml import etree


def open_xml_file(filename):
    with open(filename, encoding="UTF8") as file:
        try:
            return etree.parse(file, parser=etree.XMLParser(encoding="utf-8"))
        except KeyError as e:
            print('XML 데이터 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None


# message1.xml
xml_tree = open_xml_file("python-17techs/Chapter 2/10_XML/message1.xml")
if xml_tree:
    print(etree.tounicode(xml_tree, pretty_print=True))
