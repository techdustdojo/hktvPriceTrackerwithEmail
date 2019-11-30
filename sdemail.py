import smtplib, ssl
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr



def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

def sdemail(message):
	
	mta = "smtp.gmail.com"	#Mail transfer agent server
	
	port = 465	#465 for SMTP_SSL / 587 for .starttls()

	password = 'rrweokficgkatdxc'

	context = ssl.create_default_context()

	sendadd = 'techmaxwintest@gmail.com'
	
	recadd = 'techmaxwin@gmail.com'

#	recadd = ['techmaxwin@gmail.com','akpsvant@gmail.com']	# if mutiple reciver needed

	mime_message = MIMEText(message,'plain','utf-8')
	
	mime_message['From'] = _format_addr('hktvPriveTracker <%s>' % sendadd)
	
	mime_message['To'] =  _format_addr('I am your father <%s>' % recadd)
	
	mime_message['Subject'] = Header(message, 'utf-8').encode()
	

	with smtplib.SMTP_SSL(mta, port, context=context) as server:
		server.login(sendadd, password)
	#	server.set_debuglevel(1) #print out the debug message
		server.sendmail(sendadd,recadd, mime_message.as_string())	#(sender,recevier,message)
		server.quit
