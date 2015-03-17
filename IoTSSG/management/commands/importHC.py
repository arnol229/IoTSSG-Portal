from optparse import make_option
import urllib2
import csv
from IoTSSG.models import Employee, Department
from IoTSSG.mappings import dep_map
from django.core.exceptions import ObjectDoesNotExist
import logging
import sys
from time import sleep
 
from django.core.management.base import BaseCommand, CommandError
 
class Command(BaseCommand):
    help = 'Runs the next item in the import queue'
    # HRurl = 'https://labtools.cisco.com/general/orgchart.php?tops=kip&format=csv'

    def handle(self, *args, **options):
        ## Delete all current emps
        print "Cleaning Employee Database"
        sleep(10)
        Employee.objects.all().delete()
        print "Done"

        ## download HR Data as CSV
        response = urllib2.urlopen('https://labtools.cisco.com/general/orgchart.php?tops=kip&format=csv')
        cr = csv.reader(response)
        next(cr)
        created_count = 0
        updated_count = 0

        print "Running through CEC HR data"
        for row in cr:
            ## General Information
            userID = row[0]
            firstName = row[2]
            lastName = row[1]
            managerID = row[7]
            ## badge assignment
            if row[4] == "consvend":
                empType = "Contractor"
            elif row[4] == "mgr" or row[4] == "regular":
                empType = "Employee"
            else:
                empType = row[4]
            ## Department Assignment
            if userID in dep_map:
                dep = dep_map[userID]
            mgrchain = row[8].split(':')
            if len(mgrchain) >= 7:
                if mgrchain[6] in dep_map:
                    dep = dep_map[mgrchain[6]]
                else:
                    try:
                        dep = dep_map[mgrchain[5]]
                    except Exception as e:
                        print "couldnt map " + mgrchain[5] + ". " + str(e)
                        dep = 'unknown'
            elif len(mgrchain) == 6:
                try:
                    dep = dep_map[mgrchain[5]]
                except KeyError:
                    dep = 'unknown'

            emp, created = Employee.objects.get_or_create(user_id=userID,defaults={'department':dep})
            if created:
                created_count += 1
            else:
                updated_count += 1
                emp.department = dep
                # emp.last_name = lastName
                # emp.first_name = firstName
                # emp.emptype = empType
                # emp.direct_mgr = managerID
                emp.save()

            sys.stdout.write(str(created_count) + " Employees added to Database\r ")
            sys.stdout.flush()