# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employee'
        db.create_table(u'IoTSSG_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('portrait', self.gf('django.db.models.fields.files.ImageField')(default='images/portraits/default.jpg', max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('emptype', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('direct_mgr', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('primary_role', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('role_catagory', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'IoTSSG', ['Employee'])

        # Adding model 'Project'
        db.create_table(u'IoTSSG_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('clarity_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fcs_target', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fcs_commit', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fcs_current', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('ec', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cc', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('health', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('health_schedule', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
            ('health_resources', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
            ('health_budget', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
            ('health_technical', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['IoTSSG.Employee'])),
            ('lead', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['IoTSSG.Employee'])),
            ('executive_sponsor', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('overview', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('technical_description', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('releases', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['IoTSSG.Employee'])),
            ('phase', self.gf('django.db.models.fields.CharField')(default='UNDEFINED', max_length=16)),
        ))
        db.send_create_signal(u'IoTSSG', ['Project'])

        # Adding model 'Task'
        db.create_table(u'IoTSSG_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task_id', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('milestone', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('percent_complete', self.gf('django.db.models.fields.FloatField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('created_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['IoTSSG.Project'])),
            ('last_updated_by', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
        ))
        db.send_create_signal(u'IoTSSG', ['Task'])

        # Adding model 'Allocation'
        db.create_table(u'IoTSSG_allocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['IoTSSG.Project'])),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['IoTSSG.Employee'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('fte_total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'IoTSSG', ['Allocation'])

        # Adding model 'Bug'
        db.create_table(u'IoTSSG_bug', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['IoTSSG.Project'])),
            ('bug_id', self.gf('django.db.models.fields.CharField')(max_length=64, db_index=True)),
            ('manager_id', self.gf('django.db.models.fields.CharField')(max_length=16, db_index=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('severity', self.gf('django.db.models.fields.IntegerField')()),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('is_open', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('month_start', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'IoTSSG', ['Bug'])

        # Adding model 'Meeting'
        db.create_table(u'IoTSSG_meeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meeting_date', self.gf('django.db.models.fields.DateField')()),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('meeting_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'IoTSSG', ['Meeting'])

        # Adding M2M table for field participants on 'Meeting'
        m2m_table_name = db.shorten_name(u'IoTSSG_meeting_participants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('meeting', models.ForeignKey(orm[u'IoTSSG.meeting'], null=False)),
            ('employee', models.ForeignKey(orm[u'IoTSSG.employee'], null=False))
        ))
        db.create_unique(m2m_table_name, ['meeting_id', 'employee_id'])

        # Adding model 'Minute'
        db.create_table(u'IoTSSG_minute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('meeting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['IoTSSG.Meeting'])),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['IoTSSG.Project'])),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'IoTSSG', ['Minute'])

        # Adding model 'Department'
        db.create_table(u'IoTSSG_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('director', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['IoTSSG.Employee'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'IoTSSG', ['Department'])


    def backwards(self, orm):
        # Deleting model 'Employee'
        db.delete_table(u'IoTSSG_employee')

        # Deleting model 'Project'
        db.delete_table(u'IoTSSG_project')

        # Deleting model 'Task'
        db.delete_table(u'IoTSSG_task')

        # Deleting model 'Allocation'
        db.delete_table(u'IoTSSG_allocation')

        # Deleting model 'Bug'
        db.delete_table(u'IoTSSG_bug')

        # Deleting model 'Meeting'
        db.delete_table(u'IoTSSG_meeting')

        # Removing M2M table for field participants on 'Meeting'
        db.delete_table(db.shorten_name(u'IoTSSG_meeting_participants'))

        # Deleting model 'Minute'
        db.delete_table(u'IoTSSG_minute')

        # Deleting model 'Department'
        db.delete_table(u'IoTSSG_department')


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
            'phase': ('django.db.models.fields.CharField', [], {'default': "'UNDEFINED'", 'max_length': '16'}),
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