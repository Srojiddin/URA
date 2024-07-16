from django import forms
from apps.doctors.models import Doctor

# from .models import DoctorProfile

class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'choosing_a_specialization', 'phone_number', 'email', 'image_for_doctor']


class DoctorBaseForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'choosing_a_specialization', 'phone_number', 'email', 'image_for_doctor']


# class DoctorCreateForm(DoctorBaseForm):
#     pass

#
# class DoctorDetailForm(DoctorBaseForm):
#     class Meta(DoctorBaseForm.Meta):
#         fields = ['name', ' 'age', 'image_for_doctor', 'choosing_a_specialization', 'creation_date']


class DoctorUpdateForm(DoctorBaseForm):
    pass


class DoctorDeleteForm(DoctorBaseForm):
    pass


# class DoctorProfileForm(forms.ModelForm):
#     class Meta:
#         model = DoctorProfile
#         fields = ('bio', 'address', 'phone_number')