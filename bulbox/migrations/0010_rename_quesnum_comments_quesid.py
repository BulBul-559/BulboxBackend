# Generated by Django 4.2.4 on 2023-10-27 21:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bulbox", "0009_comments_iwanna_alter_question_ans_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comments",
            old_name="quesNum",
            new_name="quesId",
        ),
    ]