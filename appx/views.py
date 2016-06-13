"""
Definition of views.
"""

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )



def T1_input(request):
    from app.forms import BootstrapCurveFittingForm
        
    return render(
        request,
        'app/inp_T1.html',
        context_instance = RequestContext(request,
        { 
            'title':'T1 Fitting',
            'form': BootstrapCurveFittingForm,
               })
    )


def T1_result(request):
    import pyFitMR.T1_lib as T1_lib
    
    t_value = request.POST.get('t_value')
    y_value = request.POST.get('y_value')
    fitted_result_dict = T1_lib.T1fit(t_value, y_value)
    return render(
        request,
        'app/resultpage.html',
        context_instance = RequestContext(request, fitted_result_dict)
       )


def T1LL_input(request):
    from app.forms import BootstrapCurveFittingForm
        
    return render(
        request,
        'app/inp_T1LL.html',
        context_instance = RequestContext(request,
        { 
            'title':'Look-Locker T1 Fitting',
            'form': BootstrapCurveFittingForm,
               })
    )


def T1LL_result(request):
    import pyFitMR.T1LL_lib as T1LL_lib
    
    t_value = request.POST.get('t_value')
    y_value = request.POST.get('y_value')
    fitted_result_dict = T1LL_lib.T1LLfit(t_value, y_value)
    return render(
        request,
        'app/resultpage.html',
        context_instance = RequestContext(request, fitted_result_dict)
       )

def T2_input(request):
    from app.forms import T2Form
         
    return render(
        request,
        'app/inp_T2.html',
        context_instance = RequestContext(request, 
		{'title':'T2 Fitting Input',
	            'form': T2Form}))		

def T2_result(request):
    
    import pyFitMR.T2_lib as T2_lib
    
    t_value = request.POST.get('t_value')
    y_value = request.POST.get('y_value')
    fitted_result_dict = T2_lib.T2fit(t_value, y_value)  
    
    return render(
        request,

        'app/resultpage.html',
        context_instance = RequestContext(request, fitted_result_dict)
    )



def AHA17_input(request):
    from app.forms import AHAForm        
    return render(
        request,
        'app/inp_AHA17.html',
        context_instance = RequestContext(request, 
        {'title':'AHA 17 Input',
                'form': AHAForm}))      

def AHA17_result(request):
    import pyFitMR.AHA17_lib as AHA17_lib
    
    t_value = request.POST.get('t_value')
  
    result_dict=AHA17_lib.Plot17(t_value)

    return render(request,'app/resultpage.html',
        context_instance = RequestContext(request, result_dict)
       )
	   
def perfusion_input(request):
    from app.forms import perfusionForm
         
    return render(
        request,
        'app/inp_perfusion.html',
        context_instance = RequestContext(request, 
		{'title':'perfusion Fitting Input',
	            'form': perfusionForm}))		

def perfusion_result(request):
    
    import pyFitMR.perfusion_lib as perfusion_lib
    
    t_value = request.POST.get('t_value')
    y_value = request.POST.get('y_value')
    fitted_result_dict = perfusion_lib.perfusionfit(t_value, y_value)  
    
    return render(
        request,

        'app/resultpage.html',
        context_instance = RequestContext(request, fitted_result_dict)
    )


def fcmat_input(request):
    from app.models import Document
    from app.forms import DocumentForm
    from django.http import HttpResponseRedirect
    from django.core.urlresolvers import reverse
    from django.conf import settings #or from my_project import settings
    import os
    # Handle file upload
    #print 
    
    form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    #documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'app/inp_fcmat.html',
        {'title':'Displaying Functional Connectivity Matrix','form': form},
        context_instance=RequestContext(request)
    )
    

def fcmat_result(request):
    from app.models import Document
    from app.forms import DocumentForm
    from django.http import HttpResponseRedirect
    from django.core.urlresolvers import reverse
    from django.conf import settings #or from my_project import settings
    import os
    import pyFitMR.fcmat_lib as fcmat_lib
    from django.conf import settings #or from my_project import settings
    uploadedfile = False
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            matfile = os.path.join(settings.MEDIA_ROOT,newdoc.docfile.name)
            uploadedfile = True
        else:
            FILE_ROOT = os.path.abspath(os.path.dirname(__file__))
            matfile = os.path.join(FILE_ROOT,'CC_testfile.mat')
    else:
        #form = DocumentForm() # A empty, unbound form
        return HttpResponseRedirect(reverse('fcmat_input'))

    import scipy.io
    #import matplotlib.pyplot as plt
    mat = scipy.io.loadmat(matfile)
    FC=mat['connectome']
    #FC=mat.items()[0][1]
    #plt.imshow(FC)
    #print FC
    script, div = fcmat_lib.plot(FC)
    if uploadedfile:
        newdoc.docfile.delete()
    return render(request, 'app/fcmat_result.html', {"the_script":script, "the_div":div})




@login_required
def list_MRAPP(request):
    from app.models import MRAPP, file_log
    """retrun restaurant list

    :request: client request
    :returns: restaurant list webpage

    """
    MRAPPs = MRAPP.objects.all()
    file_logs = file_log.objects.all()
    #request.session['restaurants'] = restaurants
    return render(request, 'app/list_MRAPP.html', {"MRAPPs":MRAPPs,
        "file_logs":file_logs,})
    #return render_to_response('app/list_MRAPP.html', locals())



