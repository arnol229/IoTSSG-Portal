from optparse import make_option
import csv
from IoTSSG.models import Allocation, Employee, Project
from IoTSSG.mappings import dep_map
import xml.etree.ElementTree as ET
from django.core.exceptions import ObjectDoesNotExist
import sys
import urllib2
from datetime import datetime
import os
from time import sleep
 
from django.core.management.base import BaseCommand, CommandError
 
class Command(BaseCommand):
    help = 'Imports allocations based on current Employee roster. IMPORTANT: run importHC to update employee roster'
    option_list = BaseCommand.option_list + (
        make_option('--username',
            dest='username',
            default=None,
            help='CEC username'),
        make_option('--password',
            dest='password',
            default=None,
            help='CEC password'),
    )
 
    def handle(self, *args, **options):
        emps = Employee.objects.all()
        unallocatedProject = Project.objects.get(clarity_id='999999')
        empcount = len(emps)
        proj_count = 0 #New projects created
        running_count = 0 #Allocations created
        count=0 #overall progress
        err_count = 0 #number of errors
        error_msgs = [] #contains error messages to display at end of script
        unassigned_count = 0 #employees unassigned to projects
        print "Deleting all Allocations..."
        Allocation.objects.all().delete()
        print"done\nStarting Clarity Extraction..."
        sleep(4)
        
        
        for emp in emps:
            url = 'http://ppm-prod-int:8888/ppmws/api/resources/resourceById/' + emp.user_id
            p = urllib2.HTTPPasswordMgrWithDefaultRealm()
            p.add_password(None, url, 'deryarno', 'SKIUMAHr4h')
            handler = urllib2.HTTPBasicAuthHandler(p)
            opener = urllib2.build_opener(handler)
            urllib2.install_opener(opener)

            xmldata = urllib2.urlopen(url)
            tree = ET.parse(xmldata)
            xmldata.close()


            root = tree.getroot()
            FTE_count = 0.0
            try:
                for month in root[0].find('monthlySums'):
                    if float(month.get('fte')) == 0:
                        Allocation.objects.create(program=unallocatedProject,
                            employee=emp,
                            date=datetime.strptime(month.get('start').split('T')[0],"%Y-%m-%d"),
                            fte_total=0
                            )
                        running_count += 1

                for project in root[0].find('allocations'):
                    for month in project.find('monthlySegments'):
                        if float(month.get('fte')) > 0:
                            proj, created = Project.objects.get_or_create(clarity_id=project.get('investmentId'),defaults={'name':project.get('investmentName')[:-9]})
                            if created:
                                proj_count += 1
                            Allocation.objects.create(program=proj,
                                employee=emp,
                                date=datetime.strptime(month.get('start').split('T')[0],"%Y-%m-%d"),
                                fte_total=float(month.get('fte')))
                            running_count += 1

                            
            except TypeError as e:
                # print """
                # No Projects Found for {0}\n
                # Creating default unallocation for current month.
                # """.format(emp.user_id)
                Allocation.objects.create(program=unallocatedProject,
                            employee=emp,
                            date=datetime.strftime(datetime.today(),"%Y-%m-01"),
                            fte_total=0
                            )
                unassigned_count += 1

            except Exception as e:
                error_msgs.append(""""
                ----------------------\n
                error parsing allocations: {0}: {1}\n
                while attempting to add: {2} - {3}\n
                ----------------------
                """.format(type(e).__name__,str(e),project.get('investmentId'),project.get('investmentName')[:-9]))
                err_count += 1

            ## Update emp info
            try:
                # print "employee name: " + root[0].get('firstName')
                emp.first_name = root[0].get('firstName')
                emp.first_name = root[0].get('lastName')
                emp.emptype = root[0].get('type')
                emp.direct_mgr = root[0].get('managerId')
                # emp.region = root[0].get('Region')
                emp.country = root[0].get('wprCountry')
                emp.state = root[0].get('wprState')
                emp.city = root[0].get('wprCity')
                emp.primary_role = root[0].get('primaryRole')
                emp.role_catagory = root[0].get('roleGroup')
                emp.save()
            except Exception as e:
                error_msgs.append(""""
                ----------------------\n
                error while adding employee information:\n
                emp id: {0}
                message: {1}\n
                ----------------------
                """.format(emp.user_id,str(e)))
                err_count += 1

            count +=1
            os.system('cls')
            print """
            Progress: {0:.0f}%
            Allocations Created: {1}
            Errors: {2}
            Unassigned Employees: {3}
            New Projects Created: {4}
            """.format(
                float(unicode(count))/empcount,
                str(running_count),
                str(err_count),
                str(unassigned_count),
                str(proj_count))
        if error_msgs:
            if raw_input('View error messages? (1 or 0)'):
                for err in error_msgs:
                    print err
                    raw_input('press any enter to continue')
        if proj_count:
            print "New projects have been created. Run importProjects to update"
        print "----Success----"