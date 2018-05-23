#import glob
#import iglob
import pprint
import os


#glob.iglob("*.txt")

f_ist=os.listdir('C:\\Users\\pekhterev\\PycharmProjects\\p4ne\\Lab1.5')
ip_list=[]

for cur_file_name in f_ist:
#    print(cur_file_name)
    with open(cur_file_name) as f:
        for cur_file in f:
            f_as_lines = list(cur_file)
            for next_line in f_as_lines:
                if next_line.find(' ip address '):
                    ip_list.append(next_line)
                   # print (next_line)
#
            # print (f_as_lines)
#           cur_line = str(f_as_lines.find(" ip address ")))
            #ip_list.append(str("1")
            print(ip_list)



