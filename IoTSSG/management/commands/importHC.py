from optparse import make_option
import csv
from IoTSSG.models import Employee, Department
from IoTSSG.mappings import dep_map
from django.core.exceptions import ObjectDoesNotExist
import logging
 
from django.core.management.base import BaseCommand, CommandError
 
class Command(BaseCommand):
    help = 'Runs the next item in the import queue'
    option_list = BaseCommand.option_list + (
        make_option('--path',
            dest='path',
            default=None,
            help='File to Ingest'),
    )
 
    def handle(self, *args, **options):
        def map_keys(keys, data):
            d={}
            for i in range(0, len(data)):
                d[keys[i]] = data[i]
            return d

        def populate_dept():
            depts = {}
            departments = Department.objects.all()
            for department in departments:
                depts[department.director] = department
            return depts

# Extract filepath from command to dir that houses both csv's
        filepath = options['path']
        if filepath is None:
            raise CommandError('No file path passed (pass --path=***)')
        HR = filepath + "HR.csv"
        Vlite = filepath + "vliteHC.csv"

#1st CSV: HR data
        try:
            with open(HR, 'rb') as csvfile:
                reader = csv.reader(csvfile)
#get keys, the first row of the csv file
                keys = reader.next()
#instantiate list to store new employee objects
                new_HR_emps = []
                for entry in reader:
#for each line, create dict reference to extract data
                    HR_mappings = map_keys(keys,entry)
                    try:
#Try to find employee first. add first and last name if not already there
                        emp = Employee.objects.get(user_id=HR_mappings['uid'])
                        if not emp.first_name or not emp.last_name:
                            emp.first_name = HR_mappings['firstname']
                            emp.last_name = HR_mappings['lastname']
                            emp.save()
# print emp.email_id + " already exists."
                        pass
#If employee is not found,
#Create a blank object with email address for vlite CSV to fill in
                    except Employee.DoesNotExist:
                        new_HR_emps.append(Employee(
                            user_id=HR_mappings['uid'],
                            ))
                logging.error("# of employees added from HR: " + str(len(new_HR_emps)))
                Employee.objects.bulk_create(new_HR_emps)

        except Exception as e:
            raise CommandError("error processing HR csv file: " + str(e))

#2nd CSV: Vlite Data
        try:
            department_map = populate_dept()
            with open(Vlite, 'rb') as csvfile:
                reader = csv.DictReader(csvfile,delimiter=',',quotechar='"')
                #keys = reader.next()
                new_Vlite_emps = []
                logging.error('ready to read csv')

                for entry in reader:
#Try to find the employee if it already exists
                    try:
                        emp = Employee.objects.get(user_id=entry['Resource ID'])
#Add/update info from Vlite
                        emp.name = entry.get('Resource Name', None)
                        emp.emptype = entry.get('Employment Type',None)
                        emp.job_title = entry.get('Job Title',None)
                        emp.direct_mgr = entry.get('Direct Manager')
                        emp.region = entry.get('Region',None)
                        emp.country = entry.get('Country',None)
                        emp.state = entry.get('State',None)
                        emp.city = entry.get('City',None)
                        emp.primary_role = entry.get('Primary Role',None)
                        emp.role_catagory = entry.get('Role Group',None)
                        try:
                            if entry['Manager Tier 5'] == "bapgar":
                                emp.department = department_map.get("bapgar", None)
                            else:
                                emp.department = department_map.get('Manager Tier 6',None)
                        except Exception as e:
                            logging.error("couldn't assign dept: " + str(e))
                        emp.save()

#Create a new Vlite employee if not in HR chart
#This person is likely outside IoTSSG
#Should add attr to indicate inside HR or outside
                    except Employee.DoesNotExist:
                        new_Vlite_emps.append(Employee(
                            user_id = entry['Resource ID'],
                            name = entry['Resource Name'],
                            emptype = entry['Employment Type'],
                            job_title = entry['Job Title'],
                            direct_mgr = entry['Direct Manager'],
                            region = entry['Region'],
                            country = entry['Country'],
                            state = entry['State'],
                            city = entry['City'],
                            primary_role = entry['Primary Role'],
                            role_catagory = entry['Role Group'],
                            department = get_dept(entry['Manager Tier 6'])
                            ))
#print "added " + mappings['Resource ID']

                Employee.objects.bulk_create(new_Vlite_emps)
        except Exception as e:
            raise CommandError("error processing Vlite csv file: " + str(e))