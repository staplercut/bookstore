from django.core.management.base import BaseCommand, CommandError
from books.models import Book


class Command(BaseCommand):
    help = 'list all books. add parameter desc for descending list, asc for ascending'

    def add_arguments(self, parser):
        parser.add_argument('sort_type', type=str)

    def handle(self, *args, **options):
        if options['sort_type'] == 'desc':
            print(Book.objects.all().order_by('-publish_date'))
        elif options['sort_type'] == 'asc':
            print(Book.objects.all())
