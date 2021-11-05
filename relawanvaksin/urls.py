from django.urls import path

from .views import detail_relawan_vaksin, lihat_data_relawan_vaksin,index,MainView,PostJsonListView
# from Module_relawan_vaksin.views import MainView, PostJson

app_name = 'relawanvaksin'
#Url untuk page daftar dan melihat data relawan vaksin
urlpatterns = [
    path('', index, name='index'),
    path('lihat_data_relawan_vaksin/',lihat_data_relawan_vaksin.as_view(), name="data-relawan-vaksin"),
    path('detail_relawan_vaksin/<int:pk>', detail_relawan_vaksin.as_view(),name="detail-relawan-vaksin"),
    path('data_relawan_vaksin_singkat/', MainView.as_view(),name='main-view'),
    path('data_relawan_vaksin_singkat/data_relawan_json/<int:num_posts>/', PostJsonListView.as_view(),name='data-relawan-json-view')
]
