from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse

# FUNCTIONS FOR PATHS
def index(request):
    return HttpResponse("This is a bad request. Start with music route.")



def music(request):
    return HttpResponse("Artists: Masego, Jorja Smith, Galimatias")


def masego(request):
     return HttpResponse("Micah Davis (born June 8, 1993), by his stage name Masego, is an American musician who was born in Jamaica with South African heritage. Masego is an international, contemporary genre-bending entertainer who refers to his own music style as TrapHouseJazz or Emotion.")



def jorjaSmith(request):
    return HttpResponse("Smith has released several singles since January 2016 and collaborated with other artists, including Drake, Kali Uchis, and Stormzy. She released her debut extended play, Project 11, in November 2016. In 2018, she won the Brit Critics' Choice Award. Her debut studio album, Lost & Found, was released in June 2018 and peaked at number three on the UK Albums Chart.")



def galimatias(request):
    return HttpResponse("Born Matias Saabye Køedt, is a 26-year-old electronic artist from the small town of Fredericia in rural Denmark. He currently resides in Los Angeles, CA. Galimatias is most known for his 2015 EP release Urban Flora with American singer/songwriter Alina Baraz.")

