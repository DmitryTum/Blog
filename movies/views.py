from django.db import models
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .service import get_client_ip
from .models import *
from .serializers import MovieSerializer, CreateRatingSerializer, MovieDetailSerializer, ReviewCreateSerializer, \
    ActorListSerializer, ActorDetailSerializer


class MovieListView(APIView):

    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(generics.RetrieveAPIView):

    def get(self, request, pk):
        movies = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movies)
        return Response(serializer.data)


class ReviewCreateView(APIView):

    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class AddStarRatingView(APIView):

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)


class ActorsListView(APIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorDetailView(APIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
