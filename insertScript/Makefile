#
# ====================================================
# Valualize Graphic (http://graphic.valualize.com)
# 
# insertScript
# 
# author: Jungtaek Kim
# mail: jungtaek.kim@jt-inc.net
# site: http://www.jt-inc.net
# 
# ====================================================
# Description
# 
# Insert the script which get data.
# 
# ====================================================
# Version
# 
# created on 2014.05.13
#
# ====================================================
# 

CC = gcc
OBJS = insertScript.o
TARGET = insertScript.out

.SUFFIXES : .c .o

all : $(TARGET)

$(TARGET) : $(OBJS)
	$(CC) -o $@ $(OBJS)

clean :
	rm -f $(OBJS) $(TARGET)

getData.o : insertScript.c insertScript.h ../path.h ../max.h
