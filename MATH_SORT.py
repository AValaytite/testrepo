#!/usr/bin/env python
# -*- coding: cp1251 -*-# , "utf-8"
import fnmatch
import math
import os
import os.path

# from string import float, atoi, split, lstrip
def _percent_of_array(array,per):
    ar_len_per=int(len(array)*per);
    return array[ar_len_per];
from math import trunc, sqrt

def Average(lst):
    print("dd"+str(len(lst)))
    return sum(lst) / len(lst)


def sort_max(name,name2,name3):
    MAS=[];
    MAS2=[];
    f = open(name, "rb");
    data = f.read();
    lines = "".join(map(chr, data))
    del data;
    lines = lines.split("\r\n")
    f.close()
    f1 = open(name3, "w");
    for item1 in lines:
        if item1:
            line = item1.split("\t")
            MAS.append(math.fabs(float(line[1])));
            MAS2.append(math.fabs(float(line[2])));
            #f1.write(str(math.fabs(float(line[1]))) + "\t"+str(math.fabs(float(line[2]))) + "\n");
            f1.write(str(math.fabs(float(line[1])))  + "\n");
            #MAS.append(abs((float(line))));
    f1.close()
    MAS.sort();
    MAS2.sort();
    f = open(name2, "w");
    f.write(str(Average(MAS)) + "\n");
    f.write(str(_percent_of_array(MAS,0.95))+"\n");
    f.write(str(_percent_of_array(MAS,0.99))+"\n");
    f.write( "------horizontal-----------\n");
    f.write(str(Average(MAS2)) + "\n");
    f.write(str(_percent_of_array(MAS2, 0.95)) + "\n");
    f.write(str(_percent_of_array(MAS2, 0.99)) + "\n");
    f.close();
    del MAS, MAS2,line, item1,lines;
    return 1;

mask = '*.txt'
todir=input("input your folder") 
folderlist=os.listdir(todir);
for file in folderlist:
    if fnmatch.fnmatch(file,mask):
        name = os.path.join(todir,file);
        name2=os.path.join(todir,"stat_"+file);
        name3 = os.path.join(todir, "mod_" + file);
        sort_max(name, name2,name3)