from django.shortcuts import render
from .models import Post

# Временные данные
posts = [
    {
        "id": 0,
        "location": "Остров отчаянья",
        "date": "30 сентября 1659 года",
        "category": "travel",
        "text": """Наш корабль, застигнутый в открытом море...""",
    },
    {
        "id": 1,
        "location": "Остров отчаянья",
        "date": "1 октября 1659 года",
        "category": "not-my-day",
        "text": """Проснувшись поутру...""",
    },
    {
        "id": 2,
        "location": "Остров отчаянья",
        "date": "25 октября 1659 года",
        "category": "not-my-day",
        "text": """Всю ночь и весь день шёл дождь...""",
    },
]


def index(request):
    return render(request, "index.html", {"posts": posts})


def post_detail(request, id):
    # Проверяем, есть ли пост с таким id
    post = next((post for post in posts if post['id'] == id), None)

    if post is None:
        raise Http404("Post not found")  # Если пост с таким id не найден, выбрасываем 404 ошибку

    # Отправляем найденный пост в шаблон
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    return render(request, "category.html", {"category_slug": category_slug})
