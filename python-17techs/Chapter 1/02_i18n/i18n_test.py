# -*- coding: utf-8 -*-
# python-gettext 모듈 
import gettext

translation_ko = gettext.translation(
    domain='i18n_test', localedir='./locale', languages=['ko_KR']
)
translation_ja = gettext.translation(
    domain='i18n_test', localedir='./locale', languages=['ja_JP']
)
translation_zh = gettext.translation(
    domain='i18n_test', localedir='./locale', languages=['zh_CN']
)

# 설정 변경 시 다른 translation 오브젝트의 install() 함수를 호출하면 된다. 

translation_ko.install()
# translation_ja.install()
# # translation_zh.install()


print(_('Test message 1'))
print(_('Test message 2'))
print(_('Test message 3'))
