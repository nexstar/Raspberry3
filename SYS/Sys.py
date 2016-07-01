def getMAC('wlan0'):
	try:
		str=open('/sys/class/net/'+interface+'/address').read()
	except:
		str="00:00:00:00:00:00"
	return  str[0:17]
