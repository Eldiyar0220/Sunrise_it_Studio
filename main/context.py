from .models import Country, CountrySklad

def get_Countries(request):
    Countries = Country.objects.filter()
    return {'Countries': Countries}


def get_CountrySklad(request):
    CountrySklads = CountrySklad.objects.filter()
    return {'CountrySklads': CountrySklads}