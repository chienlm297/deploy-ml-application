import os

config = {
    "TORCHSERVE_ADDRESS": os.environ.get("TORCHSERVE_ADDRESS") or "0.0.0.0",
    "TORCHSERVE_PORT": os.environ.get("TORCHSERVE_PORT") or "8000",
    "MINIO_ADDRESS": os.environ.get("MINIO_ADDRESS") or "0.0.0.0",
    "MINIO_PORT": os.environ.get("MINIO_PORT") or "9000",
    "MINIO_ACCESS_KEY": os.environ.get("MINIO_ACCESS_KEY") or "",
    "MINIO_SECRET_KEY": os.environ.get("MINIO_SECRET_KEY") or "",
    "BUCKET_IMAGE": os.environ.get("BUCKET_IMAGE") or "pdf-files",
    "CELERY_CONVERT_TASK": os.environ.get("CELERY_CONVERT_TASK") or "tasks.convert",
    "CELERY_BROKER_URL": os.environ.get("CELERY_BROKER_URL")
    or "amqp://guest:**@localhost:5672//",
    "CELERY_RESULT_BACKEND": os.environ.get("CELERY_RESULT_BACKEND")
    or "amqp://guest:**@localhost:5672//",
    "CELERY_ACKS_LATE": os.environ.get("CELERY_ACKS_LATE") or None,
    "CELERYD_PREFETCH_MULTIPLIER": os.environ.get("CELERYD_PREFETCH_MULTIPLIER")
    or None,
    "X_MAX_PRIORITY": os.environ.get("X_MAX_PRIORITY") or None,
    "BUCKET_FILE_EXPIRATION_DAYS": os.environ.get("BUCKET_FILE_EXPIRATION_DAYS") or 2,
}
