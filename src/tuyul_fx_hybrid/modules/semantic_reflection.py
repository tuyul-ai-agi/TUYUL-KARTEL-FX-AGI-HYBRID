"""
Semantic Reflection Module
Analyzes past decisions and reasoning to improve future performance.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import numpy as np

from ..core.logger import logger


class SemanticReflection:
    """
    Semantic reflection system for analyzing and learning from past reasoning.
    """
    
    def __init__(self):
        """Initialize Semantic Reflection."""
        self.reflections: List[Dict[str, Any]] = []
        self.insights: Dict[str, List[str]] = {}
        self.reasoning_patterns: Dict[str, Any] = {}
        logger.info("Semantic Reflection initialized")
    
    async def reflect_on_decision(
        self, 
        decision: Dict[str, Any], 
        outcome: Dict[str, Any],
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Reflect on a past decision and its outcome.
        
        Args:
            decision: The decision that was made
            outcome: The result of the decision
            context: Context in which decision was made
            
        Returns:
            Reflection analysis
        """
        try:
            reflection = {
                "decision_id": decision.get("id", "unknown"),
                "timestamp": datetime.utcnow().isoformat(),
                "decision_summary": self._summarize_decision(decision),
                "outcome_summary": self._summarize_outcome(outcome),
                "success": outcome.get("success", False),
                "analysis": {},
                "lessons_learned": []
            }
            
            # Analyze decision quality
            reflection["analysis"] = await self._analyze_decision_quality(
                decision, outcome, context
            )
            
            # Extract lessons
            reflection["lessons_learned"] = await self._extract_lessons(
                decision, outcome, context
            )
            
            # Store reflection
            self.reflections.append(reflection)
            
            # Update insights
            await self._update_insights(reflection)
            
            # Update reasoning patterns
            await self._update_reasoning_patterns(decision, outcome)
            
            logger.info(
                f"Reflected on decision: success={reflection['success']}, "
                f"lessons={len(reflection['lessons_learned'])}"
            )
            
            return reflection
            
        except Exception as e:
            logger.error(f"Reflection failed: {e}")
            return {
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    def _summarize_decision(self, decision: Dict[str, Any]) -> str:
        """Create a summary of the decision."""
        action = decision.get("action", "unknown")
        reasoning = decision.get("reasoning", "")
        confidence = decision.get("confidence", 0)
        
        return f"Action: {action}, Reasoning: {reasoning}, Confidence: {confidence:.2f}"
    
    def _summarize_outcome(self, outcome: Dict[str, Any]) -> str:
        """Create a summary of the outcome."""
        success = outcome.get("success", False)
        result = outcome.get("result", "")
        impact = outcome.get("impact", "")
        
        return f"Success: {success}, Result: {result}, Impact: {impact}"
    
    async def _analyze_decision_quality(
        self, 
        decision: Dict[str, Any], 
        outcome: Dict[str, Any],
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Analyze the quality of the decision."""
        analysis = {
            "appropriateness": 0.0,
            "timeliness": 0.0,
            "effectiveness": 0.0,
            "overall_quality": 0.0
        }
        
        # Appropriateness: Was it the right decision for the context?
        if outcome.get("success", False):
            analysis["appropriateness"] = 0.8
        else:
            analysis["appropriateness"] = 0.3
        
        # Timeliness: Was it made at the right time?
        response_time = decision.get("response_time", 1.0)
        if response_time < 2.0:
            analysis["timeliness"] = 0.9
        elif response_time < 5.0:
            analysis["timeliness"] = 0.7
        else:
            analysis["timeliness"] = 0.4
        
        # Effectiveness: Did it achieve the desired outcome?
        impact = outcome.get("impact_score", 0.5)
        analysis["effectiveness"] = impact
        
        # Overall quality
        analysis["overall_quality"] = np.mean([
            analysis["appropriateness"],
            analysis["timeliness"],
            analysis["effectiveness"]
        ])
        
        return analysis
    
    async def _extract_lessons(
        self, 
        decision: Dict[str, Any], 
        outcome: Dict[str, Any],
        context: Dict[str, Any]
    ) -> List[str]:
        """Extract lessons learned from the decision-outcome pair."""
        lessons = []
        
        if outcome.get("success", False):
            # Successful outcomes
            action = decision.get("action", "")
            lessons.append(f"Action '{action}' was effective in this context")
            
            if decision.get("confidence", 0) > 0.8:
                lessons.append("High confidence decisions tend to be successful")
        else:
            # Unsuccessful outcomes
            reasoning = decision.get("reasoning", "")
            lessons.append(f"Reasoning '{reasoning}' may need refinement")
            
            if decision.get("confidence", 0) > 0.7:
                lessons.append("High confidence doesn't guarantee success")
        
        # Context-specific lessons
        if "risk_level" in context:
            risk = context["risk_level"]
            success = outcome.get("success", False)
            lessons.append(
                f"Risk level '{risk}' correlated with "
                f"{'success' if success else 'failure'}"
            )
        
        return lessons
    
    async def _update_insights(self, reflection: Dict[str, Any]):
        """Update insights database with new reflection."""
        decision_type = reflection.get("decision_summary", "").split(":")[0]
        
        if decision_type not in self.insights:
            self.insights[decision_type] = []
        
        for lesson in reflection["lessons_learned"]:
            if lesson not in self.insights[decision_type]:
                self.insights[decision_type].append(lesson)
    
    async def _update_reasoning_patterns(
        self, 
        decision: Dict[str, Any], 
        outcome: Dict[str, Any]
    ):
        """Update reasoning patterns based on decision outcomes."""
        reasoning = decision.get("reasoning", "unknown")
        success = outcome.get("success", False)
        
        if reasoning not in self.reasoning_patterns:
            self.reasoning_patterns[reasoning] = {
                "attempts": 0,
                "successes": 0,
                "success_rate": 0.0
            }
        
        pattern = self.reasoning_patterns[reasoning]
        pattern["attempts"] += 1
        if success:
            pattern["successes"] += 1
        pattern["success_rate"] = pattern["successes"] / pattern["attempts"]
    
    async def get_insights_for_context(self, context: Dict[str, Any]) -> List[str]:
        """
        Get relevant insights for a given context.
        
        Args:
            context: Current context
            
        Returns:
            List of relevant insights
        """
        relevant_insights = []
        
        # Gather all insights
        for category, insights in self.insights.items():
            relevant_insights.extend(insights)
        
        # Filter based on context (simplified)
        if "risk_level" in context:
            relevant_insights = [
                i for i in relevant_insights 
                if context["risk_level"] in i.lower()
            ]
        
        return relevant_insights[:5]  # Return top 5
    
    async def analyze_reasoning_effectiveness(self) -> Dict[str, Any]:
        """
        Analyze effectiveness of different reasoning patterns.
        
        Returns:
            Analysis of reasoning effectiveness
        """
        if not self.reasoning_patterns:
            return {
                "total_patterns": 0,
                "best_pattern": None,
                "worst_pattern": None,
                "status": "no_data"
            }
        
        # Find best and worst patterns
        patterns = [
            (reasoning, data["success_rate"], data["attempts"])
            for reasoning, data in self.reasoning_patterns.items()
            if data["attempts"] >= 3  # Minimum attempts for significance
        ]
        
        if not patterns:
            return {
                "total_patterns": len(self.reasoning_patterns),
                "best_pattern": None,
                "worst_pattern": None,
                "status": "insufficient_data"
            }
        
        patterns.sort(key=lambda x: x[1], reverse=True)
        
        return {
            "total_patterns": len(self.reasoning_patterns),
            "best_pattern": {
                "reasoning": patterns[0][0],
                "success_rate": patterns[0][1],
                "attempts": patterns[0][2]
            },
            "worst_pattern": {
                "reasoning": patterns[-1][0],
                "success_rate": patterns[-1][1],
                "attempts": patterns[-1][2]
            },
            "average_success_rate": np.mean([p[1] for p in patterns]),
            "status": "operational"
        }
    
    async def generate_reflection_report(self) -> Dict[str, Any]:
        """
        Generate a comprehensive reflection report.
        
        Returns:
            Reflection report
        """
        if not self.reflections:
            return {
                "total_reflections": 0,
                "status": "no_data"
            }
        
        successes = sum(1 for r in self.reflections if r["success"])
        total = len(self.reflections)
        
        # Average quality scores
        quality_scores = [
            r["analysis"]["overall_quality"] 
            for r in self.reflections 
            if "analysis" in r and "overall_quality" in r["analysis"]
        ]
        
        return {
            "total_reflections": total,
            "success_rate": successes / total if total > 0 else 0,
            "average_decision_quality": np.mean(quality_scores) if quality_scores else 0,
            "total_insights": sum(len(insights) for insights in self.insights.values()),
            "reasoning_patterns": len(self.reasoning_patterns),
            "status": "operational"
        }
    
    async def get_reflection_status(self) -> Dict[str, Any]:
        """Get current status of Semantic Reflection."""
        return {
            "total_reflections": len(self.reflections),
            "insights_categories": len(self.insights),
            "reasoning_patterns": len(self.reasoning_patterns),
            "status": "operational"
        }
