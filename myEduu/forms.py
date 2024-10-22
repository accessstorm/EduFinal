
#own
from django import forms
from .models import Post, Category, Comment


#choices = [('coding', 'coding'), ('Java', 'Java'), ('Python (py3)', 'Python (py3)'), ('Frontend', 'Frontend'), ('Backend', 'Backend'), ('nodejs', 'nodejs'), ('API', 'API')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'summary')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Enter Title"}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '','type':'hidden', 'id':'author'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', "placeholder":"Write a short overview of your topic"}),
            
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'summary')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', "placeholder":"Write a short overview of your topic"}),

        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('heading', 'body')
        
        widgets = {
            'heading': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }
        
        
        
