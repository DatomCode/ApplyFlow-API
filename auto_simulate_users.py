import requests

BASE_URL = "http://127.0.0.1:8003"

# The Jobs Data
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

# Dummy Users
users_to_create = [
    {
        "username": "dev_alice", 
        "password": "password123", 
        "email": "alice@example.com", 
        "first_name": "Alice", 
        "last_name": "Wonderland"
    },
    {
        "username": "dev_bob", 
        "password": "password123", 
        "email": "bob@example.com", 
        "first_name": "Bob", 
        "last_name": "Builder"
    },
    {
        "username": "dev_charlie", 
        "password": "password123", 
        "email": "charlie@example.com", 
        "first_name": "Charlie", 
        "last_name": "Chaplin"
    },
    {
        "username": "dev_david", 
        "password": "password123", 
        "email": "david@example.com", 
        "first_name": "David", 
        "last_name": "Beckham"
    },
    {
        "username": "dev_eve", 
        "password": "password123", 
        "email": "eve@example.com", 
        "first_name": "Eve", 
        "last_name": "Polastri"
    },
]

def run_simulation():
    print("Starting Multi-User Simulation...")

    #distribute jobs in chunks of 4
    # User 1 gets jobs 0-4, User 2 gets 4-8, etc.
    job_index = 0
    jobs_per_user = 4

    for user in users_to_create:
        print(f"\n Processing User: {user['username']}...")

        #Register Dummy User (Try to create, ignore if already exists)
        print(f"Attempting to register {user['username']}")
        reg_resp = requests.post(f"{BASE_URL}/register-user", json=user)
        
        #DEBUG: If registration fails, tell us why
        if reg_resp.status_code != 201 and "already exists" not in reg_resp.text:
            print(f"REGISTRATION ERROR: {reg_resp.text}")
        #Login to get THEIR unique token
        resp = requests.post(f"{BASE_URL}/login/", json=user)
        if resp.status_code != 200:
            print(f"Could not login {user['username']}")
            continue
        
        token = resp.json()['access']
        headers = {"Authorization": f"Bearer {token}"}

        #Assign to them their 4 jobs
        my_jobs = all_jobs[job_index : job_index + jobs_per_user]
        
        for job in my_jobs:
            job['application_date'] = "2025-12-16"
            r = requests.post(f"{BASE_URL}/jobs/", json=job, headers=headers)
            if r.status_code == 201:
                print(f"Added job: {job['company_name']}")
            else:
                # DEBUB and PRINT THE ACTUAL ERROR MESSAGE FROM THE SERVER
                print(f"Failed: {job['company_name']} - Status: {r.status_code}")
                print(f"Error: {r.text}")

        # Move the index forward for the next user
        job_index += jobs_per_user

    print("\nSimulation Complete! 5 Users created, 20 Jobs distributed.")

if __name__ == "__main__":
    run_simulation()