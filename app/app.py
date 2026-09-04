import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "local")
COMMIT_SHA = os.getenv("COMMIT_SHA", "local")


@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Cloud Deployment Platform</title>

      <style>
        * {{
          box-sizing: border-box;
        }}

        body {{
          margin: 0;
          font-family: Arial, Helvetica, sans-serif;
          background:
            radial-gradient(circle at top right, #1e3a8a 0%, transparent 35%),
            linear-gradient(135deg, #0f172a, #020617);
          color: #e2e8f0;
          min-height: 100vh;
        }}

        .container {{
          width: min(1100px, 90%);
          margin: 0 auto;
          padding: 70px 0;
        }}

        .badge {{
          display: inline-block;
          padding: 8px 14px;
          border: 1px solid #334155;
          border-radius: 999px;
          background: rgba(15, 23, 42, 0.8);
          color: #38bdf8;
          font-size: 14px;
          margin-bottom: 24px;
        }}

        h1 {{
          font-size: clamp(42px, 7vw, 72px);
          line-height: 1;
          margin: 0;
          max-width: 850px;
        }}

        .highlight {{
          color: #38bdf8;
        }}

        .subtitle {{
          max-width: 700px;
          color: #94a3b8;
          font-size: 20px;
          line-height: 1.6;
          margin: 25px 0 45px;
        }}

        .status {{
          display: inline-flex;
          align-items: center;
          gap: 10px;
          padding: 10px 16px;
          border-radius: 10px;
          background: rgba(34, 197, 94, 0.1);
          border: 1px solid rgba(34, 197, 94, 0.35);
          color: #86efac;
          margin-bottom: 40px;
        }}

        .dot {{
          width: 10px;
          height: 10px;
          border-radius: 50%;
          background: #22c55e;
          box-shadow: 0 0 12px #22c55e;
        }}

        .grid {{
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
          gap: 18px;
        }}

        .card {{
          background: rgba(15, 23, 42, 0.75);
          border: 1px solid #1e293b;
          border-radius: 16px;
          padding: 24px;
          backdrop-filter: blur(8px);
        }}

        .card-title {{
          color: #94a3b8;
          font-size: 13px;
          text-transform: uppercase;
          letter-spacing: 1.5px;
          margin-bottom: 12px;
        }}

        .card-value {{
          font-size: 20px;
          font-weight: 700;
          word-break: break-word;
        }}

        .pipeline {{
          margin-top: 50px;
          padding: 26px;
          border-radius: 16px;
          border: 1px solid #1e293b;
          background: rgba(15, 23, 42, 0.55);
        }}

        .pipeline h2 {{
          margin-top: 0;
        }}

        .steps {{
          display: flex;
          gap: 12px;
          flex-wrap: wrap;
          color: #cbd5e1;
        }}

        .step {{
          padding: 10px 14px;
          background: #111827;
          border: 1px solid #334155;
          border-radius: 8px;
        }}

        .arrow {{
          display: flex;
          align-items: center;
          color: #38bdf8;
          font-weight: bold;
        }}

        footer {{
          margin-top: 50px;
          color: #64748b;
          font-size: 14px;
        }}
      </style>
    </head>

    <body>
      <main class="container">

        <div class="badge">
          AWS ECS Fargate • GitHub Actions • Terraform
        </div>

        <h1>
          Cloud Deployment
          <span class="highlight">Platform</span>
        </h1>

        <p class="subtitle">
          A containerized application deployed automatically to AWS ECS,
          through a secure CI/CD pipeline using GitHub Actions and AWS OIDC.
        </p>

        <div class="status">
          <span class="dot"></span>
          System is Healthy
        </div>

        <div class="grid">

          <div class="card">
            <div class="card-title">Environment</div>
            <div class="card-value">AWS ECS Fargate</div>
          </div>

          <div class="card">
            <div class="card-title">Application Version</div>
            <div class="card-value">{APP_VERSION}</div>
          </div>

          <div class="card">
            <div class="card-title">Commit</div>
            <div class="card-value">{COMMIT_SHA[:12]}</div>
          </div>

          <div class="card">
            <div class="card-title">Deployment</div>
            <div class="card-value">GitHub Actions</div>
          </div>

        </div>

        <section class="pipeline">
          <h2>Deployment Pipeline</h2>

          <div class="steps">
            <span class="step">GitHub</span>
            <span class="arrow">→</span>
            <span class="step">OIDC</span>
            <span class="arrow">→</span>
            <span class="step">Docker</span>
            <span class="arrow">→</span>
            <span class="step">Amazon ECR</span>
            <span class="arrow">→</span>
            <span class="step">ECS Fargate</span>
            <span class="arrow">→</span>
            <span class="step">ALB</span>
          </div>
        </section>

        <footer>
          Infrastructure provisioned with Terraform • Containers deployed automatically through CI/CD.
        </footer>

      </main>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        version=APP_VERSION
    )


@app.route("/api/version")
def version():
    return jsonify(
        version=APP_VERSION,
        commit=COMMIT_SHA
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)