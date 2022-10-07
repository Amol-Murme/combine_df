import pandas as pd
import os
working_dir = os.getcwd()
input_file_path = working_dir + "/All_Data_Files/"
output_file_path = working_dir +"/"


excel_file_list = os.listdir(input_file_path)

#excel_file_list

df = pd.DataFrame()
#Run a for loop to loop through each file in the list
df_list=[ ]
for excel_files in excel_file_list:
 #check for .xlsx suffix files only
 if excel_files.endswith(".xlsx"):
   temp = pd.read_excel(input_file_path+excel_files,nrows=5)
   str_temp = excel_files.split('.')
   id = str_temp[0][23:]
   id = "".join(id.split())
   temp['ID'] = id
   temp['ID'] = pd.to_datetime(temp['ID']).dt.date
   df_list.append(temp)
df = pd.concat(df_list,axis=0)
df.set_index('ID',inplace=True)
#transfer final output to an Excel (xlsx) file on the output path 
# print(df.head(25))
# print(df.info())

df.to_excel(output_file_path+"Consolidated_file8.xlsx")