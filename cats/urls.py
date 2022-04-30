from django.urls import path
from . import views
app_name = 'cats'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    # Page description cats
    path('cats/', views.cats, name='cats'),
    # Page new_cats
    path('new_cats/', views.new_cats, name='new_cats'),
    # Page cats
    path('cat/<int:cats_id>/', views.cat, name='cat'),
    # Page edit cats
    path('edit_cat/<int:cats_id>/', views.edit_cats, name='edit_cats'),
    # Page del cats
    path('del_cats/<int:cats_id>/', views.del_cats, name='del_cats'),
]