from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer


class CategoryView(APIView):
    def get(self, request):
        return Response(CategorySerializer(Category.objects.all(), many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        if not name:
            return Response({'msg': '未获取到类别名称'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            Category.objects.create(name=name)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'ok'}, status=status.HTTP_200_OK)

    def put(self,request):
        pass


class ListCountView(APIView):
    def get(self, request):
        category = request.GET.get('category_id', 0)
        if int(category) == 0:
            total = Article.objects.count()
        else:
            total = Article.objects.filter(source_id=int(category)).count()
        return Response({'total': total}, status=status.HTTP_200_OK)


class ListView(APIView):
    def get(self, request):
        aid = request.GET.get('aid')
        if not aid:
            return Response({'msg': '未获取到文章编号'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'ok', 'data': ArticleSerializer(Article.objects.filter(id=aid), many=True).data},
                        status=status.HTTP_200_OK)

    def post(self, request):
        title = request.data.get('title')
        source_id = request.data.get('category_id', 1)
        url = request.data.get('url')
        click_count = request.data.get('click_count')
        try:
            Article.objects.create(
                title=title,
                source_id=int(source_id),
                url=url,
                click_count=click_count
            )
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'ok'}, status=status.HTTP_201_CREATED)

    def put(self, request):
        aid = request.data.get('aid')
        if not aid:
            return Response({'msg': '未获取到文章编号'}, status=status.HTTP_400_BAD_REQUEST)
        title = request.data.get('title')
        source_id = request.data.get('category_id', 1)
        url = request.data.get('url')
        click_count = request.data.get('click_count')
        try:
            article_obj = Article.objects.get(id=aid)
            article_obj.title = title
            article_obj.source_id = int(source_id)
            article_obj.url = url
            article_obj.click_count = int(click_count)
            article_obj.save()
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'ok'}, status=status.HTTP_200_OK)

    def delete(self, request):
        aid = request.data.get('aid')
        if not aid:
            return Response({'msg': '未获取到文章编号'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            Article.objects.filter(id=aid).delete()
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'ok'}, status=status.HTTP_200_OK)


class ListViews(APIView):
    def get(self, request):
        category = request.GET.get('category_id', 0)
        page_start = request.GET.get('page_start', 0)
        page_end = request.GET.get('page_end', 10)
        if int(category) == 0:
            article_ls = Article.objects.all()[int(page_start):int(page_end) + 1]
        else:
            article_ls = Article.objects.filter(source_id=int(category))[int(page_start):int(page_end) + 1]
        return Response(ArticleSerializer(article_ls, many=True).data, status=status.HTTP_200_OK)
