from django.shortcuts import render , redirect ,HttpResponseRedirect
from django.views.generic import ( View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView)
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from core.models import Product, Category, SubCategory ,Service
from core.forms import ProductForms , ContactForm , ServiceForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages


from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


class HomeView(ListView):
    template_name = "home.html"
    ordering = ['-published']

    def get_queryset(self):
        return Product.objects.filter(
            published__lte=timezone.now()).order_by('-published')[0:20]


class ProductView(DetailView):
    model = Product
    template_name = "product.html"


class AddProduct(LoginRequiredMixin, CreateView):
    form_class = ProductForms 
    model = Product
    template_name = "addproduct.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(AddProduct, self).form_valid(form)



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProductForms
    model = Product
    template_name = "update-product.html"



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('home')
    template_name = "delete-product.html"


class AboutView(TemplateView):
    template_name="about.html"



class SearchView(ListView):
    template_name = "search.html"
    paginate_by = 90

    def get_queryset(self):
        qs = Product.objects.all()
        search_q = self.request.GET.get('q')
        category_q = self.request.GET.get('cat_q')
        mini_q = self.request.GET.get('min_q')
        maxi_q = self.request.GET.get('max_q')


        if search_q != '' and search_q is not None:
            qs = qs.filter(title__icontains=search_q)

        if category_q != '' and category_q is not None:
            qs = qs.filter(category__name__icontains=category_q)

        if mini_q != '' and mini_q is not None:
            qs = qs.filter(price__gte=mini_q)

        if maxi_q != '' and maxi_q is not None:
            qs = qs.filter(price__lt=maxi_q)


        # paginator = Paginator(qs, self.paginate_by)
        # page = self.request.GET.get('page')
        # try:
        #     qs = paginator.page(page)
        # except PageNotAnInteger:
        #     qs = paginator.page(1)
        # except EmptyPage:
        #     qs = paginator.page(paginator.num_pages)

        return qs

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        # context['product'] = Product.objects.all()
        context['category'] = Category.objects.all()
        context['subcategory'] = SubCategory.objects.all()
        
        return context


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['Surajbh71@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')




class CategoryView(ListView):
    template_name = 'category-product.html'
    paginate_by = 40

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context



class PosProduct(ListView):
    template_name = 'pos-products.html'
    paginate_by = 40

    def get_queryset(self):
        return Product.objects.filter(product_type='POS')


class ItProduct(ListView):
    template_name = 'it-products.html'
    paginate_by = 40
    
    def get_queryset(self):
        return Product.objects.filter(product_type='IT')




class AddService(LoginRequiredMixin, CreateView, ListView):
    form_class = ServiceForm
    model = Service
    template_name = "service.html"
    success_url = reverse_lazy('addservice')

    def get_queryset(self):
        return Service.objects.all().order_by('-updated_at')[0:10]

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(AddService, self).form_valid(form)



class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ServiceForm
    model = Service
    template_name = "update-service.html"
    success_url = reverse_lazy('addservice')



def service_delete(request, slug):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    service = Service.objects.filter(slug=slug)
    service.delete()
    messages.warning(request, 'Service has been deleted.')
    return HttpResponseRedirect(url)


class TrackService(ListView):
    template_name = "track_service.html"

    def get_queryset(self):
        qs = Service.objects.all()
        request_search = self.request.GET.get('service')
        if request_search != '' and request_search is not None:
            qs = qs.filter(tracking_code__iexact=request_search)

        return qs









        
