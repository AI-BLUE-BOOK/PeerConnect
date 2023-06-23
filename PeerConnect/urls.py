"""
URL configuration for PeerConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PAGES.urls')),
    path('nearby/', include('PAGES.urls')),


    path('newsfeed/', include('PAGES.urls')),
    path('logout/', include('PAGES.urls')),
    path('index-company/', include('PAGES.urls')),
    path('landing/', include('PAGES.urls')),
    path('time-line/', include('PAGES.urls')),
    path('timeline-groups/', include('PAGES.urls')),
    path('timeline-pages/', include('PAGES.urls')),
    path('timeline-photos/', include('PAGES.urls')),
    path('timeline-videos/', include('PAGES.urls')),
    path('groups/', include('PAGES.urls')),
    path('page-likers/', include('PAGES.urls')),
    path('people-nearby/', include('PAGES.urls')),
    path('fav-page/', include('PAGES.urls')),
    path('create-fav-page/', include('PAGES.urls')),
    path('edit-account-setting/', include('PAGES.urls')),
    path('edit-interest/', include('PAGES.urls')),
    path('edit-password/', include('PAGES.urls')),
    path('edit-profile-basic/', include('PAGES.urls')),
    path('edit-work-eductation/', include('PAGES.urls')),
    path('message/', include('PAGES.urls')),
    path('inbox/', include('PAGES.urls')),
    path('notifications/', include('PAGES.urls')),
    path('forum/', include('PAGES.urls')),
    path('forums-category/', include('PAGES.urls')),
    path('forum-open-topic/', include('PAGES.urls')),
    path('forum-create-topic/', include('PAGES.urls')),
    path('shop/', include('PAGES.urls')),
    path('shop-masonry/', include('PAGES.urls')),
    path('shop-single/', include('PAGES.urls')),
    path('shop-cart/', include('PAGES.urls')),
    path('shop-checkout/', include('PAGES.urls')),
    path('blog-grid-wo-sidebar/', include('PAGES.urls')),
    path('blog-grid-right-sidebar/', include('PAGES.urls')),
    path('blog-grid-left-sidebar/', include('PAGES.urls')),
    path('blog-list-wo-sidebar/', include('PAGES.urls')),
    path('blog-list-right-sidebar/', include('PAGES.urls')),
    path('blog-list-left-sidebar/', include('PAGES.urls')),
    path('blog-masonry/', include('PAGES.urls')),
    path('blog-detail/', include('PAGES.urls')),
    path('portfolio-2colm/', include('PAGES.urls')),
    path('portfolio-3colm/', include('PAGES.urls')),
    path('portfolio-4colm/', include('PAGES.urls')),
    path('support-and-help/', include('PAGES.urls')),
    path('support-and-help-detail/', include('PAGES.urls')),
    path('support-and-help-search-result/', include('PAGES.urls')),
    path('careers/', include('PAGES.urls')),
    path('career-detail/', include('PAGES.urls')),
    path('career-branches/', include('PAGES.urls')),
    path('404/', include('PAGES.urls')),
    path('faq/', include('PAGES.urls')),
    path('insights/', include('PAGES.urls')),
    path('knowledge-base/', include('PAGES.urls')),
    path('about/', include('PAGES.urls')),
    path('about-company/', include('PAGES.urls')),
    path('contact/', include('PAGES.urls')),
    path('timeline-videos/', include('PAGES.urls')),
    path('widgets/', include('PAGES.urls')),
    path('sitemap/', include('PAGES.urls')),
    path('/', include('PAGES.urls')),
    path('/', include('PAGES.urls')),

    
    
    
    
] ##+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)##

