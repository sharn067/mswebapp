import os

from django.core.exceptions import ValidationError


def get_path_upload_image_user(instance, filename):
    return os.path.join("users", str(instance), filename)


def get_path_upload_image_artist(instance, filename):
    return os.path.join("artists", f"{str(instance.slug)}", filename)


def get_path_upload_image_genre(instance, filename):
    return os.path.join("genres", f"{str(instance.slug)}", filename)


def get_path_upload_image_album(instance, filename):
    return os.path.join("albums", f"{str(instance.slug)}", filename)


def get_path_upload_image_playlist(instance, filename):
    return os.path.join("playlists", f"{str(instance.slug)}", filename)


def get_path_upload_image_track(instance, filename):
    return os.path.join(
        "artists",
        f"{str(instance.artist.slug)}",
        "tracks",
        f"{instance.slug}",
        filename,
    )


def get_path_upload_track(instance, filename):
    return os.path.join(
        "artists",
        f"{str(instance.artist.slug)}",
        "tracks",
        f"{instance.slug}",
        filename,
    )


def validate_image_size(file_obj):
    mb_limit = 5
    if file_obj.size > mb_limit * 1024 * 1024:
        raise ValidationError(f"Max image size {mb_limit}MB")


def validate_track_size(file_obj):
    megabyte_limit = 10
    if file_obj.size > megabyte_limit * 1024**6:
        raise ValidationError(f"Max size for audio file {megabyte_limit}MB")
