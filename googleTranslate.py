# -*- coding: utf-8 -*-

from workflow import Workflow3, ICON_WEB, web
# from urllib import unquote
from googletrans import Translator
import sys
reload(sys)
sys.setdefaultencoding('utf8')

LANGUAGES = {
  'Afrikaans': 'af',
  'Albanian': 'sq',
  'Amharic': 'am',
  'Arabic': 'ar',
  'Armenian': 'hy',
  'Azerbaijani': 'az',
  'Basque': 'eu',
  'Belarusian': 'be',
  'Bengali': 'bn',
  'Bosnian': 'bs',
  'Bulgarian': 'bg',
  'Catalan': 'ca',
  'Cebuano': 'ceb',
  'Chichewa': 'ny',
  'Chinese_Simplified': 'zh-CN',
  'Chinese_Traditional': 'zh-TW',
  'Corsican': 'co',
  'Croatian': 'hr',
  'Czech': 'cs',
  'Danish': 'da',
  'Dutch': 'nl',
  'English': 'en',
  'Esperanto': 'eo',
  'Estonian': 'et',
  'Filipino': 'tl',
  'Finnish': 'fi',
  'French': 'fr',
  'Frisian': 'fy',
  'Galician': 'gl',
  'Georgian': 'ka',
  'German': 'de',
  'Greek': 'el',
  'Gujarati': 'gu',
  'Haitian_creole': 'ht',
  'Hausa': 'ha',
  'Hawaiian': 'haw',
  'Hebrew': 'iw',
  'Hindi': 'hi',
  'Hmong': 'hmn',
  'Hungarian': 'hu',
  'Icelandic': 'is',
  'Igbo': 'ig',
  'Indonesian': 'id',
  'Irish': 'ga',
  'Italian': 'it',
  'Japanese': 'ja',
  'Javanese': 'jw',
  'Kannada': 'kn',
  'Kazakh': 'kk',
  'Khmer': 'km',
  'Korean': 'ko',
  'Kurdish': 'ku',
  'Kyrgyz': 'ky',
  'Lao': 'lo',
  'Latin': 'la',
  'Latvian': 'lv',
  'Lithuanian': 'lt',
  'Luxembourgish': 'lb',
  'Macedonian': 'mk',
  'Malagasy': 'mg',
  'Malay': 'ms',
  'Malayalam': 'ml',
  'Maltese': 'mt',
  'Maori': 'mi',
  'Marathi': 'mr',
  'Mongolian': 'mn',
  'Myanmar': 'my',
  'Nepali': 'ne',
  'Norwegian': 'no',
  'Pashto': 'ps',
  'Persian': 'fa',
  'Polish': 'pl',
  'Portuguese': 'pt',
  'Punjabi': 'pa',
  'Romanian': 'ro',
  'Russian': 'ru',
  'Samoan': 'sm',
  'Scots_gaelic': 'gd',
  'Serbian': 'sr',
  'Sesotho': 'st',
  'Shona': 'sn',
  'Sindhi': 'sd',
  'Sinhala': 'si',
  'Slovak': 'sk',
  'Slovenian': 'sl',
  'Somali': 'so',
  'Spanish': 'es',
  'Sundanese': 'su',
  'Swahili': 'sw',
  'Swedish': 'sv',
  'Tajik': 'tg',
  'Tamil': 'ta',
  'Telugu': 'te',
  'Thai': 'th',
  'Turkish': 'tr',
  'Ukrainian': 'uk',
  'Urdu': 'ur',
  'Uzbek': 'uz',
  'Vietnamese': 'vi',
  'Welsh': 'cy',
  'Xhosa': 'xh',
  'Yiddish': 'yi',
  'Yoruba': 'yo',
  'Zulu': 'zu'}

ICON_DEFAULT = 'icon.png'
ICON_PHONETIC = 'icon_phonetic.png'
ICON_BASIC = 'icon_basic.png'
ICON_WEB = 'icon_web.png'
ICON_UPDATE = 'icon_update.png'
ICON_ERROR = 'icon_error.png'

def check_Update():
    # 检查更新
    if wf.update_available:
        arg = ['', '', '', '', 'error']
        arg = '$%'.join(arg)
        wf.add_item(
            title='有新版本更新', subtitle='', arg=arg,
            valid=True, icon=ICON_UPDATE)
    else:
        wf.add_item('谷歌翻译')


def check_English(query):
    # 检查英文翻译中文
    import re

    if re.search(u"[\u4e00-\u9fa5]+", query):
        return False
    return True


def get_translation(query, isEnglish, res):
    # 翻译结果
    subtitle = '翻译结果'
    translations = res["translation"]
    for title in translations:
        arg = [query, title, query, '', ''] if isEnglish else [
            query, title, title, '', '']
        arg = '$%'.join(arg)

        wf.add_item(
            title=title, subtitle=subtitle, arg=arg,
            valid=True, icon=ICON_DEFAULT)


def get_phonetic(query, isEnglish, res):
    # 发音
    if u'basic' in res.keys():
        if res["basic"].get("phonetic"):
            title = ""
            if res["basic"].get("us-phonetic"):
                title += ("[美: " + res["basic"]["us-phonetic"] + "] ")
            if res["basic"].get("uk-phonetic"):
                title += ("[英: " + res["basic"]["uk-phonetic"] + "] ")
            title = title if title else "[" + res["basic"]["phonetic"] + "]"
            subtitle = '有道发音'
            arg = [query, title, query, '', ''] if isEnglish else [
                query, title, '', query, '']
            arg = '$%'.join(arg)
            wf.add_item(
                title=title, subtitle=subtitle, arg=arg,
                valid=True, icon=ICON_PHONETIC)


def get_explains(query, isEnglish, res):
    # 简明释意
    if u'basic' in res.keys():
        for i in range(len(res["basic"]["explains"])):
            title = res["basic"]["explains"][i]
            subtitle = '简明释意'
            arg = [query, title, query, '', ''] if isEnglish else [
                query, title, '', title, '']
            arg = '$%'.join(arg)
            wf.add_item(
                title=title, subtitle=subtitle, arg=arg,
                valid=True, icon=ICON_PHONETIC)


def get_translation(query):
  srclang = 'English'
  destlang = 'Chinese_Simplified'
  service_urls = ['translate.google.com']
  proxies = {'http': '127.0.0.1:1087','https': '127.0.0.1:1087'}
  translator = Translator(service_urls=service_urls, proxies=proxies)
  result = translator.translate(query, src=LANGUAGES[srclang], dest=LANGUAGES[destlang]).text.encode('utf-8')
  wf.add_item(title='翻译结果', subtitle=result, arg='', valid=True, icon=ICON_DEFAULT)

def main(wf):
  query = wf.args[0].strip().replace("\\", "")
  query = query.decode('utf8')

  get_translation(query)
  wf.send_feedback()

if __name__ == '__main__':
  wf = Workflow3()
  wf.run(main)