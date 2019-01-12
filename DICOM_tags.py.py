# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 01:42:23 2019

@author: sumit
"""

import pydicom
import os

#finding the .dcm files in a folder
dcm_files = os.listdir('C:\\DCM_FILES')

for each_file in dcm_files:
  #accessing and reading the dcm files one by one.
  filename = each_file
  ds = pydicom.dcmread("C:\\DCM_FILES\\"+filename)
  
  #writing the tags of dcm files in a .txt file as an output
  fp = open(str(filename)+"_output_text_file.txt","w")
  
  try:
    fp.write("List of all dicom tags of "+str(filename)+" file.\n\n")
    
    try:
      for tag in ds.dir():
        fp.write(tag+"\n")
  
    except:
      continue
  
  finally:
    fp.close()
    
#END OF FILE

