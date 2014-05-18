ValualizeGraphic
==============================

http://graphic.valualize.com
==============================
author: Jungtaek Kim
email: jungtaek.kim@jt-inc.net
site: http://www.jt-inc.net
==============================

Description
==============================
Get Google Finance data such as closed price, market capitalization and volume.
Download a html file of each stock, and extract the data in the html file. Finally, save the data to data format file. 

Executing Order
==============================
getHtml.out -> getData.out -> collectData.out

Compile Method
==============================
Type 'make' on each directory.

Result
==============================
Collected data is on 'data' folder and collected html file is on 'data__html' folder.
Collected data is saved in 'year-month-day.data'. The format of data extension is "%s\t%s\t%s".

Directory
==============================
/
	path.h
	max.h
	stock.list
getHtml/
	getHtml.c
	getHtml.h
getData/
	getData.c
	getData.h
insertScript/
	insertScript.c
	insertScript.h
collectData/
	collectData.c
	collectData.h
