from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib import messages

from users.models import User

# Create your views here.
def home_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request, "home.html", {})

def profile_info(request, *args, **kwargs):
	new_username = args[0]
	request.session['username'] = new_username
	all_labels = User.objects.filter(username = new_username)
	length = len(all_labels)
	context = {"new_username" : new_username,
				"all_labels": all_labels,
				"length": length}
	return render(request, "detail.html", context)


def login_page(request):
	if request.method == "POST":
		new_username = request.POST.get('username')
		# check whether new username is empty string
		if new_username.isspace():
			messages.error(request, 'You cannot set your label as empty string')
			return render(request, "home.html", {})
		return profile_info(request, new_username)
	context = {}
	return render(request, "home.html", context)


def add_function(request):
	new_username = request.session.get('username')
	if request.method == "POST":
		new_label = request.POST.get('labelname')
		# check whether new label is empty string
		if new_label.isspace():
			messages.error(request, 'You cannot set your label as empty string')
			return profile_info(request, new_username)
		# check duplicate label name
		all_labels = User.objects.filter(labels = new_label)
		length = len(all_labels)
		if length != 0:
			messages.error(request, 'You cannot set a duplicate label name')
			return profile_info(request, new_username)
		new_object = User.objects.create(username = new_username, labels = new_label)
		return profile_info(request, new_username)
	context = {}
	return render(request, "add.html", context)
	
def delete_function(request):
	new_username = request.session.get('username')
	all_labels = User.objects.filter(username = new_username)
	length = len(all_labels)
	context = {"all_labels": all_labels, "length": length}
	if request.method == "POST":
		new_radio = request.POST.get('selected')
		User.objects.filter(labels = new_radio).delete()
		return profile_info(request, new_username)
	return render(request, "delete.html", context)


def rename_function(request):
	# combination of delete && add
	new_username = request.session.get('username')
	all_labels = User.objects.filter(username = new_username)
	length = len(all_labels)
	context = {"all_labels": all_labels, "length": length}
	if request.method == "POST":
		new_radio = request.POST.get('selected')
		new_label = request.POST.get('labelname')
		if new_label.isspace():
			messages.error(request, 'You cannot choose your new label name as empty string')
			return profile_info(request, new_username)
		all_labels = User.objects.filter(labels = new_label)
		length = len(all_labels)
		if length != 0:
			messages.error(request, 'You cannot rename a label with the same name as the one you already have')
			return profile_info(request, new_username)
		User.objects.filter(labels = new_radio).delete()
		new_object = User.objects.create(username = new_username, labels = new_label)
		return profile_info(request, new_username)
	return render(request, "rename.html", context)