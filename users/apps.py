from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # def ready(self):
    #     from users.init_groups import init_groups
        
    #     post_migrate.connect(init_groups, sender=self)
    #     return super().ready()
