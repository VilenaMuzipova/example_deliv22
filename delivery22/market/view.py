
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def import_data(request):
    url = 'https://www.delikateska.ru/catalog'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = []
    for product in soup.find_all('div', class_='product'):
        name = product.find('div', class_='product-name').text.strip()
        price = product.find('div', class_='product-price').text.strip()
        image_url = product.find('img')['src']
        products.append({'name': name, 'price': price, 'image_url': image_url})
    # Сохраняем данные в базу данных или возвращаем их в шаблон для отображения
    return render(request, 'products.html', {'products': products})