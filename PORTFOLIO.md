# AI Defense Lab — Portfolio

**Student:** [Abati Moses]

**GitHub:** [XMoxez](https://github.com/XMoxez) 

**Hugging Face Space:** [[Your HF Space URL](https://huggingface.co/settings/account)]

**Completed:** [Date]

---

Fill in each section as you complete a level. Link directly to your commit diff so a recruiter can see exactly what you changed.

---

## Level 1 — MedVitals AI · Cloud Infrastructure Security
Project Overview
MedVitals AI is a healthcare AI application scenario focused on securing cloud infrastructure and protecting sensitive patient information stored in AWS services.

Security Problem
The project addressed the risk of excessive or incorrectly scoped AWS IAM permissions that could allow unauthorized access to patient documents stored in Amazon S3 and sensitive resources in Amazon RDS.

What I Did
I reviewed an AWS IAM policy to identify potential access-control weaknesses and assess whether the application's permissions followed the principle of least privilege.

What I Changed or Built
I worked on refining the IAM policy to restrict access to the required S3 and RDS resources. The objective was to ensure that the application received only the permissions necessary to perform its intended functions.

How I Verified the Result
I reviewed the policy's allowed actions and resource ARNs to identify mismatches between permissions and resources. Further validation would involve testing authorized and unauthorized access in a controlled AWS environment.

Security Impact
The project demonstrates how properly scoped IAM permissions can reduce the risk of unauthorized access to healthcare data, limit potential damage from compromised credentials, and strengthen cloud infrastructure security.

Key Security Lessons
- Apply least-privilege access controls.
- Separate S3 bucket-level permissions from object-level permissions.
- Restrict access to sensitive database resources.
- Validate IAM policies through controlled security testing.
- Protect patient information through layered cloud security controls.

**Problem:** [What was the vulnerability? What could an attacker do with it?]
What was the vulnerability?
The vulnerability was an improperly scoped AWS IAM policy that could grant excessive or incorrectly configured permissions to Amazon S3 and RDS resources, potentially exposing sensitive patient information.
What could an attacker do with it?
An attacker who compromised credentials associated with the policy could potentially access or list patient documents, discover database information, or attempt database connections, depending on the effective permissions and other security controls in place.

**Method:** [How did you find it and what did you do to fix it?]
I found the vulnerability by reviewing the AWS IAM policy and identifying mismatches between the permitted actions and resource ARNs. I worked on correcting the resource scopes by separating S3 bucket-level and object-level permissions and ensuring RDS connection permissions were properly scoped, following the principle of least privilege.

**Evidence:** [Link to your GitHub commit diff showing the patch]

**Outcome:** [What changed as a result? What is more secure now and why does it matter to the business?]
The IAM policy was refined to better restrict access to the required S3 and RDS resources, reducing the risk of unauthorized access to sensitive patient data. This strengthens cloud security by limiting the potential damage from compromised credentials. For the business, it helps protect patient confidentiality, reduce the risk of data breaches, support regulatory compliance, and maintain patient trust.

**Skills:** CloudTrail Log Forensics · IAM Least Privilege · Secrets Management · Incident Timeline Reporting

**Others:**
- [Technical write-up link e.g. Medium blog post]
- Level 1 Complete: HealthTech MedVitals AI Defense Lab

Today marks another milestone in my cybersecurity journey.

I successfully completed the Level 1 HealthTech MedVitals AI, Cloud Infrastructure Security – AI Defense Lab.

Step by step, I:
✅ Identified security weaknesses.
✅ Fixed hard-coded credentials.
✅ Applied least-privilege IAM permissions.
✅ Improved secrets governance.
✅ Committed my security fixes to GitHub.

Along the way, I also learned that solving technical challenges isn't always the hardest part. Sometimes, navigating unexpected platform issues tests your patience just as much. Despite completing my work, I encountered a submission issue with the lab interface. It was a reminder that persistence is part of every learning journey.

Each lab is helping me think more like a defender—analyzing risks, securing cloud infrastructure, and building practical skills that go beyond theory.

I'm grateful for the opportunity to keep growing through hands-on experience and real-world security scenarios.

Now, I'm excited for the next challenge:
🚀 Level 2: BioTech DataForge ML – AI Model Security

The journey continues, one secure system at a time.

This is a win-win to myself and HerNetIq Damilola Aibinuola supper glad we made it.

#CyberSecurity #CloudSecurity #AISecurity #IAM #GitHub #HealthTech #BioTech #MachineLearning #HerNetIQ #ContinuousLearning #BuildInPublic

- [LinkedIn post link]
- https://lnkd.in/p/eRuc4CWm
- 
- [Any other documentation, video walkthrough, or public content]

---

## Level 2 — DataForge ML · AI Model Security
Project Overview
DataForge ML focuses on AI Model Security, examining how machine learning models can be exposed to security risks throughout their lifecycle, from downloading and loading models to deploying them in production.

Security Problem
The key challenge was understanding how malicious or tampered machine learning models, unsafe model files, and untrusted model sources could compromise an AI application. A model file may contain more than learned parameters; certain formats can execute malicious code when loaded unsafely.

What I Worked On
I explored AI model security risks, including malicious model artifacts, unsafe deserialization, model integrity, and the importance of verifying model sources before use. I focused on safer model-loading practices, trusted sources, file integrity checks, and secure model formats such as Safetensors.

Security Impact
The objective was to reduce the risk of malicious code execution, unauthorized model modification, and compromise of the ML pipeline. These controls help protect the application, its data, and the infrastructure supporting the model.

Key Lesson
AI security does not stop at protecting prompts and APIs. The model itself is part of the attack surface and must be treated as an untrusted asset until its source, integrity, and loading behavior have been verified.

**Problem:**
The problem I was solving was the risk of malicious or tampered machine learning models entering the AI development pipeline. Loading models from untrusted sources or using unsafe serialization formats can expose systems to remote code execution, data theft, and infrastructure compromise. Without proper model integrity verification, trusted-source validation, and secure loading practices, an attacker could introduce a malicious model artifact and compromise the application or its underlying environment. My focus was understanding these risks and identifying security controls to make the machine learning pipeline safer.

**Method:**
I approached the DataForge ML challenge by examining how machine learning models were sourced, stored, and loaded into the application. I focused on identifying risks associated with untrusted model files, unsafe deserialization, and model tampering. I investigated safer alternatives, including using the Safetensors format, verifying model integrity with cryptographic hashes, validating trusted model sources, and restricting unsafe loading operations. My approach was to identify potential attack paths, apply appropriate security controls, and verify that the controls reduced the risk of malicious code execution and unauthorized model modification.

**Evidence:** [Link to commit]

**Outcome:**
The assessment improved my understanding of how malicious or tampered model files can threaten an AI system. By focusing on trusted model sources, model integrity verification, and safer model-loading practices, I identified controls that can reduce the risk of code execution, data exposure, and ML pipeline compromise. The key outcome was recognizing that AI models must be treated as potential security risks until their origin and integrity are verified. This strengthens the security of the machine learning pipeline and helps protect sensitive data, application availability, and business operations.

**Skills:** Model Supply Chain Verification · Pickle Exploit Detection · Safetensors · Automated Model Scanning

**Others:**
- [Technical write-up link]
- Lab Level 2 - DataForge ML Model Security Assessment on AI Defense Lab successful completed! HerNetIQ 👍

The lab was easier than I thought, was not surprised, my instructor Damilola Aibinuola told me to apply the walkthrough deligently and that was it.

Running Picklescan and seeing the result felt both surprising and concerning. It showed me how easily a seemingly normal AI model can contain hidden security risks that may not be obvious from its intended purpose.

The experience made the importance of scanning and validating machine-learning models before deployment very real to me.

The fact that this model was already running in healthcare pipelines before anyone scanned it means a potentially vulnerable component had entered a sensitive environment without proper security verification. In healthcare, where AI systems may process confidential patient information, this creates serious risks. It highlights why model security must be part of the development and deployment process.

#HerNetIq #AiSecurity #BuildInPublic 

- [LinkedIn post link]
- https://lnkd.in/p/eEqKDN-Z

---

## Level 3 — CartBot AI · Application & API Security
Project Overview
CartBot AI is an AI-powered shopping application security project focused on identifying and addressing vulnerabilities in application logic and API endpoints. The project explores how weaknesses in authentication, authorization, input validation, and access control can expose customer information and compromise shopping transactions.
The primary focus is Broken Object-Level Authorization (BOLA), a vulnerability that can occur when an application fails to verify whether a user is authorized to access a specific resource. An attacker could potentially manipulate an API request to access another customer's shopping cart or order information.
The project involves examining API request handling, identifying authorization weaknesses, and applying security controls at the server side. It also emphasizes validating user permissions for every sensitive operation and ensuring that users can access only the resources they are authorized to use.
The goal is to strengthen application security, protect customer data, prevent unauthorized access, and improve the reliability of AI-powered shopping systems.

**Problem:**
CartBot AI focuses on securing an AI-powered shopping application against application-layer and API security vulnerabilities. The key risks include broken object-level authorization (BOLA), improper input validation, and insufficient access controls. An attacker could potentially manipulate API requests to access another customer's cart, view unauthorized order information, or modify shopping data. If the server does not properly verify user permissions, attackers may exploit these weaknesses to compromise customer privacy and transaction integrity.
CartBot AI’s customer-facing API trusted a client-supplied customer_id header with no cryptographic verification.

**Method:**
The Method: What Did I Change or Build?
I examined how CartBot AI handles API requests, authenticates users, and authorizes access to shopping carts and customer records. I focused on identifying weaknesses in object-level authorization and input validation. I worked on strengthening server-side access controls so that each authenticated user could access only the resources they were authorized to use. I also considered how to validate incoming requests, restrict unauthorized operations, and ensure that security checks were enforced beyond the application interface.

**Evidence:** [Link to commit]
https://github.com/XMoxez/ai-security-defense-lab

**Outcome:**
The assessment helped establish a stronger approach to protecting customer data and shopping transactions. By focusing on server-side authorization and API request validation, I learned how to reduce the risk of unauthorized cart access, customer data exposure, and transaction manipulation. The key lesson was that hiding information in the user interface is not enough; the server must independently verify every sensitive request. This is important for businesses because effective application and API security protects customer trust, data confidentiality, and the integrity of online transactions.

**Skills:** AI API Hardening · Rate Limiting · Output Filtering · OWASP LLM Top 10 · Direct Prompt Injection Defence

**Others:**
- [Technical write-up link]
- Congratulations, Level 3 of the AI Defense Lab successful completed.

Reading an API configuration file, identifying the broken auth pattern, and tracing how a missing check at the API layer becomes exploitable through an AI interface. - API threat modelling 

Was able to triggered a real injection payload hidden in untrusted content and understood why filtering the AI 's prompts can never fully close this gap on it own. - Indirect prompt injection 

I demonstrated the flaw manually, then watched a scripted version drain multiple records within a second, connecting a single-record vulnerability to its real business impact. - BOLA at both scales

Also mapped my findings to API1:2023, AML.T0051, and AML.T0054, the standardized language security teams, auditors, and hiring managers uses. - OWASP &MITRE ATLAS classification 

Finally, Implemented JWT validation and rate limiting as well as explaining why securing the API layer holds even when the AI layer is successful manipulated. - Defence-in-depth architecture 

This is a documented, and a verifiable skill. The GitHub commit is my evidence. - https://lnkd.in/eUmSX4RK

The journey wouldn't have been possible, without the guide of my instructor Damilola Aibinuola of HerNetIQ 

#AISecurity #BuildInPublic #HerNetIq

- [LinkedIn post link]
- https://lnkd.in/p/eEZxTi2v

---

## Level 4 — PayGuard · Data Security in AI

**Problem:** PayGuard’s RAG-powered AI advisory assistant retrieved documents from a shared vector database with no per-tenant access enforcement — a client-supplied tenant_id to gain access but needs verification.

**Method:** Audited rag_config.py and identified TRUST_CLIENT_TENANT_ID = True and METADATA_FILTER_ENFORCED = False. Triggered cross-tenant retrieval by spoofing the tenant_id field, then trigger cross-tenant trivial. 

**Evidence:** [Link to commit]https://glowing-xylophone-6vvqj976w574hqxx.github.dev/

**Outcome:** Cross-tenant retrieval is no longer possible at the application layer or the database layer — even a future code change that forgets to check tenant_id cannot bypass the platform.

**Skills:** STRIDE Threat Modeling · RAG Pipeline Security · Multi-Tenant Data Isolation · Indirect Prompt Injection Defence. RAG security · Vector database access control · OWASP LLM Top 10 (LLM09, LLM05) · STRIDE threat modeling · Airflow pipeline security · Database-level authorization design · Semgrep static analysis.

**Others:**
- [Technical write-up link]
- Two vulnerabilities. One root cause. What happens when the same security mistake appears at two different layers of the same system?

The Level 4 of AI Security Defense Lab fulfilled, during this process, I assessed a simulated multi-tenant RAG system and discovered a critical weakness: tenant isolation depended too heavily on application-level checks.

By changing a client-supplied "tenant_id", I demonstrated cross-tenant retrieval because the vector store did not enforce tenant filtering.

And seriously, that was a part of the investigation.
I also examined embedding inversion, fine-tuning data poisoning, model backdoors, query abuse, and security gaps in an Airflow fine-tuning pipeline.

My takeaway was - Different vulnerabilities can share the same root cause: trusting one layer to enforce a security boundary that should be protected across the system.

When application code fails to validate access and the database or vector store does not independently enforce tenant isolation, sensitive information becomes exposed.

My remediation focused on strengthening isolation at the database/vector-store layer, ensuring unauthorized access is blocked even if application-level checks fail.
I documented my findings using STRIDE, OWASP LLM Top 10 (LLM09/LLM05), and Semgrep.

The lesson: Security is not just about fixing individual vulnerabilities. It is about identifying the underlying design weakness and building defenses that remain effective when another layer fails. Damilola Aibinuola HerNetIQ 

As AI systems become more complex, defense in depth must be a design principle, not an afterthought.
#AISecurity #Cybersecurity #RAGSecurity #BuildInPublic

- [LinkedIn post link]
- https://lnkd.in/p/evehNqrP

---

## Level 5 — LegalBot Municipal · Agentic AI Security

**Problem:**
LegalBot had architectural weaknesses that could allow an AI agent to perform sensitive actions without sufficient restrictions or human approval. Standing authority increased the risk of unauthorized actions, while untrusted citizen input could potentially manipulate the agent. Without proper audit logging, investigating agent activities would also be difficult.

**Method:**
I reviewed the LegalBot configuration and implemented security improvements by removing unnecessary standing authority, treating citizen input as untrusted data, introducing human approval for sensitive actions, and enabling audit logging. I then tested the updated system to verify that sensitive actions could not execute directly without approval. Finally, I mapped the security controls to the MAESTRO framework and the NIST AI Risk Management Framework (AI RMF).

**Evidence:** [Link to commit]

**Outcome:**
The remediation established stronger authorization boundaries, added human oversight for sensitive actions, and improved accountability through audit logging. Verification focused on demonstrating that restricted actions were blocked pending approval. The MAESTRO and NIST AI RMF mappings connected the technical improvements to broader AI risk management practices.

**Skills:** Excessive Agency Mitigation · Llama Guard Integration · Pydantic Schema Enforcement · Autonomous Agent Containment

**Others:**
- [Technical write-up link]
- ✅AI Defense Lab Level 5 Completed: LegalBot AI Security Remediation

Another milestone in my AI Security journey!
In Level 5 of the HerNetIq AI Security Fellowship, I worked on strengthening LegalBot by addressing architectural weaknesses and implementing meaningful security controls.

My focus was on:
🔐 Removing unnecessary standing authority.
🛡️ Treating citizen input as untrusted data.
👤 Introducing human approval for sensitive actions.
📝 Implementing audit logging for agent activities.
🧪 Verifying that sensitive actions could not execute directly without proper approval.
I also mapped the remediation to the MAESTRO framework and the NIST AI Risk Management Framework (AI RMF), connecting technical fixes to broader AI risk management practices.

My biggest takeaway: Securing an AI agent is not just about what it can do, but also about what it is allowed to do, when it can act, and who must approve its actions.
On this challenge, my tutors where Damilola Aibinuola & Faith Ashiedu ! 🚀

#AISecurity #Cybersecurity #AgenticAI #NIST #MAESTRO #BuildInPublic

- [LinkedIn post link]
- https://lnkd.in/p/eADZ3qFg
