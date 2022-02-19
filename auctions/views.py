from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ModelForm
from .models import User

from .forms import CreateForm
from .forms import CreateListing
from .forms import CreateComment
from .forms import Comment
from .forms import FilterByCategory

from .forms import Watchlist
from .forms import CreateWatchlist

from .forms import CreateBid
from .forms import Bid
from django.db.models import Max

from .filters import OrderFilter
from django.contrib import messages

def index(request):
    elements = CreateListing.objects.all()
    context = {'elements' : elements}
    return render(request, "auctions/index.html", context)
 
def watchlist(request):
    profile = request.user

    #watchlist = Watchlist.objects.all()
    return render(request, "auctions/watchlist.html", {
        #"watchlist" : watchlist,
        "profile" : profile,
    })

def bidTo(request, pk):
    profile = request.user

    some = 'approve'

    #maxim = Bid.objects.aggregate(Max('bid'))
    #maxList = Bid.objects.order_by('-listToBid')[0]

    obj = CreateListing.objects.get(title=pk)

    form = CreateBid()

    bids = Bid.objects.all()

    if request.method == 'POST':
        form = CreateBid(request.POST)
        form.instance.user = profile
        form.instance.listToBid = obj
       

        if form.is_valid():
                #print(form.instance.bid)
                #print(obj.startingBid)

                if form.instance.bid > obj.startingBid:
                    form.save()
                    obj.startingBid = form.instance.bid
                    obj.currentbidder = str(form.instance.user)
                    print(obj.currentbidder)
                    print(obj.closing)

                    obj.save()

                    form=CreateBid()

                else:
                    messages.success(request, ("Number is lower!"))
                    #return redirect('watchlist')
    return render(request, "auctions/create-bid.html",{
            "element" : obj,
            "bids" : bids,
            "form" : form,
            'some' : some

        })

def closeBid(request,pk):
    obj = CreateListing.objects.get(title=pk)
    obj.closing = True
    obj.currentbidder = str(obj.currentbidder+ " WON! - CLOSED")
    obj.save()
    #print(obj.closing)
    return redirect('index')



def createWatchlist(request, event_id):
    profile = request.user
    obj = CreateListing.objects.get(title=event_id)
    #form.instance.listToComment = obj

    if request.method == 'POST':
        form = CreateWatchlist(request.POST)
        form.instance.userlist = profile
        form.instance.element = obj

        if form.is_valid():
            form.save()

        return redirect('index')
        
  
def add_event(request, event_id):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

   
def entry(request, pk):
        profile = request.user
        bids = Bid.objects.all()

        comments = Comment.objects.all()


        obj = CreateListing.objects.get(title=pk)

        form = CreateComment()
        if request.method == 'POST':
            form = CreateComment(request.POST)
            form.instance.user = profile
            form.instance.listToComment = obj

            if form.is_valid():
                form.save()
                form=CreateComment()
        return render(request, "auctions/entry.html",{
            'profile' : profile,
            'comments' : comments,
            'element' : obj,
            'form' : form,
            'bids' : bids

            })

def delete_event(request, event_id):
    event = Watchlist.objects.get(pk=event_id)
    event.delete()
    return redirect("watchlist")
   
            
def categories(request):
    elements = CreateListing.objects.all()

    myFilter = OrderFilter(request.GET, queryset=elements)
    multis = myFilter.qs

    return render(request, "auctions/categories.html",
        {       'myFilter' : myFilter,
                'multis' : multis
        })


def create(request):
    profile = request.user
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        form.instance.user = profile

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form' : form}
    return render(request, "auctions/create.html", context)



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
