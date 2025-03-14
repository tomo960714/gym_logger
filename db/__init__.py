from .config import supabase
from .auth import db_sign_up,db_sign_in,db_sign_out


__all__ = ["db_sign_up","db_sign_in","db_sign_out"]

## will be for queries to be ableto load them easily
# from .queries import func1,func2,func3,func3
# __all__ = ["func1", "func2", "func3", "func3"]
# Then can use them like this in other places:
# from db import func1, func2

