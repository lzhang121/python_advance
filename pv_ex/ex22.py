# -*- coding: utf-8 -*-
# @Time : 2024/12/25 18:11
# @Author : zhanglei
# @Email : zhanglei@bonree.com
import os
import json
import requests
import pandas as pd


def json_parse():
    # 读取JSON文件
    with open('result.json', 'r') as file:
        data = json.load(file)
    # 假设你需要选择JSON中的特定字段（例如 'name', 'age', 'city'）
    # 如果JSON数据是嵌套的，可以通过访问字典来提取需要的字段
    selected_data = []
    # 这里假设你的JSON数据是一个列表，里面包含多个字典
    for item in data['d']['results']:
        selected_item = {
            'fioriId': item.get('fioriId'),
            'AppName': item.get('AppName')
        }
        selected_data.append(selected_item)
    return selected_data


def update_excel():
    fioriId_AppName = json_parse()
    #fioriId_AppName = [{"fioriId": "F0714A", "AppName": "Manage Funds"},{"fioriId": "F3082", "AppName": "Manage Funds Centers"}]
    releaseId = {
	    'S15OP': 'S / 4HANA 1909',
	    'S16OP': 'S / 4HANA 1909 FPS01',
	    'S17OP': 'S / 4HANA 1909 FPS02',
		'S18OP': 'S / 4HANA 2020',
	    'S19OP': 'S / 4HANA 2020 FPS01',
	    'S20OP': 'S / 4HANA 2020 FPS02',
		'S21OP': 'S / 4HANA 2021',
	    'S22OP': 'S / 4HANA 2021 FPS01',
	    'S23OP': 'S / 4HANA 2021 FPS02',
		'S24OP': 'S / 4HANA 2022',
	    'S25OP': 'S / 4HANA 2022 FPS01',
	    'S26OP': 'S / 4HANA 2022 FPS02',
		'S27OP': 'S / 4HANA 2023',
	    'S28OP': 'S / 4HANA 2023 FPS01',
	    'S29OP': 'S / 4HANA 2023 FPS02',
		'S29PCE': 'S / 4HANA 2023 FPS02 - PCE'
        }
    tmp_data = []
    count = 0
    for item in fioriId_AppName:
        count += 1
        tmp_dict = item
        pre_url = "https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/services/getGTMDescription.xsjs?fioriId={}".format(item['fioriId'])
        for key, value in releaseId.items():
            url = pre_url + '&releaseId=' + key
            payload = {}
            headers = {
	            'Cookie': 'sapxslb=BBBE8BA0B5C1C7409C1DA71C628CB438; BIGipServerboma0d717969.factory.customdomain=!x5bNrMOYQ8/cJbheaBxHSKFoIXUAnB75Dnb/+QwDUWw9oUBqdPs0vW4ljTzOSU22yinSrCrNUDeDw6o=; language=None; xsSecureId5ABB8FCC7F4EC1526A2A6CE5FFD964CF=8C83D5235FB15245A563D8ADA2ADF2F4',
	            'Sec-Fetch-Dest': 'document',
	            'Sec-Fetch-Mode': 'navigate',
	            'Sec-Fetch-Site': 'cross-site'
	        }
            response = requests.request("GET", url, headers=headers, data=payload)
            json_data = response.json()
            tmp_dict[value] = json_data["GTMAppDescription"]
            # if json_data["GTMAppDescription"] == "<p>This app is a SAP GUI for HTML transaction. These classic transactions are available in the SAP Fiori theme to support a seamless user experience across the SAP Fiori launchpad and to provide a harmonized user experience across on-premise and cloud solutions. <br />The single point of entry for SAP Fiori apps and classic applications in SAP S/4HANA Cloud Private Edition and SAP S/4HANA is the SAP Fiori launchpad.</p>":
            #     tmp_dict[key] = "----"


        tmp_data.append(tmp_dict)
        print("已经处理完第: {}条记录".format(count))


    #将选定的数据转换为DataFrame
    df = pd.DataFrame(tmp_data)
    # 写入Excel文件
    df.to_excel('result.xlsx', index=False, engine='openpyxl')
    print("\n数据已成功写入Excel文件！")


if __name__ == "__main__":
    file_path = "output.xlsx"
    if os.path.exists(file_path):
        os.remove(file_path)
    update_excel()