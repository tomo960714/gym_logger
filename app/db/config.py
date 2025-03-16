from dotenv import load_dotenv
import os
# Load environment variables in development
if os.getenv("FLASK_ENV") != "production":
    load_dotenv()



class Config:
    SUPABASE_URL : str= os.environ.get("SUPABASE_URL")
    SUPABASE_KEY : str= os.environ.get("SUPABASE_KEY")

