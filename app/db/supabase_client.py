# app/supabase_client.py
from supabase import create_client, Client
from .config import Config

# Initialize Supabase client using Config values
supabase: Client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)