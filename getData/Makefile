#
# ====================================================
# Valualize Graphic (http://graphic.valualize.com)
# 
# getData
# 
# author: Jungtaek Kim
# mail: jungtaek.kim@jt-inc.net
# site: http://www.jt-inc.net
# 
# ====================================================
# Description
# 
# Get stock data.
# 
# ====================================================
# Version
# 
# created on 2014.05.13
#
# ====================================================
# 

CC = gcc
OBJS = getData.o
TARGET = getData

.SUFFIXES : .c .o

all : $(TARGET)

$(TARGET) : $(OBJS)
	$(CC) -o $@ $(OBJS)

clean :
	rm -f $(OBJS) $(TARGET)

getData.o : getData.c getData.h
