from .serializers import NewsSerializer, SocialsSerializer
from .models import News, Socials
from rest_framework import generics


class SocialView(generics.ListAPIView):
    queryset = Socials.objects.all()
    serializer_class = SocialsSerializer
    
class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer 


class NewsDetailView(generics.ListAPIView):
    model = News
    context_object_name = 'news'
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.get(id=self.id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   

        id = self.kwargs['id']

        context['id'] = id

        return context 







    





