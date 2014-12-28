from bs4 import BeautifulSoup
import requests
from math import sqrt
import sqlite3
from datetime import datetime
from time import gmtime, strftime
import time

conn = sqlite3.connect('/var/www/graphic/db.sqlite3')
c = conn.cursor()

company_list = []
currency_list = []

for row in c.execute('SELECT * FROM marketCaps_company ORDER BY -shorten_name'):
	company_list.append(row)

for row in c.execute('SELECT * FROM marketCaps_currency ORDER BY -to_currency'):
	currency_list.append(row)

conn.close()

while True:
	while datetime.now().minute != 0:
		dummy = 1		

	price_list = []
	market_cap_list = []

	temp_usd_market_cap_list = []
	temp_krw_market_cap_list = []
	temp_twd_market_cap_list = []
	temp_jpy_market_cap_list = []
	temp_hkd_market_cap_list = []

	temp_2_usd_market_cap_list = []
	temp_2_krw_market_cap_list = []
	temp_2_twd_market_cap_list = []
	temp_2_jpy_market_cap_list = []
	temp_2_hkd_market_cap_list = []

	temp_3_usd_market_cap_list = []
	temp_3_krw_market_cap_list = []
	temp_3_twd_market_cap_list = []
	temp_3_jpy_market_cap_list = []
	temp_3_hkd_market_cap_list = []
	
	temp_usd_price_list = []
	temp_krw_price_list = []
	temp_twd_price_list = []
	temp_jpy_price_list = []
	temp_hkd_price_list = []
	
	temp_2_usd_price_list = []
	temp_2_krw_price_list = []
	temp_2_twd_price_list = []
	temp_2_jpy_price_list = []
	temp_2_hkd_price_list = []
	
	temp_usd_company_list = []
	temp_krw_company_list = []
	temp_twd_company_list = []
	temp_jpy_company_list = []
	temp_hkd_company_list = []
	
	KRW = 0.0
	JPY = 0.0
	TWD = 0.0
	HKD = 0.0
	TMP = "NULL"
	
	for (id, usd, to_currency, google_url) in currency_list:
		r = requests.get(google_url)
		data = r.text
		soup = BeautifulSoup(data)
		TMP = soup.findAll("span", {"class" : "bld"})[0].next_element
		TMP = TMP.strip("KRWJPYTWDHKD ")
		TMP = TMP.replace(',', '')
	
		if to_currency == "KRW":
			KRW = float(TMP)
		elif to_currency == "JPY":
			JPY = float(TMP)
		elif to_currency == "TWD":
			TWD = float(TMP)
		elif to_currency == "HKD":
			HKD = float(TMP)

	for (id, company_name, shorten_name, google_url, stock_symbol) in company_list:
		r = requests.get(google_url)
		data = r.text
		soup = BeautifulSoup(data)
		pr = soup.findAll("span", {"class" : "pr"})[0].next_element.next_element.next_element
		mc = soup.findAll("td", {"data-snapfield" : "market_cap"})[0].next_element.next_element.next_element.next_element
		pr = pr.replace(',', '')
		pr = pr.rstrip()
		mc = mc.rstrip()
		price_list.append(pr)
	
		if "NASDAQ" in stock_symbol:
			temp_usd_market_cap_list.append(mc)
			temp_usd_price_list.append(pr)
			temp_usd_company_list.append(company_name)
		elif "NYSE" in stock_symbol:
			temp_usd_market_cap_list.append(mc)
			temp_usd_price_list.append(pr)
			temp_usd_company_list.append(company_name)
		elif "KRX" in stock_symbol:
			temp_krw_market_cap_list.append(mc)
			temp_krw_price_list.append(pr)
			temp_krw_company_list.append(company_name)
		elif "KOSDAQ" in stock_symbol:
			temp_krw_market_cap_list.append(mc)
			temp_krw_price_list.append(pr)
			temp_krw_company_list.append(company_name)
		elif "TPE" in stock_symbol:
			temp_twd_market_cap_list.append(mc)
			temp_twd_price_list.append(pr)
			temp_twd_company_list.append(company_name)
		elif "TYO" in stock_symbol:
			temp_jpy_market_cap_list.append(mc)
			temp_jpy_price_list.append(pr)
			temp_jpy_company_list.append(company_name)
		elif "HKG" in stock_symbol:
			temp_hkd_market_cap_list.append(mc)
			temp_hkd_price_list.append(pr)
			temp_hkd_company_list.append(company_name)
	
	for price in temp_usd_price_list:
		price = float(price)
		temp_2_usd_price_list.append(price)
	
	for price in temp_krw_price_list:
		price = float(price)
		price = price / KRW
		temp_2_krw_price_list.append(price)
	
	for price in temp_twd_price_list:
		price = float(price)
		price = price / TWD
		temp_2_twd_price_list.append(price)
	
	for price in temp_jpy_price_list:
		price = float(price)
		price = price / JPY
		temp_2_jpy_price_list.append(price)
	
	for price in temp_hkd_price_list:
		price = float(price)
		price = price / HKD
		temp_2_hkd_price_list.append(price)
	
	for market in temp_usd_market_cap_list:
		if "T" in market:
			temp_3_usd_market_cap_list.append(market)
			market = market.strip("T")
			market = float(market)
			market = market * 1000000
			temp_2_usd_market_cap_list.append(market)
		elif "B" in market:
			temp_3_usd_market_cap_list.append(market)
			market = market.strip("B")
			market = float(market)
			market = market * 1000
			temp_2_usd_market_cap_list.append(market)
		elif "M" in market:
			temp_3_usd_market_cap_list.append(market)
			market = market.strip("M")
			market = float(market)
			market = market * 1
			temp_2_usd_market_cap_list.append(market)
	
	for market in temp_krw_market_cap_list:
		if "T" in market:
			market = market.strip("T")
			market = float(market)
			market = market * 1000000 / KRW
	#			market = 10 * sqrt(market)
			temp_2_krw_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market
				market = '%.2f' % market
				market = market + "M" 
			temp_3_krw_market_cap_list.append(market)
		elif "B" in market:
			market = market.strip("B")
			market = float(market)
			market = market * 1000 / KRW
	#			market = 10 * sqrt(market)
			temp_2_krw_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market
				market = '%.2f' % market
				market = market + "M" 
			temp_3_krw_market_cap_list.append(market)
		elif "M" in market:
			market = market.strip("M")
			market = float(market)
			market = market * 1 / KRW
			temp_2_krw_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market * 1
				market = '%.2f' % market
				market = market + "M" 
			temp_3_krw_market_cap_list.append(market)
	
	for market in temp_twd_market_cap_list:
		if "T" in market:
			market = market.strip("T")
			market = float(market)
			market = market * 1000000 / TWD
			temp_2_twd_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market * 1
				market = '%.2f' % market
				market = market + "M" 
			temp_3_twd_market_cap_list.append(market)
		elif "B" in market:
			market = market.strip("B")
			market = float(market)
			market = market * 1000 / TWD
			temp_2_twd_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market * 1
				market = '%.2f' % market
				market = market + "M" 
			temp_3_twd_market_cap_list.append(market)
		elif "M" in market:
			market = market.strip("M")
			market = float(market)
			market = market * 1 / TWD
			temp_2_twd_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market * 1
				market = '%.2f' % market
				market = market + "M" 
			temp_3_twd_market_cap_list.append(market)
	
	for market in temp_jpy_market_cap_list:
		if "T" in market:
			market = market.strip("T")
			market = float(market)
			market = market * 1000000 / JPY
	#			market = 10 * sqrt(market)
			temp_2_jpy_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market * 1
				market = '%.2f' % market
				market = market + "M" 
			temp_3_jpy_market_cap_list.append(market)
		elif "B" in market:
			market = market.strip("B")
			market = float(market)
			market = market * 1000 / JPY
			temp_2_jpy_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market * 1
				market = '%.2f' % market
				market = market + "M" 
			temp_3_jpy_market_cap_list.append(market)
		elif "M" in market:
			market = market.strip("M")
			market = float(market)
			market = market * 1 / JPY
	#			market = 10 * sqrt(market)
			temp_2_jpy_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market * 1
				market = '%.2f' % market
				market = market + "M" 
			temp_3_jpy_market_cap_list.append(market)
	
	for market in temp_hkd_market_cap_list:
		if "T" in market:
			market = market.strip("T")
			market = float(market)
			market = market * 1000000 / HKD
			temp_2_hkd_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market * 1
				market = '%.2f' % market
				market = market + "M" 
			temp_3_hkd_market_cap_list.append(market)
		elif "B" in market:
			market = market.strip("B")
			market = float(market)
			market = market * 1000 / HKD
	#			market = 10 * sqrt(market)
			temp_2_hkd_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market * 1
				market = '%.2f' % market
				market = market + "M" 
			temp_3_hkd_market_cap_list.append(market)
		elif "M" in market:
			market = market.strip("M")
			market = float(market)
			market = market * 1 / HKD
	#			market = 10 * sqrt(market)
			temp_2_hkd_market_cap_list.append(market)
			if market >= 1000000:
				market = market / 1000000
				market = '%.2f' % market
				market = market + "T"
			elif market >= 1000:
				market = market / 1000
				market = '%.2f' % market
				market = market + "B"
			else:
				market = market * 1
				market = '%.2f' % market
				market = market + "M" 
			temp_3_hkd_market_cap_list.append(market)
	
	company_usd_market_cap_list = zip(temp_usd_company_list, temp_2_usd_market_cap_list)
	company_krw_market_cap_list = zip(temp_krw_company_list, temp_2_krw_market_cap_list)
	company_twd_market_cap_list = zip(temp_twd_company_list, temp_2_twd_market_cap_list)
	company_jpy_market_cap_list = zip(temp_jpy_company_list, temp_2_jpy_market_cap_list)
	company_hkd_market_cap_list = zip(temp_hkd_company_list, temp_2_hkd_market_cap_list)
	
	company_usd_raw_market_cap_list = zip(temp_usd_company_list, temp_3_usd_market_cap_list)
	company_krw_raw_market_cap_list = zip(temp_krw_company_list, temp_3_krw_market_cap_list)
	company_twd_raw_market_cap_list = zip(temp_twd_company_list, temp_3_twd_market_cap_list)
	company_jpy_raw_market_cap_list = zip(temp_jpy_company_list, temp_3_jpy_market_cap_list)
	company_hkd_raw_market_cap_list = zip(temp_hkd_company_list, temp_3_hkd_market_cap_list)
	
	company_usd_price_list = zip(temp_usd_company_list, temp_2_usd_price_list)
	company_krw_price_list = zip(temp_krw_company_list, temp_2_krw_price_list)
	company_twd_price_list = zip(temp_twd_company_list, temp_2_twd_price_list)
	company_jpy_price_list = zip(temp_jpy_company_list, temp_2_jpy_price_list)
	company_hkd_price_list = zip(temp_hkd_company_list, temp_2_hkd_price_list)
	
	company_market_cap_list = company_usd_market_cap_list + company_krw_market_cap_list + company_twd_market_cap_list + company_jpy_market_cap_list + company_hkd_market_cap_list
	company_raw_market_cap_list = company_usd_raw_market_cap_list + company_krw_raw_market_cap_list + company_twd_raw_market_cap_list + company_jpy_raw_market_cap_list + company_hkd_raw_market_cap_list
	company_price_list = company_usd_price_list + company_krw_price_list + company_twd_price_list + company_jpy_price_list + company_hkd_price_list

	price_list = temp_2_usd_price_list + temp_2_krw_price_list + temp_2_twd_price_list + temp_2_jpy_price_list + temp_2_hkd_price_list 

	company_whole_list = zip(company_market_cap_list, price_list)
	date = strftime("%Y-%m-%d-%H", gmtime())
	path_date = '../data_background/' + date + '.csv'

	f = open(path_date, 'w')

	for ((company_name, company_market_cap), company_price) in company_whole_list:
		f.write(company_name)
		f.write(',')
		f.write(str(company_price))
		f.write(',')
		f.write(str(company_market_cap))
		f.write('\n')

	f.close()

