from django.forms import ModelForm
from .models import CreateListing
from .models import Watchlist
from .models import Comment
from .models import Bid

from django import forms


class CreateForm(ModelForm):
    class Meta:
        model = CreateListing
        fields = ['title','description','startingBid','url','tags']

        labels = {
            'title':'',
            'description': '',
            'startingBid' : '',
            'url': '',
           'tags':'Category',
        }

        widgets = {
            'title' :forms.TextInput(attrs={'class' :'form-control', 'placeholder' :'Title' }),
            'description':forms.TextInput(attrs={'class' :'form-control', 'placeholder' :'Description'}),
            'startingBid':forms.TextInput(attrs={'class' :'form-control', 'placeholder' :'Starting Bid $'}),
            #'url':forms.TextInput(attrs={'class' :'form-control', 'placeholder' :'Url'}),
            'tags':forms.Select(attrs={'class' :'form-control', 'placeholder' :'Tags'}),
            'url': forms.URLInput(attrs={"class": "form-control" ,'placeholder' :'Image URL'})

        }

class FilterByCategory(ModelForm):
    class Meta:
        model = CreateListing
        fields = ['tags']

        widgets = {
            'tags' :forms.Select(attrs={'class' :'form-control', 'placeholder' :'Tag' }),
        }


class CreateWatchlist(ModelForm):
    class Meta:
        model = Watchlist
        fields = []


class CreateComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        widgets = {
            'comment' :forms.Textarea(attrs={'class' :'form-control', 'placeholder' :'Comment..here' }),
        }

class CreateBid(ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']
    