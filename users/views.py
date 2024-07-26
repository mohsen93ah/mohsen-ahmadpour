from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from django.db.models import Q
from .models import Profile, Message
from .forms import ProfileForm, PublicationForm, HonersAndAwardsForm, ResearchInterestsForm, SkillForm, MessageForm

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    publication = profile.publication_set.all()
    honersandawards = profile.honersandawards_set.all()
    research_interests = profile.researchinterests_set.exclude(description__exact="")
    other_research_interests = profile.researchinterests_set.filter(description="")
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'publication':publication, 
    'honersandawards':honersandawards, 'research_interests':research_interests, 'other_research_interests':other_research_interests,
    'topSkills': topSkills, "otherSkills": otherSkills}
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    publication = profile.publication_set.all()
    honersandawards = profile.honersandawards_set.all()
    research_interests = profile.researchinterests_set.all()
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'publication':publication, 'honersandawards':honersandawards, 'research_interests':research_interests, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def createPublication(request):
    profile = request.user.profile
    form = PublicationForm()

    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.owner = profile
            publication.save()
            messages.success(request, 'Publication was added successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/publication_form.html', context)


@login_required(login_url='login')
def updatePublication(request, pk):
    profile = request.user.profile
    publication = profile.publication_set.get(id=pk)
    form = PublicationForm(instance=publication)

    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publication was updated successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/publication_form.html', context)


@login_required(login_url='login')
def deletePublication(request, pk):
    profile = request.user.profile
    publication = profile.publication_set.get(id=pk)
    if request.method == 'POST':
        publication.delete()
        messages.success(request, 'Publication was deleted successfully!')
        return redirect('account')

    context = {'object': publication}
    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def createHonersAndAwards(request):
    profile = request.user.profile
    form = HonersAndAwardsForm()

    if request.method == 'POST':
        form = HonersAndAwardsForm(request.POST)
        if form.is_valid():
            honersandawards = form.save(commit=False)
            honersandawards.owner = profile
            honersandawards.save()
            messages.success(request, 'Honers and awards was added successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/honers_and_awards_form.html', context)

@login_required(login_url='login')
def updateHonersAndAwards(request, pk):
    profile = request.user.profile
    honersandawards = profile.honersandawards_set.get(id=pk)
    form = HonersAndAwardsForm(instance=honersandawards)

    if request.method == 'POST':
        form = HonersAndAwardsForm(request.POST, instance=honersandawards)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/honers_and_awards_form.html', context)


@login_required(login_url='login')
def deleteHonersAndAwards(request, pk):
    profile = request.user.profile
    honersandawards = profile.honersandawards_set.get(id=pk)
    if request.method == 'POST':
        honersandawards.delete()
        messages.success(request, 'honers and awards was deleted successfully!')
        return redirect('account')

    context = {'object': honersandawards}
    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def createResearchInterests(request):
    profile = request.user.profile
    form = ResearchInterestsForm()

    if request.method == 'POST':
        form = ResearchInterestsForm(request.POST)
        if form.is_valid():
            research_interests = form.save(commit=False)
            research_interests.owner = profile
            research_interests.save()
            messages.success(request, 'Research interests was added successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/research_interests_form.html', context)

@login_required(login_url='login')
def updateResearchInterests(request, pk):
    profile = request.user.profile
    research_interests = profile.researchinterests_set.get(id=pk)
    form = ResearchInterestsForm(instance=research_interests)

    if request.method == 'POST':
        form = ResearchInterestsForm(request.POST, instance=research_interests)
        if form.is_valid():
            form.save()
            messages.success(request, 'Research interests was updated successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/research_interests_form.html', context)


@login_required(login_url='login')
def deleteResearchInterests(request, pk):
    profile = request.user.profile
    research_interests = profile.researchinterests_set.get(id=pk)
    if request.method == 'POST':
        research_interests.delete()
        messages.success(request, 'research_interests was deleted successfully!')
        return redirect('account')

    context = {'object': research_interests}
    return render(request, 'delete_template.html', context)

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)

@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully!')
        return redirect('account')

    context = {'object': skill}
    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request, 'users/inbox.html', context)


@login_required(login_url='login')
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message': message}
    return render(request, 'users/message.html', context)


def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, 'Your message was successfully sent!')
            return redirect('user-profile', pk=recipient.id)

    context = {'recipient': recipient, 'form': form}
    return render(request, 'users/message_form.html', context)
