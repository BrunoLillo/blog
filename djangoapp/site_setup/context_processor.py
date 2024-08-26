from site_setup.models import SiteSetup
def context(request):
    return{
        'example':'Veio do context'
}
def site_setup(request):
    setup= SiteSetup.objects.order_by('-id')
    
    return{
        'site_setup':{
            'title':setup,
        }
}