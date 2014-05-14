#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "getHtml.h"
#include "../path.h"
#include "../max.h"

int main()
{
	FILE* stockListFile;
	FILE* htmlFile;

	char company[MAX_COMPANY];
	char symbol[MAX_SYMBOL];
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

	memset(commandMakeRootDirectory, '\0', MAX_COMMAND);
	strcpy(commandMakeRootDirectory, "mkdir ");
	strcat(commandMakeRootDirectory, "../data_html/");
	strcat(commandMakeRootDirectory, currentTime); 

	system(commandMakeRootDirectory);	

	stockListFile = fopen("../stock.list", "r");

	while(fscanf(stockListFile, "%s %s %s", company, symbol, url) != EOF)
	{
		strcpy(pathHtml, "../data_html/");
		strcat(pathHtml, currentTime);
		strcat(pathHtml, "/");
		strcat(pathHtml, company);
		strcat(pathHtml, "/");

		memset(commandMakeDirectory, '\0', MAX_COMMAND);
		memset(commandGetHtml, '\0', MAX_COMMAND);

		strcpy(commandMakeDirectory, "mkdir ");
		strcat(commandMakeDirectory, pathHtml);

		strcpy(commandGetHtml, "wget ");
		strcat(commandGetHtml, "-P ");
		strcat(commandGetHtml, pathHtml);
		strcat(commandGetHtml, " ");
		strcat(commandGetHtml, "--html-extension ");
		strcat(commandGetHtml, url);

		system(commandMakeDirectory);
		system(commandGetHtml);

		strcpy(commandCopyHtaccess, "cp ");
		strcat(commandCopyHtaccess, ".htaccess");
		strcat(commandCopyHtaccess, " ");
		strcat(commandCopyHtaccess, pathHtml);
		
		system(commandCopyHtaccess);
	}

	return 0;
}
