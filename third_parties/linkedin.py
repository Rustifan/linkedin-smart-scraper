import os
from linkedin_api import Linkedin

def scrape_linkedin_profile(url: str)->dict:
    profile_id = get_profile_id_from_linkedin_url(url)
    email = os.environ.get("LINKEDIN_EMAIL")
    password = os.environ.get("LINKEDIN_PASSWORD")
    api = Linkedin(email, password)
    profile = api.get_profile(profile_id)
    
    return profile


def get_profile_id_from_linkedin_url(url: str) -> str:
    return url.split("in/")[1].split("/")[0]


def get_img_url_from_linkedin_data(linkedin_data: dict, size="400")-> str:
    base = linkedin_data.get("displayPictureUrl")
    size_key = f"img_{size}_{size}"
    size = linkedin_data.get(size_key)
    if base is None or size is None:
        return ""
    return f"{base}{size}"
    
    
    