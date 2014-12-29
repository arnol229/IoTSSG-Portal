from optparse import make_option
import csv
from IoTSSG.models import Allocation
from IoTSSG.mappings import dep_map
from django.core.exceptions import ObjectDoesNotExist
 
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
            print d
            return d
        def is_open(data):
            if data == 'FALSE':
                return 0
            else:
                return 1
        def get_dept(manager):
            if manager:
                for mgr, dep in dep_map.iteritems():
                    if manager == mgr:
                        return dep
            return "Unknown"

        filepath = options['path']
        if filepath is None:
            raise CommandError('No file path passed (pass --path=***)')
        HR = filepath + "HR.csv"
        Vlite = filepath + "vliteHC.csv"
        # print "HR csv path: " + HR
        # print "Vlite csv path: " + Vlite

        try:
            with open(HR, 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                keys = reader.next()
                new_HR_emps = []

                # print keys
                for entry in reader:
                    HR_mappings = map_keys(keys,entry)
                    ## Try to find employee first. add first and last name if found
                    try:
                        emp = Employee.objects.get(email_id=HR_mappings['uid'])
                        if not emp.first_name or not emp.last_name:
                            emp.first_name = HR_mappings['firstname']
                            emp.last_name = HR_mappings['lastname']
                            emp.save()
                        # print emp.email_id + " already exists."
                        pass
                    ## Create a blank object with email address for vlite to fill in
                    except Employee.DoesNotExist:
                        new_HR_emps.append(Employee(
                            email_id=HR_mappings['uid'],
                            ))
                Employee.objects.bulk_create(new_HR_emps)

        except Exception as e:
            raise CommandError("error processing HR csv file: " + str(e))

        try:
            with open(Vlite, 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                keys = reader.next()
                new_Vlite_emps = []

                for entry in reader:
                    mappings = map_keys(keys,entry)
                    try:
                        emp = Employee.objects.get(email_id=mappings['Resource ID'])
                        emp.name = list(mappings['Resource Name']),
                        emp.emptype = mappings['Employment Type'],
                        emp.job_title = mappings['Job Title'],
                        emp.direct_mgr = mappings['Direct Manager'],
                        emp.region = mappings['Region'],
                        emp.country = mappings['Country'],
                        emp.state = mappings['State'],
                        emp.city = mappings['City'],
                        emp.primary_role = mappings['Primary Role'],
                        emp.role_catagory = mappings['Role Group'],
                        emp.department = get_dept(mappings['Manager Tier 6'])
                        emp.save(update_fields=['name','emptype','job_title'])
                        print emp.name
                    except Employee.DoesNotExist:
                        new_Vlite_emps.append(Employee(
                            email_id = mappings['Resource ID'],
                            name = mappings['Resource Name'],
                            emptype = mappings['Employment Type'],
                            job_title = mappings['Job Title'],
                            direct_mgr = mappings['Direct Manager'],
                            region = mappings['Region'],
                            country = mappings['Country'],
                            state = mappings['State'],
                            city = mappings['City'],
                            primary_role = mappings['Primary Role'],
                            role_catagory = mappings['Role Group'],
                            department = get_dept(mappings['Manager Tier 6'])
                            ))
                        # print "added " + mappings['Resource ID']

                Employee.objects.bulk_create(new_Vlite_emps)
        except Exception as e:
            raise CommandError("error processing Vlite csv file: " + str(e))