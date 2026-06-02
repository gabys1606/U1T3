"""
data.py - Conference data store for Google Cloud Summit 2026
"""

EVENT = {
    "name": "Google Cloud Summit 2026",
    "tagline": "Build Smarter. Scale Faster. Go Further.",
    "date": "Tuesday, June 2, 2026",
    "location": "Moscone Center West, San Francisco, CA",
    "address": "800 Howard St, San Francisco, CA 94103",
    "venue_map_url": "https://maps.google.com/?q=Moscone+Center+West+San+Francisco",
    "registration_email": "register@gcloudsummit2026.io",
}

SPEAKERS = [
    {
        "id": "sp1",
        "first_name": "Priya",
        "last_name": "Nambiar",
        "title": "Principal Cloud Architect",
        "company": "Google Cloud",
        "linkedin": "https://www.linkedin.com/in/priyanambiar",
        "avatar_initials": "PN",
        "avatar_color": "#4285F4",
    },
    {
        "id": "sp2",
        "first_name": "Marcus",
        "last_name": "Delgado",
        "title": "DevOps Lead",
        "company": "Spotify",
        "linkedin": "https://www.linkedin.com/in/marcusdelgado",
        "avatar_initials": "MD",
        "avatar_color": "#34A853",
    },
    {
        "id": "sp3",
        "first_name": "Yuna",
        "last_name": "Kim",
        "title": "ML Engineer",
        "company": "DeepMind",
        "linkedin": "https://www.linkedin.com/in/yunakim",
        "avatar_initials": "YK",
        "avatar_color": "#FBBC04",
    },
    {
        "id": "sp4",
        "first_name": "Ravi",
        "last_name": "Shankar",
        "title": "Site Reliability Engineer",
        "company": "Airbnb",
        "linkedin": "https://www.linkedin.com/in/ravishankar",
        "avatar_initials": "RS",
        "avatar_color": "#EA4335",
    },
    {
        "id": "sp5",
        "first_name": "Sofia",
        "last_name": "Andreou",
        "title": "Data Platform Lead",
        "company": "Zalando",
        "linkedin": "https://www.linkedin.com/in/sofiaandreou",
        "avatar_initials": "SA",
        "avatar_color": "#9C27B0",
    },
    {
        "id": "sp6",
        "first_name": "James",
        "last_name": "Okafor",
        "title": "Security Architect",
        "company": "Palo Alto Networks",
        "linkedin": "https://www.linkedin.com/in/jamesokafor",
        "avatar_initials": "JO",
        "avatar_color": "#00BCD4",
    },
    {
        "id": "sp7",
        "first_name": "Leila",
        "last_name": "Farsi",
        "title": "Serverless Specialist",
        "company": "Google Cloud",
        "linkedin": "https://www.linkedin.com/in/leilafarsi",
        "avatar_initials": "LF",
        "avatar_color": "#FF5722",
    },
    {
        "id": "sp8",
        "first_name": "Tom",
        "last_name": "Brennan",
        "title": "Kubernetes & GKE Advocate",
        "company": "Weaveworks",
        "linkedin": "https://www.linkedin.com/in/tombrennan",
        "avatar_initials": "TB",
        "avatar_color": "#607D8B",
    },
    {
        "id": "sp9",
        "first_name": "Aisha",
        "last_name": "Osei",
        "title": "AI/ML Product Manager",
        "company": "Google",
        "linkedin": "https://www.linkedin.com/in/aishaosei",
        "avatar_initials": "AO",
        "avatar_color": "#E91E63",
    },
    {
        "id": "sp10",
        "first_name": "Carlos",
        "last_name": "Vega",
        "title": "Senior Data Engineer",
        "company": "Databricks",
        "linkedin": "https://www.linkedin.com/in/carlosvega",
        "avatar_initials": "CV",
        "avatar_color": "#FF9800",
    },
    {
        "id": "sp11",
        "first_name": "Nina",
        "last_name": "Petrov",
        "title": "Cloud Database Architect",
        "company": "Shopify",
        "linkedin": "https://www.linkedin.com/in/ninapetrov",
        "avatar_initials": "NP",
        "avatar_color": "#26C6DA",
    },
    {
        "id": "sp12",
        "first_name": "Daniel",
        "last_name": "Mwangi",
        "title": "FinOps & Cloud Economics Lead",
        "company": "HSBC",
        "linkedin": "https://www.linkedin.com/in/danielmwangi",
        "avatar_initials": "DM",
        "avatar_color": "#8BC34A",
    },
]

# Categories
CATEGORIES = {
    1: "Infrastructure & DevOps",
    2: "AI & Data",
}

TALKS = [
    {
        "id": "T001",
        "title": "Keynote: The Cloud-Native Future on Google Cloud",
        "category": 1,
        "speaker_ids": ["sp1", "sp2"],
        "time_start": "09:00",
        "time_end": "09:50",
        "duration_min": 50,
        "description": (
            "Kick off Google Cloud Summit 2026 with a sweeping look at the cloud-native "
            "landscape. Priya Nambiar and Marcus Delgado walk through the latest innovations "
            "in GKE Autopilot, Cloud Run v3, and Anthos, and share a live demo of a "
            "zero-downtime migration from on-premises to Google Cloud using infrastructure-as-code "
            "and GitOps workflows. Expect real customer stories, benchmark data, and a preview of "
            "what's coming in the second half of 2026."
        ),
        "room": "Main Stage",
    },
    {
        "id": "T002",
        "title": "Vertex AI in Production: Lessons from the Trenches",
        "category": 2,
        "speaker_ids": ["sp3", "sp9"],
        "time_start": "10:00",
        "time_end": "10:45",
        "duration_min": 45,
        "description": (
            "Deploying a model in a notebook is easy — deploying it reliably at scale is hard. "
            "Yuna Kim and Aisha Osei draw on real production incidents to reveal the hidden "
            "complexity of Vertex AI pipelines: feature store drift, shadow traffic testing, "
            "model versioning strategies, and cost-aware scaling. You will leave with a "
            "production-readiness checklist you can apply immediately."
        ),
        "room": "Hall A",
    },
    {
        "id": "T003",
        "title": "SRE on GCP: Achieving Five-Nines with SLOs and Error Budgets",
        "category": 1,
        "speaker_ids": ["sp4"],
        "time_start": "11:00",
        "time_end": "11:45",
        "duration_min": 45,
        "description": (
            "Ravi Shankar, SRE Lead at Airbnb, unpacks how the team migrated critical booking "
            "services to GCP while maintaining 99.999% availability. The talk covers SLO "
            "definition, Cloud Monitoring custom metrics, alerting without alert fatigue, "
            "automated runbooks with Cloud Workflows, and the cultural shift needed to embrace "
            "error budgets as a product decision tool rather than an ops metric."
        ),
        "room": "Hall B",
    },
    {
        "id": "T004",
        "title": "BigQuery Omni & Data Mesh: Breaking the Warehouse Monolith",
        "category": 2,
        "speaker_ids": ["sp5", "sp10"],
        "time_start": "11:55",
        "time_end": "12:40",
        "duration_min": 45,
        "description": (
            "Sofia Andreou and Carlos Vega present Zalando's journey from a single BigQuery "
            "project to a federated data mesh spanning AWS, Azure, and GCP. They explain "
            "BigQuery Omni's cross-cloud query engine, Dataplex data catalog governance, "
            "column-level security with policy tags, and how dbt Cloud was integrated to "
            "provide lineage and testing across domains. Includes a live cost-comparison demo."
        ),
        "room": "Hall A",
    },
    # LUNCH BREAK 12:40 - 13:40
    {
        "id": "T005",
        "title": "Zero-Trust Security in Google Cloud with BeyondCorp Enterprise",
        "category": 1,
        "speaker_ids": ["sp6"],
        "time_start": "13:40",
        "time_end": "14:25",
        "duration_min": 45,
        "description": (
            "James Okafor walks through a real-world BeyondCorp Enterprise deployment at "
            "a Fortune 500 company, covering Identity-Aware Proxy, VPC Service Controls, "
            "Cloud Armor WAF rules, and Secret Manager rotation policies. He also explores "
            "how Chronicle SIEM integrates with Google Cloud's telemetry to deliver "
            "sub-second threat detection across a hybrid cloud environment."
        ),
        "room": "Main Stage",
    },
    {
        "id": "T006",
        "title": "Serverless at Scale: Cloud Run, Eventarc & the Event-Driven Revolution",
        "category": 1,
        "speaker_ids": ["sp7", "sp2"],
        "time_start": "14:35",
        "time_end": "15:20",
        "duration_min": 45,
        "description": (
            "Leila Farsi and Marcus Delgado demonstrate how to build a fully event-driven "
            "architecture using Cloud Run, Eventarc, Pub/Sub, and Cloud Tasks — with zero "
            "idle cost and automatic scaling from 0 to 10,000 requests per second in seconds. "
            "The session includes a live coding demo of a multi-region order-processing "
            "pipeline and a deep dive into cold-start mitigation strategies and minimum "
            "instance configuration."
        ),
        "room": "Hall B",
    },
    {
        "id": "T007",
        "title": "Generative AI with Gemini API: Building Production-Grade LLM Apps",
        "category": 2,
        "speaker_ids": ["sp9", "sp3"],
        "time_start": "15:30",
        "time_end": "16:15",
        "duration_min": 45,
        "description": (
            "Aisha Osei and Yuna Kim take you from prompt engineering basics to production "
            "LLM applications using the Gemini API on Google Cloud. Topics include RAG "
            "architectures with Vertex AI Search, grounding responses with Google Search, "
            "function calling for tool use, safety filters and responsible AI controls, "
            "and structured output with JSON mode. A live demo builds a document Q&A "
            "assistant end-to-end in 20 minutes."
        ),
        "room": "Hall A",
    },
    {
        "id": "T008",
        "title": "GKE Platform Engineering: From Clusters to Internal Developer Portals",
        "category": 1,
        "speaker_ids": ["sp8", "sp1"],
        "time_start": "16:25",
        "time_end": "17:10",
        "duration_min": 45,
        "description": (
            "Tom Brennan and Priya Nambiar close the day with a deep dive into platform "
            "engineering on GKE — covering Config Connector for Kubernetes-native Google "
            "Cloud resource management, Fleet management for multi-cluster visibility, "
            "and a live walkthrough of a Backstage-powered Internal Developer Portal "
            "integrated with Cloud Build, Cloud Deploy, and GKE. Learn how to give "
            "developers a self-service golden path without sacrificing platform control."
        ),
        "room": "Hall B",
    },
    {
        "id": "T009",
        "title": "Cloud Spanner: Globally Distributed Transactions Without Compromise",
        "category": 1,
        "speaker_ids": ["sp11", "sp4"],
        "time_start": "17:20",
        "time_end": "18:05",
        "duration_min": 45,
        "description": (
            "Nina Petrov and Ravi Shankar demystify Cloud Spanner's TrueTime protocol and "
            "explain how it achieves external consistency across continents without sacrificing "
            "relational semantics. The session covers schema design for Spanner's interleaved "
            "tables, hot-spot avoidance, change streams for CDC pipelines, and a live "
            "benchmark comparing Spanner against CockroachDB and AlloyDB for a high-throughput "
            "e-commerce workload. Walk away knowing exactly when Spanner is the right choice "
            "and how to migrate an existing PostgreSQL database with minimal downtime."
        ),
        "room": "Main Stage",
    },
    {
        "id": "T010",
        "title": "FinOps on Google Cloud: Taming Cloud Costs at Scale",
        "category": 1,
        "speaker_ids": ["sp12"],
        "time_start": "18:15",
        "time_end": "19:00",
        "duration_min": 45,
        "description": (
            "Cloud bills don't have to be a surprise. Daniel Mwangi, FinOps Lead at HSBC, "
            "shares how the team reduced Google Cloud spend by 38% in six months without "
            "slowing product delivery. He walks through Committed Use Discounts vs Sustained "
            "Use Discounts, right-sizing recommendations from the Active Assist API, Cloud "
            "Billing export to BigQuery for showback/chargeback, and budget alerts that "
            "actually drive action. Includes a live demo of a FinOps dashboard built on "
            "Looker Studio and BigQuery."
        ),
        "room": "Hall A",
    },
    {
        "id": "T011",
        "title": "Responsible AI in the Enterprise: Safety, Fairness & Governance on GCP",
        "category": 2,
        "speaker_ids": ["sp9", "sp5"],
        "time_start": "19:10",
        "time_end": "19:55",
        "duration_min": 45,
        "description": (
            "Aisha Osei and Sofia Andreou tackle one of the most pressing questions in AI "
            "deployment: how do you ship models that are safe, fair, and auditable in a "
            "regulated enterprise context? This session covers Vertex AI Model Evaluation's "
            "fairness metrics, SHAP-based explainability, data lineage with Dataplex, and "
            "how to implement a model governance framework that satisfies both legal teams "
            "and product stakeholders. Real anonymised case studies from financial services "
            "and healthcare sectors illustrate the framework in action."
        ),
        "room": "Hall B",
    },
]

SCHEDULE = [
    {"type": "session", "talk_id": "T001", "time_start": "09:00", "time_end": "09:50"},
    {"type": "break", "label": "Break & Networking", "time_start": "09:50", "time_end": "10:00"},
    {"type": "session", "talk_id": "T002", "time_start": "10:00", "time_end": "10:45"},
    {"type": "break", "label": "Break", "time_start": "10:45", "time_end": "11:00"},
    {"type": "session", "talk_id": "T003", "time_start": "11:00", "time_end": "11:45"},
    {"type": "break", "label": "Break", "time_start": "11:45", "time_end": "11:55"},
    {"type": "session", "talk_id": "T004", "time_start": "11:55", "time_end": "12:40"},
    {"type": "lunch", "label": "Lunch Break", "time_start": "12:40", "time_end": "13:40"},
    {"type": "session", "talk_id": "T005", "time_start": "13:40", "time_end": "14:25"},
    {"type": "break", "label": "Break", "time_start": "14:25", "time_end": "14:35"},
    {"type": "session", "talk_id": "T006", "time_start": "14:35", "time_end": "15:20"},
    {"type": "break", "label": "Break", "time_start": "15:20", "time_end": "15:30"},
    {"type": "session", "talk_id": "T007", "time_start": "15:30", "time_end": "16:15"},
    {"type": "break", "label": "Break", "time_start": "16:15", "time_end": "16:25"},
    {"type": "session", "talk_id": "T008", "time_start": "16:25", "time_end": "17:10"},
    {"type": "break", "label": "Break", "time_start": "17:10", "time_end": "17:20"},
    {"type": "session", "talk_id": "T009", "time_start": "17:20", "time_end": "18:05"},
    {"type": "break", "label": "Break", "time_start": "18:05", "time_end": "18:15"},
    {"type": "session", "talk_id": "T010", "time_start": "18:15", "time_end": "19:00"},
    {"type": "break", "label": "Break", "time_start": "19:00", "time_end": "19:10"},
    {"type": "session", "talk_id": "T011", "time_start": "19:10", "time_end": "19:55"},
    {"type": "break", "label": "Closing Drinks & Networking", "time_start": "19:55", "time_end": "21:00"},
]


def get_speaker_map():
    return {s["id"]: s for s in SPEAKERS}


def get_talk_map():
    return {t["id"]: t for t in TALKS}


def enrich_talks(talks, speaker_map):
    """Attach full speaker objects to each talk."""
    enriched = []
    for talk in talks:
        t = dict(talk)
        t["speakers"] = [speaker_map[sid] for sid in talk["speaker_ids"] if sid in speaker_map]
        t["category_name"] = CATEGORIES.get(talk["category"], "General")
        enriched.append(t)
    return enriched
