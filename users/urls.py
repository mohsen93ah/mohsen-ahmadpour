from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('account/', views.userAccount, name="account"),

    path('edit-account/', views.editAccount, name="edit-account"),

    path('create-publication/', views.createPublication, name="create-publication"),
    path('update-publication/<str:pk>/', views.updatePublication, name="update-publication"),
    path('delete-publication/<str:pk>/', views.deletePublication, name="delete-publication"),

    path('create-honersandawards/', views.createHonersAndAwards, name="create-honersandawards"),
    path('update-honersandawards/<str:pk>/', views.updateHonersAndAwards, name="update-honersandawards"),
    path('delete-honersandawards/<str:pk>/', views.deleteHonersAndAwards, name="delete-honersandawards"),

    path('create-research-interests/', views.createResearchInterests, name="create-research-interests"),
    path('update-research-interests/<str:pk>/', views.updateResearchInterests, name="update-research-interests"),
    path('delete-research-interests/<str:pk>/', views.deleteResearchInterests, name="delete-research-interests"),

    path('create-skill/', views.createSkill, name="create-skill"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),

    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),
]
