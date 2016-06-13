# encoding: utf-8
import json

from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, ListView
from .models import Picture
from .response import JSONResponse, response_mimetype
from .serialize import serialize



from django.shortcuts import render

class PictureCreateView(CreateView):
    model = Picture
    #template_name="upload_template.html"
    fields = "__all__"
    #def as_view(request,id, *args, **kwargs):
    #根據號碼來判定目前是那個MRAPP，然後將資料存入app_run之後帶入template
    def get_context_data(self, **kwargs):
        from app.models import MRAPP
        app_run = MRAPP.objects.get(id = self.args[0])
        self.request.session['app_id']=self.args[0]
        ctx = super(PictureCreateView, self).get_context_data(**kwargs)
        ctx['app_run'] = app_run  # add something to ctx
        ctx['username'] = self.request.user.username
        return ctx

        #return render(request, 'fileupload/picture_form.html', {"app_run":app_run})

    def form_valid(self, form): #當檔案正確上傳之後，將進入這個function
        from app.models import MRAPP
        from app.models import file_log
        from django.contrib.auth.models import User
        import os
        self.object = form.save()

        app_run = MRAPP.objects.get(id = self.args[0])
        #app_run.info_html3 = app_run.info_html3 + self.object.__unicode__()
        app_run.save()


        app_user = User.objects.get(username = self.request.user)

        

        #newfile = file_log(user = app_user.email ,fname = self.object.__unicode__(), MRAPP_id = app_run.id)
        newfile = file_log(user_id = self.request.user.id ,
            fname = os.path.basename(self.object.__unicode__()), MRAPP_id = app_run.id)
        newfile.save()
        
        #因為要開放demo使用者，每個demo使用的人email不一樣
        if self.request.user.username == 'demo':
            user_email = self.request.POST.get('email')
        else:
            user_email = self.request.user.email

        
        

        txt = app_run.name + '\n' + app_run.name + '\n' + user_email + '\n'
        txt += newfile.fname + '\n' + app_run.cmd + '\n'
        txt += app_run.apptype + '\n' + self.request.user.username + '\n'
        txt += str(newfile.id) + '\n'
             

        from django.conf import settings
        print txt
        print os.path.join(settings.MEDIA_ROOT,self.object.__unicode__() + '.info')
        with open(os.path.join(settings.MEDIA_ROOT,self.object.__unicode__() + '.info'), 'a') as the_file:
            the_file.write(txt)
        '''
        //Write info file for the uploaded data
        /*$myfile = fopen($file_path.".info", "w");
        $orig_name=$name;
        $uniqid = $_POST['APPNAME'].'_' . uniqid();
        $name=$uniqid.'.'.pathinfo($name, PATHINFO_EXTENSION); //HTY
        import string, time, math, random
 
        def uniqid(prefix='', more_entropy=False):
            m = time.time()
            uniqid = '%8x%05x' %(math.floor(m),(m-math.floor(m))*1000000)
            if more_entropy:
                valid_chars = list(set(string.hexdigits.lower()))
                entropy_string = ''
                for i in range(0,10,1):
                    entropy_string += random.choice(valid_chars)
                uniqid = uniqid + entropy_string
            uniqid = prefix + uniqid
            return uniqid
        '''

        #################################################
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(content=data, status=400, content_type='application/json')
'''
class BasicVersionCreateView(PictureCreateView):
    template_name_suffix = '_basic_form'


class BasicPlusVersionCreateView(PictureCreateView):
    template_name_suffix = '_basicplus_form'


class AngularVersionCreateView(PictureCreateView):
    template_name_suffix = '_angular_form'


class jQueryVersionCreateView(PictureCreateView):
    template_name_suffix = '_jquery_form'
    '''


class PictureDeleteView(DeleteView):
    model = Picture

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class PictureListView(ListView):
    pass
    '''model = Picture

    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset() ]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response'''
