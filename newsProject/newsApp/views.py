from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsApp/index.html')

def moviesinfo(request):
    hmsg="Latest Movies Information"
    msg1="RRR is going to release on 30-07-2020"
    msg2="Ravinder is producing NTR's next movie"
    msg3="Sahoo is ready to release in second part of 2019"
    myDict = {'head_msg':hmsg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
    return render(request,'newsApp/news.html',context=myDict)

def sportsinfo(request):
    hmsg="Latest Sports Information"
    msg1="India won 2019 Worldcup"
    msg2="Kohli reached his 50th ODI hundred in Worldcup final match"
    msg3="Rohit sharma received MOS"
    myDict = {'head_msg':hmsg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
    return render(request,'newsApp/news.html',context=myDict)

def politicsinfo(request):
    hmsg="Latest Politics Information"
    msg1="Khajavali's party won in the 2024 elections"
    msg2="Khajavali's party won 160 seats"
    msg3="Khajvali's party CM candidates are Sai Naryana and Khajavali"
    myDict = {'head_msg':hmsg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
    return render(request,'newsApp/news.html',context=myDict)
