from config import supabase
from supabase import SupabaseException

def db_sign_up(email,password):
    
    try:
        # Attempt to sign up the user
        response = supabase.auth.sign_up({"email": email, "password": password})
        # If successful, return the response
        return response
    except SupabaseException as e:
        # Catch any Supabase-related errors
        return {"error": f"Supabase error: {e}"}
    except Exception as e:
        # Catch any other errors that may occur
        return {"error": f"An unexpected error occurred: {e}"}
    
def db_sign_in(email, password):
    try:
        # Attempt to sign in the user
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return response  # Successful sign-in
    except SupabaseException as e:
        # Catch Supabase-related errors
        return {"error": f"Supabase error during sign-in: {e}"}
    except Exception as e:
        # Catch any other unexpected errors
        return {"error": f"An unexpected error occurred during sign-in: {e}"}
    
def db_sign_out():
    ### Returns None if succesfull
    try:
        # Attempt to sign out the user
        response = supabase.auth.sign_out()
        return response  # Successful sign-out
    except SupabaseException as e:
        # Catch Supabase-related errors
        return {"error": f"Supabase error during sign-out: {e}"}
    except Exception as e:
        # Catch any other unexpected errors
        return {"error": f"An unexpected error occurred during sign-out: {e}"}

#response = db_sign_out()
#response = db_sign_in(email="valaky96@gmail.com",password="password")
#print(response.session.access_token)