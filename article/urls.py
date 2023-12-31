from django.urls import path
from . import views

urlpatterns = [
    path("category", views.CategoryView.as_view()),
    path("list", views.ListView.as_view()),
    path("lists", views.ListViews.as_view()),
    path("count", views.ListCountView.as_view()),

    path("nightingale", views.NightingaleChartView.as_view()),
    path("line", views.LineChartView.as_view()),
    path("codeforces", views.CodeforcesStatusView.as_view())
]
