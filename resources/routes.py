from resources.auth import RegisterClient, LoginClient
from resources.order import OrderResource

routes = (
    (RegisterClient, "/register"),
    (LoginClient, "/login"),
    (OrderResource, "/order"),

)
