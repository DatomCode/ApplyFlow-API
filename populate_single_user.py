import requests

# ⚠️ CHECK YOUR PORT: Your last error showed port 8003. 
# If you are on 8000, change this to http://127.0.0.1:8000
BASE_URL = "http://127.0.0.1:8003" 

#THE TARGET USER (Who gets all the jobs?)
# You can change this to your main admin account if you want.
target_user = {
    "username": "ApplyFlow-Admin", 
    "password": "damilare007", 
    "email": "applyflowadmin@gmail.com", 
    "first_name": "apply", 
    "last_name": "flow"
}

# 2. THE DATA (20 Jobs)
all_jobs = [
  { "company_name": "Google", "job_title": "Backend Engineer", "status": "Applied", "job_url": "https://careers.google.com" },
  { "company_name": "Netflix", "job_title": "Senior Python Developer", "status": "Interviewing", "job_url": "https://jobs.netflix.com" },
  { "company_name": "Amazon", "job_title": "SDE I", "status": "Rejected", "job_url": "https://amazon.jobs" },
  { "company_name": "Meta", "job_title": "DevOps Engineer", "status": "Applied", "job_url": "https://metacareers.com" },
  { "company_name": "Spotify", "job_title": "Backend Developer", "status": "Offer", "job_url": "http://spotify.com" },
  { "company_name": "Tesla", "job_title": "Autopilot Engineer", "status": "Applied", "job_url": "https://tesla.com" },
  { "company_name": "Microsoft", "job_title": "Cloud Architect", "status": "Interviewing", "job_url": "https://microsoft.com" },
  { "company_name": "Airbnb", "job_title": "Full Stack Dev", "status": "Applied", "job_url": "https://airbnb.com" },
  { "company_name": "Uber", "job_title": "Systems Engineer", "status": "Rejected", "job_url": "https://uber.com" },
  { "company_name": "Twitter", "job_title": "SRE", "status": "Applied", "job_url": "https://twitter.com" },
  { "company_name": "Slack", "job_title": "API Engineer", "status": "Offer", "job_url": "https://slack.com" },
  { "company_name": "Discord", "job_title": "Python Dev", "status": "Interviewing", "job_url": "https://discord.com" },
  { "company_name": "Twitch", "job_title": "Video Engineer", "status": "Applied", "job_url": "https://twitch.tv" },
  { "company_name": "Stripe", "job_title": "Payment Infra", "status": "Interviewing", "job_url": "https://stripe.com" },
  { "company_name": "Coinbase", "job_title": "Blockchain Dev", "status": "Rejected", "job_url": "https://coinbase.com" },
  { "company_name": "Robinhood", "job_title": "Backend Engineer", "status": "Applied", "job_url": "https://robinhood.com" },
  { "company_name": "Dropbox", "job_title": "Cloud Engineer", "status": "Applied", "job_url": "https://dropbox.com" },
  { "company_name": "Pinterest", "job_title": "ML Engineer", "status": "Rejected", "job_url": "https://pinterest.com" },
  { "company_name": "Reddit", "job_title": "Data Engineer", "status": "Applied", "job_url": "https://reddit.com" },
  { "company_name": "Zoom", "job_title": "VoIP Engineer", "status": "Interviewing", "job_url": "https://zoom.us" }
]

def run_simulation():
    print(f"Starting Bulk Upload for user: {target_user['username']}...")

    #Register (Skip if they already exist)
    print(f"... Checking registration for {target_user['username']}")
    reg_resp = requests.post(f"{BASE_URL}/register-user/", json=target_user)
    
    if reg_resp.status_code == 201:
        print("User created successfully.")
    elif "already exists" in reg_resp.text:
        print("User already exists. Proceeding to login.")
    else:
        print(f"Registration Warning: {reg_resp.text}")

    #Login to get Token
    resp = requests.post(f"{BASE_URL}/login/", json=target_user)
    if resp.status_code != 200:
        print(f"FATAL: Could not login {target_user['username']}")
        print(f"Server said: {resp.text}")
        return
    
    token = resp.json()['access']
    headers = {"Authorization": f"Bearer {token}"}
    print("Login Successful! Token acquired.")

    #Upload ALL 20 Jobs
    print(f"\nUploading {len(all_jobs)} jobs...")
    
    success_count = 0
    for job in all_jobs:
        # Add the required date
        job['application_date'] = "2025-12-16"
        
        r = requests.post(f"{BASE_URL}/jobs/", json=job, headers=headers)
        
        if r.status_code == 201:
            print(f" Added: {job['company_name']}")
            success_count += 1
        else:
            print(f"Failed: {job['company_name']} ({r.status_code})")
            print(f"Reason: {r.text}")

    print(f"\nDONE! Successfully uploaded {success_count}/{len(all_jobs)} jobs.")

if __name__ == "__main__":
    run_simulation()