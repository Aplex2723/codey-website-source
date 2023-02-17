from django.urls import path
from .views import ProjectsListView, ProjectDetailView

portfolio_patterns = ([
    path("", ProjectsListView.as_view(), name="portfolios"),
    path("<slug:slug>", ProjectDetailView.as_view(), name="project")
], 'portfolio')