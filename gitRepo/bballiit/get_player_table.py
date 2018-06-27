import re
import csv
def get_player_table(player_name,player_table_name):


	file_needed  = open('/Users/dilruba_p/Desktop/player.txt/"+player_name+".txt","r")
	lines = []

	for line in file_needed:
		lines.append(line)

	in_table = False
	in_row = False
	in_columns = False
	end_of_table = False

	in_columns_sign = re.compile(r'([^\t])')
	in_rows_sign = re.compile(r'([\t])')
	end_of_table_sign = re.compile(r'^\s*$')

	row_1 =[]
	columns_1 = []

	for line in lines:
		if(in_table and end_of_table):
			break
		else:
			in_columns = bool(in_columns_sign.search(line))
		
			print("in_columns: "+str(in_columns))

			in_row = bool(in_rows_sign.search(line))
		
			print("in_row: "+str(in_row))

			end_of_table = bool(end_of_table_sign.search(line))

			print("end_of_table: "+str(end_of_table))
			print("in_table: " +str(in_table)+'\n')


			if(in_table and in_columns and in_row==False and line.count(' ')<=1):
				columns_1.append(line.strip())
			elif((in_table and in_columns and in_row == True)or(in_table and in_columns and line.count(' ')>1)):
				row_1.append(line.strip().split('\t'))	
			elif(in_table and end_of_table):
				break
			elif(line.rstrip() == player_table_name):
				in_table = True
				columns_1.append(line.rstrip())

	print(len(row_1))
	print(columns_1)

	for i in range(len(row_1)):
		print(row_1[i])

	print("length of columns : "+ str(len(columns_1)))

	with open('/Users/dilruba_p/Desktop/Bball_Proj_Tables/Player2.0_CSVs/'+player_name+player_table_name+'.csv','w', newline = '') as ft:
		a = csv.writer(ft,delimiter = ',')
		a.writerow(columns_1)
		a.writerows(row_1)
