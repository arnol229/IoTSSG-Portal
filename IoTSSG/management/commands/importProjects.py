from optparse import make_option
import csv
from IoTSSG.models import Allocation, Employee, Project, Task
from IoTSSG.mappings import dep_map
import xml.etree.ElementTree as ET
from django.core.exceptions import ObjectDoesNotExist
import sys
import urllib2
from datetime import datetime
import os
 
from django.core.management.base import BaseCommand, CommandError
 

class Command(BaseCommand):
    help = 'Imports/Refreshes current project data'
 
    def handle(self, *args, **options):
        ## all but the manually created unallocated project
        projects = Project.objects.all().exclude(clarity_id='999999')
        ## feedback info
        task_created_count = 0
        project_count = len(projects)
        update_progress = 0
        error_count = 0

        def update_feedback():
            os.system('cls')
            print """
            Progress: {0:.0f}%
            Tasks Created: {1}
            Errors: {2}
            """.format(
                float(update_progress)/project_count*100,
                str(task_created_count),
                str(error_count)
                )

        update_feedback()

        for project in projects:
            ## set up url params
            url = 'http://ppm-prod-int:8888/ppmws/api/projects/projectById/' + project.clarity_id
            p = urllib2.HTTPPasswordMgrWithDefaultRealm()
            p.add_password(None, url, 'deryarno', 'SKIUMAHr4h')
            handler = urllib2.HTTPBasicAuthHandler(p)
            opener = urllib2.build_opener(handler)
            urllib2.install_opener(opener)
            # XML prep
            xmldata = urllib2.urlopen(url)
            tree = ET.parse(xmldata)
            xmldata.close()
            root = tree.getroot()

            try:
                #Get project data
                project.end_date = root[0].get('endDate',None)
                project.start_date = root[0].get('startDate',None)
                project.active = root[0].get('active',None)
                project.last_updated_by = root[0].get('lastUpdatedBy',None)
                ## Project lead may be a problem if doesnt exist.
                # project.project_lead, created = Employee.objects.get_or_create(user_id=root[0].get('projectLeadID'))
                # project.created_by = root[0].get('createdBy')
                project.last_updated_date = root[0].get('lastUpdatedDate',None)
                project.description = root[0].findtext('description')
                project.objective = root[0].findtext('objective')
                project.progress = root[0].findtext('progress')
                project.phase = root[0].findtext('phase')
                project.status = root[0].findtext('status')
                project.goal = root[0].findtext('goal')
                project.health = root[0].findtext('projectHealth')
                project.methodology = root[0].findtext('methodology')
                project.status = root[0].findtext('status')
                ## poorly done. how to incorporate multiple families?
                # platformFamilies = ''
                # for family in root[0].find('platformFamilies'):
                    # platformFamilies += family.text
                # project.platform_family = platformFamilies
                ## ew.

                project.save()
                update_progress += 1
                update_feedback()
                ## Project Tasks
                for task in root[0].find('tasks'):
                    # print task.get('investmentID')
                    task, created = Task.objects.get_or_create(task_id=task.get('internalId'),
                        defaults={
                        'name':task.get('name'),
                        'percent_complete':float(task.get('percentComplete')),
                        'project':project,
                        'milestone':task.get('milestone'),#boolean
                        'status':task.get('status'),
                        'start_date':task.get('startDate').split('T')[0],#datetime
                        'end_date':task.get('endDate').split('T')[0],#datetime
                        'created_date':task.get('createdDate').split('T')[0],#datetime
                        'last_updated_by':task.get('lastUpdatedBy').split('T')[0],
                        'last_updated':task.get('lastUpdated').split('T')[0]#datetime
                        })
                    if created:
                        task_created_count += 1
                        update_feedback()

            except Exception as e:
                error_count += 1
                print str(e)
                # update_feedback()