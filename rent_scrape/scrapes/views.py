from django.shortcuts import redirect, render
import requests

from .models import Scrapy, UserSearch


def chart(request, id: int):
    cl = Scrapy.objects.get(id=id)
    price = (cl.price)
    average = (cl.average)
    location = (cl.location)
    authors = UserSearch.objects.all()
    context = {
        'cl': cl,
        'price': price,
        'authors': authors,
        'location': location,
        'average': average
    }
    return render(request, 'scrapes/line_chart.html', context)


def user_page(request, id: int):
    authors = Scrapy.objects.filter(author_id=id)
    context = {
        'authors': authors
    }

    return render(request, 'scrapes/account.html', context)


def search(request):
    cl = Scrapy.objects.all()
    authors = UserSearch.objects.all()

    # Alters craigslist search address to use user input for zipcode and bedroom size
    if request.method == 'POST':
        print('hi')
        zip_codes = request.POST.get('zip_codes')
        br = request.POST.get('br')

        if br == 0 or zip_codes == '':
            context = {
                'cl': cl,
                'authors': authors,
            }
            return render(request, 'scrapes/index.html', context)
        if br == '1':
            br = 'one-bedroom-apartment'
        if br == '2':
            br = 'two-bedroom-apartment'

        r = requests.get(
            f'https://vermont.craigslist.org/search/field/price?cl_url=https%3A%2F%2Fvermont.craigslist.org%2Fsearch%2F{br}%3Fsearch_distance%3D0%26postal%3D{zip_codes}%26min_price%3D%26max_price%3D%26availabilityMode%3D0%26sale_date%3Dall%2Bdate')

        a = r.json(),
        x = a[0]['data']['values']

        if x == []:
            context = {
                'cl': cl,
                'authors': authors,
            }
            return render(request, 'scrapes/index.html', context)

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
    print('hi')
    # cl = Scrapy.objects.all()
    # authors = Scrapy.objects.filter(author_id=id)
    item = Scrapy.objects.get(id=id)
    item.delete()

    return redirect('userpage', id=item.author_id)
