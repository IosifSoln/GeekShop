from django.shortcuts import render


# Create your views here.
def index(request):
    # context словарь название
    context = {
        'name': 'Geekshop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    # context словарь продукты и название
    context = {
        'name': 'GeekShop-Каталог',
        'products': [{'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
                      'descipt': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                      'photo': '/static/vendor/img/products/Adidas-hoodie.png'},
                     {'name': 'Синяя куртка The North Face', 'price': 23735,
                      'descipt': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                      'photo': '/static/vendor/img/products/Blue-jacket-The-North-Face.png'},
                     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390,
                      'descipt': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                      'photo': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
                     {'name': 'Черный рюкзак Nike Heritage', 'price': 2340,
                      'descipt': 'Плотная ткань. Легкий материал.',
                      'photo': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png'},
                     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590,
                      'descipt': 'Гладкий кожаный верх. Натуральный материал.',
                      'photo': '/static/vendor/img/products/Black-Dr-Martens-shoes.png'},
                     {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890,
                      'descipt': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                      'photo': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'}

                     ]

    }
    return render(request, 'products/products.html', context)
