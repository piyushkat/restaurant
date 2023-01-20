from django.urls import path,include
from food.views import UserRegistrationView,VerifyOtpForEmailVerification,VerifyEmailSecondTime,UserLoginView,UpdateUserProfile,DeleteUserProfile,SendPasswordEmailView,UserChangePasswordView,UserPasswordResetView,GoogleAuthView

urlpatterns = [

    path('signup',UserRegistrationView.as_view(), name='signup'),
    path('verifyotp',VerifyOtpForEmailVerification.as_view(), name='verifyotp'),
    path('verifyemail',VerifyEmailSecondTime.as_view(), name='verifyemail'),
    path('signin',UserLoginView.as_view(), name='signin'),
    path('profile/<int:id>',UpdateUserProfile.as_view(), name='profileupdate'),
    path('deleteprofile/<int:id>',DeleteUserProfile.as_view(), name='deleteprofile'),
    path('sendemailforpassword',SendPasswordEmailView.as_view(), name='sendemail'),
    path('changepassword',UserChangePasswordView.as_view(), name='changepassword'),
    path('resetpassword/<uid>/<token>',UserPasswordResetView.as_view(), name='resetpassword'),


    path('google',GoogleAuthView.as_view(), name='google'),

]
