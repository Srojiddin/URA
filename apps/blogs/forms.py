from django import forms
from apps.blogs.models import Blog
from .models import Gallery



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


class NewsSearchForm(forms.Form):
    search_name = forms.CharField(label='Search by Name', required=False)

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