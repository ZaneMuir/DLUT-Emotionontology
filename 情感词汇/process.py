import xlrd

data=xlrd.open_workbook('情感词汇.xlsx')
table=data.sheets()[0]
data_list = []

for index in range(len(table.col(0))):
    data_list.append(table.row_values(index))
#data_list.append(table.row_values(1))
with open('情感词汇.csv', 'w') as out_file:
    for index in range(len(data_list)):
        for item in range(len(data_list[index])):
            out_file.write(data_list[index][item].__str__()+', ')
        out_file.write('\n')
print('ok')
