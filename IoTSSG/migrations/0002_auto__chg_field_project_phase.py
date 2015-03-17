# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.phase'
        db.alter_column(u'IoTSSG_project', 'phase', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

    def backwards(self, orm):

        # Changing field 'Project.phase'
        db.alter_column(u'IoTSSG_project', 'phase', self.gf('django.db.models.fields.CharField')(max_length=16))

    models = {
        u'IoTSSG.allocation': {
            'Meta': {'object_name': 'Allocation'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IoTSSG.Employee']"}),
            'fte_total': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IoTSSG.Project']"})
        },
        u'IoTSSG.bug': {
            'Meta': {'object_name': 'Bug'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'bug_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_open': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manager_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'}),
            'month_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IoTSSG.Project']"}),
            'severity': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        u'IoTSSG.department': {
            'Meta': {'object_name': 'Department'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'director': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['IoTSSG.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'IoTSSG.employee': {
            'Meta': {'object_name': 'Employee'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'direct_mgr': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'emptype': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'portrait': ('django.db.models.fields.files.ImageField', [], {'default': "'images/portraits/default.jpg'", 'max_length': '100'}),
            'primary_role': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'role_catagory': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'IoTSSG.meeting': {
            'Meta': {'object_name': 'Meeting'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting_date': ('django.db.models.fields.DateField', [], {}),
            'meeting_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['IoTSSG.Employee']", 'symmetrical': 'False'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'IoTSSG.minute': {
            'Meta': {'object_name': 'Minute'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IoTSSG.Meeting']"}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IoTSSG.Project']"}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'IoTSSG.project': {
            'Meta': {'object_name': 'Project'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'cc': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'clarity_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': u"orm['IoTSSG.Employee']"}),
            'created_on': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ec': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'executive_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'fcs_commit': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fcs_current': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fcs_target': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'health': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'health_budget': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'health_resources': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'health_schedule': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'health_technical': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['IoTSSG.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'overview': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['IoTSSG.Employee']"}),
            'phase': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'releases': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'technical_description': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'})
        },
        u'IoTSSG.task': {
            'Meta': {'object_name': 'Task'},
            'created_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'last_updated_by': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'milestone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'percent_complete': ('django.db.models.fields.FloatField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IoTSSG.Project']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'task_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['IoTSSG']