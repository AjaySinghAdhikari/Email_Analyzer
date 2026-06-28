# Marketing Email Analyzer

An AI-powered CLI tool that analyzes marketing emails 
and provides actionable improvements to increase open rates.

## The Problem
Most marketing emails never get opened. Weak subject lines, 
wrong tone, and vague messaging lose customers before they 
even read the content.

## What It Does
Paste any marketing email and instantly get:
- Subject line quality score (1-10)
- 3 optimized subject line alternatives
- Tone analysis (casual/formal/urgent/promotional)
- One specific improvement recommendation

## Built With
- Python
- Groq API (LLaMA 3.3 70B)
- python-dotenv

## Setup

1. Clone the repository
   git clone https://github.com/yourusername/email-analyzer

2. Install dependencies
   pip install -r requirements.txt

3. Create a .env file in the root directory
   GROQ_API_KEY=your_groq_api_key_here

4. Run the tool
   python main.py

5. Paste your email content and press Enter twice

## Example Output
Subject Score: 6/10
Reason: Short but lacks specificity and urgency

Better Subject Lines:
1. Limited Time Offer: Up to 50% Off Today Only
2. Exclusive Sale: 24-Hour Deals Inside
3. Flash Sale: Don't Miss Out

Tone: promotional
Tip: Add a specific discount percentage to increase urgency

## Why I Built This
Built this as a practical project before joining Anchora 
Excellence as a MarTech and AI Engineer — directly relevant 
to improving marketing communication at scale.