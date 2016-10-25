
# get the connection to the poper database
from porper.models.connection import mysql_connection
connection = mysql_connection()


# create the first user, admin
from porper.controllers.user_controller import UserController
user_controller = UserController(connection)
admin_access_token = 'ffffffff-ffff-ffff-ffff-ffffffffffff'
admin_user_id = 'ffffffff-ffff-ffff-ffff-ffffffffffff'
admin_email_address = 'admin@porper.com'
params = {
  'id': admin_user_id,
  'email': admin_email_address,
  'family_name': "admin",
  'given_name': 'user'
};
admin_user_id = user_controller.create(admin_access_token, params)
connection.commit()


# simulate the login by admin
from porper.controllers.token_controller import TokenController
token_controller = TokenController(connection)
admin_access_token = 'ffffffff-ffff-ffff-ffff-ffffffffffff'
admin_refresh_token = 'ffffffff-ffff-ffff-ffff-ffffffffffff'
token_controller.save(admin_access_token, admin_refresh_token, admin_user_id)
connection.commit()


# create a new role
from porper.controllers.role_controller import RoleController
role_controller = RoleController(connection)
params = {
    'name': 'demo'
}
role_id = role_controller.create(admin_access_token, params)
connection.commit()


# invite a user so that the user can login to the system
from porper.controllers.invited_user_controller import InvitedUserController
invited_user_controller = InvitedUserController(connection)
email_address = 'demo@porper.com'
invited_by = 'ffffffff-ffff-ffff-ffff-ffffffffffff'
params = {
    'email': email_address,
    'role_id': role_id,
    'invited_by': invited_by
};
invited_user_controller.create(admin_access_token, params)
connection.commit()


# now register the invited user, which will be automatically done once the invited user successfully logs in using open-id
from porper.controllers.user_controller import UserController
user_controller = UserController(connection)
user_id = 'abcd1234'
family_name = 'family'
given_name = 'given'
params = {
  'id': user_id,
  'email': email_address,
  'family_name': family_name,
  'given_name': given_name
};
user_controller.create(admin_access_token, params)
connection.commit()


# create a table for a sample resource, demo
cursor = connection.cursor()
sql = "CREATE TABLE demo (id varchar(10), name varchar(50), description varchar(100))"
cursor.execute(sql)
connection.commit()
