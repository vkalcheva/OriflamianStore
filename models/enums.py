import enum


class RoleType(enum.Enum):
    partner = "partner"
    client = "client"
    admin = "admin"


class State(enum.Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
