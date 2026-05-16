---
name: seo
description: "Comprehensive SEO analysis for any website or business type. Full site audits, single-page analysis, technical SEO (crawlability, indexability, Core Web Vitals with INP), schema markup, content quality (E-E-A-T), image optimization, sitemap analysis, and GEO for AI Overviews/ChatGPT/Perplexity. Industry detection for SaaS, e-commerce, local, publishers, agencies."
version: "1.9.9"
author: AgriciDaniel
---

# 🚀 Universal SEO Skill

This skill provides a comprehensive framework for SEO analysis, orchestrating 24 sub-skills and 18 sub-agents.

## 🛠 Commands Reference

| Command | Description |
|---------|-------------|
| `/seo audit <url>` | Full website audit with parallel subagent delegation |
| `/seo page <url>` | Deep single-page analysis |
| `/seo sitemap <url>` | Analyze or generate XML sitemaps |
| `/seo schema <url>` | Detect, validate, and generate Schema.org markup |
| `/seo technical <url>` | Technical SEO audit (9 categories) |
| `/seo content <url>` | E-E-A-T and content quality analysis |
| `/seo geo <url>` | AI Overviews / Generative Engine Optimization |
| `/seo plan <type>` | Strategic SEO planning for business types |
| `/seo local <url>` | Local SEO (GBP, citations, reviews, maps) |
| `/seo cluster <keyword>`| Semantic clustering and content architecture |

## 🏗 Orchestration Logic (Audit)
When an audit is triggered, the system:
1. **Detects business type**: SaaS, local, e-commerce, publisher, etc.
2. **Spawns parallel subagents**: `seo-technical`, `seo-content`, `seo-schema`, `seo-sitemap`, `seo-performance`, `seo-visual`, `seo-geo`.
3. **Unified Reporting**: Calculates an **SEO Health Score (0-100)** and creates a prioritized action plan.

## 📊 Scoring Methodology
- **Technical SEO (22%)**
- **Content Quality (23%)**
- **On-Page SEO (20%)**
- **Schema (10%)**
- **Performance (CWV) (10%)**
- **AI Search Readiness (10%)**
- **Images (5%)**

## 🎯 Industry Detection
- **SaaS**: pricing page, /features, /docs, "free trial".
- **Local Service**: phone number, address, service area, Google Maps embed.
- **E-commerce**: /products, /cart, product schema.
- **Publisher**: /blog, /articles, article schema.
