import pandas as pd
import os

input_file_path = "/home/amol-murme/combine_df/All_Data_Files/"
output_file_path = "/home/amol-murme/combine_df/"


excel_file_list = os.listdir(input_file_path)

#excel_file_list

df = pd.DataFrame()

#Run a for loop to loop through each file in the list
for excel_files in excel_file_list:
 #check for .xlsx suffix files only
 if excel_files.endswith(".xlsx"):
 
    df1 = pd.read_excel(input_file_path+excel_files,nrows=5)
 #append each file into the original empty dataframe
 df = pd.concat([df,df1],axis=0)
 df_cols = df.columns.to_list()
 temp_cols = df1.columns.to_list()

 #print(df_cols)
 #print(temp_cols)
 if len(df_cols) < len(temp_cols):
   print(len(list(set(temp_cols) - set(df_cols))))
 else:  
   print(len(list(set(df_cols) - set(temp_cols))))

#transfer final output to an Excel (xlsx) file on the output path 
df.to_excel(output_file_path+"Consolidated_file1.xlsx")