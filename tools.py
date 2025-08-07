from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class SentimentInput(BaseModel):
    """Tool input schema for sentiment analysis."""
    text: str = Field(..., description="Text to analyze")

class SentimentAnalysisTool(BaseTool):
    name: str = "sentiment_analysis"
    description: str = (
        "Analyzes the sentiment of a given text "
        "and returns 'positive', 'neutral', or 'negative'."
    )
    args_schema: type = SentimentInput  # <-- Add type annotation here

    def _run(self, text: str) -> str:
        # (Your actual analysis logic here)
        return "positive"

def agents_tools():
    directory_read_tool = DirectoryReadTool(directory='./instructions')
    file_read_tool = FileReadTool()
    search_tool = SerperDevTool()
    sentiment_analysis_tool = SentimentAnalysisTool()
    return {
        "directory_read_tool": directory_read_tool,
        "file_read_tool": file_read_tool,
        "search_tool": search_tool,
        "sentiment_analysis_tool": sentiment_analysis_tool,
    }
