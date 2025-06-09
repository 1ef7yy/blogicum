import pytest
from django.urls import reverse
from django.test import Client
from blog.models import Post

@pytest.mark.django_db
def test_index_view():
    # Создаём несколько записей
    Post.objects.create(location='Остров отчаянья', date='30 сентября 1659 года', category='travel', text='Тестовый пост 1')
    Post.objects.create(location='Остров отчаянья', date='1 октября 1659 года', category='not-my-day', text='Тестовый пост 2')

    client = Client()  # Клиент для имитации запросов
    response = client.get(reverse('blog:index'))  # Делаем GET-запрос на главную страницу

    assert response.status_code == 200  # Проверяем, что ответ успешный

    # Декодируем байтовую строку в строку с кодировкой utf-8
    response_content = response.content.decode('utf-8')

    # Проверяем, что на странице есть нужные посты
    assert 'Наш корабль, застигнутый в открытом море...' in response_content  # Ищем текст первого поста
    assert 'Проснувшись поутру...' in response_content  # Ищем текст второго поста

