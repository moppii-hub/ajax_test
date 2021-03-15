from django.views import generic
from .models import Post, InputRecord
from django.http import JsonResponse
from django.shortcuts import render


class PostList(generic.ListView):
    model = Post



def ajax_post_add(request):
    title = request.POST.get('title')
    post = Post.objects.create(title=title)
    post.save()
    d = {
        'title': post.title,
    }
    return JsonResponse(d)


def post_list(request):
    post = Post.objects.all()
    data = {}
    data["post"] = post
    return render(request, "post_list.html", data)



    # input_str = models.CharField('input_str', max_length=512)
    # type_str = models.CharField('type_str', max_length=32)
    # username_str = models.CharField('username_str', max_length=128)
    # dt_str = models.CharField('dt_str', max_length=128)
    # x_str = models.CharField('x_str', max_length=16)
    # y_str = models.CharField('y_str', max_length=16)

def clicktest_add(request):
    input_str_ = request.POST.get('title')
    input_str_list = input_str_.split('|')
    dt_str_ = input_str_list[0]
    type_str_ = input_str_list[1]
    username_str_ = input_str_list[2]
    x_str_ = input_str_list[3]
    y_str_ = input_str_list[4]
    ir = InputRecord.objects.create(input_str=input_str_, dt_str=dt_str_, 
    type_str=type_str_, username_str=username_str_, x_str=x_str_, y_str=y_str_)
    ir.save()
    ir_all = InputRecord.objects.all()
    datas_ = []
    for ir_ in ir_all:
        datas_.append(ir_.dt_str)
    data_dict = {'datas' : datas_}
    return JsonResponse(data_dict)


def clicktest_list(request):
    ir_all = InputRecord.objects.all()
    data = {}
    data["post"] = ir_all
    return render(request, "clicktest.html", data)

