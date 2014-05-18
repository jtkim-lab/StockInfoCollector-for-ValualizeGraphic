#
# ====================================================
# Valualize Graphic (http://graphic.valualize.com)
# 
# getHtml
# 
# author: Jungtaek Kim
# mail: jungtaek.kim@jt-inc.net
# site: http://www.jt-inc.net
# 
# ====================================================
# Description
# 
# Get html files at Google Finance.
# 
# ====================================================
# Version
# 
# created on 2014.05.13
#
# ====================================================
# 

CC = gcc
OBJS = getHtml.o
TARGET = getHtml.out

.SUFFIXES : .c .o

all : $(TARGET)

$(TARGET) : $(OBJS)
	$(CC) -o $@ $(OBJS)

clean :
	rm -f $(OBJS) $(TARGET)

getData.o : getHtml.c getHtml.h ../path.h ../max.h
