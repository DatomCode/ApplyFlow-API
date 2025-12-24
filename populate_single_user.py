import requests

BASE_URL = "http://127.0.0.1:8003" 

#THE TARGET USER (Who gets all the jobs?)
target_user = {
    "username": "ApplyFlow-Admin", 
    "password": "damilare007", 
    "email": "applyflowadmin@gmail.com", 
    "first_name": "apply", 
    "last_name": "flow"
}

# 2. THE DATA (48 Jobs)
all_jobs = [
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
  { "company_name": "Zoom", "job_title": "VoIP Engineer", "status": "Interviewing", "job_url": "https://zoom.us" },

#New 28 jobs data

  { "company_name": "Adobe", "job_title": "UX Engineer", "status": "Applied", "job_url": "https://adobe.com/careers" },
  { "company_name": "Salesforce", "job_title": "CRM Developer", "status": "Interviewing", "job_url": "https://salesforce.com/jobs" },
  { "company_name": "Oracle", "job_title": "Database Admin", "status": "Rejected", "job_url": "https://oracle.com/careers" },
  { "company_name": "IBM", "job_title": "Cloud Consultant", "status": "Applied", "job_url": "https://ibm.com/jobs" },
  { "company_name": "Intel", "job_title": "Hardware Engineer", "status": "Offer", "job_url": "https://intel.com/jobs" },
  { "company_name": "AMD", "job_title": "Chip Architect", "status": "Applied", "job_url": "https://amd.com/careers" },
  { "company_name": "Nvidia", "job_title": "AI Researcher", "status": "Interviewing", "job_url": "https://nvidia.com/careers" },
  { "company_name": "SpaceX", "job_title": "Flight Software Eng", "status": "Applied", "job_url": "https://spacex.com/careers" },
  { "company_name": "Blue Origin", "job_title": "Propulsion Engineer", "status": "Rejected", "job_url": "https://blueorigin.com" },
  { "company_name": "NASA", "job_title": "Data Scientist", "status": "Applied", "job_url": "https://nasa.gov/careers" },
  { "company_name": "Goldman Sachs", "job_title": "Quant Analyst", "status": "Interviewing", "job_url": "https://goldmansachs.com" },
  { "company_name": "JP Morgan", "job_title": "Java Developer", "status": "Offer", "job_url": "https://jpmorgan.com/careers" },
  { "company_name": "Morgan Stanley", "job_title": "Cyber Security", "status": "Applied", "job_url": "https://morganstanley.com" },
  { "company_name": "Bank of America", "job_title": "Full Stack Dev", "status": "Rejected", "job_url": "https://bankofamerica.com" },
  { "company_name": "Citi", "job_title": "DevOps Engineer", "status": "Applied", "job_url": "https://citi.com/careers" },
  { "company_name": "Wells Fargo", "job_title": "System Admin", "status": "Interviewing", "job_url": "https://wellsfargo.com" },
  { "company_name": "Visa", "job_title": "Payment Engineer", "status": "Applied", "job_url": "https://visa.com/careers" },
  { "company_name": "Mastercard", "job_title": "Blockchain Lead", "status": "Offer", "job_url": "https://mastercard.com" },
  { "company_name": "PayPal", "job_title": "iOS Developer", "status": "Applied", "job_url": "https://paypal.com/jobs" },
  { "company_name": "Square", "job_title": "Android Developer", "status": "Interviewing", "job_url": "https://squareup.com" },
  { "company_name": "Shopify", "job_title": "Ruby Developer", "status": "Applied", "job_url": "https://shopify.com/careers" },
  { "company_name": "Atlassian", "job_title": "Jira Admin", "status": "Rejected", "job_url": "https://atlassian.com" },
  { "company_name": "Asana", "job_title": "Frontend Engineer", "status": "Applied", "job_url": "https://asana.com/jobs" },
  { "company_name": "Trello", "job_title": "Backend Engineer", "status": "Applied", "job_url": "https://trello.com/jobs" },
  { "company_name": "Notion", "job_title": "Full Stack Lead", "status": "Interviewing", "job_url": "https://notion.so/jobs" },
  { "company_name": "Linear", "job_title": "React Developer", "status": "Offer", "job_url": "https://linear.app/careers" },
  { "company_name": "Vercel", "job_title": "Next.js Engineer", "status": "Applied", "job_url": "https://vercel.com/careers" },
  { "company_name": "Heroku", "job_title": "Platform Engineer", "status": "Rejected", "job_url": "https://heroku.com/careers" },
]

def run_simulation():
    print(f"Starting Bulk Upload for user: {target_user['username']}...")

    #Register (Skip if they already exist)
    print(f"... Checking registration for {target_user['username']}")
    reg_resp = requests.post(f"{BASE_URL}/api/auth/register/", json=target_user)
    
    if reg_resp.status_code == 201:
        print("User created successfully.")
    elif "already exists" in reg_resp.text:
        print("User already exists. Proceeding to login.")
    else:
        print(f"Registration Warning: {reg_resp.text}")

    #Login to get Token
    resp = requests.post(f"{BASE_URL}/api/auth/login/", json=target_user)
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
        
        r = requests.post(f"{BASE_URL}/api/jobs/", json=job, headers=headers)
        
        if r.status_code == 201:
            print(f" Added: {job['company_name']}")
            success_count += 1
        else:
            print(f"Failed: {job['company_name']} ({r.status_code})")
            print(f"Reason: {r.text}")

    print(f"\nDONE! Successfully uploaded {success_count}/{len(all_jobs)} jobs.")

if __name__ == "__main__":
    run_simulation()