
from porper.controllers.resource_controller import ResourceController

class DemoController(ResourceController):

    def __init__(self, permission_connection):
        ResourceController.__init__(self, None, None, permission_connection)
        self.resource = 'demo'

        from demo import Demo
        self.model = Demo(permission_connection)


    def add_permissions(self, access_token, id):

        from porper.controllers.token_controller import TokenController
        token_controller = TokenController(self.connection)
        user_id = token_controller.find(access_token)[0]['user_id']

        from porper.controllers.permission_controller import PermissionController
        permission_controller = PermissionController(self.connection)

        # give read/update/delete permissions to this user
        user_permission_params = {
            "user_id": user_id,
            "resource": self.resource,
            "value": '%s' % id
        }
        user_permission_params["action"] = "read"
        permission_controller.create(access_token, user_permission_params)
        user_permission_params["action"] = "update"
        permission_controller.create(access_token, user_permission_params)
        user_permission_params["action"] = "delete"
        permission_controller.create(access_token, user_permission_params)


    def create(self, access_token, params):
        demo_id = ResourceController.create(self, access_token, params)

        # add necessary permissions for this newly created record to the current user
        self.add_permissions(access_token, demo_id)

        return demo_id
