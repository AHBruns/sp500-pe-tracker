import requests
import time
sc = requests.get('http://www.multpl.com/').text
data_str = sc.split('<b>Current<span class="currentTitle"> S&amp;P 500 PE Ratio</span>:</b>')[1].split('<div id="timestamp">')[0]
pe_cur = float(data_str.split('<span class="pos">')[0].strip("\n").strip(" "))
pe_pt_chg = float(data_str.split('<span class="pos">')[1].split('</span>')[0].split(" ")[0])
pe_pcnt_chg = float(data_str.split('<span class="pos">')[1].split('</span>')[0].split(" ")[1].strip("(").strip("%)"))
print(pe_cur, pe_pt_chg, pe_pcnt_chg)