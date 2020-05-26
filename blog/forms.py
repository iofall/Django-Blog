from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'banner_image_url', 'text')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control textinputclass'}),
            'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent form-control',
                                            'placeholder': "Enter your blog post",
                                            }),
            'banner_image_url': forms.URLInput(attrs={'class': 'form-control',
                                                        'spellcheck': 'false'}),
                    }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
                'author' : forms.TextInput(attrs={'class':'form-control textinputclass'}),
                'text' : forms.Textarea(attrs={'class':'editable form-control medium-editor-textarea',
                                                'rows': 10})
                  }
