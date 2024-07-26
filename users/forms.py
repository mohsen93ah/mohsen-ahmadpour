from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Publication, HonersAndAwards, ResearchInterests,Skill, Message


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'email', 'username',
                  'location', 'bio', 'short_intro', 'profile_image',
                  'social_github', 'social_linkedin',
                  'social_youtube']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(PublicationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class HonersAndAwardsForm(ModelForm):
    class Meta:
        model = HonersAndAwards
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(HonersAndAwardsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ResearchInterestsForm(ModelForm):
    class Meta:
        model = ResearchInterests
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(ResearchInterestsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
