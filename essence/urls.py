from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mainApp import views as mainApp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainApp.home),
    path('checkout/',mainApp.checkout),
    path('shop/<str:mc>/<str:sc>/<str:br>/',mainApp.shop),
    path('contact/',mainApp.contact),
    path('single-product/<int:num>/',mainApp.singleProduct),
    path('price-filter/<str:mc>/<str:sc>/<str:br>/',mainApp.priceFilter),
    path('sort-filter/<str:mc>/<str:sc>/<str:br>/',mainApp.sortFilter),
    path('search/',mainApp.searchPage),
    path('login/',mainApp.loginPage),
    path('signup/',mainApp.signupPage),
    path('logout/',mainApp.logoutPage),
    path('profile/',mainApp.profilePage),
    path('update-profile/',mainApp.updateProfilePage),
    path('add-to-cart/<int:num>/',mainApp.addToCart),
    path('cart/',mainApp.cartPage),
    path('delete-cart/<str:id>/',mainApp.deleteCartPage),
    path('update-cart/<str:id>/<str:op>/',mainApp.updateCartPage),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





