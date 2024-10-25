from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Members
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm, MembersForm
from django.contrib import messages
# Define correct credentials (for demonstration purposes)
ADMIN_CREDENTIALS = {
    'username': 'admin',
    'password': 'admin123'
}

USER_CREDENTIALS = {
    'username': 'user',
    'password': 'user123'
}

def login_view(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')  # Get the selected user type
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check credentials based on user type
        if user_type == 'admin' and username == ADMIN_CREDENTIALS['username'] and password == ADMIN_CREDENTIALS['password']:
            return redirect('admin_home')  # Redirect to the admin home page
        elif user_type == 'user' and username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            return redirect('user_page')  # Redirect to the user page
        else:
            # Render the login page with an error message if credentials are invalid
            return render(request, 'login.html', {'error': 'Invalid credentials. Please try again.'})

    return render(request, 'login.html')  # Render the login page for GET requests

def user_page(request):
    return render(request, 'user_page.html')  # Render your user page template
# start maintance
def maintenance_page(request):
    return render(request, 'maintenance.html')  

def add_membership(request):

    return render(request, 'add_membership.html')

def update_membership(request):
 
    return render(request, 'update_membership.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book_list')  # Replace with your book list URL name
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# View to update an existing book
def update_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_list')  # Replace with your book list URL name
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form, 'book': book})

def add_user_management(request):

    return render(request, 'add_user_management.html')

def update_user_management(request):
   
    return render(request, 'update_user_management.html')

def logout(request):
  
    return redirect('login_view')
# end maintance
#start addmembership
def add_membership(request):
    if request.method == 'POST':
        if 'cancel' in request.POST:
            messages.info(request, 'Transaction cancelled.')  # Set cancellation message
            return redirect('add_membership')  # Redirect to the same page

        elif 'confirm' in request.POST:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            contact_name = request.POST.get('contact_name')
            contact_address = request.POST.get('contact_address')
            adhaar_card_no = request.POST.get('adhaar_card_no')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            membership_duration = request.POST.get('membership_duration')

            # Process the data as needed (e.g., save it to the database)
            # Example: save_membership_to_db(first_name, last_name, contact_name, contact_address, adhaar_card_no, start_date, end_date, membership_duration)

            messages.success(request, 'Transaction completed successfully.')  # Set success message
            return redirect('add_membership')  # Redirect to the same page

    return render(request, 'add_membership.html')

#end add membership

#start update membership


from django.shortcuts import render, redirect
from django.contrib import messages

def update_membership(request):
    if request.method == 'POST':
        # Check which button was pressed
        if 'cancel' in request.POST:
            messages.info(request, 'Transaction cancelled.')  # Set cancellation message
            return redirect('update_membership')  # Redirect to the same page

        # Handle the Confirm action
        membership_number = request.POST.get('membership_number')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        membership_extension = request.POST.get('membership_extension')

        # Here you would normally process the data, such as updating the database.
        # Example: update_membership_in_db(membership_number, start_date, end_date, membership_extension)

        messages.success(request, 'Transaction completed successfully.')  # Set success message
        return redirect('update_membership')  # Redirect to the same page

    return render(request, 'update_membership.html')


#end update membership
#start add book

# View to add a new book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('admin_home')  # Replace with your book list URL name
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# View to update an existing book
def update_book(request, book_id):
    book = get_object_or_404(Book, BookID=book_id)  # Use BookID here
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('admin_home')  # Redirect to the list page after update
    return render(request, 'update_book.html', {'form': form})



def add_user_management(request):
    if request.method == 'POST':
        is_admin = request.POST.get('admin', 'off') == 'on'
        messages.success(request, "User management added successfully.")
        return redirect('add_user_management') 

    return render(request, 'add_user_management.html')

def update_user_management(request):
    if request.method == 'POST':
        is_active = request.POST.get('active', 'off') == 'on'
        messages.success(request, "User management updated successfully.")
        return redirect('update_user_management')  # Adjust redirect as needed

    return render(request, 'update_user_management.html')
def user_management(request):
    # Logic for displaying user management
    return render(request, 'user_management.html')

def reports_page(request):
    return render(request, 'reports.html')  # Render your reports page template

def transactions_page(request):
    return render(request, 'transactions.html')  # Render your transactions page template

def admin_home(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'admin_home.html', {'books': books})

def issue_book(request):
    if request.method == 'POST':
        # Process the form data here
        pass  # Add your form processing logic

    books = Book.objects.all()  # Fetch available books
    members = Members.objects.all()  # Fetch members

    return render(request, 'issue_book.html', {'books': books, 'members': members})

def add_member(request):
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')  # Adjust this to your member listing page or home
    else:
        form = MembersForm()
    
    return render(request, 'add_member.html', {'form': form})