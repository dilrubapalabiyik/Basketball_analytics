import re

file_needed  = open("/Users/dilruba_p/Desktop/table1.txt","r")

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

row =[]
columns = []

q = 1

for line in lines:
	if(in_table and end_of_table):
		break
	else:
		in_columns = bool(in_columns_sign.search(line))
	
		print(q)
		print("in_columns: "+str(in_columns))

		in_row = bool(in_rows_sign.search(line))
	
		print("in_row: "+str(in_row))

		end_of_table = bool(end_of_table_sign.search(line))

		print("end_of_table: "+str(end_of_table))
		print("in_table: " +str(in_table)+'\n')


		if(in_table and in_columns and in_row==False and line.count(' ')<=1):
			columns.append(line.strip())
		elif((in_table and in_columns and in_row == True)or(in_table and in_columns and line.count(' ')>1)):
			row.append(line.split('\t'))	
		elif(in_table and end_of_table):
			break
		elif(line.rstrip() == 'Overall Offense'):
			in_table = True
			columns.append(line.rstrip())

	
	q=q+1

print(len(row))
print(columns)

for i in range(len(row)):
	print(row[i])

print("length of columns : "+ str(len(columns)))












