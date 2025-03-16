import datetime

now_time = datetime.datetime.now()

wrfile =  open('users_stats.txt', 'w')

with open(r"forum_users.txt") as file:
    for string in file:
        temp_data = string.rstrip()
        temp_data = temp_data.split('\t')
        lifetime1 = datetime.datetime.strptime(temp_data[2], '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(temp_data[1], '%Y-%m-%d %H:%M:%S')
        lifetime2 = now_time - datetime.datetime.strptime(temp_data[2], '%Y-%m-%d %H:%M:%S')
        print(f'{temp_data[0]}\t{lifetime1.days}\t{lifetime2.days}', file = wrfile)

        

