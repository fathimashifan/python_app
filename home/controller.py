from django.shortcuts import render
from .models import MovieDisplay
from .pydantic_models import *
from pydantic import TypeAdapter
from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import MovieDisplay
from .serializers import MovieDisplaySerializer
from .pydantic_models import MovieDisplayModel
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status, views
class Interface(object):
    def __init__(self, request):
        self.request = request
        if request.method == 'POST':
            self.data = request.POST
    def get(self,request):
        movies = MovieDisplay.objects.all()
            # Convert Django model instances to dictionaries
        movie_dicts = [
            {
                "display_id": movie.display_id,
                "movie_name": movie.movie_name,
                "image": movie.image.url
            }
            for movie in movies
        ]

        # Use TypeAdapter to validate the dictionaries
        adapter = TypeAdapter(list[MovieDisplayModel])
        movies_data = adapter.validate_python(movie_dicts)
        
        return render(request, 'home.html', {'movies': movies_data})
    #adding new element to database using command line--------------------------------------
    def post(self,request):

        try:
            # Construct the URL for the image
            image_url = 'images/movie.jpg'  # Adjust this path based on your actual file structure
            # Create and save MovieDisplay instance
            movie_display = MovieDisplay(movie_name='The First Omen (2024)', image=image_url)
            movie_display.save()
       
            return JsonResponse({"message": "Movie inserted successfully"}, status=201)
        except ValidationError as e:
            return JsonResponse({"error": e.errors()}, status=400)
    def post_data(self,request):
        try:
            # Extract data from request
            data = request.data.dict()
            
            # Process movie_name
            movie_name = data.get('movie_name')
            if movie_name:
                data['movie_name'] = movie_name[0] if isinstance(movie_name, list) else movie_name
            
            # Process image file
            if 'image' in request.FILES:
                image = request.FILES['image']
                data['image'] = image.name  # Set image name for validation
            else:
                return Response({'error': 'Image file is required'}, status=status.HTTP_400_BAD_REQUEST)

            # Validate data with Pydantic
            movie_display_data = MovieDisplayModel(**data)

            # Check if this is an update operation
            if movie_display_data.display_id:
                movie_display = get_object_or_404(MovieDisplay, pk=movie_display_data.display_id)
                if movie_display_data.movie_name:
                    movie_display.movie_name = movie_display_data.movie_name
                if image:
                    movie_display.image.save(image.name, image)
                movie_display.save()
                serializer = MovieDisplaySerializer(movie_display)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # Create new MovieDisplay
                serializer = MovieDisplaySerializer(data={'movie_name': movie_display_data.movie_name, 'image': image})
                if serializer.is_valid():
                    movie_display = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({'error': e.errors()}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)    
        

        