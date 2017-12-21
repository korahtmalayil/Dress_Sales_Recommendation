'''
Created on 13-Dec-2017

@author: Korah
'''
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from .model import final_answer

@permission_classes((permissions.AllowAny,))
class Answer(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        result = {}
        result['Recommendation'] = final_answer(question['messageText'])[0]
        return Response(result)