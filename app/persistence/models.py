from pynamodb.attributes import NumberAttribute, UnicodeAttribute
from pynamodb.models import Model
from settings import get_settings

settings = get_settings()


class CakeDb(Model):
    """Model of a cake for the DynamoDB interface."""

    comment = UnicodeAttribute()
    id = NumberAttribute(hash_key=True)
    image_url = UnicodeAttribute()
    name = UnicodeAttribute()
    yum_factor = NumberAttribute()

    class Meta:
        aws_access_key_id = settings.aws_access_key_id
        aws_secret_access_key = settings.aws_secret_access_key
        host = settings.dynamodb_host
        region = settings.aws_region
        table_name = settings.dynamodb_table_name


def ensure_table_is_created():
    """Convenience function to create the table if not already created.

    NOTE: ideally this would be done with IAC."""
    if not CakeDb.exists():
        CakeDb.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
