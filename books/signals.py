from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.dispatch import receiver
from .models import Book
from authors.models import Author
from logs.models import BookChangeLogs
from django.utils import timezone


@receiver(pre_delete, sender=Book)
def audit_log_delete(instance, **kwargs):
    action = 'delete'
    model_id = instance.pk
    entry = BookChangeLogs.objects.create(model_id=model_id, action=action, timestamp=timezone.now())
    entry.save()


@receiver(post_save, sender=Book)
def audit_log_create(instance, created, **kwargs):
    if created:
        action = 'create'
        model_id = instance.pk
        fields = Book._meta.get_fields()
        for field in fields:
            field_name = field.name
            if field_name is not 'authors':
                    data = getattr(instance, field.name)
                    entry = BookChangeLogs.objects.create(model_id=model_id, field=field_name, data=data, action=action,
                                                          timestamp=timezone.now())
                    entry.save()


@receiver(m2m_changed, sender=Book.authors.through)
def m2m_change(**kwargs):
    m2m_action = kwargs.pop('action', None)
    new_instance = kwargs['instance']
    pk_set = kwargs['pk_set']
    if m2m_action == "pre_add":
        inst = Book.objects.get(pk=new_instance.pk)
        action = 'create' if not getattr(inst, 'authors').all() else 'add'
        data = list(Author.objects.filter(pk__in=list(pk_set)))
        entry = BookChangeLogs.objects.create(model_id=new_instance.pk, field='authors', data=data, action=action,
                                              timestamp=timezone.now())
        entry.save()
    elif m2m_action == "pre_remove":
        action = 'remove'
        data = list(Author.objects.filter(pk__in=list(pk_set)))
        entry = BookChangeLogs.objects.create(model_id=new_instance.pk, field='authors', data=data, action=action,
                                              timestamp=timezone.now())
        entry.save()




