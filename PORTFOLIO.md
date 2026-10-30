AI Defense Lab — Portfolio

Student: Abati Moses Oluwaseyi 
GitHub: XMoxez
Hugging Face Space: [Insert Hugging Face Space link]
Completed: 21 October 2026

---

Level 1 — MedVitals AI: Cloud Infrastructure Security

1. Scenario / Investigation

MedVitals AI is a simulated healthcare application that uses AWS services to store and manage sensitive patient information. My task was to assess its cloud security configuration, focusing on how the application's permissions controlled access to patient documents in Amazon S3 and resources in Amazon RDS.

2. Problem / Vulnerability

I identified weaknesses in the AWS IAM policy, particularly permissions that were excessively or incorrectly scoped. If an attacker gained access to credentials associated with the policy, they could potentially access patient documents, list stored information, or attempt unauthorized database connections, depending on the effective permissions and other security controls.

3. Evidence

- IAM policy assessment and permission review: [Insert evidence link]
- Supporting screenshots or relevant configuration evidence: [Insert screenshot or file link]
- Relevant GitHub code and changes: [Insert link if separate from the commit below]

4. Remediation

I worked on refining the IAM permissions to follow the principle of least privilege. This involved separating S3 bucket-level permissions from object-level permissions and reviewing the resource scopes for the required S3 and RDS actions. The objective was to ensure that the application could access only the resources necessary for its intended functions.

5. Commit

"GitHub commit diff — Level 1" (https://github.com/XMoxez/ai-security-defense-lab/commit/7b008788c864946c7cbfe7ade1baf3fb07394da3)

6. Outcome

The assessment and permission changes strengthened the approach to controlling access to healthcare data. Properly scoped IAM permissions reduce the risk of unauthorized access and limit the potential damage if application credentials are compromised. This matters because protecting patient information supports confidentiality, business continuity, regulatory responsibilities, and patient trust.

7. Skills Demonstrated

- AWS IAM Policy Analysis
- IAM Least Privilege
- Amazon S3 Access Control
- Amazon RDS Permission Scoping
- Cloud Security Assessment
- Security Configuration Review

8. Supporting Artifacts

- Technical documentation: [Insert link]
- Supporting screenshots or architecture diagram: [Insert link]
- Lab walkthrough: [Insert link, if available]

9. LinkedIn Case Study

[Insert Level 1 LinkedIn post link or combined Levels 1–3 case study link]

---

Level 2 — DataForge ML: AI Model Security

1. Scenario / Investigation

DataForge ML is a simulated machine-learning environment used to examine security risks affecting AI models and their development pipeline. My investigation focused on how models were obtained, stored, and loaded, particularly the risks associated with untrusted model sources and unsafe serialization formats.

2. Problem / Vulnerability

The main security concern was the possibility of malicious or tampered model files entering the machine-learning pipeline. Unsafe deserialization, especially when loading untrusted pickle files, can expose an application to malicious code execution. Without verifying the source and integrity of a model, an attacker could introduce a harmful model artifact and potentially compromise the application or its supporting infrastructure.

3. Evidence

- Model security assessment and scanning evidence: [Insert evidence link]
- Picklescan results or relevant screenshots: [Insert screenshot or file link]
- Supporting model source or configuration evidence: [Insert link, if available]

4. Remediation

I focused on safer model-loading practices and stronger model supply-chain verification. The security measures I worked with included using safer formats such as Safetensors, checking model integrity through cryptographic hashes, validating trusted model sources, and identifying unsafe loading operations. These controls help reduce the risk of malicious model files entering the pipeline.

5. Commit

"GitHub commit diff — Level 2" (https://github.com/XMoxez/ai-security-defense-lab/commit/16650b78b485ff3c3ee115e91ea689f9edc266b8)

6. Outcome

This investigation strengthened my understanding of how model files can become an attack surface. It demonstrated why AI models should not automatically be trusted simply because they are available for download or appear to serve a legitimate purpose. Source validation, integrity checks, and safer loading practices help reduce the risk of code execution, data exposure, and machine-learning pipeline compromise.

7. Skills Demonstrated

- AI Model Supply Chain Security
- Model Source Verification
- Pickle Exploit Detection
- Safetensors
- Model Integrity Verification
- Machine-Learning Pipeline Security

8. Supporting Artifacts

- Model security assessment: [Insert technical write-up link]
- Picklescan output or screenshots: [Insert link]
- Supporting documentation or walkthrough: [Insert link, if available]

9. LinkedIn Case Study

[Insert Level 2 LinkedIn post link or combined Levels 1–3 case study link]

---

Level 3 — CartBot AI: Application & API Security

1. Scenario / Investigation

CartBot AI is a simulated AI-powered shopping application. My investigation focused on its API security, especially how the application authenticated users and controlled access to shopping carts and customer order information. I examined how API requests were handled and whether the server properly verified a user's authority before allowing access to sensitive records.

2. Problem / Vulnerability

I identified a Broken Object-Level Authorization (BOLA) risk. The application's customer-facing API trusted a client-supplied "customer_id" header without cryptographic verification. This could allow an attacker to manipulate a request and attempt to access another customer's cart or order information. The weakness could expose customer data and compromise the integrity of shopping transactions.

3. Evidence

- API authorization assessment: [Insert evidence link]
- Relevant screenshots showing the vulnerability or test results: [Insert screenshot or file link]
- Supporting API request or response evidence: [Insert link, if available]

4. Remediation

I worked on strengthening the API's server-side security controls. My approach focused on introducing JWT validation, improving authorization checks, and applying rate limiting. The purpose was to ensure that the server independently verifies a user's identity and permissions instead of trusting a customer identifier supplied by the client.

5. Commit

"GitHub commit diff — Level 3" (https://github.com/XMoxez/ai-security-defense-lab/commit/6f84dc75c7f5ad85c41f89d9af044cb4c1a42aea)

6. Outcome

The investigation demonstrated why API authorization must be enforced at the server side. A user interface alone cannot protect customer records if the API accepts unverified identifiers. Strengthening authentication, authorization, and request controls helps reduce unauthorized access, protect customer privacy, and maintain the integrity of online transactions.

7. Skills Demonstrated

- Application Security Testing
- API Security Assessment
- Broken Object-Level Authorization (BOLA)
- JWT Authentication and Validation
- API Rate Limiting
- Indirect Prompt Injection Analysis
- OWASP API Security
- MITRE ATLAS Mapping

8. Supporting Artifacts

- API security technical write-up: [Insert link]
- Screenshots or API testing evidence: [Insert link]
- Lab walkthrough or supporting documentation: [Insert link, if available]

9. LinkedIn Case Study

[Insert Level 3 LinkedIn post link or combined Levels 1–3 case study link]

---

Portfolio Repository

AI Defense Lab Repository: [Insert repository link]

Portfolio File: [Insert direct PORTFOLIO.md link]

Combined Levels 1–3 LinkedIn Case Study: [Insert published LinkedIn post link]
