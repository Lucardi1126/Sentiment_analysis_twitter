
with open('datos.txt', 'r') as file_obj:
    file_cont = file_obj.readlines()

    retweets = ''
    net_score = ''


    for line in file_cont:
        spl_line = line.split(',')

        retweets =  retweets + '\n' + spl_line[0]
        net_score = net_score + spl_line[-1]

#print(retweets, '\n')
print(net_score)

        

    
