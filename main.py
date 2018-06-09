import sys
from User.table import table

Table = table()

input_file = sys.argv[1]
input_test_file = sys.argv[2]
file_prefix = './data/'
output_file = file_prefix + input_file + '_prediction.txt'
input_file = file_prefix + input_file
input_test_file = file_prefix + input_test_file

Table.add_user(input_file)
Table.add_test(input_test_file)
Table.test_fill(output_file)



