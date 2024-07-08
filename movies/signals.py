from django.db.models.signals import post_save
from django.dispatch import receiver
import django.dispatch

from movies.models import SearchTerm
from movies.tasks import notify_on_new_search_term

@receiver(post_save, sender=SearchTerm, dispatch_uid="search_term_saved")
def search_term_saved(sender, instance, created, **kwargs):
    if created:
        notify_on_new_search_term.delay(instance.term)


movie_filled = django.dispatch.Signal()
@receiver(movie_filled, sender="fill_movie_details")
def movie_details_filled(sender, **kwargs):
    print(f"Movie detail filled for the movie: {kwargs.get('movie').title}")