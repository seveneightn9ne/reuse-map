DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'reuse_map',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'reuse_map',
        'PASSWORD': '*** secret.from.local_settings ***',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
