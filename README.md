# pgsql-aws-s3-backup

[Latest Release](https://github.com/yelluw/pgsql-aws-s3-backup/releases/latest)

Utility to backup a postgresql db and upload it to aws s3.

This is not meant to work with any other databases.

However, it could be easily be modified to do so.

Feel free to fork and modify to your needs. Just make sure to change the name to fit your database 😎


# Requirements

`Python 3.6+    # This was developed on 3.9`

`PostgreSQL 9+  # This was developed with 13`

`Amazon AWS account with access keys`


# Install

It is strongly recommended that you install it on a virtual environment

Download latest release to wherever you want to run it from. 


`python3 -m venv .venv`

On Linux/OSX:

`source .venv/bin/activate`

On Windows:

	This has not been tested on windows at all. Feeling lucky?


`pip install -r requirements.txt`


# Run

This program is meant to be run by cron.
There is no bash script included. Please build your own.

This is how *I* have it setup on my crontab:

    
		          # Path to to the virtual env python executable    # Path to main on script
		* * * * * /path/to/my/python/environment/env/bin/python && /path/to/pgsql-aws-s3-backup/main.py > /dev/null 2>&1

[This](https://crontab.guru/) is a good utility to help you figure out your crontab setup.

From whatever directory you downloaded it to: Run `python3 main.py`


#### Helpful advice

- You should run this through your cron tab.
- I did not include a bash script on purpose.
- Do not blindly trust automated backups. Always test them.
- Call your mother.


# Required Items

- AWS credentials
- An S3 with correct ACL (this script does not modify ACL)
- PostgreSQL database credentials
- The path of the directory where the backup files are stored


# Configuration


		
		# postgreSQL
		PG_HOST=localhost
		PG_PORT=5432
		PG_USER=user
		DB_NAME=example
		
		# used by pg_dump directly
		PGPASSWORD=123
		
		# output directories
		SQL_DIR=/
		LOG_DIR=/var/log
		
		# logging stuff
		# Optional, but nice to have
		DEBUG_LEVEL=DEBUG
		MAX_BYTES=2097152. # Default - 2MB (1024*1024*2)
		BACKUP_COUNT=10 # Default - 10 log files
		
		# aws s3
		AWS_ACCESS_KEY_ID=12345
		AWS_SECRET_ACCESS_KEY=12345
		AWS_S3_BUCKET_NAME=test_bucket
		



# Development

Run `pip install -r requirements-dev.txt`

To run tests:

`pytest tests.py`


# License

MIT

# Koan

#### The Stone Mind

Hogen, a Chinese Zen teacher, lived alone in a small temple in the country. One day four traveling monks appeared and asked if they might make a fire in his yard to warm themselves.

While they were building the fire, Hogen heard them arguing about subjectivity and objectivity. He joined them and said: There is a big stone. Do you consider it to be inside or outside your mind?'

One of the monks replied: 'From the Buddhist viewpoint everything is an objectification of mind, so I would say that the stone is inside my mind.'

'Your head must feel very heavy’, observed Hogen. 'if you are carrying around a stone like that in your mind.'
