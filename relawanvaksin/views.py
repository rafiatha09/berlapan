from django.http import response,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import Form_relawan_vaksin
from .models import Model_relawan_vaksin
from django.views.generic import ListView, DetailView,TemplateView,View
 # Create your views here.
 #Views form daftar relawan vaksin
def index(request) :
    submitted = False
    response ={}
    form = Form_relawan_vaksin(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Daftar_relawan/?submitted=True')
    else :
        form = Form_relawan_vaksin
        if 'submitted' in request.GET :
            submitted = True

        # return redirect('/Daftar_relawan/selesai')
    response['form']= form
    response['submitted'] = submitted
    return render(request,'Daftar_relawan_vaksin.html',response)
   


# Hanya dapat diakses setelah login
@method_decorator(login_required, name='dispatch')
class lihat_data_relawan_vaksin(ListView):
   
    model= Model_relawan_vaksin
    template_name = "data_relawan_vaksin.html"
    

@method_decorator(login_required, name='dispatch')
class detail_relawan_vaksin(DetailView):
    model = Model_relawan_vaksin
    template_name = "detail_relawan_vaksin.html"
    context_object_name = 'relawan_vaksin'

# Membuat fungsi load more di js
# Sumber :https://www.youtube.com/watch?v=P2KdFZZyruo
class MainView(TemplateView):
      template_name = "data_relawan_vaksin_singkat.html"

class PostJsonListView(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        indeks_akhir = kwargs.get('num_posts')
        indeks_awal = indeks_akhir - 3 
        posts = list(Model_relawan_vaksin.objects.values()[indeks_awal:indeks_akhir])
        posts_size = len(Model_relawan_vaksin.objects.all())
        max_size = True if indeks_akhir >= posts_size else False
        return JsonResponse({'data': posts, 'max': max_size}, safe=False)
