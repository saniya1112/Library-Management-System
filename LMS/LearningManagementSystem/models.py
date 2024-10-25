from django.db import models
from datetime import date
from django.core.exceptions import ValidationError




class BookMovie(models.Model):
    book_movie_name = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=50)
    user_management = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.book_movie_name

class Members(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    member_id = models.CharField(max_length=10, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    aadhar = models.CharField(max_length=12, unique=True)
    enroll_date = models.DateField(default=date.today)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Active')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.member_id:
            last_member = Members.objects.order_by('member_id').last()
            if last_member:
                new_id = int(last_member.member_id[3:]) + 1
            else:
                new_id = 1001
            self.member_id = f"LMS{new_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Book(models.Model):
    BookID = models.PositiveIntegerField(primary_key=True)  # Use PositiveIntegerField for custom ID
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    procurement_date = models.DateField()

    def save(self, *args, **kwargs):
        # Set BookID to start from 1001
        if not self.BookID:
            last_book = Book.objects.order_by('BookID').last()
            if last_book:
                self.BookID = last_book.BookID + 1
            else:
                self.BookID = 1001
        elif self.BookID < 1001:
            raise ValidationError("BookID cannot be less than 1001.")

        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Issue(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    member = models.ForeignKey('Members', on_delete=models.CASCADE)
    date_of_issue = models.DateField()
    date_of_return = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Issue: {self.book.name} to {self.member.name}"
    
    
class OverdueReturn(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    member = models.ForeignKey('Members', on_delete=models.CASCADE)
    date_of_issue = models.DateField()
    date_of_return = models.DateField()
    fine_per_day = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    @property
    def fine_calculation(self):
        # Calculate the number of overdue days and multiply by fine per day
        overdue_days = (self.date_of_return - self.date_of_issue).days - 14  # Assuming a 14-day return period
        return max(overdue_days * self.fine_per_day, 0)  # Fine only if overdue

    def __str__(self):
        return f"Overdue: {self.book.name} by {self.member.name}"

