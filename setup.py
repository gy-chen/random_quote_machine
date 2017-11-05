from setuptools import find_packages, setup

setup(
    name="random_quote_machine",
    version="0.0.1",
    description="A challange from FreeCodeCamp",
    author="GYCHEN",
    email="gy.chen@gms.nutc.edu.tw",
    packages=find_packages(),
    install_requires=['google-api-python-client',
                      'youtube-dl',
                      'pysrt',
                      'sumy',
                      'numpy',
                      'sqlalchemy',
                      'flask',
                      'gunicorn',
                      'psycopg2'],
    entry_points={
        'console_scripts': [
            'rqm_update_videos_from_youtube=random_quote_machine.job:update_videos_from_youtube'
        ]
    },
    scripts=[
        'scripts/rqm_web'
    ]
)
