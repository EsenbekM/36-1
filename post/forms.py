from django import forms

from post.models import Post, Comment


class PostCreateForm(forms.Form):
    photo = forms.ImageField(
        required=False,
        label="Фото",
    )
    title = forms.CharField(
        max_length=10,
        label="Название",
    )
    content = forms.CharField(
        required=False,
        label="Контент",
        widget=forms.Textarea
    )

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 10:
            raise forms.ValidationError("Длина превышает 10 символов")
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title == content:
            raise forms.ValidationError("Заголовок и контент совпадают")

        return cleaned_data
    

class PostCreateForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('photo', 'title', 'content', 'hashtags')
        labels = {
            'photo': 'Фото',
            'title': 'Название',
            'content': 'Контент',
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 10:
            raise forms.ValidationError("Длина превышает 10 символов")
        return title
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
    
        if title == content:
            raise forms.ValidationError("Заголовок и контент совпадают")
    
        return cleaned_data
    

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        labels = {
            'content': 'Контент',
        }