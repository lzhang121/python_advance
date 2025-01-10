# -*- coding: utf-8 -*-
# @Time : 2024/12/23 23:36
# @Author : zhanglei
# @Email : zhanglei@bonree.com
import requests
import json
import csv

def check(fioriId, releaseId):
	pre_url = "https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/services/getGTMDescription.xsjs?fioriId={}".format(fioriId)
	count = 0
	for key, value in releaseId.items():
		url = pre_url + '&releaseId=' + key
		payload = {}
		headers = {
			'Cookie': 'sapxslb=BBBE8BA0B5C1C7409C1DA71C628CB438; BIGipServerboma0d717969.factory.customdomain=!x5bNrMOYQ8/cJbheaBxHSKFoIXUAnB75Dnb/+QwDUWw9oUBqdPs0vW4ljTzOSU22yinSrCrNUDeDw6o=; language=None; xsSecureId5ABB8FCC7F4EC1526A2A6CE5FFD964CF=8C83D5235FB15245A563D8ADA2ADF2F4',
			'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site'
		}
		response = requests.request("GET", url, headers=headers, data=payload)
		json_data = response.json()

		if json_data["GTMAppDescription"] != "":
			version = releaseId[key]
			info = json_data["GTMAppDescription"]

	return version,info

def write_csv(start_version):
	# 文件路径设置
	input_csv_file = "FM_Excel_1.csv"  # 原始CSV文件路径
	output_csv_file = "FM_Excel_Version_1.csv"  # 保存符合条件记录的新CSV文件

	input_csv_file = "FM_Excel.csv"  # 原始CSV文件路径
	output_csv_file = "FM_Excel_Version.csv"  # 保存符合条件记录的新CSV文件

	# 打开输入CSV文件并读取内容
	with open(input_csv_file, mode='r', encoding='utf-8') as infile, open(output_csv_file, mode='w', encoding='utf-8',
	                                                                      newline='') as outfile:
		csv_reader = csv.reader(infile)
		csv_writer = csv.writer(outfile)

		# 读取表头并写入到新文件中
		headers = next(csv_reader)
		cloumn_1 = "Start Version"
		cloumn_2 = "Version INFO"
		headers.append(cloumn_1)
		headers.append(cloumn_2)
		csv_writer.writerow(headers)

		# 遍历CSV内容
		matching_count = 0
		for row in csv_reader:
			# 检查每个字段是否包含关键字
			if matching_count <= len(start_version):
				row.append(start_version[matching_count][0])
				row.append(start_version[matching_count][1])
			csv_writer.writerow(row)  # 写入符合条件的行
			matching_count += 1
			print("处理进度: {}".format(matching_count))


if __name__ == "__main__":
	start_version = []
	releaseId = {
		'S29PCE': 'S / 4HANA 2023 FPS02 - PCE',
		'S29OP': 'S / 4HANA 2023 FPS02',
		'S28OP': 'S / 4HANA 2023 FPS01',
		'S27OP': 'S / 4HANA 2023',
		'S26OP': 'S / 4HANA 2022 FPS02',
		'S25OP': 'S / 4HANA 2022 FPS01',
		'S24OP': 'S / 4HANA 2022',
		'S23OP': 'S / 4HANA 2021 FPS02',
		'S22OP': 'S / 4HANA 2021 FPS01',
		'S21OP': 'S / 4HANA 2021',
		'S20OP': 'S / 4HANA 2020 FPS02',
		'S19OP': 'S / 4HANA 2020 FPS01',
		'S18OP': 'S / 4HANA 2020',
		'S17OP': 'S / 4HANA 1909 FPS02',
		'S16OP': 'S / 4HANA 1909 FPS01',
		'S15OP': 'S / 4HANA 1909'
	}
	versions = ["FM03","FM5I","FM5S","FM5U","FM6I","FM6S","FM6U","FMAO","FMAVCCUST01","FMAVCDERIAOR","FMAVCDERICHR","FMAVCDERITPROFR","FMAVCDERITRACE","FMAVCDIFF","FMAVCDISPCHANGEDOC","FMAVCH01","FMAVCINDINCON","FMAVCINDMISS","FMAVCR01","FMAVCR02","FMAVCREINIT","FMAVC_PERS_ANNUAL","FMAVC_PERS_GENERATE","FMAVC_PERS_OVERALL","FMAVC_TEST_QUEUE","FMBB","FMBBC","FMBLEXT0","FMBOSTAT","FMBPD","FMBPD_MASS","FMBROWSER","FMBSBO","FMBSBOHIS","FMBSBOHISDEL","FMBSBOS","FMBSBO_DATA","FMBSBO_GEN","FMBSBO_HIE_MULT","FMBSBO_MULT","FMBSCPY","FMBSCPYN","FMBSDERIBOR","FMBSIDX_INCON","FMBSIDX_RECON","FMBSPO","FMBSPOHIS","FMBSPOHISDEL","FMBSPOS","FMBSPO_DATA","FMBSPO_GEN","FMBSPO_MULT","FMBS_STAT","FMBTB","FMBUD_APP","FMB_B01","FMCAARFB0","FMCAARFB1","FMCAARFB2","FMCABILLI","FMCABILLM","FMCACOV","FMCAINCOC","FMCAINCOH","FMCAM1","FMCAOGRM","FMCAPFPF","FMCAPFPFS","FMCA_EXCEP_HIS_SEARCH ()","FMCA_GEN_WD_FROM_UI","FMCA_TPOV (FMCA_TPOV)","FMCA_WDY_FPF (FMCA_WDY_FPF_CONF)","FMCA_WDY_FPF_DA_FPM (FMCA_WDY_FPF_DA_FPM_AC)","FMCA_WDY_REG (FMCA_WDY_REG_CONF)","FMCA_WDY_RETURN_SEARCH (FMCA_WDY_RETURN_SEARCH_CONF)","FMCA_WDY_WI_MANAGE (FMCA_WDY_WI_MANAGE_CONF)","FMCCFBR","FMCCF_MONI","FMCCOVR","FMCECPYCG","FMCEDELCG","FMCEGENCG","FMCEHISCG","FMCEHISDEL","FMCEMON01","FMCERGR","FMCERULE","FMCIA","FMCIC","FMCID","FMCIE","FMCIH","FMCP_EF_CLOSE","FMCP_EF_CREATE","FMCYCOPI_BW","FMCYCOPI_CO","FMCYCOPI_SAC","FMCYDOC","FMCYFREEZEN","FMCYLOADN","FMCYPREP","FMCYRESET","FMCYTEXT","FMDERIVE","FMDERIVER","FMDM","FMDOCREV","FMEDD","FMEDDH","FMEDDW","FMFGTB","FMFG_E_BR1","FMFG_E_BS1","FMFG_E_CA1","FMFG_E_FI1","FMFG_E_NET_COST","FMFG_E_NP1","FMFG_E_RB1","FMFG_E_RC1","FMFG_E_RP1","FMFG_E_SF132","FMFG_E_SF133","FMFG_E_SF224","FMFG_E_TP1","FMFG_E_TRANS_REG","FMFG_E_ZFZALI00","FMFG_GTAS_FILE","FMFG_YEAR_END_CLOSE","FMIR","FMJ0","FMJ2","FMJ2_D","FMJ3","FMJ_ANZ","FMJ_APP","FMJ_CHAIN1","FMJ_DISP","FMJ_DISPLAY","FMMC","FMMDAUTO","FMMDCICOPY","FMMDFCCOPY","FMMDFDCOPY","FMMDFNCOPY","FMMD_SETGEN","FMMEASURE","FMMEASURED","FMMI","FMMPCEBAL","FMMPCOVRN","FMMPLOADBS","FMMPLOADBUD","FMMPLOADBUDN","FMMPPCLO","FMMPRBB","FMMPRELEN","FMMPSTAT","FMMPTRAN","FMOPER","FMPEP","FMPEPE","FMPEP_ADMIN","FMPSO001","FMRBCPY","FMRBDEL","FMRBDERIMDR","FMRBDERIROR","FMRBDISPCHANGEDOC","FMRBGENMD","FMRBIDXREC","FMRBMON01","FMRBREINIT","FMRBRULE","FMRBRULEHIS","FMRBRULEHISDEL","FMRESDISPLAY","FMRE_ARCH","FMRE_KERLK","FMRE_SERLK","FMRP_CI_SET_HIER","FMRP_FC_SET_HIER","FMRP_FW_BROWSER","FMRP_RFFMEP1AX","FMRP_RFFMEP1CX","FMRP_RFFMEP1FX","FMRP_RFFMEP1OX","FMRP_RW_BUDCON","FMRP_RW_BUDGET","FMRP_RW_BUDVER","FMSA","FMSB","FMSC","FMSD","FMSE","FMSL","FMSPLITMAINT","FMSRCICHNG","FMTB","FMTEXT","FMV1","FMV2","FMV3","FMV4","FMV5","FMV6","FMVA01","FMVPM1","FMVPM2","FMVPM3","FMVPM4","FMVT","FMW1","FMW2","FMW3","FMW4","FMW5","FMWA","FMWB","FMWC","FMWD","FMWE","FMWPM1","FMWPM2","FMWPM3","FMWPM4","FMX1","FMX2","FMX3","FMX4","FMX5","FMX6","FMXPM1","FMXPM2","FMXPM3","FMXPM4","FMY1","FMY2","FMY3","FMY4","FMY5","FMY6","FMYCR","FMYC_DELWF","FMYC_VA","FMYC_VA_REV","FMYPM1","FMYPM2","FMYPM3","FMYPM4","FMZ1","FMZ2","FMZ3","FMZ4","FMZ5","FMZ6","FMZPM1","FMZPM2","FMZPM3","FMZPM4","FMZZ","FM_CISUB_SET1","FM_CISUB_SET2","FM_CISUB_SET3","FM_FCSUB_SET1","FM_FCSUB_SET2","FM_FCSUB_SET3","FM_FDSUB_SET1","FM_FDSUB_SET2","FM_FDSUB_SET3","FM_FINAL_AA","FM_FNSUB_SET1","FM_FNSUB_SET2","FM_FNSUB_SET3","FM_FUNCTION","FM_REVALUATION_PO","FM_SETS_FICTR1","FM_SETS_FICTR2","FM_SETS_FICTR3","FM_SETS_FIPEX1","FM_SETS_FIPEX2","FM_SETS_FIPEX3","FM_SETS_FUNCTION1","FM_SETS_FUNCTION2","FM_SETS_FUNCTION3","FM_SETS_FUND1","FM_SETS_FUND2","FM_SETS_FUND3","FM_SETS_FUNDPRG1","FM_SETS_FUNDPRG2","FM_SETS_FUNDPRG3"]
	#versions = ["FM03", "FM5I"]
	for item in versions:
		version_info = check(item, releaseId)
		print("处理进度: {}".format(versions.index(item)+1))
		start_version.append((version_info[0],version_info[1]))
	write_csv(start_version)
