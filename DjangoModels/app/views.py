from django.http import HttpResponse

def first(request):
    html = """
     <h1> First Page </h1>
     <a href="second/">Second Page</a>
     """

    return HttpResponse(html)

def second(request):
    html = """
     <h1> Second Page </h1>
     <a href="../">First Page</a>
     """

    return HttpResponse(html)