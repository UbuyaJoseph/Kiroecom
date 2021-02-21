from django.urls import path
from . import views

urlpatterns = [
    #Leave as empty string for base url
	path('', views.Store, name='Store'),
	path('Cart/', views.Cart, name="Cart"),
	path('Checkout/', views.Checkout, name="Checkout"),
	path('About/', views.About, name="About"),#To be worked upon!
	#path('Login/', views.Login, name="Login"),
	path('Contact/', views.Contact, name="Contact"),
	path('Men/', views.Men, name="Men"),
	path('Women/', views.Women, name="Women"),
	path('Children/', views.Children, name="Children"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),


]
