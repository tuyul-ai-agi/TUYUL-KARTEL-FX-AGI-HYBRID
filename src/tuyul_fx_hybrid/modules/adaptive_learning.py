"""
Adaptive Learning Module
Continuously learns from interactions and improves performance over time.
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import numpy as np
from collections import defaultdict

from ..core.config import settings
from ..core.logger import logger


class AdaptiveLearning:
    """
    Adaptive learning system for continuous improvement.
    Uses reinforcement learning principles and pattern recognition.
    """
    
    def __init__(self):
        """Initialize Adaptive Learning."""
        self.learning_rate = settings.learning_rate
        self.experiences: List[Dict[str, Any]] = []
        self.knowledge_base: Dict[str, Any] = {}
        self.performance_history: List[float] = []
        self.pattern_memory: Dict[str, Dict[str, Any]] = defaultdict(dict)
        self.adaptation_count = 0
        logger.info("Adaptive Learning initialized")
    
    async def learn_from_experience(
        self, 
        state: Dict[str, Any], 
        action: Dict[str, Any], 
        reward: float,
        next_state: Optional[Dict[str, Any]] = None
    ) -> bool:
        """
        Learn from an experience (state, action, reward, next_state).
        
        Args:
            state: Current state
            action: Action taken
            reward: Reward received
            next_state: Resulting state
            
        Returns:
            Success status
        """
        try:
            experience = {
                "state": state,
                "action": action,
                "reward": reward,
                "next_state": next_state,
                "timestamp": datetime.utcnow().isoformat()
            }
            
            self.experiences.append(experience)
            self.performance_history.append(reward)
            
            # Update knowledge base
            await self._update_knowledge(experience)
            
            # Detect and store patterns
            await self._detect_patterns(experience)
            
            self.adaptation_count += 1
            
            logger.info(f"Learned from experience: reward={reward:.2f}")
            return True
            
        except Exception as e:
            logger.error(f"Learning from experience failed: {e}")
            return False
    
    async def _update_knowledge(self, experience: Dict[str, Any]):
        """Update knowledge base with new experience."""
        state_key = self._state_to_key(experience["state"])
        action_key = self._action_to_key(experience["action"])
        
        if state_key not in self.knowledge_base:
            self.knowledge_base[state_key] = {}
        
        if action_key not in self.knowledge_base[state_key]:
            self.knowledge_base[state_key][action_key] = {
                "count": 0,
                "total_reward": 0.0,
                "avg_reward": 0.0
            }
        
        entry = self.knowledge_base[state_key][action_key]
        entry["count"] += 1
        entry["total_reward"] += experience["reward"]
        entry["avg_reward"] = entry["total_reward"] / entry["count"]
    
    async def _detect_patterns(self, experience: Dict[str, Any]):
        """Detect and store recurring patterns."""
        # Look for patterns in recent experiences
        if len(self.experiences) >= 3:
            recent = self.experiences[-3:]
            
            # Check for state-action-reward patterns
            pattern_key = self._create_pattern_key(recent)
            
            if pattern_key not in self.pattern_memory:
                self.pattern_memory[pattern_key] = {
                    "occurrences": 0,
                    "avg_reward": 0.0,
                    "confidence": 0.0
                }
            
            pattern = self.pattern_memory[pattern_key]
            pattern["occurrences"] += 1
            
            # Update average reward for this pattern
            rewards = [exp["reward"] for exp in recent]
            pattern["avg_reward"] = np.mean(rewards)
            pattern["confidence"] = min(pattern["occurrences"] / 10.0, 1.0)
    
    def _state_to_key(self, state: Dict[str, Any]) -> str:
        """Convert state to string key."""
        return str(sorted(state.items()))
    
    def _action_to_key(self, action: Dict[str, Any]) -> str:
        """Convert action to string key."""
        return str(action.get("id", action))
    
    def _create_pattern_key(self, experiences: List[Dict[str, Any]]) -> str:
        """Create a key for a pattern of experiences."""
        keys = []
        for exp in experiences:
            state_key = self._state_to_key(exp["state"])
            action_key = self._action_to_key(exp["action"])
            keys.append(f"{state_key}:{action_key}")
        return "->".join(keys)
    
    async def predict_reward(
        self, 
        state: Dict[str, Any], 
        action: Dict[str, Any]
    ) -> Tuple[float, float]:
        """
        Predict expected reward for a state-action pair.
        
        Args:
            state: Current state
            action: Proposed action
            
        Returns:
            Tuple of (expected_reward, confidence)
        """
        try:
            state_key = self._state_to_key(state)
            action_key = self._action_to_key(action)
            
            if state_key in self.knowledge_base:
                if action_key in self.knowledge_base[state_key]:
                    entry = self.knowledge_base[state_key][action_key]
                    confidence = min(entry["count"] / 10.0, 1.0)
                    return entry["avg_reward"], confidence
            
            # Default prediction
            return 0.5, 0.1
            
        except Exception as e:
            logger.error(f"Reward prediction failed: {e}")
            return 0.0, 0.0
    
    async def suggest_action(
        self, 
        state: Dict[str, Any], 
        available_actions: List[Dict[str, Any]]
    ) -> Optional[Dict[str, Any]]:
        """
        Suggest best action based on learned knowledge.
        
        Args:
            state: Current state
            available_actions: List of possible actions
            
        Returns:
            Suggested action or None
        """
        try:
            best_action = None
            best_reward = float('-inf')
            
            for action in available_actions:
                expected_reward, confidence = await self.predict_reward(state, action)
                
                # Weight by confidence
                weighted_reward = expected_reward * confidence
                
                if weighted_reward > best_reward:
                    best_reward = weighted_reward
                    best_action = action
            
            return best_action
            
        except Exception as e:
            logger.error(f"Action suggestion failed: {e}")
            return None
    
    async def get_performance_trend(self) -> Dict[str, Any]:
        """
        Analyze performance trend over time.
        
        Returns:
            Performance analysis
        """
        if not self.performance_history:
            return {
                "trend": "no_data",
                "average_reward": 0.0,
                "improvement": 0.0
            }
        
        history = self.performance_history
        
        # Calculate recent vs old performance
        if len(history) >= 10:
            recent_avg = np.mean(history[-10:])
            old_avg = np.mean(history[:10])
            improvement = recent_avg - old_avg
        else:
            recent_avg = np.mean(history)
            improvement = 0.0
        
        # Determine trend
        if improvement > 0.1:
            trend = "improving"
        elif improvement < -0.1:
            trend = "declining"
        else:
            trend = "stable"
        
        return {
            "trend": trend,
            "average_reward": np.mean(history),
            "recent_average": recent_avg if len(history) >= 10 else np.mean(history),
            "improvement": improvement,
            "total_experiences": len(history)
        }
    
    async def adapt_learning_rate(self, performance: float):
        """
        Adapt learning rate based on performance.
        
        Args:
            performance: Current performance metric
        """
        if performance < 0.3:
            # Poor performance, increase learning rate
            self.learning_rate = min(self.learning_rate * 1.1, 0.1)
        elif performance > 0.8:
            # Good performance, decrease learning rate for fine-tuning
            self.learning_rate = max(self.learning_rate * 0.9, 0.0001)
        
        logger.info(f"Adapted learning rate to {self.learning_rate:.6f}")
    
    async def get_learning_status(self) -> Dict[str, Any]:
        """Get current learning status."""
        return {
            "total_experiences": len(self.experiences),
            "knowledge_base_size": len(self.knowledge_base),
            "patterns_detected": len(self.pattern_memory),
            "adaptation_count": self.adaptation_count,
            "learning_rate": self.learning_rate,
            "status": "operational"
        }
