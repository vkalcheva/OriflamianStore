from resources.auth import RegisterClient, LoginClient
from resources.auth_admin import CreateAdminResource, LoginAdminResource
from resources.category import CategoryResource
from resources.order import OrderResource, ApproveOrderResource, RejectOrderResource
from resources.product import ProductResource

routes = (
    (RegisterClient, "/register"),
    (LoginClient, "/login"),
    (CreateAdminResource, "/create_admin"),
    (LoginAdminResource, "/login_admin"),
    (OrderResource, "/order"),
    (ApproveOrderResource, "/order/<int:id>/approve"),
    (RejectOrderResource, "/order/<int:id>/reject"),
    (ProductResource, "/product"),
    (CategoryResource, "/category"),
)
