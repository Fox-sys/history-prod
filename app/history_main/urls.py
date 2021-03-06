from django.urls import path
from .views import SolderList, SolderDetail, CreateUpdateSolder, \
                   Register, ConfirmLogoutView, \
                   ExhibitDetail, ExhibitList, ProfileDetail, \
                   ProfileList, ConfirmDeleteSolder, \
                   EditProfile, ChangePasswordView

urlpatterns = [
    path('', SolderList.as_view(), name="index"),
    path('solders/<int:pk>/', SolderDetail.as_view(), name="solder_detail"),
    # path('solders/create/', CreateUpdateSolder.as_view(), name="create_solder"),
    # path('solders/update/<int:pk>/', CreateUpdateSolder.as_view(), name="update_solder"),
    # path('solders/delete/<int:pk>/', ConfirmDeleteSolder.as_view(), name="confirm_delete_solder"),
    # path('register/', Register.as_view(), name="register"),
    # path('logout/', ConfirmLogoutView.as_view(), name="confirm_logout"),
    path('exhibits/', ExhibitList.as_view(), name="exhibit_list"),
    path('exhibits/<int:pk>', ExhibitDetail.as_view(), name="exhibit_detail"),
    # path('profiles/<int:pk>', ProfileDetail.as_view(), name="profile_detail"),
    # path('profiles/', ProfileList.as_view(), name="profile_list"),
    # path('profiles/edit/', EditProfile.as_view(), name="edit_profile"),
    # path('changepassword/', ChangePasswordView.as_view(), name="change_password"),
]
