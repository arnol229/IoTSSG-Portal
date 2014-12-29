from django.db import models
from choices import HEALTH_CHOICES, PHASE_CHOICES

default_phase = "Unknown"

class Employee(models.Model):
	user_id = models.CharField(max_length=16)
	name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	first_name = models.CharField(max_length=32)

	emptype = models.CharField(max_length=16)
	job_title = models.CharField(max_length=64)
	direct_mgr = models.CharField(max_length=16)
	region = models.CharField(max_length=64)
	country = models.CharField(max_length=64)
	state = models.CharField(max_length=64)
	city = models.CharField(max_length=64)
	primary_role = models.CharField(max_length=64)
	role_catagory = models.CharField(max_length=64)
	department = models.CharField(max_length=16)

	def __unicode__(self):
		return str(self.last_name) +", " + str(self.first_name)

class Program(models.Model):
	# Required Fields
	name = models.CharField(max_length=32,unique=True)
	clarity_id = models.CharField(max_length=16,unique=True)
	
	category = models.CharField(max_length=16,blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	# Date Fields 
	fcs_commit = models.DateField(blank=True,null=True)
	fcs_current = models.DateField(blank=True,null=True)
	ec = models.DateField(blank=True,null=True)
	cc = models.DateField(blank=True,null=True)
	created_on = models.DateField(blank=True,null=True)

	health = models.CharField(max_length=16,choices=HEALTH_CHOICES)
	created_by = models.CharField(max_length=16,editable=False)
	
	lead = models.ForeignKey(Employee,related_name='+',blank=True,null=True)
	executive_sponsor = models.CharField(max_length=16,blank=True,null=True)
	overview = models.CharField(max_length=16,blank=True,null=True)
	technical_description = models.CharField(max_length=16,blank=True,null=True)
	releases = models.CharField(max_length=16,blank=True,null=True)
	comments = models.CharField(max_length=16,blank=True,null=True)
	owner = models.ForeignKey(Employee,related_name='+',blank=True,null=True)
	phase = models.CharField(max_length=16,default="UNDEFINED",choices=PHASE_CHOICES)#include options to choose from

	class Meta:
		verbose_name_plural = "Programs"
	def __unicode__(self):
		return self.name

	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Program._meta.fields]

	def bug_count(self):
		return Bug.objects.all().count()

class Allocation(models.Model):
	program = models.ForeignKey(Program)
	employee = models.ForeignKey(Employee)
	fiscal_month = models.DateField()
	fte_total = models.PositiveIntegerField()
	# to archive allocation points #
	generated_date = models.DateField()

class Bug(models.Model):
	program = models.ForeignKey(Program)
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
	program = models.ForeignKey(Program)
	summary = models.CharField(max_length=256)
	notes = models.CharField(max_length=256)

class Department(models.Model):
	name = models.CharField(max_length=255)
	director = models.ForeignKey(Employee,related_name='+')
	description = models.CharField(max_length=255)