from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core import serializers
from datetime import datetime
import logging
from models import Program, Employee
import json
from forms import ProgramForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def landing(request):
	logging.error('landing page processing')
	if request.METHOD =="POST":
		logging.error('its a post')
		username = request.POST['username']
		password = request.POST['password']
		logging.error('authenticating user...')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				context = {'message':'successful login!'}
				return render(request, 'home.html', context)
			else:
				raise Http404
		else:
			raise Http404

	return render(request, 'landing.html', {})

@login_required(login_url='login/')
def home(request):
	logging.error('processing home...')
	current_date = datetime.now().strftime('%m/%d/%y')
	current_time = datetime.now().strftime('%I:%M')
	user_stuff = {}
	context = {'message':'Welcome to the IoTSSG home page.',
				'current_time':current_time,
				'current_date':current_date,
				'username':request.user.username,}
	return render(request, 'home.html', context)

@login_required(login_url='login/')
def program_list(request):
	def pkg_autocomplete(prog_list):
		search_list = []
		for program in prog_list:
			search_list.append(str(program))
		return search_list
	logging.error('getting program list')
	program_stage = request.GET.get('program_stage', None)
	programs = Program.objects.all()

	if request.method == 'POST':
		form = ProgramForm(request.POST)
		if form.is_valid():
			form.cleaned_data['Created by'] = "User"
			new_program = form.save()
			logging.error('valid')
			attempt = "success"
			form = ProgramForm()
			context = {"programs": programs,
				"search_list":pkg_autocomplete(programs),
				"form":form,
				"attempt":attempt}

			return render(request,"program_list.html", context)
		else:
			logging.error('invalid')
			attempt = 'error'
			context = {"programs": programs,
				"search_list":pkg_autocomplete(programs),
				"form":form,
				"attempt":attempt}
			return render(request,"program_list.html", context)

	if program_stage:
		programs = programs.Filter(program_stage__in = program_stage)

	form = ProgramForm()
	context = {"programs": programs,
				"search_list":pkg_autocomplete(programs),
				"form":form,}

	return render(request,"program_list.html", context)

@login_required(login_url='login/')
def retrieve_programs(request):
	logging.error('processing retrieve_program...')
	if request.method == "GET":
		programs = Program.objects.all()

		if request.GET.has_key('program_name_search'):
			programs = Program.objects.filter(phase__in = str(request.GET['program_name_search']))
			response = {}
			for obj in programs:
				logging.error(obj.name)
				response.append(obj.name)
			HttpResponse(response)
		if request.GET.has_key('program_phase'):
			programs = Program.objects.filter(phase__in = str(request.GET['program_phase']))
			logging.error("filtering for phase: " + str(request.GET['program_phase']))

		response = serializers.serialize("json", programs)
		return HttpResponse(response, content_type='application/json')
	else:
		raise Http404

@login_required(login_url='login/')
def program(request, program_name):
	logging.error('processing program...')
	try:
		program = Program.objects.get(name=program_name)
		programs = Program.objects.all()
		context = {'program':program,
					'programs':programs}
		return render(request, 'program.html', context)
	except Exception as e:
		logging.error(str(e))
		raise Http404

@login_required(login_url='login/')
def community(request):
	return render(request, 'community.html', {'message':'Community page.'})

@login_required(login_url='login/')
def roster(request):
	return render(request, 'roster.html', {'employees':Employee.objects.all()})

@login_required(login_url='login/')
def meeting(request):
	context ={}
	return render(request, 'meeting.html', context)

def the_gate(request):
	logging.error('login page processing')
	if request.method =="POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			form_data = form.cleaned_data
			logging.error('authenticating user...')
			# CEC AD API CALL HERE!!!
			user = authenticate(username=form_data['username'], password=form_data['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					logging.error('user successfully logged in!')
					context = {'message':'successful login!'}
					return HttpResponseRedirect('/')
				else:
					raise Http404
		else:
			context = {"form":LoginForm()}
			return render(request, 'login.html', context)
	context = {"form":LoginForm()}
	return render(request, 'login.html', context)

def analytics(request):
	context = {}
	return render(request, 'analytics.html', context)

def about(request):
	context = {}
	return render(request, 'about.html', context)

# def upload_file(request):
# 	def handle_upload(f):
# 		with open('some/text/file.doc')

#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render_to_response('upload.html', {'form': form})