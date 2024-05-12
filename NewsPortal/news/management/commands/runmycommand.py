from django.core.management.base import BaseCommand
from news.models import Post





class Command(BaseCommand):
    help = 'Удаление поста'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Вы действительно хотите удалить пост?')

        answer = input()
        if answer == 'YES':
            Post.objects.all.delete()
            self.stdout.write(self.sryle.SUCCESS('Посты удалены'))
            return

        self.stdout.write(self.style.ERROR('Неверная команда'))

