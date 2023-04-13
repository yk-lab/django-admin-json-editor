import os

from setuptools import setup
from setuptools_scm import get_version


project_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(project_path, 'README.md'), 'r') as fout:
    README = fout.read()

# allow setup.py to be run from any path
os.chdir(project_path)

requirements = [
    'Django',
]

setup_requires = [
    'setuptools_scm',
    'pytest-runner',
]

test_requirements = [
    'pytest',
    'pytest-django',
]

setup(
    name='django-admin-json-editor',
    version=get_version(),
    packages=['django_admin_json_editor'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to add JSON widget into Django Administration.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/abogushov/django-admin-json-editor',
    author='Alexander Bogushov',
    author_email='abogushov@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=requirements,
    test_suite='tests',
    setup_requires=setup_requires,
    tests_require=test_requirements,
)
