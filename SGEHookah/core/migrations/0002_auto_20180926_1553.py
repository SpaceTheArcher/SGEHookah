# Generated by Django 2.0.4 on 2018-09-26 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formapagamento',
            name='dt_alteracao',
        ),
        migrations.RemoveField(
            model_name='formapagamento',
            name='dt_cadastro',
        ),
        migrations.RemoveField(
            model_name='formapagamento',
            name='fkid_usuario_alteracao',
        ),
        migrations.RemoveField(
            model_name='pedidovenda',
            name='dt_alteracao',
        ),
        migrations.RemoveField(
            model_name='pedidovenda',
            name='dt_cadastro',
        ),
        migrations.RemoveField(
            model_name='pedidovenda',
            name='fkid_pessoa',
        ),
        migrations.RemoveField(
            model_name='pedidovenda',
            name='fkid_usuarioalteracao',
        ),
        migrations.AddField(
            model_name='pedidofabricacao',
            name='lote',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='pedidovenda',
            name='fkid_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa'),
        ),
        migrations.AddField(
            model_name='produto',
            name='vendivel',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='formapagamento',
            name='hide',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='fkid_entrega',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='fkid_formapag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Formapagamento'),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='fkid_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Statusvenda'),
        ),
        migrations.AlterField(
            model_name='pedidovenda',
            name='fkid_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]