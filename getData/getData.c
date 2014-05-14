#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "getData.h"

int main()
{
	FILE* infile;

	char company[MAX_COMPANY];
	char url[MAX_URL];
	
	char year[5];
	char month[3];
	char day[3];
	char currentTime[11];

	char commandMakeRootDirectory[MAX_COMMAND];
	char commandMakeDirectory[MAX_COMMAND];
	char commandGetHtml[MAX_COMMAND];

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
	strcat(commandMakeRootDirectory, ROOT_PATH);
	strcat(commandMakeRootDirectory, currentTime); 

	system(commandMakeRootDirectory);	

	infile = fopen("stock.list", "r");

	while(fscanf(infile, "%s %s", company, url) != EOF)
	{
		memset(commandMakeDirectory, '\0', MAX_COMMAND);
		memset(commandGetHtml, '\0', MAX_COMMAND);

		strcpy(commandMakeDirectory, "mkdir ");
		strcat(commandMakeDirectory, ROOT_PATH);
		strcat(commandMakeDirectory, currentTime);
		strcat(commandMakeDirectory, "/");
		strcat(commandMakeDirectory, company);

		strcpy(commandGetHtml, "wget ");
		strcat(commandGetHtml, "-P ");
		strcat(commandGetHtml, ROOT_PATH);
		strcat(commandGetHtml, currentTime);
		strcat(commandGetHtml, "/");
		strcat(commandGetHtml, company);
		strcat(commandGetHtml, " ");
		strcat(commandGetHtml, url);

		system(commandMakeDirectory);
		system(commandGetHtml);
	}

	return 0;
}
