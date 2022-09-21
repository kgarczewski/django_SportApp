from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .forms import CreateUserForm, CommentForm, EventAttendanceForm, CreateEvent
from .models import UserProfile, Post, Event, Comment, EventAttendance, Message, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import random


class Home(View):
    def get(self, request):
        posts = list(Post.objects.all())
        events = list(Event.objects.all())
        user = UserProfile.objects.get(user=request.user)
        message = Message.objects.filter(receiver=request.user).count()
        random.shuffle(posts)

        return render(request, "home.html", {'posts': posts, 'events': events, 'user': user, 'message':message})


class Home2(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('home')
        return render(request, "home2.html")


class Register(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'signup.html', context={'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            messages.success(request, 'Konto zostalo utworzone! Mozesz sie zalogowac!')
            return redirect('login')

        return render(request, 'signup.html', {'form': form})


class Login(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Haslo albo nazwa uzytkownika jest nieprawidlowe')
            return render(request, 'login.html')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home2')


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'update_profile.html'
    fields = ['bio', 'age', 'city', 'gender', 'level', 'favourite_sports']
    success_url = '/home'


class DeleteProfile(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'account_delete.html'
    success_url = '/'


# class ProfilePage(LoginRequiredMixin, DetailView):
#     """ Displays user's details. """
#     model = UserProfile
#     template_name = 'user_profile.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ProfilePage, self).get_context_data(*args, **kwargs)
#         page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
#         context['page_user'] = page_user
#         return context

class ProfilePage(LoginRequiredMixin, View):
    """
    Displays user profile with details information.
    """
    login_url = '/login/'

    def get(self, request):
        message = Message.objects.filter(receiver=request.user).count()
        page_user = UserProfile.objects.get(user = request.user.id)
        return render(request, 'user_profile.html', {'message':message, 'page_user':page_user})

class PostsPage(LoginRequiredMixin, ListView):
    """ Shows all active posts """
    model = Post
    template_name = 'posts_view.html'
    context_object_name = 'posts'


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'postdetail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        user = UserProfile.objects.get(user=self.request.user)
        context['post'] = post
        context['user'] = user

        return context


class AddPost(LoginRequiredMixin, CreateView):
    """ Renders form which enables user to create post."""
    model = Post
    template_name = 'addpost.html'
    fields = ('title', 'sport', 'accepted_levels', 'content')
    success_url = '/posts'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, UpdateView):
    """Enables users to edit their own post"""
    model = Post
    template_name = 'edit_post.html'
    fields = ('title', 'content', 'sport', 'accepted_levels')
    success_url = '/posts'


class DeletePost(LoginRequiredMixin, DeleteView):
    """Enables users to delete their own post"""
    model = Post
    template_name = 'delete_post.html'
    success_url = '/posts'


class AddEvent(LoginRequiredMixin, CreateView):
    """ Renders form which enables user to create event"""
    model = Event
    template_name = 'add_event.html'
    form_class = CreateEvent
    success_url = '/events'

    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.cleaned_data.get('start') > form.cleaned_data.get('end'):
            form.add_error('start', 'Wprowadz poprawna date!')
            return self.form_invalid(form)
        return super().form_valid(form)




class EditEvent(LoginRequiredMixin, UpdateView):
    """Enables users to edit their own even"""
    model = Event
    template_name = 'edit_event.html'
    fields = ('title', 'number_of_players', 'location', 'start', 'end', 'price', 'content', 'sport')
    success_url = '/events'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventPage(LoginRequiredMixin, ListView):
    """Renders page with active events"""
    model = Event
    template_name = 'events_page.html'
    context_object_name = 'events'


class DeleteEvent(LoginRequiredMixin, DeleteView):
    """Enables users to delete their own event"""
    model = Event
    template_name = 'delete_event.html'
    success_url = '/events'


class EventDetail(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'event_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EventDetail, self).get_context_data(*args, **kwargs)
        event = get_object_or_404(Event, id=self.kwargs['pk'])
        user = UserProfile.objects.get(user=self.request.user)
        context['user'] = user
        context['events'] = event
        values = EventAttendance.objects.filter(person=self.request.user, event=event).exists()
        context['values'] = values
        return context


class AddEventAttendance(LoginRequiredMixin, CreateView):
    model = EventAttendance
    form_class = EventAttendanceForm
    template_name = 'add_atendance.html'
    success_url = '/events'

    def form_valid(self, form):
        form.instance.person = self.request.user
        form.instance.event_id = self.kwargs['pk']
        return super().form_valid(form)


class EditAttendance(LoginRequiredMixin, DeleteView):
    model = EventAttendance
    template_name = 'edit_attendance.html'
    fields = ['attended']
    success_url = '/events'


class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = '/events'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.event_id = self.kwargs['pk']
        return super().form_valid(form)


class EditComment(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'edit_comment.html'
    fields = ['content']
    success_url = '/events'


class DeleteComment(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = '/events'


class CreateMessage(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['subject', 'content']
    template_name = 'message.html'
    success_url = '/inbox'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.receiver_id = self.kwargs['id']
        return super().form_valid(form)


class DeleteMessage(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'delete_message.html'
    success_url = '/inbox'


class InboxView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        messages_in = Message.objects.filter(receiver=user).order_by('date_sent')
        messages_out = Message.objects.filter(sender=user).order_by('date_sent')
        return render(request, 'inbox.html', {'messages_in': messages_in, 'messages_out': messages_out})


class CreateGroup(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name', 'description']
    template_name = 'group.html'
    success_url = '/groups'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class JoinGroup(LoginRequiredMixin, View):
    def post(self, request, id):
        group = get_object_or_404(Group, id=id)
        group.members.add(request.user)
        group.save()
        return redirect('/home')

    def get(self, request, id):
        group = get_object_or_404(Group, id=id)
        group.members.add(request.user)
        group.save()
        return render(request, 'group_detail.html', {'group': group})


class LeaveGroup(LoginRequiredMixin, View):
    def post(self, request, id):
        group = get_object_or_404(Group, id=id)
        group.members.remove(request.user)
        group.save()
        return redirect('/home')

    def get(self, request, id):
        group = get_object_or_404(Group, id=id)
        group.members.remove(request.user)
        group.save()
        return render(request, 'group_detail.html', {'group': group})


class GroupDetail(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'group_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GroupDetail, self).get_context_data(*args, **kwargs)
        group = get_object_or_404(Group, id=self.kwargs['pk'])
        context['group'] = group

        return context


class GroupsPage(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups_view.html'
    context_object_name = 'groups'
    queryset = Group.objects.prefetch_related('members')


class DeleteGroup(DeleteView):
    model = Group
    template_name = 'delete_group.html'
    success_url = '/groups'


class EditGroup(UpdateView):
    model = Group
    template_name = 'edit_group.html'
    fields = ['name', 'description']
    success_url = '/groups'
