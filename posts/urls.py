from django.urls import path,include
from . import views


urlpatterns = [

    path('unpublished', views.unpublished_list,name='unpublished'),
    path('published', views.published_list , name="published"),
    path('create_post', views.createpost,name='create_post'),
    path('edit_details/p=<int:id>', views.edit_details,name='edit_details'),
    path('edit_schedule_post/p=<int:id>', views.edit_schedule_post,name='edit_schedule_post'),
    path('schedule_posts', views.schedule_posts,name='schedule_posts'),
    path('show/p=<int:id>', views.post_details,name='post_details'),
    path('delete/p=<int:id>', views.delete_post,name='delete_post'),
    path('add_to_schedule/p=<int:id>', views.add_to_schedule,name='add_to_schedule'),
    path('get_posts', views.get_posts,name='get_posts'),
    path('upload', views.upload,name='upload'),
    path('publish_now/p=<int:id>', views.publish_now,name='publish_now'),
    path('delete_schedule/p=<int:id>', views.delete_schedule,name='delete_schedule'),
    path('make_design/p=<int:id>', views.make_design,name='make_design'),
    path('new_design/p=<int:id>',views.new_design,name="new_design"),
    path('schedule_design/<int:id>',views.schedule_design,name="schedule_design"),
    path('test',views.test,name="test"),


    ##################################################################################################
                                   ###### Ajax_URLS ######
                                   #######################
    path('delete_post_ajax/p=<int:id>', views.delete_post_ajax,name='delete_post_ajax'),

]
