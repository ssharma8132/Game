# from django.urls import path, include
# from board.views import *
# from rest_framework.routers import DefaultRouter
#
#
# router = DefaultRouter()
# router.register('game', GameViewSet)
#
#
# game_list_view = GameViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
#
# urlpatterns = [
#     path('borad/', include(router.urls)),
#     path('board/', game_list_view, name='gamelist')
# ]

from django.urls import path, include
from rest_framework import routers
from board.views import *

router = routers.DefaultRouter()
router.register('game', GameViewSet)
router.register('player', PlayerState, basename='PlayerState')
router.register('match', Matchdata, basename='match')

urlpatterns = [
    path('', include(router.urls)),
    path('player', GameViewSet.as_view, name='playerstate')



]



# > routers.urls
# [<RegexURLPattern user-list ^minimal/$>,
# <RegexURLPattern user-list ^minimal\.(?P<format>[a-z0-9]+)/?$>,
# <RegexURLPattern user-detail ^minimal/(?P<pk>[^/.]+)/$>,
# <RegexURLPattern user-detail ^minimal/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$>,
# <RegexURLPattern user-list ^users/$>,
# <RegexURLPattern user-list ^users\.(?P<format>[a-z0-9]+)/?$>,
# <RegexURLPattern user-detail ^users/(?P<pk>[^/.]+)/$>,
# <RegexURLPattern user-detail ^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$>,
# <RegexURLPattern api-root ^$>,
# <RegexURLPattern api-root ^\.(?P<format>[a-z0-9]+)/?$>]