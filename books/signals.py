# from django.db.models.signals import post_save, pre_delete, pre_save
# from django.dispatch import receiver
# from .models import Book
# from logs.models import BookChangeLogs
# from django.utils import timezone
#
#
# # this receiver is executed every-time some data is saved in any table
# @receiver(pre_save, sender=Book)
# def audit_log(sender, **kwargs):
#     # code to execute before every model save
#     print("Inside signal code")
#
#     fields = Book._meta.get_fields()
#     new_instance = kwargs['instance']
#     prev_instance = sender.objects.get(pk=new_instance.pk)
#     action = 'create' if new_instance.pk is None else 'edit'
#     model_id = new_instance.pk
#
#     for field in fields:
#         field_name = field.name
#         if field_name is not 'authors':
#             if getattr(new_instance, field_name) != getattr(prev_instance, field_name):
#                 data = getattr(new_instance, field.name)
#                 entry = BookChangeLogs.objects.create(model_id=model_id, field=field_name, data=data, action=action, timestamp=timezone.now())
#                 entry.save()
#         else:
#             print("instance field", getattr(new_instance, field_name).all())
#             print("prev instance field", getattr(prev_instance, field_name).all())
#             if list(getattr(new_instance, field_name).all()) != list(getattr(prev_instance, field_name).all()):
#                 data = list(getattr(new_instance, field.name).all())
#                 entry = BookChangeLogs.objects.create(model_id=model_id, field=field_name, data=data, action=action, timestamp=timezone.now())
#                 entry.save()



# @receiver(pre_delete, sender=Book)
# def audit_log_delete(instance, **kwargs):
#     action = 'delete'
#     model_id = instance.pk
#     entry = BookChangeLogs.objects.create(model_id=model_id, action=action, timestamp=timezone.now())
#     entry.save()