from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def nearby(request):
    return render(request, 'pages/people-nearby.html')




def newsfeed(request):
    return render(request, 'pages/newsfeed.html')

def logout(request):
    return render(request, 'pages/logout.html')

def indexcompany(request):
    return render(request, 'pages/index-company.html')

def timeline(request):
    return render(request, 'pages/time-line.html')


def timelinevideos(request):
    return render(request, 'pages/timeline-videos.html')

def landing(request):
    return render(request, 'pages/landing.html')

def timelinefriends(request):
    return render(request, 'pages/timeline-friends.html')

def timelinegroups(request):
    return render(request, 'pages/timeline-groups.html')

def timelinepages(request):
    return render(request, 'pages/timeline-pages.html')

def timelinephotos(request):
    return render(request, 'pages/timeline-photos.html')

def groups(request):
    return render(request, 'pages/groups.html')


def pagelikers(request):
    return render(request, 'pages/page-likers.html')

def favpage(request):
    return render(request, 'pages/fav-page.html')

def favpage(request):
    return render(request, 'pages/create-fav-page.html')


def editaccountsettings(request):
    return render(request, 'pages/edit-account-settings.html')


def editinterest(request):
    return render(request, 'pages/edit-interest.html')

def profilebasic(request):
    return render(request, 'pages/edit-profile-basic.html')


def editinterest(request):
    return render(request, 'pages/edit-interest.html')


def workeducation(request):
    return render(request, 'pages/edit-work-eductation.html')


def message(request):
    return render(request, 'pages/message.html')

def inbox(request):
    return render(request, 'pages/inbox.html')

def forum(request):
    return render(request, 'pages/forum.html')

def notifications(request):
    return render(request, 'pages/notifications.html')
    
def forumcategory(request):
    return render(request, 'pages/forums-category.html')
    
def createtopic(request):
    return render(request, 'pages/forum-create-topic.html')

def opentopic(request):
    return render(request, 'pages/forum-open-topic.html')


def create(request):
    return render(request, 'pages/forum-open-topic.html')


def editpassword(request):
    return render(request, 'pages/edit-password.html')
    
def workeductation(request):
    return render(request, 'pages/edit-work-educatation.html')

def shop(request):
    return render(request, 'pages/shop.html')

def shopmasonry(request):
    return render(request, 'pages/shop-mansonry.html')
    
def shopsingle(request):
    return render(request, 'pages/shop-single.html')

def listwo(request):
    return render(request, 'pages/blog-list-wo-sidebar.html')


def listright(request):
    return render(request, 'pages/blog-list-right-sidebar.html')

def listleft(request):
    return render(request, 'pages/blog-list-left-sidebar.html')


def shopcart(request):
    return render(request, 'pages/shop-cart.html')

def shopcheckout(request):
    return render(request, 'pages/shop-checkout.html')
    
def wosidebar(request):
    return render(request, 'pages/blog-grid-wo-sidebar.html')

def rightsidebar(request):
    return render(request, 'pages/rightsidebar.html')

def leftsidebar(request):
    return render(request, 'pages/leftsidebar.html')
    
def blogmasonry(request):
    return render(request, 'pages/blog-masonry.html')

def blogdetail(request):
    return render(request, 'pages/blog-detail.html')

def portfolio2colm(request):
    return render(request, 'pages/portfolio-2colm.html')
    
def portfolio3colm(request):
    return render(request, 'pages/portfolio-3colm.html')

def portfolio4colm(request):
    return render(request, 'pages/portfolio-4colm.html')
    
def support(request):
    return render(request, 'pages/support-and-help.html')
    
def supportdetail(request):
    return render(request, 'pages/support-and-help-detail.html')

def supportsearch(request):
    return render(request, 'pages/support-and-help-search-result.html')

def careers(request):
    return render(request, 'pages/careers.html')

def careerdetail(request):
    return render(request, 'pages/career-detail.html')

def f404(request):
    return render(request, 'pages/404.html')

def faq(request):
    return render(request, 'pages/faq.html')


def insights(request):
    return render(request, 'pages/insight.html')

def knowledgebase(request):
    return render(request, 'pages/knowledge-base.html')

def about(request):
    return render(request, 'pages/about.html')


def aboutcompany(request):
    return render(request, 'pages/about-company.html')
    
def contact(request):
    return render(request, 'pages/contact.html')
    
def contactbranches(request):
    return render(request, 'pages/contact-branches.html')


def widgets(request):
    return render(request, 'pages/widgets.html')


def sitemap(request):
    return render(request, 'pages/sitemap.html')
    
def terms(request):
    return render(request, 'pages/terms.html')


def notification(request):
    return render(request, 'pages/notifications.html')

def forum(request):
    return render(request, 'pages/forum.html')
