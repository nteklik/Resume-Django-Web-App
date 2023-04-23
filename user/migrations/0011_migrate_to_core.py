# Generated by Django 4.0.6 on 2023-04-23 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_statistics'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO core_generalsetting (
                id,
                name,
                description,
                parameter,
                updated_date,
                created_date
            )
            SELECT
                id,
                name,
                description,
                parameter,
                updated_date,
                created_date
            FROM
                user_generalsetting;
            SELECT setval('core_generalsetting_id_seq', (SELECT MAX(id) FROM core_generalsetting)+1);
        """, reverse_sql="""
            INSERT INTO user_generalsetting (
                id,
                name,
                description,
                parameter,
                updated_date,
                created_date
            )
            SELECT
                id,
                name,
                description,
                parameter,
                updated_date,
                created_date
            FROM
                core_generalsetting;
            SELECT setval('user_generalsetting_id_seq', (SELECT MAX(id) FROM user_generalsetting)+1);
        """),

        migrations.RunSQL("""
            INSERT INTO core_imagesetting (
                id,
                name,
                description,
                file,
                updated_date,
                created_date
            )
            SELECT
                id,
                name,
                description,
                file,
                updated_date,
                created_date
            FROM
                user_imagesetting;
            SELECT setval('core_imagesetting_id_seq', (SELECT MAX(id) FROM core_imagesetting)+1);
        """, reverse_sql="""
            INSERT INTO user_imagesetting (
                id,
                name,
                description,
                file,
                updated_date,
                created_date
            )
            SELECT
                id,
                name,
                description,
                file,
                updated_date,
                created_date
            FROM
                core_imagesetting;
            SELECT setval('user_imagesetting_id_seq', (SELECT MAX(id) FROM user_imagesetting)+1);
        """),

        migrations.RunSQL("""
            INSERT INTO core_document (
                id,
                name,
                button_text,
                file,
                show_on_page,
                updated_date,
                created_date
            )
            SELECT
                id,
                name,
                button_text,
                file,
                show_on_page,
                updated_date,
                created_date
            FROM
                user_document;
            SELECT setval('core_document_id_seq', (SELECT MAX(id) FROM core_document)+1);
        """, reverse_sql="""
            INSERT INTO user_document (
                id,
                name,
                button_text,
                file,
                show_on_page,
                updated_date,
                created_date
            )
            SELECT
                id,
                name,
                button_text,
                file,
                show_on_page,
                updated_date,
                created_date
            FROM
                core_document;
            SELECT setval('user_document_id_seq', (SELECT MAX(id) FROM user_document)+1);
        """),

        migrations.RunSQL("""
            INSERT INTO core_message (
                id,
                name,
                email,
                subject,
                message,
                error_message,
                success,
                updated_date,
                created_date
            )
            SELECT
                id,
                name,
                email,
                subject,
                message,
                error_message,
                success,
                updated_date,
                created_date
            FROM
                user_message;
            SELECT setval('core_message_id_seq', (SELECT MAX(id) FROM core_message)+1);
        """, reverse_sql="""
            INSERT INTO user_message (
                id,
                name,
                email,
                subject,
                message,
                error_message,
                success,
                updated_date,
                created_date
            )
            SELECT
                id,
                name,
                email,
                subject,
                message,
                error_message,
                success,
                updated_date,
                created_date
            FROM
                core_message;
            SELECT setval('user_message_id_seq', (SELECT MAX(id) FROM user_message)+1);
        """),

        migrations.RunSQL("""
            INSERT INTO core_redirectslug (
                id,
                slug,
                new_url,
                updated_date,
                created_date
            )
            SELECT
                id,
                slug,
                new_url,
                updated_date,
                created_date
            FROM
                user_redirectslug;
            SELECT setval('core_redirectslug_id_seq', (SELECT MAX(id) FROM core_redirectslug)+1);
        """, reverse_sql="""
            INSERT INTO user_redirectslug (
                id,
                slug,
                new_url,
                updated_date,
                created_date
            )
            SELECT
                id,
                slug,
                new_url,
                updated_date,
                created_date
            FROM
                core_redirectslug;
            SELECT setval('user_redirectslug_id_seq', (SELECT MAX(id) FROM user_redirectslug)+1);
        """),

        migrations.RunSQL("""
            INSERT INTO core_statistics (
                id,
                statistic_type,
                action,
                source,
                ip_address,
                user_agent,
                updated_date,
                created_date
            )
            SELECT
                id,
                statistic_type,
                action,
                source,
                ip_address,
                user_agent,
                updated_date,
                created_date
            FROM
                user_statistics;
            SELECT setval('core_statistics_id_seq', (SELECT MAX(id) FROM core_statistics)+1);
        """, reverse_sql="""
            INSERT INTO user_statistics (
                id,
                statistic_type,
                action,
                source,
                ip_address,
                user_agent,
                updated_date,
                created_date
            )
            SELECT
                id,
                statistic_type,
                action,
                source,
                ip_address,
                user_agent,
                updated_date,
                created_date
            FROM
                core_statistics;
            SELECT setval('user_statistics_id_seq', (SELECT MAX(id) FROM user_statistics)+1);
        """),
    ]
