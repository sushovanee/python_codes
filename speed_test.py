# Python program to test 
# internet speed 

import speedtest 

st = speedtest.Speedtest() 

# option = int(input('''What speed do you want to test: 

# 1) Download Speed 

# 2) Upload Speed 

# 3) Ping 

# Your Choice: ''')) 


# if option == 1: 

#     print('Download Speed: ' + str((float(st.download()))/(1024*1024)) + ' MBPS')
     
# elif option == 2: 

# 	print('Upload Speed: ' + str((float(st.upload()))/(1024*1024)) + ' MBPS') 

# elif option == 3: 

# 	servernames =[] 

# 	st.get_servers(servernames) 

# 	print(st.results.ping) 

# else: 

# 	print("Please enter the correct choice !") 
def speed_check():
	action_list = ['Download' ,'Upload', 'Ping']
	for entry in action_list:
		print('Checking ' + str(entry) + ' speed....')
		if entry == 'Download':
			print('Download Speed: ' + str((float(st.download()))/(1024*1024)) + ' mbps')
		elif entry == 'Upload':
			print('Upload Speed: ' + str((float(st.upload()))/(1024*1024)) + ' mbps')
		else:
			servernames = []
			st.get_servers(servernames)
			print(st.results.ping)

# speed_check()