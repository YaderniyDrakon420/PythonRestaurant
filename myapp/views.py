from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Restaurant, Specialization, RestaurantImage, Review


@csrf_exempt
def home(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '').strip()

        if search_query:
            restaurants = Restaurant.objects.filter(
                specializations__name__icontains=search_query
            ).prefetch_related('images').distinct()
        else:
            restaurants = Restaurant.objects.prefetch_related('images').all()

        specializations = Specialization.objects.all()

        content = {
            "restaurants": restaurants,
            "specializations": specializations,
            "search_query": search_query
        }
        return render(request, 'myapp/home.html', content)

    elif request.method == 'POST':
        try:
            title = request.POST.get("title")
            address = request.POST.get("address")
            website = request.POST.get("website", "")
            phone = request.POST.get("phone")

            specialization_ids = request.POST.getlist("specializations")

            if not all([title, address, phone]):
                return JsonResponse({"error": "Title, address, and phone are required"}, status=400)

            restaurant = Restaurant.objects.create(
                title=title,
                address=address,
                website=website,
                phone=phone
            )

            if specialization_ids:
                restaurant.specializations.set(specialization_ids)

            if 'image' in request.FILES:
                uploaded_image = request.FILES['image']
                RestaurantImage.objects.create(
                    restaurant=restaurant,
                    image=uploaded_image
                )
            return JsonResponse({
                "id": restaurant.id,
                "title": restaurant.title,
                "has_image": 'image' in request.FILES
            }, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def delete_restaurant(request, restaurant_id):
    if request.method == 'DELETE':
        try:
            restaurant = get_object_or_404(Restaurant, id=restaurant_id)
            restaurant.delete()

            return JsonResponse({"message": "Ресторан успішно видалено"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def edit_restaurant(request, restaurant_id):
    if request.method == 'POST':
        try:
            restaurant = get_object_or_404(Restaurant, id=restaurant_id)

            restaurant.title = request.POST.get("title")
            restaurant.address = request.POST.get("address")
            restaurant.website = request.POST.get("website", "")
            restaurant.phone = request.POST.get("phone")

            if not all([restaurant.title, restaurant.address, restaurant.phone]):
                return JsonResponse({"error": "Назва, адреса та телефон обов'язкові"}, status=400)

            restaurant.save()

            specialization_ids = request.POST.getlist("specializations")
            if specialization_ids:
                restaurant.specializations.set(specialization_ids)
            else:
                restaurant.specializations.clear()

            if 'image' in request.FILES:
                uploaded_image = request.FILES['image']
                RestaurantImage.objects.create(
                    restaurant=restaurant,
                    image=uploaded_image
                )
            return JsonResponse({"message": "Дані ресторану успішно оновлено!"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

def make_review(request, restaurant_id):
    if request.method == 'POST':
        try:
            restaurant = get_object_or_404(Restaurant, id=restaurant_id)
            title = request.POST.get("title")
            text = request.POST.get("text")
            if not title or not text:
                return JsonResponse({"error": "Заголовок та текст відгуку обов'язкові"}, status=400)
            Review.objects.create(
                title=title,
                text=text,
                restaurant=restaurant
            )
            return JsonResponse({"message": "Відгук успішно додано!"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

def contacts(request):
    return render(request, 'myapp/contacts.html')

def about(request):
    return render(request, 'myapp/about.html')

def layout(request):
    return render(request, 'myapp/layout.html')

def page_not_found(request, exception):
    return render(request, 'myapp/not_found.html', status=404)