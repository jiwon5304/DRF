from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action

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
    # http PATCH http://127.0.0.1:8000/post/3/ is_public=True
    # viewset 안에 있는 partial_update를 활용
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # http://127.0.0.1:8000/post/public/
    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
    
    # http://127.0.0.1:8000/post/2/set_public/
    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public']) # is_public 만 업데이트 함
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    # def dispatch(self, request, *args, **kwargs):
    #     # print 비추천, logger 추천
    #     print("request.body :", request.body)     #request.body : b'{"message": "\\uc138\\ubc88\\uc9f8 \\ud3ec\\uc2a4\\ud305"}'
    #     print("request.POST :", request.POST)     #request.POST : <QueryDict: {}>
    #     return super().dispatch(request, *args, **kwargs)



# 클래스 기반 뷰 방법1  
# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# 클래스 기반 뷰 방법2 
# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

# public_post_list = PublicPostListAPIView.as_view()

# 함수 기반 뷰 방법3
# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'instagram/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({
            'post': post,   # Post object (1)
        })





