# This file is just Python, with a touch of Django which means
# you can inherit and tweak settings to your hearts content.
from sentry.conf.server import *

import os.path

DATABASES = {
    "default": {
        "ENGINE": "sentry.db.postgres",
        "NAME": "sentry",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "",
        "AUTOCOMMIT": True,
        "ATOMIC_REQUESTS": False,
    }
}

# If you're expecting any kind of real traffic on Sentry, we highly recommend
# configuring the CACHES and Redis settings

###########
# General #
###########

# Instruct Sentry that this install intends to be run by a single organization
# and thus various UI optimizations should be enabled.
SENTRY_SINGLE_ORGANIZATION = False
DEBUG = True

#########
# Cache #
#########

# Sentry currently utilizes two separate mechanisms. While CACHES is not a
# requirement, it will optimize several high throughput patterns.

# If you wish to use memcached, uncomment the following:
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#         'LOCATION': ['127.0.0.1:11211'],
#         'OPTIONS': {'ignore_exc': True},
#     }
# }

# A primary cache is required for things such as processing events
SENTRY_CACHE = "sentry.cache.redis.RedisCache"

#########
# Queue #
#########

# See https://develop.sentry.dev/services/queue/ for more information on
# configuring your queue broker and workers. Sentry relies on a Python
# framework called Celery to manage queues.

BROKER_URL = "redis://localhost:6379"

###############
# Rate Limits #
###############

# Rate limits apply to notification handlers and are enforced per-project
# automatically.

SENTRY_RATELIMITER = "sentry.ratelimits.redis.RedisRateLimiter"

##################
# Update Buffers #
##################

# Buffers (combined with queueing) act as an intermediate layer between the
# database and the storage API. They will greatly improve efficiency on large
# numbers of the same events being sent to the API in a short amount of time.
# (read: if you send any kind of real data to Sentry, you should enable buffers)

SENTRY_BUFFER = "sentry.buffer.redis.RedisBuffer"

##########
# Quotas #
##########

# Quotas allow you to rate limit individual projects or the Sentry install as
# a whole.

SENTRY_QUOTAS = "sentry.quotas.redis.RedisQuota"

########
# TSDB #
########

# The TSDB is used for building charts as well as making things like per-rate
# alerts possible.

SENTRY_TSDB = "sentry.tsdb.redissnuba.RedisSnubaTSDB"

###########
# Digests #
###########

# The digest backend powers notification summaries.

SENTRY_DIGESTS = "sentry.digests.backends.redis.RedisBackend"

##############
# Web Server #
##############

# If you're using a reverse SSL proxy, you should enable the X-Forwarded-Proto
# header and uncomment the following settings
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

SENTRY_WEB_HOST = "0.0.0.0"
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    # 'workers': 1,  # the number of web workers
    # 'protocol': 'uwsgi',  # Enable uwsgi protocol instead of http
}

##############
# Devserver #
##############

# Exclude logs caused by Relay polling every 100ms.
# Makes it rather hard to use Python debugger
DEVSERVER_REQUEST_LOG_EXCLUDES = ["/api/0/relays/projectconfigs/"]


# This is where I start changing shit

SENTRY_USE_RELAY = True
CSRF_TRUSTED_ORIGINS = [
    "https://leeandher.ngrok.io",
    "https://us.leeandher.ngrok.io",
    "http://dev.getsentry.net",
    "https://dev.getsentry.net",
    "http://localhost",
]
ALLOWED_HOSTS = [
    ".leeandher.ngrok.io",
    ".us.leeandher.ngrok.io",
    ".ngrok.io",
    ".dev.getsentry.net",
    ".getsentry.net",
    "localhost",
    ".docker.internal",
    "127.0.0.1",
]
SESSION_COOKIE_DOMAIN = ".leeandher.ngrok.io"
CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN
SUDO_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN

SENTRY_REGION_CONFIG = [
    {
        "name": "us",
        "snowflake_id": 1,
        "category": "MULTI_TENANT",
        "address": "http://127.0.0.1:8010",
        "visible": True,
    },
]
SENTRY_MONOLITH_REGION = SENTRY_REGION_CONFIG[0]["name"]
CHARTCUTERIE_CONFIG_PATH = "./config.yml"

SENTRY_FEATURES["system:multi-region"] = False

# Manual opt-ins
SENTRY_FEATURES["organizations:chonk-ui"] = True
SENTRY_FEATURES["organizations:discover"] = True
SENTRY_FEATURES["organizations:discover-query"] = True
SENTRY_FEATURES["organizations:agents-insights"] = True
SENTRY_FEATURES["organizations:visibility-explore-view"] = True

# Actually communicated to me that I need to enable this
# Enables the Multiple Projects Selection feature
SENTRY_FEATURES["organizations:global-views"] = True
# Enables the Issue Views feature
SENTRY_FEATURES["organizations:issue-views"] = True
# Enables the Metric Alerts feature
SENTRY_FEATURES["organizations:incidents"] = True
