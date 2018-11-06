import os

path = '/Users/Ryan/Desktop/huaxintong_log.txt'

path_base = '/Users/Ryan/Desktop/huaxintong_base.txt'

path_offset = '/Users/Ryan/Desktop/huaxintong_offset.txt'

last_done = "42"
	

if os.path.exists(path_base):
	os.remove(path_base)

if os.path.exists(path_offset):
	os.remove(path_offset)


file_base = open(path_base,"aw")
file_offset = open(path_offset,"aw")

file = open(path)
lines = file.readlines()

for i in range(len(lines)):
	elem = lines[i].split("] ")
	if len(elem) > 1:

		# if elem[1].split(",")[0].endswith("HWLs done"):
		# 	file_offset.close()
		# 	file_base.close()
		# 	if elem[1].split(",")[0].split()[0].strip() == "1":
		# 		os.rename(path_base,path_base+'_'+elem[1].split(",")[0].split()[0].strip()+".txt")
		# 		os.rename(path_offset,path_offset+'_'+elem[1].split(",")[0].split()[0].strip()+".txt")

		# 	if elem[1].split(",")[0].split()[0].strip() != last_done:
		# 		file_base_path = path_base+'_'+str(int(elem[1].split(",")[0].split()[0].strip())+1)+".txt"
		# 		file_offset_path = path_offset+'_'+str(int(elem[1].split(",")[0].split()[0].strip())+1)+".txt"
		# 		if os.path.exists(file_base_path):
		# 			os.remove(file_base_path)
		# 		if os.path.exists(file_offset_path):
		# 			os.remove(file_offset_path)
		# 		file_base = open(file_base_path,"aw")
		# 		file_offset = open(file_offset_path,"aw")

		if elem[1].split(",")[0].endswith("HWLs done"):
			file_base.write("\n"+"*********************************"+ elem[1].split(",")[0] +"****************************************"+"\n\n")
			file_offset.write("\n"+"*********************************"+ elem[1].split(",")[0] +"**************************************"+ "\n\n")


		elem2 = elem[1].split(":")
		if elem2[0].startswith("dla_reg"):
			# for j in range(i+1,len(lines)):
			# 	if (len(lines[j].split("] ")) > 1):
			# 		if lines[j].split("] ")[1].split(",")[0].endswith("HWLs done"):
			# 			#print(lines[j].split("] ")[1].split(",")[0])
			# 			num_done = lines[j].split("] ")[1].split(",")[0].split()[0].strip()
			# 			break

			op = elem2[0][4:len(elem2[0])]
			base = elem2[1].split("),")[0].split("(")[1].split(",")[0].strip()
			base = base[0:2] + "ffff" + (4-len(base[2:len(base)]))*"0" + base[2:len(base)]
			offset = elem2[1].split("),")[0].split("(")[1].split(",")[1].strip()
			offset = offset[0:2] + "ffff" + (4-len(base[2:len(offset)]))*"0" + offset[2:len(offset)]
			vertify = "0xffffffff"
			val = elem2[1].split("),")[1].split("(")[1].split(")")[0].strip()
			if len(val) == 10 and val[2] == 'c':
				val = val[0:2] + "8" + val[3:len(val)]

			note = "#"+lines[i-1].split("] ")[1].strip()
			if op == "reg_write":
				op = "write_reg"
				#print(num_done)
				result_for_base = op + " " + base + " " + val + " " + note #+ "(" + num_done + ")"
				result_for_offset = op + " " + offset + " " + val + " " + note  #+ "(" + num_done + ")"
				file_base.write(result_for_base+"\n")
				file_offset.write(result_for_offset+"\n")

			elif op == "reg_read":
				op = "read_reg"
				result_for_base = op + " " + base + " " + vertify + " " + val + " " + note  #+ "(" + num_done + ")"
				result_for_offset = op + " " + offset + " " + vertify + " " + val + " " + note #+ "(" + num_done + ")"
				file_base.write(result_for_base+"\n")
				file_offset.write(result_for_offset+"\n")


file.close()
file_base.close()
file_offset.close()

