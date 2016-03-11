# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models, connections


class Migration(SchemaMigration):

    def forwards(self, orm):
        table_names = connections[db.db_alias].introspection.table_names()
        if 'cmsplugin_fancyboxplugin' in table_names:
            db.rename_table('cmsplugin_fancyboxplugin', 'cmsplugin_fancybox_fancyboxplugin')

    def backwards(self, orm):
        db.rename_table('cmsplugin_fancybox_fancyboxplugin', 'cmsplugin_fancyboxplugin')

    complete_apps = ['cmsplugin_fancybox']
