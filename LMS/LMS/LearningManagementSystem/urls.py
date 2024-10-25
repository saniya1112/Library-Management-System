from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LogoutView  # Import the LogoutView
from .views import (
    login_view,
    admin_home,
    user_page,
    maintenance_page,
    reports_page,
    transactions_page,
    add_membership,      # Import the views you need
    update_membership,
    add_book,
    add_user_management,
    update_user_management,
    book_list,
    update_book,
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', login_view, name='login_view'),  # Root URL for login
    path('user-page/', user_page, name='user_page'),  # User page
    path('admin-home/', admin_home, name='admin_home'),  # Admin home page
    path('maintenance/', maintenance_page, name='maintenance_page'),  # Maintenance page
    path('reports/', reports_page, name='reports_page'),  # Reports page
    path('transactions/', transactions_page, name='transactions_page'),  # Transactions page
    path('logout/', LogoutView.as_view(), name='logout'),  # Add logout URL
    path('membership/add/', add_membership, name='add_membership'),  # Add Membership
    path('membership/update/', update_membership, name='update_membership'), 
    path('add-book/', add_book, name='add_book'), 
    path('update_book/<int:book_id>/', update_book, name='update_book_movie'),
    path('user/add/', add_user_management, name='add_user_management'),  # Add User
    path('user/update/', update_user_management, name='update_user_management'),
    path('membership/add/', add_membership, name='add_membership'), # Update User
    path('book-list/', book_list, name='book_list'),
]
