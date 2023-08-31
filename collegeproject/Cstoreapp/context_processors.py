from . models import Department,Courses,Product

def menu_links(request):
    links=Department.objects.all()
    return dict(links=links)

def menu_link(request):
    link=Courses.objects.all()
    return dict(link=link)

def menu(request):
    datas=Product.objects.all()
    return dict(datas=datas)