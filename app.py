from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
JOBS = [
    {"id": "qa-engineer", "title": "QA Engineer", "salary": "4.5–4.8 LPA",
     "experience": "Fresher", "description": "Test web workflows, report defects, and maintain browser automation."},
    {"id": "junior-systems", "title": "Junior Systems Specialist", "salary": "4.0–5.0 LPA",
     "experience": "0–1 years", "description": "Support internal systems and troubleshoot common issues."},
]
applications = []

BASE = '''
<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{{ title }}</title>
<style>body{font:16px/1.5 Arial,sans-serif;max-width:850px;margin:2rem auto;padding:0 1rem;color:#222}
.job{border:1px solid #ddd;border-radius:8px;padding:1rem;margin:1rem 0}
label{display:block;margin:.8rem 0 .25rem}input{width:100%;box-sizing:border-box;padding:.65rem}
button{margin-top:1rem;padding:.7rem 1rem;cursor:pointer}.error{color:#a11}.success{color:#176b36}.meta{color:#555}</style>
</head><body><header><a href="/">Crew Logocrew | Careers</a></header>{{ body|safe }}</body></html>
'''

def page(title, body):
    return render_template_string(BASE, title=title, body=body)

@app.get("/")
def index():
    body = "<h1>Open roles</h1><p>Browse current opportunities.</p>"
    for job in JOBS:
        body += (f'<section class="job" data-job-id="{job["id"]}"><h2>{job["title"]}</h2>'
                 f'<p class="meta">Salary: {job["salary"]} · Experience: {job["experience"]}</p>'
                 f'<p>{job["description"]}</p><a href="/jobs/{job["id"]}">View role</a></section>')
    return page("Open roles", body)

@app.get("/jobs/<job_id>")
def detail(job_id):
    job = next((j for j in JOBS if j["id"] == job_id), None)
    if not job:
        return page("Not found", "<h1>Job not found</h1>"), 404
    body = (f'<h1>{job["title"]}</h1><p>Salary: {job["salary"]}</p>'
            f'<p>Experience: {job["experience"]}</p><p>{job["description"]}</p>'
            f'<a href="/apply/{job["id"]}">Apply for this role</a>')
    return page(job["title"], body)

def form_body(job, error=""):
    err = f'<p class="error" role="alert">{error}</p>' if error else ""
    return (f'<h1>Apply: {job["title"]}</h1>{err}<form method="post">'
            '<label for="name">Full name</label><input id="name" name="name" required>'
            '<label for="email">Email address</label><input id="email" name="email" type="email" required>'
            '<button type="submit">Submit application</button></form>')

@app.route("/apply/<job_id>", methods=["GET", "POST"])
def apply(job_id):
    job = next((j for j in JOBS if j["id"] == job_id), None)
    if not job:
        return page("Not found", "<h1>Job not found</h1>"), 404
    if request.method == "POST":
        name, email = request.form.get("name", ""), request.form.get("email", "")
        if not name.strip() or not email.strip():
            return page("Apply", form_body(job, "Name and email are required.")), 400
        if "@" not in email or "." not in email.split("@")[-1]:
            return page("Apply", form_body(job, "Enter a valid email address.")), 400
        key = (job_id, email.strip().lower())
        if any((a["job_id"], a["email"].lower()) == key for a in applications):
            return page("Apply", form_body(job, "An application already exists for this email and role.")), 409
        applications.append({"job_id": job_id, "name": name.strip(), "email": email.strip()})
        return page("Application received",
                    f'<h1>Application received</h1><p class="success" role="status">Thanks, {name.strip()}. Your application was recorded locally.</p><a href="/">Back to roles</a>')
    return page("Apply", form_body(job))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")), debug=False)\n