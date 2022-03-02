from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Quiz
from .serilizers import QuizSerializer

@api_view(['GET'])
# @login_required
def get_quiz_questions(request, category):
    try:
        data = Quiz.objects.get(quiz_subject=category)
        serializers = QuizSerializer(data)
        data = {'data': serializers.data}
        return Response(data)
    except Exception as e:
        return Response({'Error': f"{e}"})


# @api_view(['POST'])
# # @login_required
# def create_defib(request):
#     # return HttpResponse('Hello World!')
#     user_id = User.objects.get(username=request.data['username'])
#     new_defib = Defib.objects.create(
#         address = request.data['address'],
#         post_code = request.data['post_code'],
#         long = request.data['long'],
#         lat = request.data['lat'],
#         what3words_link = request.data['what3words_link'],
#         photo_url = request.data['photo_url'],
#         access = request.data['access'],
#         approved = request.data['approved'],
#         comments = request.data['comments'],
#         user_id = user_id
#     )
#     return Response({'Success': f'Created new defibrillator with id: {new_defib.id}'})
