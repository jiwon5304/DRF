from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

## 방법1
# def post_list(request):
#     #2개분기
#     pass

# def post_detail(request, pk):
#     # request.method -> 3개 분기
#     pass

## 방법2
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # def dispatch(self, request, *args, **kwargs):
    #     # print 비추천, logger 추천
    #     print("request.body :", request.body)     #request.body : b'{"message": "\\uc138\\ubc88\\uc9f8 \\ud3ec\\uc2a4\\ud305"}'
    #     print("request.POST :", request.POST)     #request.POST : <QueryDict: {}>
    #     return super().dispatch(request, *args, **kwargs)
    
class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()   #filter(is_public=True)
    serializer_class = PostSerializer