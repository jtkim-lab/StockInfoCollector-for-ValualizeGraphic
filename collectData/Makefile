#
# ====================================================
# Valualize Graphic (http://graphic.valualize.com)
# 
# collectData
# 
# author: Jungtaek Kim
# mail: jungtaek.kim@jt-inc.net
# site: http://www.jt-inc.net
# 
# ====================================================
# Description
# 
# Collect data which is in the specific directory.
# 
# ====================================================
# Version
# 
# created on 2014.05.18
#
# ====================================================
# 

CC = gcc
OBJS = collectData.o
TARGET = collectData

.SUFFIXES : .c .o

all : $(TARGET)

$(TARGET) : $(OBJS)
	$(CC) -o $@ $(OBJS)

clean :
	rm -f $(OBJS) $(TARGET)

getData.o : collectData.c collectData.h
