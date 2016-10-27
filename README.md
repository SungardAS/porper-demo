
# Porper (Portable Permission Controller) Demo

Overview
=================

This is a project to provide scripts that are used to demonstrate the Porper library.


## Database Initialization

After creating a database, populate initial data using 'porper_initial.sql'
```
$ mysql -h <db_host> -u <db_user> -p <db_name> < porper_initial.sql
```


## Demo Environment Initialization

Set environment variables for the database connection
```
export MYSQL_HOST=<db_host>
export MYSQL_USER=<db_user>
export MYSQL_PASSWORD=<db_password>
export MYSQL_DATABASE=<db_name>
```

Run 'init.py' with python command to set up the demo environment
```
$ python init.py
```

## Controller & Model for a custom sample resource
```
Controller : demo_controller.py
Model : demo.py
```

## Demo Environment Initialization

Run the python commands in 'commands.py' step by step


## Sungard Availability Services | Labs
[![Sungard Availability Services | Labs][labs-image]][labs-github-url]

This project is maintained by the Labs team at [Sungard Availability
Services][sungardas-url]

GitHub: [https://sungardas.github.io][sungardas-github-url]

Blog: [http://blog.sungardas.com/CTOLabs/][sungardaslabs-blog-url]

[porper-core-url]: https://github.com/SungardAS/porper-core
[labs-github-url]: https://sungardas.github.io
[labs-image]: https://raw.githubusercontent.com/SungardAS/repo-assets/master/images/logos/sungardas-labs-logo-small.png
[sungardas-github-url]: https://sungardas.github.io
[sungardas-url]: http://sungardas.com
[sungardaslabs-blog-url]: http://blog.sungardas.com/CTOLabs/
