import requests
from bs4 import BeautifulSoup

def get_github_profile_image(user):
    # URL of the GitHub user's profile
    url = f"https://github.com/{user}"
    
    try:
        # Send a GET request to fetch the raw HTML content
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Error: Unable to fetch profile for {user}. HTTP Status code: {response.status_code}")
            return
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the profile image tag using its class name
        # GitHub profile image is usually stored in the 'avatar-user' class
        profile_img_tag = soup.find('img', {'class': 'avatar-user'})
        
        if profile_img_tag:
            # Get the 'src' attribute which contains the image URL
            profile_image_url = profile_img_tag['src']
            
            # Full URL of the image 
            if not profile_image_url.startswith('http'):
                profile_image_url = 'https:' + profile_image_url
            
            print(f"GitHub Profile Image URL for {user}: {profile_image_url}")
        else:
            print(f"Error: No profile image found for user '{user}'.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching profile for {user}: {e}")

def main():
    # Ask for the GitHub username
    user = input("Enter GitHub username: ").strip()
    
    # Fetch and display the profile image URL
    get_github_profile_image(user)

if __name__ == "__main__":
    main()
