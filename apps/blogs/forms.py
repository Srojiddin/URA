from django import forms
from apps.blogs.models import Blog
from .models import Gallery

class BlogSearchForm(forms.Form):
    title = forms.CharField(required=False, label='Название')

class BlogBaseForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'description',
            'image_for_blogs',
            'creation_date'
        )

class BlogCreateForm(BlogBaseForm):
    pass

class BlogDetailForm(BlogBaseForm):
    pass

class BlogUpdateForm(BlogBaseForm):
    pass

class BlogDeleteForm(BlogBaseForm):  
    pass




class GalleryCreateForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image_for_Gallery', 'description',]


    
class GalleryUpdateForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image_for_Gallery', 'description',]




class GalleryDeleteForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image_for_Gallery', 'description',]