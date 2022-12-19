"""AI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,re_path

from user.views import account, health, sports
urlpatterns = [
    path('register/', account.register, name= 'register'),
    path('login/', account.login, name = 'login'),

    # user profile
    path('user/<int:id>/profile', account.get_user_info, name = 'user_info'),
    path('saveinfo/', account.save_user_info, name = 'save_info'),

    # health data
    path('add_datum/',health.add_datum,name='add_datum'),
    path('get_day_glucose/',health.get_day_glucose,name='get_day_glucose'),
    path('get_week_glucose/',health.get_week_glucose,name='get_week_glucose'),
    path('get_month_glucose/',health.get_month_glucose,name='get_month_glucose'),
    path('get_week_statistics/',health.get_week_statistics,name='get_week_statistics'),
    path('get_month_statistics/',health.get_month_statistics,name='get_month_statistics'),
    re_path('^active/(?P<active_code>.*)/$', account.ActiveUserView.as_view(), name='active_code'),  # 注册激活链接

    # sports data
    path('add_sports_record/', sports.add_sports_record, name = 'add_sports_record'),
    path('get_sports_data/', sports.get_sports_data, name = 'get_sports_data'),

    # check database
    path('show/', account.show_list, name = 'show'),
]