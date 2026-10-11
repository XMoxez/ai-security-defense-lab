# AI Defense Lab — Portfolio

**Student:** [Abati Moses]

**GitHub:** [XMoxez]

**Hugging Face Space:** [[Your HF Space URL](https://huggingface.co/settings/account)]

**Completed:** [Date]

---

Fill in each section as you complete a level. Link directly to your commit diff so a recruiter can see exactly what you changed.

---

## Level 1 — MedVitals AI · Cloud Infrastructure Security

**Problem:** [What was the vulnerability? What could an attacker do with it?]

**Method:** [How did you find it and what did you do to fix it?]

**Evidence:** [Link to your GitHub commit diff showing the patch]

**Outcome:** [What changed as a result? What is more secure now and why does it matter to the business?]

**Skills:** CloudTrail Log Forensics · IAM Least Privilege · Secrets Management · Incident Timeline Reporting

**Others:**
- [Technical write-up link e.g. Medium blog post]
- [LinkedIn post link]
- [Any other documentation, video walkthrough, or public content]

---

## Level 2 — DataForge ML · AI Model Security

**Problem:**

**Method:**

**Evidence:** [Link to commit]

**Outcome:**

**Skills:** Model Supply Chain Verification · Pickle Exploit Detection · Safetensors · Automated Model Scanning

**Others:**
- [Technical write-up link]
- [LinkedIn post link]

---

## Level 3 — CartBot AI · Application & API Security

**Problem:**
CartBot AI’s customer-facing API trusted a client-supplied customer_id header with no cryptographic verification
**Method:**
Audited api_config.py and identified TRUST_CUSTOMER_ID_HEADER = True, REQUIRE_JWT_VALIDATION = False, and RATE_LIMIT_ENABLED = False. Queried the CartBot AI assistant
**Evidence:** [Link to commit]
https://github.com/XMoxez/ai-security-defense-lab
**Outcome:**
The API can no longer be BOLA’d via header spoofing — any mismatched or missing JWT
**Skills:** AI API Hardening · Rate Limiting · Output Filtering · OWASP LLM Top 10 · Direct Prompt Injection Defence

**Others:**
- [Technical write-up link]
- [LinkedIn post link]

---

## Level 4 — PayGuard · Data Security in AI

**Problem:** PayGuard’s RAG-powered AI advisory assistant retrieved documents from a shared vector database with no per-tenant access enforcement — a client-supplied tenant_id to gain access but needs verification.

**Method:** Audited rag_config.py and identified TRUST_CLIENT_TENANT_ID = True and METADATA_FILTER_ENFORCED = False. Triggered cross-tenant retrieval by spoofing the tenant_id field, then trigger cross-tenant trivial. 

**Evidence:** [Link to commit]https://glowing-xylophone-6vvqj976w574hqxx.github.dev/

**Outcome:** Cross-tenant retrieval is no longer possible at the application layer or the database layer — even a future code change that forgets to check tenant_id cannot bypass the platform.

**Skills:** STRIDE Threat Modeling · RAG Pipeline Security · Multi-Tenant Data Isolation · Indirect Prompt Injection Defence. RAG security · Vector database access control · OWASP LLM Top 10 (LLM09, LLM05) · STRIDE threat modeling · Airflow pipeline security · Database-level authorization design · Semgrep static analysis.

**Others:**
- [Technical write-up link]
- [LinkedIn post link]

---

## Level 5 — LegalBot Municipal · Agentic AI Security

**Problem:**

**Method:**

**Evidence:** [Link to commit]

**Outcome:**

**Skills:** Excessive Agency Mitigation · Llama Guard Integration · Pydantic Schema Enforcement · Autonomous Agent Containment

**Others:**
- [Technical write-up link]
- [LinkedIn post link]
