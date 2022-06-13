from django.shortcuts import render
import requests
from .models import Scrapy, UserSearch


def user_page(request, id: int):

    return render(request, 'scrapes/account.html')


def search(request):
    cl = Scrapy.objects.all()
    authors = UserSearch.objects.all()

    # Alters craigslist search address to use user input for zipcode and bedroom size
    if request.method == 'POST':
        print('hi')
        zip_codes = request.POST.get('zip_codes')
        br = request.POST.get('br')

        if br == '1':
            br = 'one-bedroom-apartment'
        if br == '2':
            br = 'two-bedroom-apartment'
        print(br)
        r = requests.get(
            f'https://vermont.craigslist.org/search/field/price?cl_url=https%3A%2F%2Fvermont.craigslist.org%2Fsearch%2F{br}%3Fsearch_distance%3D0%26postal%3D{zip_codes}%26min_price%3D%26max_price%3D%26availabilityMode%3D0%26sale_date%3Dall%2Bdate')

        a = r.json(),
        print('a', a)
        x = a[0]['data']['values']
        print(x)

        def mean(x):
            return sum(x) / len(x)
        average = mean(x)
        user_name = request.user.username
        author, created = UserSearch.objects.get_or_create(
            user_name=user_name)
        Scrapy.objects.create(
            price=x,
            location=zip_codes,
            beds=br,
            author=author,
            average=average,
        )

        print(br)
        context = {
            'cl': cl,
            'authors': authors,
        }
        return render(request, 'scrapes/index.html', context)
    context = {
        'cl': cl,
        'authors': authors,
    }
    return render(request, 'scrapes/index.html', context)


def delete(request, id):
    item = Scrapy.objects.get(id=id)
    item.delete()
    return render(request, 'scrapes/index.html')
