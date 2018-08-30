# Generated by Django 2.0.7 on 2018-08-02 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0005_auto_20180731_0012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recordarticle',
            options={'ordering': ('-created',), 'verbose_name': '投稿', 'verbose_name_plural': '投稿'},
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='recorded',
            new_name='articles',
        ),
        migrations.AlterField(
            model_name='recordarticle',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writing.Article', verbose_name='投稿文章'),
        ),
        migrations.AlterField(
            model_name='recordarticle',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='投稿时间'),
        ),
        migrations.AlterField(
            model_name='recordarticle',
            name='is_pass',
            field=models.BooleanField(default=False, verbose_name='投稿状态'),
        ),
        migrations.AlterField(
            model_name='recordarticle',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.Topic', verbose_name='投稿专题'),
        ),
    ]
