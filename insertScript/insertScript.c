#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "insertScript.h"
#include "../max.h"
#include "../path.h"

int main()
{
	FILE* stockListFile;
	FILE* insertScriptFile;
	FILE* htmlFile;

	char company[MAX_COMPANY];
	char url[MAX_URL];
	char symbol[MAX_SYMBOL];
	char scriptBlock[MAX_BLOCK];

	char year[5];
	char month[3];
	char day[3];
	char currentTime[11];

	char commandMakeRootDirectory[MAX_COMMAND];
	char commandMakeDirectory[MAX_COMMAND];
	char commandGetHtml[MAX_COMMAND];
	char commandCopyHtaccess[MAX_COMMAND];

	char pathHtml[MAX_PATH];
	char pathHtmlFile[MAX_PATH];

	time_t t = time(NULL);
	struct tm tm = *localtime(&t);

	sprintf(year, "%d", tm.tm_year + 1900);
	sprintf(month, "%02d", tm.tm_mon + 1);
	sprintf(day, "%02d", tm.tm_mday);

	strcpy(currentTime, year);
	strcat(currentTime, "-");
	strcat(currentTime, month);
	strcat(currentTime, "-");
	strcat(currentTime, day);

	stockListFile = fopen("../stock.list", "r");

	while(fscanf(stockListFile, "%s %s %s", company, symbol, url) != EOF)
	{
		insertScriptFile = fopen("insertScript.html", "r");

		strcpy(pathHtml, "../data_html/");
		strcat(pathHtml, currentTime);
		strcat(pathHtml, "/");
		strcat(pathHtml, company);
		strcat(pathHtml, "/");
		
		strcpy(pathHtmlFile, pathHtml);
		strcat(pathHtmlFile, "finance?q=");
		strcat(pathHtmlFile, symbol);
		strcat(pathHtmlFile, ".html");

		htmlFile = fopen(pathHtmlFile, "a");

		while(fgets(scriptBlock, MAX_BLOCK, insertScriptFile) != NULL)
		{
			fputs(scriptBlock, htmlFile);
		}

		fclose(htmlFile);
		fclose(insertScriptFile);
	}

	fclose(stockListFile);

	return 0;
}
