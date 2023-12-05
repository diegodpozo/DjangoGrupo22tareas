from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy

# Create your views here.

def Ver_Reservas (request):
   mis_reservas = Reserva.objects.all()

   context = {
        'Lista_reservas':mis_reservas
    }
   return render (request,'web/reservas.html', context)





def index(request):
    return render (request, 'web/index.html', context={})




class reservascreateview (CreateView):
    model = Reserva
    template_name = 'web/crear.html'
    success_url = 'reservas'
    fields ='__all__' 

class reservasdetailview(DetailView):
    model = Reserva
    template_name = 'web/detalle.html'

class reservaupdateview(UpdateView):
        model = Reserva
        template_name = 'web/modificar.html'
        fields ='__all__'

        def get_success_url(self):
             return reverse('detalle', kwargs={'pk': self.object.pk})
        
class reservasdeleteview(DeleteView):
     model= Reserva
     template_name = 'web/borrar.html'
     success_url= reverse_lazy('reservas') 


def about(request):
    return render (request, 'web/about.html', context={})


