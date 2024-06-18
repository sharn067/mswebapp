from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.audio.models import Track
from apps.core.models import TimeStampedModel
from apps.core.services import get_path_upload_image_playlist, validate_image_size
from apps.other.models import Genre

User = get_user_model()


class Playlist(TimeStampedModel):
    """
    Playlist model.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
    tracks = models.ManyToManyField(Track, related_name="playlists")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name="playlists")
    title = models.CharField(_("title"), max_length=255)
    image = models.ImageField(
        verbose_name=_("image"),
        upload_to=get_path_upload_image_playlist,
        validators=[validate_image_size],
        blank=True,
        default="default/track.jpg",
    )
    release_date = models.DateField(_("release date"), blank=True, null=True)
    is_private = models.BooleanField(_("is_private"), default=False)

    @property
    def get_tracks_count(self):
        return self.tracks.count()

    @property
    def get_tracks(self):
        return self.tracks.all()

    class Meta:
        verbose_name = _("playlist")
        verbose_name_plural = _("playlists")
        ordering = ["-created_at", "-updated_at"]

    def __str__(self):
        return self.title
