from django import forms
from .models import Article

# create your forms here.

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
    
    # def clean(self):
    #     data = self.cleaned_data
    #     title = data.get('title')
    #     qs = Article.objects.filter(title=title)
    #     if qs.exists():
    #         self.add_error("title", f"{title} is already taken. Please take another title.")
    #     return data
