from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from login.models import (
    ProductReadiness, Task1StatusVideoContent, Task2StatusVideoContent, Task3StatusVideoContent
    ,Task4StatusVideoContent, Task5StatusVideoContent,Task6StatusVideoContent,Task7StatusVideoContent
    ,Task8StatusVideoContent,Task9StatusVideoContent,Task10StatusVideoContent,Task11StatusVideoContent
    ,Task12StatusVideoContent,Task13StatusVideoContent,Task14StatusVideoContent,Task15StatusVideoContent
    ,Task16StatusVideoContent,Task17StatusVideoContent,Task18StatusVideoContent,Task19StatusVideoContent
    ,Task20StatusVideoContent, videocontent, digitalcontent, callcentertraining, callcenteropertaions,
    productsupport, warehouse, fieldservice, techsupport, servicemarketing, servicetraining, parts,
Task1StatusProductReadiness, Task2StatusProductReadiness, Task3StatusProductReadiness
    ,Task4StatusProductReadiness, Task5StatusProductReadiness,Task6StatusProductReadiness,Task7StatusProductReadiness
    ,Task8StatusProductReadiness,Task9StatusProductReadiness,Task10StatusProductReadiness,Task11StatusProductReadiness
    ,Task12StatusProductReadiness,Task13StatusProductReadiness,Task14StatusProductReadiness,Task15StatusProductReadiness
    ,Task16StatusProductReadiness,Task17StatusProductReadiness,Task18StatusProductReadiness,Task19StatusProductReadiness
    ,Task20StatusProductReadiness,
Task1StatusDigitalContent, Task2StatusDigitalContent, Task3StatusDigitalContent
    ,Task4StatusDigitalContent, Task5StatusDigitalContent,Task6StatusDigitalContent,Task7StatusDigitalContent
    ,Task8StatusDigitalContent,Task9StatusDigitalContent,Task10StatusDigitalContent,Task11StatusDigitalContent
    ,Task12StatusDigitalContent,Task13StatusDigitalContent,Task14StatusDigitalContent,Task15StatusDigitalContent
    ,Task16StatusDigitalContent,Task17StatusDigitalContent,Task18StatusDigitalContent,Task19StatusDigitalContent
    ,Task20StatusDigitalContent,
Task1StatusCallCenterTraining, Task2StatusCallCenterTraining, Task3StatusCallCenterTraining
    ,Task4StatusCallCenterTraining, Task5StatusCallCenterTraining,Task6StatusCallCenterTraining,Task7StatusCallCenterTraining
    ,Task8StatusCallCenterTraining,Task9StatusCallCenterTraining,Task10StatusCallCenterTraining,Task11StatusCallCenterTraining
    ,Task12StatusCallCenterTraining,Task13StatusCallCenterTraining,Task14StatusCallCenterTraining,Task15StatusCallCenterTraining
    ,Task16StatusCallCenterTraining,Task17StatusCallCenterTraining,Task18StatusCallCenterTraining,Task19StatusCallCenterTraining
    ,Task20StatusCallCenterTraining,
Task1Statuscallcenteropertaions, Task2Statuscallcenteropertaions, Task3Statuscallcenteropertaions
    ,Task4Statuscallcenteropertaions, Task5Statuscallcenteropertaions,Task6Statuscallcenteropertaions,Task7Statuscallcenteropertaions
    ,Task8Statuscallcenteropertaions,Task9Statuscallcenteropertaions,Task10Statuscallcenteropertaions,Task11Statuscallcenteropertaions
    ,Task12Statuscallcenteropertaions,Task13Statuscallcenteropertaions,Task14Statuscallcenteropertaions,Task15Statuscallcenteropertaions
    ,Task16Statuscallcenteropertaions,Task17Statuscallcenteropertaions,Task18Statuscallcenteropertaions,Task19Statuscallcenteropertaions
    ,Task20Statuscallcenteropertaions,
Task1Statusproductsupport, Task2Statusproductsupport, Task3Statusproductsupport
    ,Task4Statusproductsupport, Task5Statusproductsupport,Task6Statusproductsupport,Task7Statusproductsupport
    ,Task8Statusproductsupport,Task9Statusproductsupport,Task10Statusproductsupport,Task11Statusproductsupport
    ,Task12Statusproductsupport,Task13Statusproductsupport,Task14Statusproductsupport,Task15Statusproductsupport
    ,Task16Statusproductsupport,Task17Statusproductsupport,Task18Statusproductsupport,Task19Statusproductsupport
    ,Task20Statusproductsupport,
Task1Statuswarehouse, Task2Statuswarehouse, Task3Statuswarehouse
    ,Task4Statuswarehouse, Task5Statuswarehouse,Task6Statuswarehouse,Task7Statuswarehouse
    ,Task8Statuswarehouse,Task9Statuswarehouse,Task10Statuswarehouse,Task11Statuswarehouse
    ,Task12Statuswarehouse,Task13Statuswarehouse,Task14Statuswarehouse,Task15Statuswarehouse
    ,Task16Statuswarehouse,Task17Statuswarehouse,Task18Statuswarehouse,Task19Statuswarehouse
    ,Task20Statuswarehouse,
Task1Statusfieldservice, Task2Statusfieldservice, Task3Statusfieldservice
    ,Task4Statusfieldservice, Task5Statusfieldservice,Task6Statusfieldservice,Task7Statusfieldservice
    ,Task8Statusfieldservice,Task9Statusfieldservice,Task10Statusfieldservice,Task11Statusfieldservice
    ,Task12Statusfieldservice,Task13Statusfieldservice,Task14Statusfieldservice,Task15Statusfieldservice
    ,Task16Statusfieldservice,Task17Statusfieldservice,Task18Statusfieldservice,Task19Statusfieldservice
    ,Task20Statusfieldservice,
Task1Statustechsupport, Task2Statustechsupport, Task3Statustechsupport
    ,Task4Statustechsupport, Task5Statustechsupport,Task6Statustechsupport,Task7Statustechsupport
    ,Task8Statustechsupport,Task9Statustechsupport,Task10Statustechsupport,Task11Statustechsupport
    ,Task12Statustechsupport,Task13Statustechsupport,Task14Statustechsupport,Task15Statustechsupport
    ,Task16Statustechsupport,Task17Statustechsupport,Task18Statustechsupport,Task19Statustechsupport
    ,Task20Statustechsupport,
Task1Statusservicemarketing, Task2Statusservicemarketing, Task3Statusservicemarketing
    ,Task4Statusservicemarketing, Task5Statusservicemarketing,Task6Statusservicemarketing,Task7Statusservicemarketing
    ,Task8Statusservicemarketing,Task9Statusservicemarketing,Task10Statusservicemarketing,Task11Statusservicemarketing
    ,Task12Statusservicemarketing,Task13Statusservicemarketing,Task14Statusservicemarketing,Task15Statusservicemarketing
    ,Task16Statusservicemarketing,Task17Statusservicemarketing,Task18Statusservicemarketing,Task19Statusservicemarketing
    ,Task20Statusservicemarketing,
Task1StatusVideoContent, Task2StatusVideoContent, Task3StatusVideoContent
    ,Task4StatusVideoContent, Task5StatusVideoContent,Task6StatusVideoContent,Task7StatusVideoContent
    ,Task8StatusVideoContent,Task9StatusVideoContent,Task10StatusVideoContent,Task11StatusVideoContent
    ,Task12StatusVideoContent,Task13StatusVideoContent,Task14StatusVideoContent,Task15StatusVideoContent
    ,Task16StatusVideoContent,Task17StatusVideoContent,Task18StatusVideoContent,Task19StatusVideoContent
    ,Task20StatusVideoContent,
Task1Statusservicetraining, Task2Statusservicetraining, Task3Statusservicetraining
    ,Task4Statusservicetraining, Task5Statusservicetraining,Task6Statusservicetraining,Task7Statusservicetraining
    ,Task8Statusservicetraining,Task9Statusservicetraining,Task10Statusservicetraining,Task11Statusservicetraining
    ,Task12Statusservicetraining,Task13Statusservicetraining,Task14Statusservicetraining,Task15Statusservicetraining
    ,Task16Statusservicetraining,Task17Statusservicetraining,Task18Statusservicetraining,Task19Statusservicetraining
    ,Task20Statusservicetraining,
Task1Statusparts, Task2Statusparts, Task3Statusparts
    ,Task4Statusparts, Task5Statusparts,Task6Statusparts,Task7Statusparts
    ,Task8Statusparts,Task9Statusparts,Task10Statusparts,Task11Statusparts
    ,Task12Statusparts,Task13Statusparts,Task14Statusparts,Task15Statusparts
    ,Task16Statusparts,Task17Statusparts,Task18Statusparts,Task19Statusparts
    ,Task20Statusparts
)
from django.forms.models import inlineformset_factory
from login.models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )

########################################################################################################################

class Task1_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1StatusProductReadiness
        fields = ('post',)

class Task1_pr_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task1_complete_date',)

class Task2_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2StatusProductReadiness
        fields = ('post',)

class Task2_pr_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task2_complete_date',)

class Task3_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3StatusProductReadiness
        fields = ('post',)

class Task3_pr_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task3_complete_date',)

class Task4_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4StatusProductReadiness
        fields = ('post',)

class Task4_pr_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task4_complete_date',)

class Task5_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5StatusProductReadiness
        fields = ('post',)

class Task5_pr_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task5_complete_date',)

class Task6_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6StatusProductReadiness
        fields = ('post',)

class Task6_pr_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task6_complete_date',)

class Task7_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7StatusProductReadiness
        fields = ('post',)

class Task7_pr_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task7_complete_date',)

class Task8_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8StatusProductReadiness
        fields = ('post',)

class Task8_pr_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task8_complete_date',)

class Task9_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9StatusProductReadiness
        fields = ('post',)

class Task9_pr_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task9_complete_date',)

class Task10_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10StatusProductReadiness
        fields = ('post',)

class Task10_pr_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task10_complete_date',)

class Task11_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11StatusProductReadiness
        fields = ('post',)

class Task11_pr_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task11_complete_date',)

class Task12_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12StatusProductReadiness
        fields = ('post',)

class Task12_pr_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task12_complete_date',)

class Task13_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13StatusProductReadiness
        fields = ('post',)

class Task13_pr_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task13_complete_date',)

class Task14_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14StatusProductReadiness
        fields = ('post',)

class Task14_pr_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task14_complete_date',)

class Task15_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15StatusProductReadiness
        fields = ('post',)

class Task15_pr_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task15_complete_date',)

class Task16_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16StatusProductReadiness
        fields = ('post',)

class Task16_pr_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task16_complete_date',)

class Task17_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17StatusProductReadiness
        fields = ('post',)

class Task17_pr_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task17_complete_date',)

class Task18_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18StatusProductReadiness
        fields = ('post',)

class Task18_pr_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task18_complete_date',)

class Task19_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19StatusProductReadiness
        fields = ('post',)

class Task19_pr_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task19_complete_date',)

class Task20_pr_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20StatusProductReadiness
        fields = ('post',)

class Task20_pr_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = ProductReadiness
        fields = ('Task20_complete_date',)


########################################################################################################################


########################################################################################################################

class Task1_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1StatusVideoContent
        fields = ('post',)

class Task1_vc_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task1_complete_date',)

class Task2_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2StatusVideoContent
        fields = ('post',)

class Task2_vc_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task2_complete_date',)

class Task3_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3StatusVideoContent
        fields = ('post',)

class Task3_vc_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task3_complete_date',)

class Task4_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4StatusVideoContent
        fields = ('post',)

class Task4_vc_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task4_complete_date',)

class Task5_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5StatusVideoContent
        fields = ('post',)

class Task5_vc_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task5_complete_date',)

class Task6_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6StatusVideoContent
        fields = ('post',)

class Task6_vc_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task6_complete_date',)

class Task7_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7StatusVideoContent
        fields = ('post',)

class Task7_vc_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task7_complete_date',)

class Task8_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8StatusVideoContent
        fields = ('post',)

class Task8_vc_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task8_complete_date',)

class Task9_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9StatusVideoContent
        fields = ('post',)

class Task9_vc_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task9_complete_date',)

class Task10_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10StatusVideoContent
        fields = ('post',)

class Task10_vc_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task10_complete_date',)

class Task11_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11StatusVideoContent
        fields = ('post',)

class Task11_vc_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task11_complete_date',)

class Task12_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12StatusVideoContent
        fields = ('post',)

class Task12_vc_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task12_complete_date',)

class Task13_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13StatusVideoContent
        fields = ('post',)

class Task13_vc_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task13_complete_date',)

class Task14_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14StatusVideoContent
        fields = ('post',)

class Task14_vc_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task14_complete_date',)

class Task15_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15StatusVideoContent
        fields = ('post',)

class Task15_vc_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task15_complete_date',)

class Task16_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16StatusVideoContent
        fields = ('post',)

class Task16_vc_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task16_complete_date',)

class Task17_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17StatusVideoContent
        fields = ('post',)

class Task17_vc_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task17_complete_date',)

class Task18_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18StatusVideoContent
        fields = ('post',)

class Task18_vc_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task18_complete_date',)

class Task19_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19StatusVideoContent
        fields = ('post',)

class Task19_vc_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task19_complete_date',)

class Task20_vc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20StatusVideoContent
        fields = ('post',)

class Task20_vc_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = videocontent
        fields = ('Task20_complete_date',)


########################################################################################################################

class Task1_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1StatusDigitalContent
        fields = ('post',)

class Task1_dc_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task1_complete_date',)

class Task2_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2StatusDigitalContent
        fields = ('post',)

class Task2_dc_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task2_complete_date',)

class Task3_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3StatusDigitalContent
        fields = ('post',)

class Task3_dc_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task3_complete_date',)

class Task4_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4StatusDigitalContent
        fields = ('post',)

class Task4_dc_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task4_complete_date',)

class Task5_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5StatusDigitalContent
        fields = ('post',)

class Task5_dc_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task5_complete_date',)

class Task6_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6StatusDigitalContent
        fields = ('post',)

class Task6_dc_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task6_complete_date',)

class Task7_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7StatusDigitalContent
        fields = ('post',)

class Task7_dc_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task7_complete_date',)

class Task8_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8StatusDigitalContent
        fields = ('post',)

class Task8_dc_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task8_complete_date',)

class Task9_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9StatusDigitalContent
        fields = ('post',)

class Task9_dc_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task9_complete_date',)

class Task10_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10StatusDigitalContent
        fields = ('post',)

class Task10_dc_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task10_complete_date',)

class Task11_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11StatusDigitalContent
        fields = ('post',)

class Task11_dc_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task11_complete_date',)

class Task12_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12StatusDigitalContent
        fields = ('post',)

class Task12_dc_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task12_complete_date',)

class Task13_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13StatusDigitalContent
        fields = ('post',)

class Task13_dc_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task13_complete_date',)

class Task14_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14StatusDigitalContent
        fields = ('post',)

class Task14_dc_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task14_complete_date',)

class Task15_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15StatusDigitalContent
        fields = ('post',)

class Task15_dc_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task15_complete_date',)

class Task16_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16StatusDigitalContent
        fields = ('post',)

class Task16_dc_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task16_complete_date',)

class Task17_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17StatusDigitalContent
        fields = ('post',)

class Task17_dc_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task17_complete_date',)

class Task18_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18StatusDigitalContent
        fields = ('post',)

class Task18_dc_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task18_complete_date',)

class Task19_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19StatusDigitalContent
        fields = ('post',)

class Task19_dc_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task19_complete_date',)

class Task20_dc_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20StatusDigitalContent
        fields = ('post',)

class Task20_dc_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = digitalcontent
        fields = ('Task20_complete_date',)

########################################################################################################################

class Task1_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1StatusCallCenterTraining
        fields = ('post',)

class Task1_cct_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task1_complete_date',)

class Task2_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2StatusCallCenterTraining
        fields = ('post',)

class Task2_cct_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task2_complete_date',)

class Task3_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3StatusCallCenterTraining
        fields = ('post',)

class Task3_cct_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task3_complete_date',)

class Task4_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4StatusCallCenterTraining
        fields = ('post',)

class Task4_cct_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task4_complete_date',)

class Task5_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5StatusCallCenterTraining
        fields = ('post',)

class Task5_cct_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task5_complete_date',)

class Task6_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6StatusCallCenterTraining
        fields = ('post',)

class Task6_cct_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task6_complete_date',)

class Task7_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7StatusCallCenterTraining
        fields = ('post',)

class Task7_cct_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task7_complete_date',)

class Task8_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8StatusCallCenterTraining
        fields = ('post',)

class Task8_cct_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task8_complete_date',)

class Task9_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9StatusCallCenterTraining
        fields = ('post',)

class Task9_cct_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task9_complete_date',)

class Task10_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10StatusCallCenterTraining
        fields = ('post',)

class Task10_cct_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task10_complete_date',)

class Task11_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11StatusCallCenterTraining
        fields = ('post',)

class Task11_cct_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task11_complete_date',)

class Task12_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12StatusCallCenterTraining
        fields = ('post',)

class Task12_cct_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task12_complete_date',)

class Task13_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13StatusCallCenterTraining
        fields = ('post',)

class Task13_cct_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task13_complete_date',)

class Task14_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14StatusCallCenterTraining
        fields = ('post',)

class Task14_cct_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task14_complete_date',)

class Task15_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15StatusCallCenterTraining
        fields = ('post',)

class Task15_cct_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task15_complete_date',)

class Task16_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16StatusCallCenterTraining
        fields = ('post',)

class Task16_cct_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task16_complete_date',)

class Task17_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17StatusCallCenterTraining
        fields = ('post',)

class Task17_cct_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task17_complete_date',)

class Task18_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18StatusCallCenterTraining
        fields = ('post',)

class Task18_cct_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task18_complete_date',)

class Task19_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19StatusCallCenterTraining
        fields = ('post',)

class Task19_cct_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task19_complete_date',)

class Task20_cct_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20StatusCallCenterTraining
        fields = ('post',)

class Task20_cct_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcentertraining
        fields = ('Task20_complete_date',)

########################################################################################################################

class Task1_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1Statuscallcenteropertaions
        fields = ('post',)

class Task1_cco_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task1_complete_date',)

class Task2_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2Statuscallcenteropertaions
        fields = ('post',)

class Task2_cco_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task2_complete_date',)

class Task3_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3Statuscallcenteropertaions
        fields = ('post',)

class Task3_cco_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task3_complete_date',)

class Task4_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4Statuscallcenteropertaions
        fields = ('post',)

class Task4_cco_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task4_complete_date',)

class Task5_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5Statuscallcenteropertaions
        fields = ('post',)

class Task5_cco_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task5_complete_date',)

class Task6_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6Statuscallcenteropertaions
        fields = ('post',)

class Task6_cco_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task6_complete_date',)

class Task7_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7Statuscallcenteropertaions
        fields = ('post',)

class Task7_cco_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task7_complete_date',)

class Task8_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8Statuscallcenteropertaions
        fields = ('post',)

class Task8_cco_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task8_complete_date',)

class Task9_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9Statuscallcenteropertaions
        fields = ('post',)

class Task9_cco_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task9_complete_date',)

class Task10_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10Statuscallcenteropertaions
        fields = ('post',)

class Task10_cco_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task10_complete_date',)

class Task11_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11Statuscallcenteropertaions
        fields = ('post',)

class Task11_cco_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task11_complete_date',)

class Task12_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12Statuscallcenteropertaions
        fields = ('post',)

class Task12_cco_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task12_complete_date',)

class Task13_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13Statuscallcenteropertaions
        fields = ('post',)

class Task13_cco_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task13_complete_date',)

class Task14_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14Statuscallcenteropertaions
        fields = ('post',)

class Task14_cco_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task14_complete_date',)

class Task15_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15Statuscallcenteropertaions
        fields = ('post',)

class Task15_cco_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task15_complete_date',)

class Task16_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16Statuscallcenteropertaions
        fields = ('post',)

class Task16_cco_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task16_complete_date',)

class Task17_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17Statuscallcenteropertaions
        fields = ('post',)

class Task17_cco_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task17_complete_date',)

class Task18_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18Statuscallcenteropertaions
        fields = ('post',)

class Task18_cco_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task18_complete_date',)

class Task19_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19Statuscallcenteropertaions
        fields = ('post',)

class Task19_cco_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task19_complete_date',)

class Task20_cco_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20Statuscallcenteropertaions
        fields = ('post',)

class Task20_cco_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = callcenteropertaions
        fields = ('Task20_complete_date',)

########################################################################################################################

class Task1_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1Statusproductsupport
        fields = ('post',)

class Task1_ps_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task1_complete_date',)

class Task2_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2Statusproductsupport
        fields = ('post',)

class Task2_ps_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task2_complete_date',)

class Task3_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3Statusproductsupport
        fields = ('post',)

class Task3_ps_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task3_complete_date',)

class Task4_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4Statusproductsupport
        fields = ('post',)

class Task4_ps_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task4_complete_date',)

class Task5_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5Statusproductsupport
        fields = ('post',)

class Task5_ps_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task5_complete_date',)

class Task6_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6Statusproductsupport
        fields = ('post',)

class Task6_ps_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task6_complete_date',)

class Task7_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7Statusproductsupport
        fields = ('post',)

class Task7_ps_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task7_complete_date',)

class Task8_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8Statusproductsupport
        fields = ('post',)

class Task8_ps_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task8_complete_date',)

class Task9_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9Statusproductsupport
        fields = ('post',)

class Task9_ps_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task9_complete_date',)

class Task10_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10Statusproductsupport
        fields = ('post',)

class Task10_ps_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task10_complete_date',)

class Task11_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11Statusproductsupport
        fields = ('post',)

class Task11_ps_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task11_complete_date',)

class Task12_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12Statusproductsupport
        fields = ('post',)

class Task12_ps_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task12_complete_date',)

class Task13_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13Statusproductsupport
        fields = ('post',)

class Task13_ps_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task13_complete_date',)

class Task14_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14Statusproductsupport
        fields = ('post',)

class Task14_ps_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task14_complete_date',)

class Task15_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15Statusproductsupport
        fields = ('post',)

class Task15_ps_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task15_complete_date',)

class Task16_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16Statusproductsupport
        fields = ('post',)

class Task16_ps_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task16_complete_date',)

class Task17_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17Statusproductsupport
        fields = ('post',)

class Task17_ps_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task17_complete_date',)

class Task18_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18Statusproductsupport
        fields = ('post',)

class Task18_ps_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task18_complete_date',)

class Task19_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19Statusproductsupport
        fields = ('post',)

class Task19_ps_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task19_complete_date',)

class Task20_ps_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20Statusproductsupport
        fields = ('post',)

class Task20_ps_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = productsupport
        fields = ('Task20_complete_date',)

########################################################################################################################

class Task1_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1Statuswarehouse
        fields = ('post',)

class Task1_w_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task1_complete_date',)

class Task2_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2Statuswarehouse
        fields = ('post',)

class Task2_w_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task2_complete_date',)

class Task3_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3Statuswarehouse
        fields = ('post',)

class Task3_w_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task3_complete_date',)

class Task4_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4Statuswarehouse
        fields = ('post',)

class Task4_w_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task4_complete_date',)

class Task5_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5Statuswarehouse
        fields = ('post',)

class Task5_w_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task5_complete_date',)

class Task6_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6Statuswarehouse
        fields = ('post',)

class Task6_w_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task6_complete_date',)

class Task7_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7Statuswarehouse
        fields = ('post',)

class Task7_w_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task7_complete_date',)

class Task8_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8Statuswarehouse
        fields = ('post',)

class Task8_w_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task8_complete_date',)

class Task9_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9Statuswarehouse
        fields = ('post',)

class Task9_w_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task9_complete_date',)

class Task10_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10Statuswarehouse
        fields = ('post',)

class Task10_w_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task10_complete_date',)

class Task11_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11Statuswarehouse
        fields = ('post',)

class Task11_w_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task11_complete_date',)

class Task12_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12Statuswarehouse
        fields = ('post',)

class Task12_w_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task12_complete_date',)

class Task13_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13Statuswarehouse
        fields = ('post',)

class Task13_w_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task13_complete_date',)

class Task14_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14Statuswarehouse
        fields = ('post',)

class Task14_w_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task14_complete_date',)

class Task15_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15Statuswarehouse
        fields = ('post',)

class Task15_w_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task15_complete_date',)

class Task16_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16Statuswarehouse
        fields = ('post',)

class Task16_w_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task16_complete_date',)

class Task17_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17Statuswarehouse
        fields = ('post',)

class Task17_w_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task17_complete_date',)

class Task18_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18Statuswarehouse
        fields = ('post',)

class Task18_w_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task18_complete_date',)

class Task19_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19Statuswarehouse
        fields = ('post',)

class Task19_w_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task19_complete_date',)

class Task20_w_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20Statuswarehouse
        fields = ('post',)

class Task20_w_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = warehouse
        fields = ('Task20_complete_date',)
########################################################################################################################

class Task1_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1Statusfieldservice
        fields = ('post',)

class Task1_fs_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task1_complete_date',)

class Task2_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2Statusfieldservice
        fields = ('post',)

class Task2_fs_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task2_complete_date',)

class Task3_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3Statusfieldservice
        fields = ('post',)

class Task3_fs_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task3_complete_date',)

class Task4_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4Statusfieldservice
        fields = ('post',)

class Task4_fs_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task4_complete_date',)

class Task5_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5Statusfieldservice
        fields = ('post',)

class Task5_fs_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task5_complete_date',)

class Task6_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6Statusfieldservice
        fields = ('post',)

class Task6_fs_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task6_complete_date',)

class Task7_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7Statusfieldservice
        fields = ('post',)

class Task7_fs_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task7_complete_date',)

class Task8_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8Statusfieldservice
        fields = ('post',)

class Task8_fs_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task8_complete_date',)

class Task9_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9Statusfieldservice
        fields = ('post',)

class Task9_fs_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task9_complete_date',)

class Task10_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10Statusfieldservice
        fields = ('post',)

class Task10_fs_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task10_complete_date',)

class Task11_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11Statusfieldservice
        fields = ('post',)

class Task11_fs_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task11_complete_date',)

class Task12_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12Statusfieldservice
        fields = ('post',)

class Task12_fs_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task12_complete_date',)

class Task13_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13Statusfieldservice
        fields = ('post',)

class Task13_fs_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task13_complete_date',)

class Task14_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14Statusfieldservice
        fields = ('post',)

class Task14_fs_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task14_complete_date',)

class Task15_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15Statusfieldservice
        fields = ('post',)

class Task15_fs_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task15_complete_date',)

class Task16_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16Statusfieldservice
        fields = ('post',)

class Task16_fs_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task16_complete_date',)

class Task17_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17Statusfieldservice
        fields = ('post',)

class Task17_fs_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task17_complete_date',)

class Task18_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18Statusfieldservice
        fields = ('post',)

class Task18_fs_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task18_complete_date',)

class Task19_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19Statusfieldservice
        fields = ('post',)

class Task19_fs_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task19_complete_date',)

class Task20_fs_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20Statusfieldservice
        fields = ('post',)

class Task20_fs_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = fieldservice
        fields = ('Task20_complete_date',)

########################################################################################################################

class Task1_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1Statustechsupport
        fields = ('post',)

class Task1_ts_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task1_complete_date',)

class Task2_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2Statustechsupport
        fields = ('post',)

class Task2_ts_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task2_complete_date',)

class Task3_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3Statustechsupport
        fields = ('post',)

class Task3_ts_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task3_complete_date',)

class Task4_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4Statustechsupport
        fields = ('post',)

class Task4_ts_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task4_complete_date',)

class Task5_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5Statustechsupport
        fields = ('post',)

class Task5_ts_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task5_complete_date',)

class Task6_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6Statustechsupport
        fields = ('post',)

class Task6_ts_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task6_complete_date',)

class Task7_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7Statustechsupport
        fields = ('post',)

class Task7_ts_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task7_complete_date',)

class Task8_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8Statustechsupport
        fields = ('post',)

class Task8_ts_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task8_complete_date',)

class Task9_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9Statustechsupport
        fields = ('post',)

class Task9_ts_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task9_complete_date',)

class Task10_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10Statustechsupport
        fields = ('post',)

class Task10_ts_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task10_complete_date',)

class Task11_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11Statustechsupport
        fields = ('post',)

class Task11_ts_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task11_complete_date',)

class Task12_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12Statustechsupport
        fields = ('post',)

class Task12_ts_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task12_complete_date',)

class Task13_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13Statustechsupport
        fields = ('post',)

class Task13_ts_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task13_complete_date',)

class Task14_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14Statustechsupport
        fields = ('post',)

class Task14_ts_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task14_complete_date',)

class Task15_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15Statustechsupport
        fields = ('post',)

class Task15_ts_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task15_complete_date',)

class Task16_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16Statustechsupport
        fields = ('post',)

class Task16_ts_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task16_complete_date',)

class Task17_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17Statustechsupport
        fields = ('post',)

class Task17_ts_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task17_complete_date',)

class Task18_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18Statustechsupport
        fields = ('post',)

class Task18_ts_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task18_complete_date',)

class Task19_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19Statustechsupport
        fields = ('post',)

class Task19_ts_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task19_complete_date',)

class Task20_ts_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20Statustechsupport
        fields = ('post',)

class Task20_ts_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = techsupport
        fields = ('Task20_complete_date',)

########################################################################################################################

class Task1_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1Statusservicemarketing
        fields = ('post',)

class Task1_sm_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task1_complete_date',)

class Task2_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2Statusservicemarketing
        fields = ('post',)

class Task2_sm_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task2_complete_date',)

class Task3_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3Statusservicemarketing
        fields = ('post',)

class Task3_sm_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task3_complete_date',)

class Task4_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4Statusservicemarketing
        fields = ('post',)

class Task4_sm_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task4_complete_date',)

class Task5_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5Statusservicemarketing
        fields = ('post',)

class Task5_sm_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task5_complete_date',)

class Task6_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6Statusservicemarketing
        fields = ('post',)

class Task6_sm_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task6_complete_date',)

class Task7_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7Statusservicemarketing
        fields = ('post',)

class Task7_sm_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task7_complete_date',)

class Task8_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8Statusservicemarketing
        fields = ('post',)

class Task8_sm_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task8_complete_date',)

class Task9_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9Statusservicemarketing
        fields = ('post',)

class Task9_sm_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task9_complete_date',)

class Task10_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10Statusservicemarketing
        fields = ('post',)

class Task10_sm_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task10_complete_date',)

class Task11_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11Statusservicemarketing
        fields = ('post',)

class Task11_sm_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task11_complete_date',)

class Task12_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12Statusservicemarketing
        fields = ('post',)

class Task12_sm_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task12_complete_date',)

class Task13_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13Statusservicemarketing
        fields = ('post',)

class Task13_sm_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task13_complete_date',)

class Task14_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14Statusservicemarketing
        fields = ('post',)

class Task14_sm_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task14_complete_date',)

class Task15_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15Statusservicemarketing
        fields = ('post',)

class Task15_sm_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task15_complete_date',)

class Task16_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16Statusservicemarketing
        fields = ('post',)

class Task16_sm_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task16_complete_date',)

class Task17_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17Statusservicemarketing
        fields = ('post',)

class Task17_sm_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task17_complete_date',)

class Task18_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18Statusservicemarketing
        fields = ('post',)

class Task18_sm_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task18_complete_date',)

class Task19_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19Statusservicemarketing
        fields = ('post',)

class Task19_sm_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task19_complete_date',)

class Task20_sm_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20Statusservicemarketing
        fields = ('post',)

class Task20_sm_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicemarketing
        fields = ('Task20_complete_date',)

########################################################################################################################

class Task1_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1Statusservicetraining
        fields = ('post',)

class Task1_st_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task1_complete_date',)

class Task2_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2Statusservicetraining
        fields = ('post',)

class Task2_st_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task2_complete_date',)

class Task3_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3Statusservicetraining
        fields = ('post',)

class Task3_st_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task3_complete_date',)

class Task4_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4Statusservicetraining
        fields = ('post',)

class Task4_st_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task4_complete_date',)

class Task5_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5Statusservicetraining
        fields = ('post',)

class Task5_st_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task5_complete_date',)

class Task6_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6Statusservicetraining
        fields = ('post',)

class Task6_st_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task6_complete_date',)

class Task7_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7Statusservicetraining
        fields = ('post',)

class Task7_st_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task7_complete_date',)

class Task8_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8Statusservicetraining
        fields = ('post',)

class Task8_st_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task8_complete_date',)

class Task9_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9Statusservicetraining
        fields = ('post',)

class Task9_st_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task9_complete_date',)

class Task10_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10Statusservicetraining
        fields = ('post',)

class Task10_st_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task10_complete_date',)

class Task11_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11Statusservicetraining
        fields = ('post',)

class Task11_st_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task11_complete_date',)

class Task12_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12Statusservicetraining
        fields = ('post',)

class Task12_st_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task12_complete_date',)

class Task13_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13Statusservicetraining
        fields = ('post',)

class Task13_st_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task13_complete_date',)

class Task14_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14Statusservicetraining
        fields = ('post',)

class Task14_st_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task14_complete_date',)

class Task15_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15Statusservicetraining
        fields = ('post',)

class Task15_st_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task15_complete_date',)

class Task16_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16Statusservicetraining
        fields = ('post',)

class Task16_st_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task16_complete_date',)

class Task17_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17Statusservicetraining
        fields = ('post',)

class Task17_st_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task17_complete_date',)

class Task18_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18Statusservicetraining
        fields = ('post',)

class Task18_st_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task18_complete_date',)

class Task19_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19Statusservicetraining
        fields = ('post',)

class Task19_st_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task19_complete_date',)

class Task20_st_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20Statusservicetraining
        fields = ('post',)

class Task20_st_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = servicetraining
        fields = ('Task20_complete_date',)

########################################################################################################################

class Task1_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task1Statusparts
        fields = ('post',)

class Task1_p_date_form(forms.ModelForm):
    Task1_complete_date = forms.DateField(required=False,
                                                            widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task1_complete_date',)

class Task2_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task2Statusparts
        fields = ('post',)

class Task2_p_date_form(forms.ModelForm):
    Task2_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task2_complete_date',)

class Task3_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task3Statusparts
        fields = ('post',)

class Task3_p_date_form(forms.ModelForm):
    Task3_complete_date = forms.DateField(required=False,
                                                         widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task3_complete_date',)

class Task4_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task4Statusparts
        fields = ('post',)

class Task4_p_date_form(forms.ModelForm):
    Task4_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task4_complete_date',)

class Task5_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task5Statusparts
        fields = ('post',)

class Task5_p_date_form(forms.ModelForm):
    Task5_complete_date = forms.DateField(required=False,
                                                                widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task5_complete_date',)

class Task6_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task6Statusparts
        fields = ('post',)

class Task6_p_date_form(forms.ModelForm):
    Task6_complete_date = forms.DateField(required=False,
                                                             widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task6_complete_date',)

class Task7_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task7Statusparts
        fields = ('post',)

class Task7_p_date_form(forms.ModelForm):
    Task7_complete_date = forms.DateField(required=False,
                                                                 widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task7_complete_date',)

class Task8_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task8Statusparts
        fields = ('post',)

class Task8_p_date_form(forms.ModelForm):
    Task8_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task8_complete_date',)

class Task9_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task9Statusparts
        fields = ('post',)

class Task9_p_date_form(forms.ModelForm):
    Task9_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task9_complete_date',)

class Task10_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task10Statusparts
        fields = ('post',)

class Task10_p_date_form(forms.ModelForm):
    Task10_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task10_complete_date',)

class Task11_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task11Statusparts
        fields = ('post',)

class Task11_p_date_form(forms.ModelForm):
    Task11_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task11_complete_date',)

class Task12_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task12Statusparts
        fields = ('post',)

class Task12_p_date_form(forms.ModelForm):
    Task12_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task12_complete_date',)

class Task13_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task13Statusparts
        fields = ('post',)

class Task13_p_date_form(forms.ModelForm):
    Task13_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task13_complete_date',)

class Task14_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task14Statusparts
        fields = ('post',)

class Task14_p_date_form(forms.ModelForm):
    Task14_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task14_complete_date',)

class Task15_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task15Statusparts
        fields = ('post',)

class Task15_p_date_form(forms.ModelForm):
    Task15_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task15_complete_date',)

class Task16_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task16Statusparts
        fields = ('post',)

class Task16_p_date_form(forms.ModelForm):
    Task16_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task16_complete_date',)

class Task17_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task17Statusparts
        fields = ('post',)

class Task17_p_date_form(forms.ModelForm):
    Task17_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task17_complete_date',)

class Task18_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task18Statusparts
        fields = ('post',)

class Task18_p_date_form(forms.ModelForm):
    Task18_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task18_complete_date',)

class Task19_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task19Statusparts
        fields = ('post',)

class Task19_p_date_form(forms.ModelForm):
    Task19_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task19_complete_date',)

class Task20_p_form(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a status...'
        }
    ))

    class Meta:
        model = Task20Statusparts
        fields = ('post',)

class Task20_p_date_form(forms.ModelForm):
    Task20_complete_date = forms.DateField(required=False,
                                                       widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = parts
        fields = ('Task20_complete_date',)
