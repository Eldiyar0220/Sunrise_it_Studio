from .models import CountrySklad

def get_CountrySklad(request):
    CountrySklads = CountrySklad.objects.filter()
    return {'CountrySklads': CountrySklads}