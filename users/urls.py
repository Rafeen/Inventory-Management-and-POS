from django.urls import path,include
from users.views.login import login_view
from users.views.dashboard import dashboard_view
from users.views.create import create_user_view, store_user
from users.views.user_list import user_list_view
from users.views.csv_import import user_csv_import
from users.views.logout import logout_view
from users.views.user_detail import user_detail_view
from users.views.change_user_details import update_user
# from users.views.reset_password_email_view import reset_password_page
# from users.views.reset_password_done import reset_password_done

from django.conf import settings
from django.conf.urls.static import static



app_name = 'users'

urlpatterns = [
                  path('login/', login_view, name='login'),
                  path('dashboard/',dashboard_view,name='dashboard'),
                  path('create-user/',create_user_view, name='create_user_view'),
                  path('store-user/', store_user, name='store_user'),
                  path('update-user/', update_user, name='update_user'),

                  path('users/', user_list_view, name='user-list'),
                  path('users/<int:id>/', user_detail_view, name='user-detail'),

                  path('user-csv-import/', user_csv_import, name='user_csv_import'),
                  path('logout/', logout_view, name='logout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)