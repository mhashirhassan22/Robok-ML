from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from .forms import ImageForm
from django.views import View
from django.views.generic.edit import FormView
from scripts.infer import main
from django.core.files.storage import default_storage


@method_decorator(login_required, name='dispatch')
class index(View):

    def get(self,request):
        form = ImageForm()
        context = {
            'form':form
        }
        return render(request, 'index.html',context=context)

    def post(self,request):
        form = ImageForm(request.POST, request.FILES)
        model = request.POST.get('model')   # fetch model selection of user from dropdown
        image = request.FILES.getlist('uploaded_image')
        count = len(image)
        print(image)
        if form.is_valid():
            ids = []
            for i in image:
                obj = ImageRequest.objects.create(user=request.user,uploaded_image=i)
                obj.save()
                ids.append(obj)
            if str(model) == 'robok_depthnet':  # write elif for your own model
                main("checkpoint/checkpoint.ckpt",(320,704),None,None,image,ids)    # import your function at start of file and call that in elif
            else:
                for i in ids:
                    i.result = i.uploaded_image
                    i.save()
            return render(request, 'images.html',context={"results":ids})
        else:
            print(form.errors)
            print("form not valid")
            return redirect('home:index')

@login_required
def Results(request):
    result = None
    try:
        result = ImageRequest.objects.filter(user=request.user).order_by('-created_at')
    except:
        pass
    return render(request,'images.html', {"results":result})
        
