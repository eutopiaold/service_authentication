import secret

# Product name
product_name = "Cube"


# Edit the below variables to match correct database settings
db_type = 'postgresql'
db_user = 'dwokggtw'
db_password = secret.database_password
db_url = 'balarama.db.elephantsql.com'
db_port = '5432'
db_name = 'dwokggtw'

db_connection_string = "%s://%s:%s@%s:%s/%s" % (db_type, db_user, db_password, db_url, db_port, db_name)


# Flask settings
flask_host = "0.0.0.0"
flask_port = 5000


# Other microservices' IPs
send_mail = "http://ec2-3-86-97-218.compute-1.amazonaws.com/send-mail"
send_mail_password = secret.send_mail_password


# Other
minimum_password_length = 8


# Auth service passwords
my_password = secret.auth_service_password
