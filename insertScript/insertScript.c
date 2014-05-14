#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "insertScript.h"

int main()
{
	FILE* stockListFile;
	FILE* insertScriptFile;
	FILE* htmlFile;

	char company[MAX_COMPANY];
	char url[MAX_URL];
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
	insertScriptFile = fopen("insertScript.html", "r");

	while(fscanf(stockListFile, "%s %s", company, url) != EOF)
	{
		strcpy(pathHtml, ROOT_PATH);
		strcat(pathHtml, currentTime);
		strcat(pathHtml, "/");
		strcat(pathHtml, company);
		strcat(pathHtml, "/");
		
		strcpy(pathHtmlFile, pathHtml);
		strcat(pathHtmlFile, "finance?q=atvi.html");

		htmlFile = fopen("/root/ValualizeGraphic/data_html/2014-05-14/Activision_Blizzard/finance?q=atvi.html", "a");

		printf("\n%d\n", htmlFile);

		while(fgets(scriptBlock, MAX_BLOCK, insertScriptFile) != NULL)
		{
			fputs(scriptBlock, htmlFile);
		}
	}

	return 0;
}
