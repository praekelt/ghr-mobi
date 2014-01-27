from setuptools import setup, find_packages

setup(
    name='app',
    version='0.0.1',
    description='Website',
    author='Unomena Developers',
    author_email='dev@unomena.com',
    url='http://unomena.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    dependency_links = [
        'http://github.com/unomena/django-photologue/tarball/2.8.praekelt#egg=django-photologue-2.8.praekelt',
        'http://github.com/unomena/django-ckeditor-new/tarball/3.6.2.2#egg=django-ckeditor-3.6.2.2',
        'http://github.com/unomena/tunobase/tarball/1.0.4#egg=tunobase-1.0.4',
        'http://github.com/unomena/django-holodeck/tarball/0.1.2#egg=django-holodeck-0.1.2',
        'http://github.com/unomena/photon/tarball/0.0.6#egg=photon-0.0.6',
    ],
    install_requires = [
        'South',
        'unipath',
        'Whoosh==2.4.1',
        'django-haystack==2.0.0',
        'django-holodeck==0.1.2',
        'django-countries',
        'django-debug-toolbar==0.11.0',
        'django-polymorphic',
        'django-ckeditor==3.6.2.2',
        'django-photologue==2.8.praekelt',
        'django-registration==1.0',
        'django-preferences',
        'python-memcached',
        'django_compressor',
        'gunicorn',
        'celery==3.0.23',
        'django-celery==3.0.23',
        'django-honeypot',
        'Pillow',
        'psycopg2',
        'photon==0.0.6',
        'flufl.password==1.2.1',
        'phonenumbers==5.9b1',
        'tunobase==1.0.4'
    ],
    include_package_data=True,
)
