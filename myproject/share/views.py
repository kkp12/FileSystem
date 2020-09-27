# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from .models import Upload
from django.http import HttpResponsePermanentRedirect,HttpResponse
import random
import string
import json
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.shortcuts import render
import os
from django.views.generic import View



class HomeView(View):
    """展示主页"""
    def get(self,request):
        """处理get请求"""
        return render(request, "base.html", {})
    
    def post(self,request):
        #如果有上传文件
        if request.FILES:
            file = request.FILES.get("file")
            name = file.name
            size = int(file.size)
            with open('static/file/'+name,'wb') as f:
                f.write(file.read())
            #生成随机8为纯数字的code
            code = ''.join(random.sample(string.digits,8))
            u = Upload(
                path = 'static/file/'+name,
                name = name,
                Filesize = round(size/1024,2),
                code = code,
                # 获取上传用户的ip地址
                PCIP = str(request.META['REMOTE_ADDR']),
            )
            u.save()
            #return HttpResponsePermanentRedirect("/s/"+code)
            return HttpResponseRedirect(reverse('MY'))


class DisplayView(View):
    """展示文件详细信息的视图类"""
    def get(self,request,code):
        #返回所有匹配的对象组成的列表
        u = Upload.objects.filter(code=str(code))
        if u:
            for i in u:
                i.DownloadDocount += 1
                i.save()
        return render(request, 'content.html',{"content":u})

class MyView(View):
    """用于展示用户自己的文件"""
    def get(self, request):
        IP = request.META['REMOTE_ADDR']
        #根据ip来区分不同用户的文件
        u = Upload.objects.filter(PCIP=str(IP))
        for i in u:
            # 访问量+1
            i.DownloadDocount += 1
            i.save()
        return render(request, 'content.html',{"content":u})


class AllView(View):
    """用于展示所有人的文件"""
    def get(self, request):
        u = Upload.objects.all()
        for i in u:
            # 访问量+1
            i.DownloadDocount += 1
            i.save()
        return render(request, 'content.html',{"content":u})




class SearchView(View):
    def get(self,request):
        keyword = request.GET.get("kw")
        u = Upload.objects.filter(name=str(keyword))
        data = {}
        if u:
            for i in range(len(u)):
                u[i].DownloadDocount += 1
                u[i].save()
                data[i]={}
                data[i]['download'] = u[i].DownloadDocount
                data[i]['filename'] = u[i].name
                data[i]['id'] = u[i].id
                data[i]['ip'] = str(u[i].PCIP)
                data[i]['size'] = u[i].Filesize
                data[i]['time'] = str(u[i].Datatime.strftime('%Y-%m-%d %H:%M'))
                data[i]['key'] = u[i].code

        return HttpResponse(json.dumps(data), content_type="application/json")



def delFile(request):
    file_id=request.POST['file_id']
    u = Upload.objects.get(id=file_id)
    if u:
        file_name = u.name
        os.popen('rm -f static/file/%s'%file_name)
        u.delete()
    #reverse函数是传urls中给网址命的名字进去就行，网址变了也没关系
    # return HttpResponseRedirect(reverse('MY'))
    return HttpResponse(json.dumps({'ret':'delsuccess'}))






        
