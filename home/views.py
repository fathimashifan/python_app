

from django.views import View
from .controller import Interface
from rest_framework import status, views


class DisplayView(View):
	template_name = 'generic_forms.html'
	def get(self, request, ):
		return Interface(self.request).get(request)
	def post(self, request, ):
		return Interface(self.request).post(request)
	
class MovieDisplayCreateUpdateView(views.APIView):
    def post(self, request,):
        return Interface(self.request).post_data(request)
        
        