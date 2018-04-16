'''
install packages 
"sudo pip install bitstring"
"sudo pip3 install bitstring"
"sudo pip install flask"
"sudo pip3 install flask"

how to execute this code

Note: place index.html in "templates" folder in same folder as the program is placed

1) go to that folder in which the program is stored using cd folder_name

2) open terminal ("ctrl+alt+t")

3) type the folloing commands to run this program
    "python3 A3.py"
    and hit enter
    click on the link "http://localhost:5000/"
    this will open the web browser and now run give input to the program on web page

follow the instructions

'''

from bitstring import BitArray  # Bitstrings can be constructed from integers (big and little endian), hex, octal, binary, strings or files.
from flask import Flask      # Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.
from flask import request    # Flask is used for web tools in python
# The Flask request object contains the data that the client (eg a browser) has sent to your app.
from flask import render_template # render_template object is used to use templates from flask
app = Flask(__name__)  # initialization of flask.

def booth(m,r,x,y):         # starting booths logic
	totalLength=x+y+1
	mA=BitArray(int=m,length=totalLength) # convert 1st no (int data) into binary and store it in mA with total length of 17 bits (16+carry)
	print (mA)
	A=mA<<(y+1)  # left shift mA by 1 bit
	print (A)
	mA1=BitArray(int=-m,length=totalLength)  # convert 2nd no (int data) into binary and store it in mA1 with total length of 17 bits (16+carry)
	S=mA1<<(y+1)  # left shift mA1 by 1 bit
	P1=BitArray(int=r,length=y)        # convert 2nd no (int data) into binary and store it in p1 with total length of 8 bits (as y=8)
	P1.prepend(BitArray(int=0,length=x)) # pre-append converted 1st no (int data) into binary at p1. now p1 is of 16 bits.
	P=P1 << (1) # left shitf operation on p1 and store it in p
	print ("A : ",A.bin)    #print binary of A
	print ("S : ",S.bin)    #print binary of S
 
	for i in range(1,y+1):              # check for -ve sign in input and output.
		if P[-2:] == '0b01':            # 1st no contains -ve sign then ans also contain -ve sign
			P=BitArray(int=P.int+A.int,length=totalLength) # add -ve sign to answer
		elif P[-2:] == '0b10':           # 2nd no contains -ve sign then ans also contain -ve sign
			P=BitArray(int=P.int+S.int,length=totalLength) # add -ve sign to answer
		P=BitArray(int=(P.int >>1),length=P.len)   # convert answer into binary and int. 
	P = P[:-1]
	print ("P : ",P.bin)    # print binary i=on terminal
	return P.bin,P.int      # print binary + integer on web page


@app.route('/')
def f():
	return render_template("index.html")   # use this "index.html" file as template

@app.route('/',methods=['POST'])
def g():
	text1 = int(request.form['text1'])  # 1st no input on web page
	text2 = int(request.form['text2'])  # 2nd no input on web page
	n,m=booth(text1,text2,8,8)          # giving that two nos to booths algorithm above.
	return "Answer in binary: "+str(n)+"<br>Answer: "+str(m)   # print binary + integer on web page
   
if __name__ == '__main__':      # main function
	app.run('localhost',debug=True)   # run output on localhost:5000
