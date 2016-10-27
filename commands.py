
# get the connection to porper database
from porper.models.connection import mysql_connection
connection = mysql_connection()

# try creating a new instance of the demo resource
from demo_controller import DemoController
demo_controller = DemoController(connection)
admin_access_token = 'ffffffff-ffff-ffff-ffff-ffffffffffff'
demo_create_params = { "id":"1", "name":"first", "description":"first instance" }
demo_controller.create(admin_access_token, demo_create_params)
### should be failed with 'Exception: not permitted'

# grant a permission to 'create' a new demo instance to 'admin' user
admin_user_id = 'ffffffff-ffff-ffff-ffff-ffffffffffff'
from porper.controllers.permission_controller import PermissionController
permission_controller = PermissionController(connection)
permission_params = {
    "user_id": admin_user_id,
    "resource": "demo",
    "value": "*",
    "action": "create"
}
permission_controller.create(admin_access_token, permission_params)
connection.commit()

# try again creating a new instance of the demo resource
demo_controller.create(admin_access_token, demo_create_params)
connection.commit()

# try retrieve the newly created instance
demo_find_params = { "id":"1" }
demo_controller.find_all(admin_access_token, demo_find_params)

# find the information of 'demo@porper.com' user
from porper.controllers.user_controller import UserController
user_controller = UserController(connection)
user_find_params = { "email": "demo@porper.com" }
user_info = user_controller.find_all(admin_access_token, user_find_params)
user_id = user_info[0][ "id"]

# simulate the login by that user
from porper.controllers.token_controller import TokenController
token_controller = TokenController(connection)
user_access_token = 'ffffffff-user-ffff-ffff-ffffffffffff'
user_refresh_token = 'ffffffff-user-ffff-ffff-ffffffffffff'
token_controller.save(user_access_token, user_refresh_token, user_id)
connection.commit()

# try retriving the newly create instance using 'demo@porper.com' user session
demo_controller.find_all(user_access_token, demo_find_params)
### should be failed with 'Exception: not permitted'

# grant a permission to 'read' the newly created instance to 'demo@porper.com' user
permission_params = {
    "user_id": user_id,
    "resource": "demo",
    "value": "1",
    "action": "read"
}
permission_controller.create(admin_access_token, permission_params)
connection.commit()

# try again retriving the newly create instance using 'demo@porper.com' user session
demo_controller.find_all(user_access_token, demo_find_params)
