from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', views.index_page, name="uploader"),

    # path('', views.hotel_image_view, name="hotel_image_view"),

    path('tts', views.tts_page, name="index"),
    path('about', views.about_page, name="about"),
    path('test', views.test_page, name="test"),
    path('todo', views.todo_page, name="todo"),
    path('testimony1', views.testimony1, name="testimony1"),

    # path('image_upload', views.hotel_image_view, name='image_upload'),
    # path('success', views.success, name='success'),
    # path('post/edit/<int:id>/', views.edit_post, name='post-edit'),
    path('post/delete/<int:id>/', views.delete_post, name='delete-item'),
    path('delete/all',views.delete_all,name='delete-all'),

    path('edit-item/<int:id>/', views.edit_item, name='edit-item'),

    path('Publish', views.Publish, name='Publish'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.PHOTOS_URL, document_root=settings.PHOTOS_ROOT)

# if settings.DEBUG:
#     urlpatterns += [
#         # path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
#         path('photos/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
#     ]