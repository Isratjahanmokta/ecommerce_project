from django.forms import ModelForm
from authentication.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
