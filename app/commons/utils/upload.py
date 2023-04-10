import os
import uuid

from rest_framework import exceptions

user_image_path = 'user/profile-pictures/'
other_image_path = 'other/images/'


def get_file_name(_, filename):
    extension = filename.split('.')[-1]
    return "%s.%s" % (uuid.uuid4(), extension)


def get_upload_path(_, filename):
    from app.products.models import Product, ProductAttachment

    if isinstance(_, User):
        path = user_image_path
    else:
        path = other_image_path
    final_path = os.path.join(path, get_file_name(_, filename))
    return final_path


def validate_file_size(file, max_size_mb, *args, **kwargs):
    file_size = file.size
    megabyte_limit = max_size_mb
    if file_size > megabyte_limit * 1024 * 1024:
        raise exceptions.NotAcceptable({"message": "file size cannot be greater than %sMB" % str(megabyte_limit)})


def validate_file_extension(file, extension, supported_extension, *args, **kwargs):
    if extension.lower() not in supported_extension:
        raise exceptions.NotAcceptable({
            "message":
                f"{extension} is invalid file extension! {', '.join(supported_extension)} are supported formats."
        })
