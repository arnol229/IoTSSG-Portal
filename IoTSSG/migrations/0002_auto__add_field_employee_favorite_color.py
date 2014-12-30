# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Employee.favorite_color'
        db.add_column(u'IoTSSG_employee', 'favorite_color',
                      self.gf('django.db.models.fields.CharField')(default='red', max_length=32),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Employee.favorite_color'
        db.delete_column(u'IoTSSG_employee', 'favorite_color')


    models = {
        u'IoTSSG.allocation': {
            'Meta': {'object_name': 'Allocation'},
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IoTSSG.Employee']"}),
            'fiscal_month': ('django.db.models.fields.DateField', [], {}),
            'fte_total': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'generated_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IoTSSG.Program']"})
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
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IoTSSG.Program']"}),
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
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'direct_mgr': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'emptype': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'favorite_color': ('django.db.models.fields.CharField', [], {'default': "'red'", 'max_length': '32'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'primary_role': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'role_catagory': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
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
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IoTSSG.Program']"}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'IoTSSG.program': {
            'Meta': {'object_name': 'Program'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'cc': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'clarity_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'created_on': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ec': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'executive_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'fcs_commit': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fcs_current': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'health': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['IoTSSG.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'overview': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['IoTSSG.Employee']"}),
            'phase': ('django.db.models.fields.CharField', [], {'default': "'UNDEFINED'", 'max_length': '16'}),
            'releases': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'technical_description': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['IoTSSG']