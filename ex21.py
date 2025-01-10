# -*- coding: utf-8 -*-
# @Time : 2024/12/25 17:43
# @Author : zhanglei
# @Email : zhanglei@bonree.com
import requests
import json

def download():
	url = "https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/services/SingleApp.xsodata/$batch"

	payload = "\r\n--batch_bd4b-17df-d0f2\r\nContent-Type: application/http\r\nContent-Transfer-Encoding: binary\r\n\r\nGET Details(inpfioriId='FMAVCH01',inpreleaseId='S25OP',inpLanguage='None',fioriId='FMAVCH01',releaseId='S25OP')/RolesPerApp(InpFioriId='FMAVCH01',fioriId='FMAVCH01',releaseId='S25OP',RoleName='Budget%20Responsible%20-%20Funds%20Management',releaseGroupText='SAP%20S%2F4HANA%20(Private%20Cloud%20and%20On-Premise)')/RelatedAppsByRole?$skip=0&$top=200&$orderby=AppName%20asc&$inlinecount=allpages HTTP/1.1\r\nAccept-Language: en\r\nAccept: application/json\r\nMaxDataServiceVersion: 2.0\r\nDataServiceVersion: 2.0\r\n\r\n\r\n--batch_bd4b-17df-d0f2--\r\n"
	headers = {
	  'Content-Type': 'multipart/mixed;boundary=batch_bd4b-17df-d0f2'
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	print(response.text)



if __name__ == "__main__":
	download()