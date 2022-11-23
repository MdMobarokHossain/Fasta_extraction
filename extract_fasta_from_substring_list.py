output = {}
curr_head = ''
curr_seq = ''
genome_list = [1]

for line in open('assembly.fasta'):
    if '>' in line:
        output[curr_head] = curr_seq
        curr_head = ''
        curr_seq = ''
        curr_head += line.replace('\n', '')
    elif '\n' != line:
        curr_seq += line.replace('\n', '')

for keys,values in output.items():
    k=keys.strip().split(" ")
    # print(k)
    kk=(k[0].split(","))
    p=(kk[0].rstrip(",").split('>'))
    # print(len(p))
    if(len(p)== 1):
        continue
    else:
        if(int(p[1]) in genome_list ):
            print(keys + "\n" + values)
            # print('/n')
            # print(values) 

    # print(type(kk))

	# p=kk.strip().split(",")
	# print (p)
	#if (int(kk[1]) in genome_list):
    		#print((keys) + '\t' + (values))
    	
