from django.shortcuts import render
from django.views.generic import ListView,DetailView
from core.models import GeneralSetting,ImageSetting,ProductImageSetting,blogPageSetting,commentSetting,contactSetting,message
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import JsonResponse
# Create your views here.
def index(request):
      #Text
    
    site_title= GeneralSetting.objects.get(name='site_title').parameter
    home_description_1= GeneralSetting.objects.get(name='home_description_1').parameter
    home_description_2= GeneralSetting.objects.get(name='home_description_2').parameter
    home_services_1=GeneralSetting.objects.get(name='home_services_1').parameter
    home_services_1_1=GeneralSetting.objects.get(name='home_services_1').description
    home_services_2=GeneralSetting.objects.get(name='home_services_2').parameter
    home_services_2_1=GeneralSetting.objects.get(name='home_services_2').description
    home_services_3=GeneralSetting.objects.get(name='home_services_3').parameter
    home_services_3_1=GeneralSetting.objects.get(name='home_services_3').description
    about_description_1=GeneralSetting.objects.get(name='about_description_1').parameter
    about_description_2=GeneralSetting.objects.get(name='about_description_2').parameter
    about_title_1=GeneralSetting.objects.get(name='about_title_1').parameter
    about_title_1_1=GeneralSetting.objects.get(name='about_title_1').description
    about_title_2=GeneralSetting.objects.get(name='about_title_2').parameter
    about_title_2_1=GeneralSetting.objects.get(name='about_title_2').description
    about_title_3=GeneralSetting.objects.get(name='about_title_3').parameter
    about_title_3_1=GeneralSetting.objects.get(name='about_title_3').description
    portfolio_title_1=GeneralSetting.objects.get(name='portfolio_title_1').parameter
    portfolio_title_2=GeneralSetting.objects.get(name='portfolio_title_2').parameter
    portfolio_title_3=GeneralSetting.objects.get(name='portfolio_title_3').parameter
    portfolio_title_4=GeneralSetting.objects.get(name='portfolio_title_4').parameter
    portfolio_title_5=GeneralSetting.objects.get(name='portfolio_title_5').parameter
    

    #image
    home_plants_1=ImageSetting.objects.get(name='home_plants_1').file
    home_services_image_1=ImageSetting.objects.get(name='home_services_image_1').file
    ProductImage=blogPageSetting.objects.all()
    
    contact1 = contactSetting.objects.get(id=1)


    comments= commentSetting.objects.all()
    ProductImage = blogPageSetting.objects.all()

    paginator = Paginator(ProductImage, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    return render(request,'index.html',{
        'site_title':site_title,
        'home_description_1':home_description_1,
        'home_description_2':home_description_2,
        'home_plants_1':home_plants_1,
        'home_services_1':home_services_1,
        'home_services_1_1':home_services_1_1,
        'home_services_2':home_services_2,
        'home_services_2_1':home_services_2_1,
        'home_services_3':home_services_3,
        'home_services_3_1':home_services_3_1,
        'home_services_image_1':home_services_image_1,
        'about_description_1':about_description_1,
        'about_description_2':about_description_2,
        'about_title_1':about_title_1,
        'about_title_1_1':about_title_1_1,
        'about_title_2':about_title_2,
        'about_title_2_1':about_title_2_1,
        'about_title_3':about_title_3,
        'about_title_3_1':about_title_3_1,
        'portfolio_title_1':portfolio_title_1,
        'portfolio_title_2':portfolio_title_2,
        'portfolio_title_3':portfolio_title_3,
        'portfolio_title_4':portfolio_title_4,
        'portfolio_title_5':portfolio_title_5,
        'ProductImage':ProductImage,
        'posts':posts,
        'comments':comments,
        'contact':contact1
        }
    )

def about(request):
    contact1 = contactSetting.objects.get(id=1)

    return render(request,'about.html',{'contact':contact1})

def blog(request):
    contact1 = contactSetting.objects.get(id=1)

    ProductImage=blogPageSetting.objects.all()
    paginator=Paginator(ProductImage,8)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    
    
    return render(request,'blog.html',{'posts':posts,'contact':contact1})

def contact(request):
    contact = contactSetting.objects.get(id=1)
    return render(request,'contact.html',{'contact':contact})

def contact1(request):
    contact1 = contactSetting.objects.get(id=1)
    return render(request,'footer.html',{'contact':contact1})

class single_post(DetailView):
    model = blogPageSetting
    template_name = "single-post.html"
    

def portfolio(request):
    contact1 = contactSetting.objects.get(id=1)

    ProductImage=blogPageSetting.objects.all()
    portfolio_title_1=GeneralSetting.objects.get(name='portfolio_title_1').parameter
    portfolio_title_2=GeneralSetting.objects.get(name='portfolio_title_2').parameter
    portfolio_title_3=GeneralSetting.objects.get(name='portfolio_title_3').parameter
    portfolio_title_4=GeneralSetting.objects.get(name='portfolio_title_4').parameter
    portfolio_title_5=GeneralSetting.objects.get(name='portfolio_title_5').parameter

    paginator=Paginator(ProductImage,8)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    
    return render(request,'portfolio.html',{'ProductImage':ProductImage,
        'portfolio_title_1':portfolio_title_1,
        'portfolio_title_2':portfolio_title_2,
        'portfolio_title_3':portfolio_title_3,
        'portfolio_title_4':portfolio_title_4,
        'portfolio_title_5':portfolio_title_5,
        'posts':posts,
        'contact':contact1})

def contact_form(request):
    if request.POST:
        name =request.POST.get('name')
        email= request.POST.get('email')
        subject =request.POST.get('subject')
        message1 =request.POST.get('message1')

        message.objects.create(
            name=name,
            email=email,
            subject=subject,
            message1=message1,
        )

        succes=True
        message2='Contact Form sent successfully'
    else:
        succes=False
        message2='Contact Form is noy valid'
    context={
        'succes':succes,
        'message':message2,
    }
    return JsonResponse(context)

