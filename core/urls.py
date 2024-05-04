from django.urls import path
from .views import index,about,blog,contact,portfolio,single_post,contact1,contact_form

urlpatterns=[
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('single_post/<int:pk>/', single_post.as_view(), name='single_post'),
    path('footer/', contact1, name='contact1'),
    path('contact_form', contact_form, name='contact_form'),

]