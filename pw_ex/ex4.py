# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:54
# @Author : zhanglei
# @Email : zhspark@gmail.com
import requests
import json


def main():
    cookies = {
        'uid_tt_ss': '7c9ddabea63cea43283994d4b6a442288ecb35fe9fb32dcb642c26077d906a83',
        'sessionid_ss': 'dbba79033a6814b7de5453aad556846f',
        '_ttp': '2l5C0k2S2EGWkKKHgjPZIN6bvYu',
        'ssid_ucp_v1': '1.0.0-KDNjYzA4ZTQ0YmRhYmE5ZjU0NTAwMGZiZTFlNTkxNDhjZWE0N2IwNzgKIQiBiI_K3sbf1WYQ4tK2ugYYswsgDDDX_K21BjgIQBJIBBADGgJteSIgZGJiYTc5MDMzYTY4MTRiN2RlNTQ1M2FhZDU1Njg0NmY',
        'tt_csrf_token': 'SZvDQnzz--5WM6O5Dhah1ol92qFekppidsl4',
        'tt_chain_token': 'I8uQBz+T2mSKyyaJyhWXcw==',
        'ak_bmsc': '76A459DCF87D1380AB1D1F18189AC643~000000000000000000000000000000~YAAQCQ8zF56ruuaTAQAAigeIUBrBNKUs8odTakG8sn55ic6HWOmAcCMrQPptswXa8YcgFUdc8ybSqzObVFjgXkkUtaQZkTT04yx7ODD9+Xv5fuSoRdqFg/vGNuHse7WYSr7dQrZBp0ZUF5eInE301dyVqisODaEy2aDMpeSDWXZkQBgbO5nEYKsK0cdumhOEt54xWExOlcP+5rdJ1vU3rmrwgp7fwYRkTgqV3nqqihpd4t68wVRYwpQi9UXoobg99nLHItRlKjStwKiUV+qlIpSK4xBGBLN4gqH5skBbg3niMpGr8TG7rILRezXLhq2Ip5Sa8AhUM6Ps/EuQsCfeCZ07vB6afdJdMyidUkUaY29GJX/orYbhDHGt/p9MNcIIt94j20mUW/na',
        'tiktok_webapp_theme_source': 'system',
        'tiktok_webapp_theme': 'dark',
        'delay_guest_mode_vid': '8',
        'sid_guard': 'dbba79033a6814b7de5453aad556846f%7C1736517880%7C12177002%7CSat%2C+31-May-2025+12%3A34%3A42+GMT',
        'uid_tt': '7c9ddabea63cea43283994d4b6a442288ecb35fe9fb32dcb642c26077d906a83',
        'sid_tt': 'dbba79033a6814b7de5453aad556846f',
        'sessionid': 'dbba79033a6814b7de5453aad556846f',
        'store-idc': 'alisg',
        'store-country-code': 'jp',
        'store-country-code-src': 'uid',
        'tt-target-idc': 'alisg',
        'msToken': 't8mkrOLdA3RSmUGiBut0fpj1s4vxTO_MnEZuvzcDRtyXJO8zjrT7d17-U_IQEgl0LdWahpUSbaa9XoqHWoEAxJOsQLAKY3GmDY0vfAZd-eoOj5JDmvpTAdgHM3k1XDeGx-gR4MxOaSue0s_cPzUUZZM=',
        'bm_sv': 'B4EF533397147D2B7A3E00E7B3F74737~YAAQCw8zF9Py30iUAQAAQOqMUBrbtsu/Fc8lcHo51xNI4WIViKsV3uye+dVhigU+jUzNX1Tpp+v6HD/YERsZD/L7CFsnYv9qMXJ1odUo2Nn8zXdRDvTV8uf9F+hJW4sPEpbWWvNsIZA4GsJA7/7AtNr2SZGTJNJg+zsZMo6LREN+YdWq4HUke/gLNTWhvH+L/nru9n+HTBVRSN6u5QqQFXfFfkk6C69AFRZavgxNYRw/LZ8wW45vweT0sAKiBzkl~1',
        'ttwid': '1%7CjwITGu9_SLKr1XyxagtlmF8_x7cnAMs_ccGfib1-6gU%7C1736518200%7C38b00d522cf53e640cf681f663dbaf363890091b9b25c5d715018d07f981112d',
        'passport_fe_beating_status': 'true',
        'odin_tt': '118fea5842254664f33fa0ce7cb3652505d2ce2971c26cb8551143d4a6455aec3d9587566dbc4ffb836ba46eefc8f688f928f8533c97d26d528147e088f3ec07c01e478f855d32b0d66bca13e75b9691', }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'priority': 'u=1, i',
        'referer': 'https://www.tiktok.com/@cartoon2203/video/7457744817322233096',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36', }

    response = requests.get(
        'https://www.tiktok.com/api/comment/list/?WebIdLastTime=1724421784&aid=1988&app_language=zh-Hans&app_name=tiktok_web&aweme_id=7457744817322233096&browser_language=zh-CN&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F130.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=20&cursor=0&data_collection_enabled=true&device_id=7406335101192553992&device_platform=web_pc&focus_state=true&from_page=video&history_len=4&is_fullscreen=true&is_page_visible=true&os=mac&priority_region=JP&referer=&region=JP&screen_height=900&screen_width=1440&tz_name=Asia%2FTokyo&webcast_language=zh-Hans&msToken=HWHgWu-uI-x3PbWAjMQAfrWgNoQUhR7_I1hBsi8z27mXE_ZT5Qw_ZfOCMlubwBmKEEZy7td3wYQCnNEknlqMiFewU17N62ZeyE5WQ5qLvI_YvkfjEyt1ruJAfnK9ge3wh7Ad0sX_F_hYzrB_lSRJNqc=&X-Bogus=DFSzswVOUIvANxpAtp1mXjLNKBT5&_signature=_02B4Z6wo00001azFrmQAAIDC.jqOfpR6pJ2sxarAAAyxaf',
        cookies=cookies,
        headers=headers,)
    res = json.loads(response.text)
    for item in res['comments']:
        print(item['text'])




if __name__ == '__main__':
    main()
