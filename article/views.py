import requests
from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from fake_useragent import UserAgent
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

    def delete(self, request):
        cid = request.data.get('cid')
        if not cid:
            return Response({'msg': '未获取到类别编号'}, status=status.HTTP_400_BAD_REQUEST)
        article_count = Article.objects.filter(source_id=int(cid)).count()
        if article_count != 0:
            return Response({'msg': '该类别下还有文章'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            Category.objects.filter(id=int(cid)).delete()
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'ok'}, status=status.HTTP_200_OK)


class ListCountView(APIView):
    def get(self, request):
        category = request.GET.get('category_id', 0)
        keyword = request.GET.get('keyword')
        if not keyword or keyword == '':
            if int(category) == 0:
                total = Article.objects.count()
            else:
                total = Article.objects.filter(source_id=int(category)).count()
        else:
            if int(category) == 0:
                total = Article.objects.filter(title__icontains=keyword).count()
            else:
                total = Article.objects.filter(title__icontains=keyword, source_id=int(category)).count()
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
        keyword = request.GET.get('keyword')
        if not keyword or keyword == '':
            if int(category) == 0:
                article_ls = Article.objects.all()[int(page_start):int(page_end) + 1]
            else:
                article_ls = Article.objects.filter(
                    source_id=int(category)
                )[int(page_start):int(page_end) + 1]
        else:
            if int(category) == 0:
                article_ls = Article.objects.filter(title__icontains=keyword)[int(page_start):int(page_end) + 1]
            else:
                article_ls = Article.objects.filter(
                    title__icontains=keyword,
                    source_id=int(category)
                )[int(page_start):int(page_end) + 1]
        return Response(ArticleSerializer(article_ls, many=True).data, status=status.HTTP_200_OK)


class NightingaleChartView(APIView):
    def get(self, request):
        chart_type = request.GET.get('chart_type')
        if chart_type == 'count':
            category_id_ls = Category.objects.values_list('id', flat=True)
            category_name_ls = Category.objects.values_list('name', flat=True)
            res_data = []
            for index in range(len(category_id_ls)):
                article_count = Article.objects.filter(source_id=int(category_id_ls[index])).count()
                dt = {'name': category_name_ls[index], 'value': article_count}
                res_data.append(dt)
            return Response(res_data, status=status.HTTP_200_OK)
        elif chart_type == 'click':
            category_id_ls = Category.objects.values_list('id', flat=True)
            category_name_ls = Category.objects.values_list('name', flat=True)
            res_data = []
            for index in range(len(category_id_ls)):
                click_count = \
                    Article.objects.filter(source_id=int(category_id_ls[index])).aggregate(
                        total_click=Sum('click_count'))[
                        'total_click']
                dt = {'name': category_name_ls[index], 'value': click_count}
                res_data.append(dt)
            return Response(res_data, status=status.HTTP_200_OK)
        return Response({'msg': '未获取数据类型'}, status=status.HTTP_400_BAD_REQUEST)


class LineChartView(APIView):
    def get(self, request):
        chart_type = request.GET.get('chart_type')
        if chart_type == 'year':
            distinct_years = Article.objects.dates('create_time', 'year', order='DESC')
            year_list = list(set(str(year.year) for year in distinct_years))
            year_list.sort(reverse=False)
            series = []
            category_id_ls = Category.objects.values_list('id', flat=True)
            category_name_ls = Category.objects.values_list('name', flat=True)
            for category_id, category_name in zip(category_id_ls, category_name_ls):
                count_list = []
                for year in year_list[-10:]:
                    count = Article.objects.filter(create_time__year=year, source_id=int(category_id)).count()
                    count_list.append(count)
                series.append({
                    'name': category_name,
                    'type': 'line',
                    # 'stack': 'Total',
                    'data': count_list
                })
            data = {
                'year_list': year_list[-10:],
                'category_list': category_name_ls,
                'series': series
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'msg': 'ok'})


class CodeforcesStatusView(APIView):
    def get(self, request):
        url = 'https://codeforces.com/api/problemset.recentStatus'
        params = {'count': request.GET.get('count', 50)}
        res = requests.get(
            url=url,
            params=params,
            headers={'user-agent': UserAgent().random}
        )
        try:
            json_data = res.json()
        except Exception as e:
            print(str(e))
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        programming_language_dt = {}
        verdict_dt = {}
        for submit in json_data['result']:
            if submit.get('programmingLanguage') not in programming_language_dt:
                programming_language_dt[submit.get('programmingLanguage')] = 0
            programming_language_dt[submit.get('programmingLanguage')] += 1
            if submit.get('verdict') not in verdict_dt:
                verdict_dt[submit.get('verdict')] = 0
            verdict_dt[submit.get('verdict')] += 1
        pie_list = []
        for k, v in programming_language_dt.items():
            pie_list.append({
                'name': k,
                'value': v
            })
        x_axis_data = []
        column_res = []
        for k, v in verdict_dt.items():
            x_axis_data.append(k)
            column_res.append({
                'groupId': k,
                'value': v,
                'itemStyle': {
                    'color': '#a90000'
                }
            })
        return Response(
            {
                'msg': 'ok',
                'data': json_data,
                'pie_list': pie_list,
                'x_axis_data': x_axis_data,
                'column_res': column_res
            },
            status=status.HTTP_200_OK
        )
