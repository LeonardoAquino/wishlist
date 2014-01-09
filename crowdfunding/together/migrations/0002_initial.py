# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoProyecto'
        db.create_table(u'together_tipoproyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('impuesto', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'together', ['TipoProyecto'])

        # Adding model 'Proyecto'
        db.create_table(u'together_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('creador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creador', to=orm['auth.User'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('fecha_modificacion', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('terminado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('video_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('duracion', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['together.TipoProyecto'])),
        ))
        db.send_create_signal(u'together', ['Proyecto'])

        # Adding M2M table for field contribuyentes on 'Proyecto'
        m2m_table_name = db.shorten_name(u'together_proyecto_contribuyentes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm[u'together.proyecto'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proyecto_id', 'user_id'])

        # Adding model 'ImagenProyecto'
        db.create_table(u'together_imagenproyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagen', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['together.Proyecto'], null=True)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'together', ['ImagenProyecto'])

        # Adding model 'Moneda'
        db.create_table(u'together_moneda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'together', ['Moneda'])

        # Adding model 'Producto'
        db.create_table(u'together_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('precio', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('moneda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['together.Moneda'])),
            ('es_recomendado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['together.Proyecto'])),
        ))
        db.send_create_signal(u'together', ['Producto'])

        # Adding model 'ImagenProducto'
        db.create_table(u'together_imagenproducto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagen', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['together.Producto'], null=True)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'together', ['ImagenProducto'])

        # Adding model 'Categoria'
        db.create_table(u'together_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'together', ['Categoria'])

        # Adding model 'Region'
        db.create_table(u'together_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'together', ['Region'])

        # Adding model 'Comuna'
        db.create_table(u'together_comuna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('codigo', self.gf('django.db.models.fields.IntegerField')()),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['together.Region'])),
        ))
        db.send_create_signal(u'together', ['Comuna'])

        # Adding model 'TipoCuenta'
        db.create_table(u'together_tipocuenta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'together', ['TipoCuenta'])

        # Adding model 'Banco'
        db.create_table(u'together_banco', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'together', ['Banco'])

        # Adding model 'CuentaBancaria'
        db.create_table(u'together_cuentabancaria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero_cuenta', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_cuenta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['together.TipoCuenta'])),
            ('banco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['together.Banco'])),
        ))
        db.send_create_signal(u'together', ['CuentaBancaria'])

        # Adding model 'DetalleUsuario'
        db.create_table(u'together_detalleusuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(related_name='usuario', unique=True, to=orm['auth.User'])),
            ('fb_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rut', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True, null=True, blank=True)),
            ('comuna', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['together.Comuna'], null=True, blank=True)),
            ('sexo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('cuenta_bancaria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['together.CuentaBancaria'], null=True, blank=True)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'together', ['DetalleUsuario'])


    def backwards(self, orm):
        # Deleting model 'TipoProyecto'
        db.delete_table(u'together_tipoproyecto')

        # Deleting model 'Proyecto'
        db.delete_table(u'together_proyecto')

        # Removing M2M table for field contribuyentes on 'Proyecto'
        db.delete_table(db.shorten_name(u'together_proyecto_contribuyentes'))

        # Deleting model 'ImagenProyecto'
        db.delete_table(u'together_imagenproyecto')

        # Deleting model 'Moneda'
        db.delete_table(u'together_moneda')

        # Deleting model 'Producto'
        db.delete_table(u'together_producto')

        # Deleting model 'ImagenProducto'
        db.delete_table(u'together_imagenproducto')

        # Deleting model 'Categoria'
        db.delete_table(u'together_categoria')

        # Deleting model 'Region'
        db.delete_table(u'together_region')

        # Deleting model 'Comuna'
        db.delete_table(u'together_comuna')

        # Deleting model 'TipoCuenta'
        db.delete_table(u'together_tipocuenta')

        # Deleting model 'Banco'
        db.delete_table(u'together_banco')

        # Deleting model 'CuentaBancaria'
        db.delete_table(u'together_cuentabancaria')

        # Deleting model 'DetalleUsuario'
        db.delete_table(u'together_detalleusuario')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'together.banco': {
            'Meta': {'object_name': 'Banco'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'together.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'together.comuna': {
            'Meta': {'object_name': 'Comuna'},
            'codigo': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['together.Region']"})
        },
        u'together.cuentabancaria': {
            'Meta': {'object_name': 'CuentaBancaria'},
            'banco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['together.Banco']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_cuenta': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_cuenta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['together.TipoCuenta']"})
        },
        u'together.detalleusuario': {
            'Meta': {'object_name': 'DetalleUsuario'},
            'comuna': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['together.Comuna']", 'null': 'True', 'blank': 'True'}),
            'cuenta_bancaria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['together.CuentaBancaria']", 'null': 'True', 'blank': 'True'}),
            'fb_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rut': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'usuario'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'together.imagenproducto': {
            'Meta': {'object_name': 'ImagenProducto'},
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['together.Producto']", 'null': 'True'})
        },
        u'together.imagenproyecto': {
            'Meta': {'object_name': 'ImagenProyecto'},
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['together.Proyecto']", 'null': 'True'})
        },
        u'together.moneda': {
            'Meta': {'object_name': 'Moneda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'together.producto': {
            'Meta': {'object_name': 'Producto'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'es_recomendado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['together.Moneda']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'precio': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['together.Proyecto']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        },
        u'together.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'contribuyentes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'contribuyentes'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'creador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creador'", 'to': u"orm['auth.User']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'duracion': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_modificacion': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'terminado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo_proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['together.TipoProyecto']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        },
        u'together.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'together.tipocuenta': {
            'Meta': {'object_name': 'TipoCuenta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'together.tipoproyecto': {
            'Meta': {'object_name': 'TipoProyecto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impuesto': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['together']