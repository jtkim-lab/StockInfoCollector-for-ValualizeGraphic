#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "getData.h"
#include "../max.h"
#include "../path.h"

int main()
{
	FILE* stockListFile;
	FILE* htmlFile;
	FILE* dataFile;

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

	char pathHtml[MAX_PATH];
	char pathHtmlFile[MAX_PATH];
	char pathDataFile[MAX_PATH];

	char closedPrice[MAX_DATA];
	char vol[MAX_DATA];
	char marketCap[MAX_DATA];

	char* pch1;
	char* pch2;

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
		memset(closedPrice, '\0', MAX_DATA);
		memset(closedPrice, '\0', MAX_DATA);
		memset(closedPrice, '\0', MAX_DATA);

		strcpy(pathHtml, "../data_html/");
		strcat(pathHtml, currentTime);
		strcat(pathHtml, "/");
		strcat(pathHtml, company);
		strcat(pathHtml, "/");

		strcpy(pathHtmlFile, pathHtml);
		strcat(pathHtmlFile, "finance?q=");
		strcat(pathHtmlFile, symbol);
		strcat(pathHtmlFile, ".html");

		htmlFile = fopen(pathHtmlFile, "r");

		printf("DEBUG: %s\n", pathHtmlFile);

		while(fgets(scriptBlock, MAX_BLOCK, htmlFile) != NULL)
		{
			if(strstr(scriptBlock, "<span class=\"pr\">") != NULL)
			{
				printf("DEBUG: %s\n", scriptBlock);

				fgets(scriptBlock, MAX_BLOCK, htmlFile);
				
				printf("DEBUG: %s\n", scriptBlock);
				pch1 = strchr(scriptBlock, '>');
				pch2 = strrchr(scriptBlock, '<');

				strncpy(closedPrice, pch1 + 1, pch2 - pch1 - 1);
				printf("DEBUG: closedPrice %s\n", closedPrice);
			}

			if(strstr(scriptBlock, "data-snapfield=\"vol_and_avg\">Vol / Avg.") != NULL)
			{
				printf("DEBUG: %s\n", scriptBlock);

				fgets(scriptBlock, MAX_BLOCK, htmlFile);
				fgets(scriptBlock, MAX_BLOCK, htmlFile);
				printf("DEBUG: %s\n", scriptBlock);
				pch1 = strchr(scriptBlock, '>');

				for (int i = 0; i < MAX_DATA; i++)
				{
					if(scriptBlock[i] == '\0')
						pch2 = &scriptBlock[i];
				}

				strncpy(vol, pch1 + 1, pch2 - pch1 - 1);
				printf("DEBUG: vol %s\n", vol);
			}

			if(strstr(scriptBlock, "data-snapfield=\"market_cap\">Mkt cap") != NULL)
			{
				printf("DEBUG: %s\n", scriptBlock);

				fgets(scriptBlock, MAX_BLOCK, htmlFile);
				fgets(scriptBlock, MAX_BLOCK, htmlFile);
				printf("DEBUG: %s\n", scriptBlock);
				pch1 = strchr(scriptBlock, '>');

				for (int i = 0; i < MAX_DATA; i++)
				{
					if(scriptBlock[i] == '\0')
						pch2 = &scriptBlock[i];
				}

				strncpy(marketCap, pch1 + 1, pch2 - pch1 - 1);
				
				printf("DEBUG: marketCap %s\n", marketCap);
			}
		}

		fclose(htmlFile);

		strcpy(pathDataFile, pathHtml);
		strcat(pathDataFile, company);
		strcat(pathDataFile, ".data");

		dataFile = fopen(pathDataFile, "w");
	
		printf("DEBUG: %s %s %s\n", closedPrice, vol, marketCap);
		fprintf(dataFile, "%s\n%s%s", closedPrice, vol, marketCap);	

		fclose(dataFile);
	}

	fclose(stockListFile);

	return 0;
}
