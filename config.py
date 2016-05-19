import os

# dev environment
DEBUG = True

HOST = '127.0.0.1'
PORT = 9090

# applicaiton directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


#  DB Settings, sqlite for this case using sql alchmeny
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}


# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2


# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "very_secret"

# Secret key for signing cookies
SECRET_KEY = "very_secret"
