from django.urls import path
from accounts.views import (SendPasswordResetEmailView, UserChangePasswordView, UserLoginView,
                           UserProfileView, UserRegistrationView, UserPasswordResetView, CreateMenuGrpView, UpdateMenuGrpView, UpdateMenuMasterView, CreateMenuMasterView,
                           CreateTaskMasterView, UpdateTaskMasterView, CreateUserTaskAccessView, UpdateUserTaskAccessView, CreateFieldMasterView, UpdateFieldMasterView,
                           CreateTaskFieldMasterView, UpdateTaskFieldMasterView)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(),
         name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',
         UserPasswordResetView.as_view(), name='reset-password'),

    path('menuview/', CreateMenuGrpView.as_view(), name='menuview'),
    path('menuview/<int:pk>', UpdateMenuGrpView.as_view(), name='menuviewupdate'),
    path('menumasterview/', CreateMenuMasterView.as_view(), name='menumasterview'),
    path('menumasterview/<int:pk>', UpdateMenuMasterView.as_view(),
         name='menumasterviewupdate'),
    path('taskmasterview/', CreateTaskMasterView.as_view(), name='taskmasterview'),
    path('taskmasterview/<int:pk>', UpdateTaskMasterView.as_view(),
         name='taskmasterviewupdate'),
    path('usertaskaccessview/', CreateUserTaskAccessView.as_view(),
         name='usertaskaccessview'),
    path('usertaskaccessview/<int:todo_id>/', UpdateUserTaskAccessView.as_view(),
         name='usertaskaccessviewupdate'),
    path('fieldmasterview/', CreateFieldMasterView.as_view(), name='fieldmasterview'),
    path('fieldmasterview/<int:todo_id>/', UpdateFieldMasterView.as_view(),
         name='fieldmasterviewupdate'),
    path('taskfieldmasterview/', CreateTaskFieldMasterView.as_view(),
         name='taskfieldmasterview'),
    path('taskfieldmasterview/<int:pk>/',
         UpdateTaskFieldMasterView.as_view(), name='taskfieldmasterviewupdate'),



]
