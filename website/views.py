from django.shortcuts import render, Http404, redirect, HttpResponse
from website.models import Video,Ticket, UserProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,login
from website.form import LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


# Django自带的"AuthenticationForm 登录验证
def detail_login(request):
    """登录验证"""
    context = {}
    if request.method == "GET":
        form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='listing')
    context['form'] = form
    return render(request, 'login_regist.html', context)

# 方法2：form表单验证
# def detail_login(request):
#     """登录view"""
#     context = {}
#     if request.method == "GET":
#         form = LoginForm
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         print(form)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#
#             if user:
#                 login(request, user)
#                 return redirect(to='listing')
#             else:
#                 return HttpResponse("<h1>Not found this user</h1>")
#
#     context['form'] = form
#     return render(request, 'login_regist.html', context)



# 注册
def detail_register(request):
    """注册功能"""
    context = {}
    if request.method == "GET":
        form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="detail_login")

    context['form'] = form
    return render(request, 'login_regist.html', context)




def listing(request, cate=None):
    """listing主页视图"""
    context = {}
    if cate is None:
        video_list = Video.objects.all()
    else:
        if cate == 'new':
            video_list = Video.objects.filter(new_choice=True)
        elif cate == 'editors':
            video_list = Video.objects.filter(editors_choice=True)
        else:
            video_list = Video.objects.all()   # 获取所有的视频信息

    page_data = Paginator(video_list, 9)   # 每页9个数据
    page_num = request.GET.get('page')

    try:
        video_list = page_data.page(page_num)  # get方法取哪一页
    except EmptyPage:
        video_list = page_data.page(page_data.num_pages)   # ?page=999加载最后一页
        # raise Http404('Not found this page')  第二种方法
    except PageNotAnInteger:
        video_list = page_data.page(1)  # ?page=23daf  加载第一页

    context['video_list'] = video_list
    return render(request, 'listing.html', context)


def detail(request,page_num):
    """详情页"""
    context = {}
    video = Video.objects.get(id=page_num)  # 投票的是哪个视频

    voter_id = request.user.profile.id  # 投票的是用户id

    like_counts = Ticket.objects.filter(choice='like', video_id=page_num).count()  #视频有多少like
    context['like_counts'] = like_counts

    #print(voter_id)
    try:
        user_ticker_for_this_video = Ticket.objects.get(voter_id=voter_id, video_id=page_num)
        context['user_ticker_for_this_video'] = user_ticker_for_this_video
        print(user_ticker_for_this_video)
    except:
        pass

    context['video'] = video
    return render(request,'detail.html',context)





def detail_voter_post(request,page_num):
    """post提交投票"""

    voter_id = request.user.profile.id   # 投票的是哪个用户

    try:
        user_ticker_for_this_video = Ticket.objects.get(voter_id=voter_id, video_id=page_num)
        user_ticker_for_this_video.choice = request.POST['vote']
        user_ticker_for_this_video.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, video_id=page_num, choice=request.POST['vote'])
        print(new_ticket)
        new_ticket.save()

    return redirect(to='detail',page_num=page_num)