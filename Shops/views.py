from django.shortcuts import render, redirect
from .forms import ShopRegistrationForm

from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Shop
from .serializers import ShopSerializer
from .utils import haversine

def register_shop(request):
    if request.method == 'POST':
        form = ShopRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_success')
    else:
        form = ShopRegistrationForm()

    return render(request, 'register_shop.html', {'form': form})

def shop_success(request):
    return render(request, 'success.html')

def nearby_shops(request):
    return render(request, 'nearby_shops.html')

def home(request):
    return render(request, 'home.html')


# Define the query parameters for Swagger documentation
latitude_param = openapi.Parameter(
    'latitude', openapi.IN_QUERY, description="User's latitude", type=openapi.TYPE_NUMBER
)
longitude_param = openapi.Parameter(
    'longitude', openapi.IN_QUERY, description="User's longitude", type=openapi.TYPE_NUMBER
)

@swagger_auto_schema(method='get', manual_parameters=[latitude_param, longitude_param])

@api_view(['GET'])
def shop_search(request):
    try:
        user_lat = float(request.query_params.get('latitude'))
        user_lon = float(request.query_params.get('longitude'))
    except (TypeError, ValueError):
        return Response({"error": "Invalid latitude or longitude"}, status=400)

    shops = Shop.objects.all()
    shop_distances = []

    for shop in shops:
        distance = haversine(user_lat, user_lon, shop.latitude, shop.longitude)
        shop_distances.append((shop, distance))

    # Sort shops by distance
    sorted_shops = sorted(shop_distances, key=lambda x: x[1])

    # Serialize sorted shops and return the response
    serialized_data = [
        {"shop": ShopSerializer(shop).data, "distance_km": round(distance, 2)}
        for shop, distance in sorted_shops
    ]

    return Response(serialized_data)