#A python scripts to find files in a folder and find contents that follows a string,
#write the filename and found contents into an excel
import os, xlsxwriter,sys

#Get path from the user
user_path=os.path.normpath(input("Store all *.txt files in a folder\nEnter path for files:"))
if os.path.isdir(user_path):
    ListofFiles = list(os.listdir(user_path))
else:
    print("Invalid path!!!")
    sys.exit()
#print filenames
#print("Files in Directory",ListofFiles,"End")

os.chdir(user_path)
#function to check substring
def find(substr, infile, outfile,row,col):
  with open(infile,'r') as a, open(outfile, 'a') as b:
   for line in a:
    if substr in line:
     worksheet.write_column(row, col, [line])
     #print(line + '\n')

#write file names to excel file
workbook = xlsxwriter.Workbook("OutputFile.xlsx")
worksheet = workbook.add_worksheet()

sub_string_to_find=input("Enter the Substring to look:")

#column names for output file
worksheet.write_column(0, 0,["File Name"])
worksheet.write_column(0, 4,["Data found in File"])

col = 4
#for each file name check for substring
for row, data in enumerate(ListofFiles):
    if data.endswith(".tdl"):
        worksheet.write_column(row+1, 0, [data])
        file1 = str(data)
        find(sub_string_to_find, file1, "OutputFile.xlsx", row+1, col)
        row+=1

workbook.close();

print("\nOut file will be created in the folder specified. :)\n")