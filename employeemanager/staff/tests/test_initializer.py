import logging

# suppresses DEBUG information from app's dependencies on tests

logging.getLogger('factory').setLevel(logging.WARN)
logging.getLogger('log_request_id.middleware').setLevel(logging.WARN)
