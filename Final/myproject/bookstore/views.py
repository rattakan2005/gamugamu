from django.shortcuts import render,redirect
from django.http import HttpResponse
from bookstore.models import Book
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import BookstoreForm
from .models import Book

# Create your views here.
def index(request):
    all_Book = Book.objects.all()
    return render(request,"index.html",{"all_book":all_Book})
def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        price = request.POST.get("price")
        status = request.POST.get("status")
        date = request.POST.get("date")

        Book.objects.create(
            name=name,
            category=category,
            price=price,
            status=status,
            date=date
        )
        return redirect("index")
    
    else:
        
        return render(request,"form.html")
    
def about(request):
    return render(request,"about.html")

def checkout(request):
    return render(request, 'checkout.html')

def search(request):
    query = request.GET.get('q','')
    bookstore = Book.objects.filter(
        Q(name__icontains=query) |
        Q(category__icontains=query) | 
        Q(status__icontains=query) 
    )
    return render(request, 'search.html', {'books': bookstore, 'query': query})

def edit(request, pk):
    bookstore = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookstoreForm(request.POST, instance=bookstore)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookstoreForm(instance=bookstore)
    
    # <<< ต้องมี return render(...) ด้านนอก if/else
    return render(request, 'edit.html', {'form': form, 'bookstore': bookstore})
    
def delete(request,pk):
    bookstore = get_object_or_404(Book,pk=pk)
    if request.method =='POST':
        bookstore.delete()
    return redirect('index')

def add_to_cart(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')  # ดึงค่าจาก input hidden
        cart = request.session.get('cart', {})

        if book_id in cart:
            cart[book_id] += 1
        else:
            cart[book_id] = 1

        request.session['cart'] = cart
    return redirect('index')

def cart_view(request):
    cart = request.session.get('cart', {})
    all_book = []

    for book_id, quantity in cart.items():
        if not str(book_id).isdigit():
            continue 
        
        book = get_object_or_404(Book, pk=int(book_id))
        book.quantity = quantity
        book.total_price = quantity * book.price
        all_book.append(book)

    return render(request, 'cart_view.html', {'all_book': all_book, 'cart': cart})



def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})