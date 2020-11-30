from ImpConn import *

def Messaged(info,number,From,To,Date):
	msg = info+" Start: "+From+" To: "+To+" Date: "+Date
	url = "https://www.fast2sms.com/dev/bulk"
	payload = "sender_id=FSTSMS&message="+str(msg)+"&language=english&route=p&numbers="+str(number)
	headers = {
	'authorization': "n2r3vSVmdsFPM9OkcqwUXKEHplzLyYtZ807jCRBNToIAxGe6QiJKBCRzylfgPjZnv5mLboYEptq2XHwi",
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)

def Messagec(info,number,From,To,Date):
	msg = info+" Name: "+From+" Surname: "+To+" Mobile: "+Date
	url = "https://www.fast2sms.com/dev/bulk"
	payload = "sender_id=FSTSMS&message="+str(msg)+"&language=english&route=p&numbers="+str(number)
	headers = {
	'authorization': "n2r3vSVmdsFPM9OkcqwUXKEHplzLyYtZ807jCRBNToIAxGe6QiJKBCRzylfgPjZnv5mLboYEptq2XHwi",
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)
