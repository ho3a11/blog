from django import forms
from .models import Post, Category , Comment
from taggit.forms import TagWidget



# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'category','image']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {

            'name': forms.Select(attrs={'class': 'form-control'}),
        }




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category','tags']
        tags = forms.CharField(widget=TagWidget)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'col-sm-3 col-form-label text-right tm-color-primary'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)
