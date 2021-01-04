from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext'] # textarea에서 input하는 데이터
    words = text.split()
    word_dic = {}
    for word in words:
        word_dic[word] = word_dic.get(word, 0) + 1

    return render(request,'result.html', {'full' : text, 'length' : len(words), 'dictionary' : word_dic.items()})
