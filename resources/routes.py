from resources.auth import RegisterClient, LoginClient
from resources.auth_admin import CreateAdminResource, LoginAdminResource
from resources.order import OrderResource, ApproveOrderResource, RejectOrderResource

routes = (
    (RegisterClient, "/register"),
    (LoginClient, "/login"),
    (OrderResource, "/order"),
    (CreateAdminResource, "/create_admin"),
    (LoginAdminResource, "/login_admin"),
    (ApproveOrderResource, "/order/<int:id>/approve"),
    (RejectOrderResource, "/order/<int:id>/reject"),
)
