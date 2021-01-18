from lxml import etree


def read_xpath(tree, xpath):
    tags = tree.xpath(xpath)
    if tags and len(tags) > 0:
        return True, tags[0]
    else:
        return False, None


def read_all(tree, xpath):
    for tag in tree:
        if len(tag) > 0:
            # 객체 또는 배열 요소인 경우
            read_all(tag, '{0}/{1}'.format(xpath, tag.tag))
        else:
            if tag.text:
                print('{0}/{1}={2}'.format(xpath, tag.tag, tag.text))
            else:
                print('{0}/{0}'.format(xpath, tag.tag))


def open_xml_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return etree.parse(file, parser=etree.XMLParser(encoding='utf-8'))
        except KeyError as e:
            print('XML 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None


xml_tree = open_xml_file('python-17techs/Chapter 2/10_XML/message1.xml')
if not xml_tree:
    exit(0)

# Iterator 기반 접근
exist, root_tree = read_xpath(xml_tree, '/message')
assert exist
read_all(root_tree, root_tree.tag)
