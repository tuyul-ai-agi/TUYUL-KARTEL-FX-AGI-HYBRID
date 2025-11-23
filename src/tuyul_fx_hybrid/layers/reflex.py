"""
Reflex Layer - Real-Time Decision Making & Adaptive Learning
Handles rapid response decisions and continuous learning from interactions.
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import numpy as np

from ..core.logger import logger


class ReflexLayer:
    """
    Reflex Layer for real-time decision making and adaptive learning.
    Provides quick responses and learns from patterns and feedback.
    """
    
    def __init__(self):
        """Initialize Reflex Layer."""
        self.decision_history: List[Dict[str, Any]] = []
        self.learning_patterns: Dict[str, Any] = {}
        self.reflex_rules: List[Dict[str, Any]] = []
        self.performance_metrics: Dict[str, float] = {
            "accuracy": 0.0,
            "response_time": 0.0,
            "learning_rate": 0.001
        }
        logger.info("Reflex Layer initialized")
    
    async def make_decision(
        self, 
        context: Dict[str, Any], 
        options: List[Dict[str, Any]], 
        mode: str = "fast"
    ) -> Dict[str, Any]:
        """
        Make a decision based on context and available options.
        
        Args:
            context: Current context and state
            options: Available decision options
            mode: Decision mode ('fast' for reflex, 'deliberate' for analysis)
            
        Returns:
            Decision result with confidence and reasoning
        """
        start_time = datetime.utcnow()
        
        try:
            # Apply reflex rules for fast mode
            if mode == "fast":
                decision = await self._apply_reflex_rules(context, options)
            else:
                decision = await self._deliberate_decision(context, options)
            
            # Record decision
            response_time = (datetime.utcnow() - start_time).total_seconds()
            decision["response_time"] = response_time
            decision["timestamp"] = datetime.utcnow().isoformat()
            
            self.decision_history.append(decision)
            
            # Update metrics
            self._update_metrics(decision, response_time)
            
            logger.info(f"Decision made in {response_time:.3f}s with confidence {decision.get('confidence', 0):.2f}")
            return decision
            
        except Exception as e:
            logger.error(f"Decision making failed: {e}")
            return {
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat(),
                "confidence": 0.0
            }
    
    async def _apply_reflex_rules(
        self, 
        context: Dict[str, Any], 
        options: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Apply fast reflex rules for immediate decisions."""
        
        # Check for matching reflex rules
        for rule in self.reflex_rules:
            if self._rule_matches(rule, context):
                return {
                    "action": rule["action"],
                    "confidence": rule.get("confidence", 0.8),
                    "reasoning": f"Reflex rule: {rule.get('name', 'unnamed')}",
                    "mode": "reflex"
                }
        
        # Default: select highest priority option
        if options:
            best_option = max(options, key=lambda x: x.get("priority", 0))
            return {
                "action": best_option,
                "confidence": 0.6,
                "reasoning": "Default priority-based selection",
                "mode": "reflex"
            }
        
        return {
            "action": "no_action",
            "confidence": 0.0,
            "reasoning": "No matching rules or options",
            "mode": "reflex"
        }
    
    async def _deliberate_decision(
        self, 
        context: Dict[str, Any], 
        options: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Make a deliberate decision with deeper analysis."""
        
        # Score each option
        scored_options = []
        for option in options:
            score = self._score_option(option, context)
            scored_options.append({
                "option": option,
                "score": score
            })
        
        # Select best option
        if scored_options:
            best = max(scored_options, key=lambda x: x["score"])
            return {
                "action": best["option"],
                "confidence": min(best["score"], 1.0),
                "reasoning": f"Deliberate analysis, score: {best['score']:.2f}",
                "mode": "deliberate"
            }
        
        return {
            "action": "no_action",
            "confidence": 0.0,
            "reasoning": "No viable options",
            "mode": "deliberate"
        }
    
    def _rule_matches(self, rule: Dict[str, Any], context: Dict[str, Any]) -> bool:
        """Check if a rule matches the current context."""
        conditions = rule.get("conditions", {})
        for key, value in conditions.items():
            if context.get(key) != value:
                return False
        return True
    
    def _score_option(self, option: Dict[str, Any], context: Dict[str, Any]) -> float:
        """Score an option based on context and learned patterns."""
        score = option.get("priority", 0.5)
        
        # Apply learned patterns
        option_id = option.get("id", "")
        if option_id in self.learning_patterns:
            pattern = self.learning_patterns[option_id]
            score *= (1 + pattern.get("success_rate", 0))
        
        return score
    
    async def learn_from_feedback(
        self, 
        decision_id: str, 
        outcome: Dict[str, Any], 
        feedback: Dict[str, Any]
    ) -> bool:
        """
        Learn from decision outcomes and feedback.
        
        Args:
            decision_id: ID of the decision
            outcome: Result of the decision
            feedback: Feedback on the decision quality
            
        Returns:
            Success status
        """
        try:
            success = feedback.get("success", False)
            quality = feedback.get("quality", 0.5)
            
            # Update learning patterns
            action_id = outcome.get("action_id", "unknown")
            if action_id not in self.learning_patterns:
                self.learning_patterns[action_id] = {
                    "attempts": 0,
                    "successes": 0,
                    "success_rate": 0.0,
                    "avg_quality": 0.0
                }
            
            pattern = self.learning_patterns[action_id]
            pattern["attempts"] += 1
            if success:
                pattern["successes"] += 1
            pattern["success_rate"] = pattern["successes"] / pattern["attempts"]
            pattern["avg_quality"] = (
                (pattern["avg_quality"] * (pattern["attempts"] - 1) + quality) 
                / pattern["attempts"]
            )
            
            logger.info(f"Learned from decision {decision_id}: success={success}, quality={quality:.2f}")
            return True
            
        except Exception as e:
            logger.error(f"Learning from feedback failed: {e}")
            return False
    
    async def add_reflex_rule(
        self, 
        name: str, 
        conditions: Dict[str, Any], 
        action: Any, 
        confidence: float = 0.8
    ) -> bool:
        """
        Add a new reflex rule.
        
        Args:
            name: Rule name
            conditions: Conditions that trigger the rule
            action: Action to take when rule matches
            confidence: Confidence level for this rule
            
        Returns:
            Success status
        """
        try:
            rule = {
                "name": name,
                "conditions": conditions,
                "action": action,
                "confidence": confidence,
                "created_at": datetime.utcnow().isoformat()
            }
            self.reflex_rules.append(rule)
            logger.info(f"Added reflex rule: {name}")
            return True
        except Exception as e:
            logger.error(f"Failed to add reflex rule {name}: {e}")
            return False
    
    def _update_metrics(self, decision: Dict[str, Any], response_time: float):
        """Update performance metrics."""
        # Update response time (exponential moving average)
        alpha = 0.3
        self.performance_metrics["response_time"] = (
            alpha * response_time + 
            (1 - alpha) * self.performance_metrics["response_time"]
        )
    
    async def get_reflex_status(self) -> Dict[str, Any]:
        """Get current status of Reflex Layer."""
        return {
            "total_decisions": len(self.decision_history),
            "active_rules": len(self.reflex_rules),
            "learned_patterns": len(self.learning_patterns),
            "metrics": self.performance_metrics,
            "status": "operational"
        }
