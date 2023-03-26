from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Item, Cart

# Create your views here.


def index(response):
    cart = Cart.objects.all()
    print(len(cart))
    return render(response, "main/base.html", {"cart": len(cart)})

def home(response):
    category = Category.objects.all()
    cart = Cart.objects.all()
    items = Item.objects.all()
    

    if response.method == "POST":
        item = response.POST.get("add")
        cartItem = Item.objects.get(id=item)
        print(cartItem.name)
        print(cartItem.imgLink)
        print(cartItem.descr)
        print(cartItem.price)
        print(cartItem.rating)

        cartAdd = Cart(title = cartItem.name, name = cartItem.name, imgLink = cartItem.imgLink, descr = cartItem.descr, price = cartItem.price, rating = cartItem.rating)
        cartAdd.save()

        print(response.POST.get("add"))
        print(Item.objects.get(id=item).name)
        return HttpResponseRedirect("/")
       
    else:
        pass

    """
    Items = [["Shirt", "Makes a man out of you", "R300", 3.0],
             ["T-shirt", "Makes you look hot in the sun", "R250", 4.0],
             ["Brief", "Makes your busines a secret", "R150", 3.0],
             ["Van Gal", "Makes you smell wonderfull", "R330", 4.0],
             ["Trousers", "Makes you feel like its a swag", "R550", 5.0],
             ["Shoes", "Makes you walk in style", "R700", 4.0],
             ["Vest", "Brings out that sexy look you derserve", 3.0]]
    item = Category.objects.get(id=1)
    for x in range(len(Items)):
        print(str(x))
        newStr = "http " + str(x)
        item.item_set.create(imgLink=newStr, name=Items[x][0], descr=Items[x][1], price=Items[x][2], rating=Items[x][3])
        print("Saved")
        """
    return render(response, "main/home.html", {"category": category, "cart": len(cart)})

def cart(response):
    cartItems = Cart.objects.all()
    cartTotal = 0
    for x in cartItems:
        cartTotal += float(x.price[1:])
        print(cartTotal)

    if response.method == "POST":
        del_item_id = response.POST.get("add")
        del_item = cartItems.get(id=del_item_id)
        print(del_item.price[1:])
        del_item.delete()
        return HttpResponseRedirect("/cart")
        """if cartItems:
            
            return render(response, "main/cart.html", {"cartItems": cartItems})
    else:
        return render(response, "main/cart.html", {"cartItems": cartItems})
        """
    return render(response, "main/cart.html", {"cartItems": cartItems, "cartTotal": cartTotal})

def signup(response):
    pass

def login(response):
    pass

def logout(response):
    pass