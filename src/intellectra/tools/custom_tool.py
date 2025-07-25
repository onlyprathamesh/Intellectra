from crewai.tools import BaseTool
from litellm import completion

import os
import requests


class TavilySearch(BaseTool):
    name: str = "Tavily Search Tool"
    description: str = "Useful for performing web search and retrieving relevant information."

    def _run(self, query: str) -> str:
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            raise ValueError("TAVILY_API_KEY environment variable is not set.")

        url = "https://api.tavily.com/search"
        headers = {"Content-Type": "application/json"}
        payload = {
            "api_key": api_key,
            "query": query,
            "search_depth": "advanced",
            "include_answer": True,
            "include_sources": True
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            return f"Search failed: {response.text}"

        data = response.json()
        answer = data.get("answer", "No answer found.")
        sources = data.get("sources", [])

        result = f"Answer:\n{answer}\n\nSources:\n"
        result += "\n".join([f"- {s['url']}" for s in sources])

        return result

class MarketResearchTool(BaseTool):
    name: str = "Market Research Tool"
    description: str = (
        "Useful for performing market analysis and competitive landscape research. "
        "Provides information about industry demand, target users, competitors, pricing, and potential opportunities."
    )

    def _run(self, query: str) -> str:
        import os, requests

        api_key = os.getenv("SERPER_API_KEY")
        if not api_key:
            raise ValueError("SERPER_API_KEY environment variable is not set.")

        url = "https://google.serper.dev/search"
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "q": query
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            return f"Market research failed: {response.text}"

        data = response.json()
        results = data.get("organic", [])

        if not results:
            return "No market data found."

        summary = "📊 Market Research Results:\n\n"
        for r in results[:5]:  # Top 5 results
            summary += f"🔹 {r.get('title', 'No Title')}\n{r.get('link', 'No Link')}\n\n"

        return summary


class RiskAssessmentTool(BaseTool):
    name: str = "Risk Assessment Tool"
    description: str = (
        "Useful for identifying risks in building a product or business idea. "
        "Analyzes potential technical, business, legal, and operational risks along with mitigation suggestions."
    )

    def _run(self, idea_description: str) -> str:
        from litellm import completion

        prompt = (
            f"You are a startup risk analyst. Evaluate the following product or business idea:\n\n"
            f"{idea_description}\n\n"
            "List the following:\n"
            "- Technical risks\n- Business risks\n- Legal/compliance risks\n"
            "- Operational/logistical risks\n- Risk mitigation strategies"
        )

        try:
            response = completion(
                model="mistral/mistral-large-latest",  # Make sure this is a supported model on your configured provider
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4
            )
            return response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            return f"Error while assessing risk: {str(e)}"

