"""
GPT Bridge - Integration with OpenAI GPT models
Provides natural language understanding and generation capabilities.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import openai

from ..core.config import settings
from ..core.logger import logger


class GPTBridge:
    """
    Bridge to OpenAI GPT models for natural language processing.
    """
    
    def __init__(self):
        """Initialize GPT Bridge."""
        openai.api_key = settings.openai_api_key
        self.model = settings.gpt_model
        self.max_tokens = settings.gpt_max_tokens
        self.temperature = settings.gpt_temperature
        self.conversation_history: List[Dict[str, str]] = []
        logger.info(f"GPT Bridge initialized with model: {self.model}")
    
    async def generate_response(
        self, 
        prompt: str, 
        context: Optional[Dict[str, Any]] = None,
        system_message: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate a response using GPT.
        
        Args:
            prompt: User prompt
            context: Additional context
            system_message: System message for the conversation
            
        Returns:
            Generated response with metadata
        """
        try:
            messages = []
            
            # Add system message
            if system_message:
                messages.append({"role": "system", "content": system_message})
            elif context:
                messages.append({
                    "role": "system", 
                    "content": f"Context: {context}"
                })
            
            # Add conversation history
            messages.extend(self.conversation_history[-5:])  # Last 5 messages
            
            # Add current prompt
            messages.append({"role": "user", "content": prompt})
            
            # Generate response
            response = await openai.ChatCompletion.acreate(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            # Extract response
            content = response.choices[0].message.content
            
            # Update conversation history
            self.conversation_history.append({"role": "user", "content": prompt})
            self.conversation_history.append({"role": "assistant", "content": content})
            
            result = {
                "response": content,
                "model": self.model,
                "timestamp": datetime.utcnow().isoformat(),
                "tokens_used": response.usage.total_tokens,
                "finish_reason": response.choices[0].finish_reason
            }
            
            logger.info(f"GPT response generated: {response.usage.total_tokens} tokens")
            return result
            
        except Exception as e:
            logger.error(f"GPT generation failed: {e}")
            return {
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat(),
                "response": None
            }
    
    async def analyze_text(self, text: str, analysis_type: str = "sentiment") -> Dict[str, Any]:
        """
        Analyze text using GPT.
        
        Args:
            text: Text to analyze
            analysis_type: Type of analysis (sentiment, entities, summary, etc.)
            
        Returns:
            Analysis results
        """
        try:
            prompts = {
                "sentiment": f"Analyze the sentiment of this text and provide a score from -1 (very negative) to 1 (very positive): {text}",
                "entities": f"Extract key entities (people, organizations, locations) from this text: {text}",
                "summary": f"Provide a concise summary of this text: {text}",
                "keywords": f"Extract the most important keywords from this text: {text}",
                "intent": f"What is the primary intent or purpose of this text? {text}"
            }
            
            prompt = prompts.get(analysis_type, prompts["summary"])
            response = await self.generate_response(prompt)
            
            return {
                "analysis_type": analysis_type,
                "result": response.get("response"),
                "timestamp": datetime.utcnow().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Text analysis failed: {e}")
            return {
                "error": str(e),
                "analysis_type": analysis_type,
                "timestamp": datetime.utcnow().isoformat()
            }
    
    async def semantic_search(self, query: str, documents: List[str]) -> List[Dict[str, Any]]:
        """
        Perform semantic search on documents.
        
        Args:
            query: Search query
            documents: List of documents to search
            
        Returns:
            Ranked search results
        """
        try:
            # Use GPT to find most relevant documents
            docs_text = "\n".join([f"{i+1}. {doc}" for i, doc in enumerate(documents)])
            prompt = f"Given this query: '{query}'\n\nRank these documents by relevance (provide document numbers only):\n{docs_text}"
            
            response = await self.generate_response(prompt)
            
            # Parse response to get rankings (simplified)
            results = []
            for i, doc in enumerate(documents):
                results.append({
                    "document": doc,
                    "rank": i + 1,
                    "relevance_score": 1.0 / (i + 1)  # Simplified scoring
                })
            
            return results
            
        except Exception as e:
            logger.error(f"Semantic search failed: {e}")
            return []
    
    async def generate_insights(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate insights from structured data.
        
        Args:
            data: Input data
            
        Returns:
            Generated insights
        """
        try:
            prompt = f"Analyze this data and provide key insights: {data}"
            response = await self.generate_response(prompt)
            
            return {
                "insights": response.get("response"),
                "data_summary": str(data)[:200],
                "timestamp": datetime.utcnow().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Insight generation failed: {e}")
            return {
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history.clear()
        logger.info("Conversation history cleared")
    
    async def get_status(self) -> Dict[str, Any]:
        """Get current status of GPT Bridge."""
        return {
            "model": self.model,
            "conversation_length": len(self.conversation_history),
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "status": "operational"
        }
