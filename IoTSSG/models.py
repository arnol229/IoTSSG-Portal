from django.db import models
from choices import HEALTH_CHOICES, PHASE_CHOICES
from datetime import datetime

default_phase = "Unknown"

class Employee(models.Model):
	user_id = models.CharField(max_length=16)
	portrait = models.ImageField(upload_to='images/portraits/',default='images/portraits/default.jpg')
	name = models.CharField(max_length=64,blank=True,null=True)
	last_name = models.CharField(max_length=32,blank=True,null=True)
	first_name = models.CharField(max_length=32,blank=True,null=True)
	emptype = models.CharField(max_length=16)
	job_title = models.CharField(max_length=64,blank=True,null=True)
	direct_mgr = models.CharField(max_length=16)
	region = models.CharField(max_length=64,blank=True,null=True)
	country = models.CharField(max_length=64,blank=True,null=True)
	state = models.CharField(max_length=64,blank=True,null=True)
	city = models.CharField(max_length=64,blank=True,null=True)
	primary_role = models.CharField(max_length=64,blank=True,null=True)
	role_catagory = models.CharField(max_length=64,blank=True,null=True)
	department = models.CharField(max_length=32)

	def __unicode__(self):
		return self.user_id# str(self.last_name) +", " + str(self.first_name)

	def get_current_allocation_summary(self):
		return Allocation.objects.filter(employee=self,date__month=datetime.now().month,date__year=datetime.now().year)

class Project(models.Model):
	# General Required Fields
	name = models.CharField(max_length=32)
	clarity_id = models.CharField(max_length=16,unique=True)
	category = models.CharField(max_length=16,blank=True,null=True)
	description = models.TextField(blank=True,null=True)

	# Dates
	fcs_target = models.DateField(blank=True,null=True)
	fcs_commit = models.DateField(blank=True,null=True)
	fcs_current = models.DateField(blank=True,null=True)
	ec = models.DateField(blank=True,null=True)
	cc = models.DateField(blank=True,null=True)
	created_on = models.DateField(blank=True,null=True)
	# Health status
	health = models.CharField(max_length=16,choices=HEALTH_CHOICES)
	health_schedule = models.CharField(max_length=16,choices=HEALTH_CHOICES,null=True)
	health_resources = models.CharField(max_length=16,choices=HEALTH_CHOICES,null=True)
	health_budget = models.CharField(max_length=16,choices=HEALTH_CHOICES,null=True)
	health_technical = models.CharField(max_length=16,choices=HEALTH_CHOICES,null=True)
	# People
	created_by = models.ForeignKey(Employee,related_name='+',blank=True,null=True,default=None)
	lead = models.ForeignKey(Employee,related_name='+',blank=True,null=True)
	executive_sponsor = models.CharField(max_length=16,blank=True,null=True)
	# Text
	overview = models.CharField(max_length=16,blank=True,null=True)
	technical_description = models.CharField(max_length=16,blank=True,null=True)
	releases = models.CharField(max_length=16,blank=True,null=True)
	comments = models.CharField(max_length=16,blank=True,null=True)
	owner = models.ForeignKey(Employee,related_name='+',blank=True,null=True)
	phase = models.CharField(max_length=16,null=True,blank=True)#include options to choose from

	def __unicode__(self):
		return self.name

	def get_current_allocation_total(self):
		return Allocation.objects.filter(program=self,date__month=datetime.now().month,date__year=datetime.now().year).aggregate(models.Sum('fte_total')).get('fte_total__sum', 0.00)

	def get_allocation_totals(self):
		return Allocation.objects.filter(program=self).values('date').annotate(models.Sum('fte_total')).order_by('date')

	def get_active_roster(self):
		return Allocation.objects.values('date').annotate(models.Sum('fte_total')).get('fte_total__sum', 0.00)

	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Program._meta.fields]

	def open_bug_count(self):
		return Bug.objects.filter(program=self,is_open=True).count()

class Task(models.Model):
	## Generals
	task_id = models.CharField(max_length=16,blank=True,null=True)
	name = models.CharField(max_length=16,blank=True,null=True)
	milestone = models.BooleanField(default=False)
	status = models.CharField(max_length=16,blank=True,null=True)
	percent_complete = models.FloatField()

	## DateFields
	start_date = models.DateField(blank=True,null=True)
	end_date = models.DateField(blank=True,null=True)
	created_date = models.DateField(blank=True,null=True)
	last_updated = models.DateField(blank=True,null=True)
	## Foreign Keys
	project = models.ForeignKey(Project,unique=False)
	last_updated_by = models.CharField(max_length=16,blank=True,null=True)

class Allocation(models.Model):
	program = models.ForeignKey(Project,unique=False)
	employee = models.ForeignKey(Employee,unique=False)
	date = models.DateField()
	fte_total = models.FloatField()

class Bug(models.Model):
	program = models.ForeignKey(Project,unique=False)
	bug_id = models.CharField(max_length=64, db_index=True)
	manager_id = models.CharField(max_length=16, db_index=True)
	entry_date = models.DateTimeField(auto_now=False)
	age = models.IntegerField()
	status = models.CharField(max_length=8)
	severity = models.IntegerField()
	product = models.CharField(max_length=36)
	is_open = models.BooleanField(default=False)
	month_start = models.BooleanField(default=False)

	def to_json(self):
		return {
		'bug_id':self.bug_id,
		'manager_id':self.manager_id,
		'entry_date':self.entry_date.isoformat(),
		'age':self.age,
		'status':self.status,
		'severity':self.severity,
		'product':self.product,
		'is_open':self.is_open,
		'month_start':self.month_start
		}

class Meeting(models.Model):
	meeting_date = models.DateField()
	topic = models.CharField(max_length=32)
	participants = models.ManyToManyField(Employee)
	meeting_file = models.FileField(upload_to='MeetingFiles')#multiple files per meeting?
	def __unicode__(self):
		return self.topic

class Minute(models.Model):
	topic = models.CharField(max_length=32)
	meeting = models.ForeignKey(Meeting)
	program = models.ForeignKey(Project)
	summary = models.CharField(max_length=256)
	notes = models.CharField(max_length=256)

class Department(models.Model):
	name = models.CharField(max_length=255)
	director = models.ForeignKey(Employee,related_name='+')
	description = models.CharField(max_length=255)