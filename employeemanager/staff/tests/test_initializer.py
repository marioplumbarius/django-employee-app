import logging

# suppresses DEBUG information from factory_boy dependency on tests
logging.getLogger('factory').setLevel(logging.WARN)
