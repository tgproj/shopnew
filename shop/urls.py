from django.urls import path
from shop import views
from django.contrib.auth import views as auth_view
from shop.forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('pdetails/<int:pk>', views.PdetailsView.as_view(), name='pdetails'),
    path('mobile',views.mobile,name='mobile'),
    path('mobile/<slug:data>',views.mobile,name='mobiledata'),
    path('laptops',views.laptops,name='laptop'),
    path('laptops/<slug:data>',views.laptops,name='laptops'),
    path('boyt_wears',views.boyt_wears,name='boyt_wear'),
    path('boyt_wears/<slug:data>',views.boyt_wears,name='boyt_wears'),
    path('boyb_wears/<slug:data>',views.boyb_wears,name='boyb_wears'),
    path('girlt_wears/<slug:data>',views.girlt_wears,name='girlt_wears'),
    path('girlb_wears/<slug:data>',views.girlb_wears,name='girlb_wears'),
    path('registration',views.CustomerRegistrationView.as_view(),name="customerregistration"),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done',auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),
    path('address/', views.address, name='address'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('shop-now/', views.shop_now, name='shop'),
    path('cart/', views.show_cart, name='showcart'),
    path('plus_cart/', views.plus_cart, name='plus_cart'),
    path('minuscart/', views.minus_cart, name='minus_cart'),
    path('removecart/', views.remove_cart, name='remove_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('orders/', views.orders, name='orders'),

]


