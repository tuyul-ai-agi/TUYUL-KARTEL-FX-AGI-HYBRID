"""
Risk Layer - Risk Assessment & Mitigation Strategies
Analyzes potential risks and provides mitigation recommendations.
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from enum import Enum
import numpy as np

from ..core.logger import logger


class RiskLevel(str, Enum):
    """Risk severity levels."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    MINIMAL = "minimal"


class RiskCategory(str, Enum):
    """Risk categories."""
    FINANCIAL = "financial"
    OPERATIONAL = "operational"
    STRATEGIC = "strategic"
    COMPLIANCE = "compliance"
    TECHNICAL = "technical"
    REPUTATIONAL = "reputational"


class RiskLayer:
    """
    Risk Layer for assessing and mitigating risks.
    Provides risk analysis, scoring, and mitigation strategies.
    """
    
    def __init__(self):
        """Initialize Risk Layer."""
        self.risk_assessments: List[Dict[str, Any]] = []
        self.risk_rules: Dict[str, Any] = {}
        self.mitigation_strategies: Dict[str, List[Dict[str, Any]]] = {}
        self.risk_thresholds = {
            RiskLevel.CRITICAL: 0.9,
            RiskLevel.HIGH: 0.7,
            RiskLevel.MEDIUM: 0.5,
            RiskLevel.LOW: 0.3,
            RiskLevel.MINIMAL: 0.0
        }
        logger.info("Risk Layer initialized")
    
    async def assess_risk(
        self, 
        action: Dict[str, Any], 
        context: Dict[str, Any],
        category: Optional[RiskCategory] = None
    ) -> Dict[str, Any]:
        """
        Assess risk for a proposed action.
        
        Args:
            action: Proposed action to assess
            context: Current context and state
            category: Specific risk category to assess
            
        Returns:
            Risk assessment result
        """
        try:
            assessment = {
                "action_id": action.get("id", "unknown"),
                "timestamp": datetime.utcnow().isoformat(),
                "risks": [],
                "overall_risk_score": 0.0,
                "risk_level": RiskLevel.MINIMAL,
                "recommendations": []
            }
            
            # Assess different risk dimensions
            financial_risk = self._assess_financial_risk(action, context)
            operational_risk = self._assess_operational_risk(action, context)
            strategic_risk = self._assess_strategic_risk(action, context)
            technical_risk = self._assess_technical_risk(action, context)
            
            risks = [
                {"category": RiskCategory.FINANCIAL, "score": financial_risk},
                {"category": RiskCategory.OPERATIONAL, "score": operational_risk},
                {"category": RiskCategory.STRATEGIC, "score": strategic_risk},
                {"category": RiskCategory.TECHNICAL, "score": technical_risk}
            ]
            
            # Filter by category if specified
            if category:
                risks = [r for r in risks if r["category"] == category]
            
            assessment["risks"] = risks
            
            # Calculate overall risk score (weighted average)
            weights = {
                RiskCategory.FINANCIAL: 0.3,
                RiskCategory.OPERATIONAL: 0.25,
                RiskCategory.STRATEGIC: 0.25,
                RiskCategory.TECHNICAL: 0.2
            }
            
            overall_score = sum(
                r["score"] * weights.get(r["category"], 0.25) 
                for r in risks
            )
            assessment["overall_risk_score"] = overall_score
            
            # Determine risk level
            assessment["risk_level"] = self._determine_risk_level(overall_score)
            
            # Generate recommendations
            assessment["recommendations"] = await self._generate_recommendations(
                assessment["risk_level"], 
                risks,
                action
            )
            
            # Store assessment
            self.risk_assessments.append(assessment)
            
            logger.info(
                f"Risk assessment completed: {assessment['risk_level']} "
                f"(score: {overall_score:.2f})"
            )
            
            return assessment
            
        except Exception as e:
            logger.error(f"Risk assessment failed: {e}")
            return {
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat(),
                "overall_risk_score": 1.0,
                "risk_level": RiskLevel.CRITICAL
            }
    
    def _assess_financial_risk(self, action: Dict[str, Any], context: Dict[str, Any]) -> float:
        """Assess financial risk."""
        cost = action.get("cost", 0)
        budget = context.get("budget", 1000)
        
        if budget == 0:
            return 1.0
        
        cost_ratio = cost / budget
        return min(cost_ratio, 1.0)
    
    def _assess_operational_risk(self, action: Dict[str, Any], context: Dict[str, Any]) -> float:
        """Assess operational risk."""
        complexity = action.get("complexity", 0.5)
        dependencies = len(action.get("dependencies", []))
        
        # Higher complexity and dependencies increase risk
        risk = (complexity + dependencies * 0.1) / 1.5
        return min(risk, 1.0)
    
    def _assess_strategic_risk(self, action: Dict[str, Any], context: Dict[str, Any]) -> float:
        """Assess strategic risk."""
        alignment = action.get("strategic_alignment", 0.5)
        impact = action.get("impact", 0.5)
        
        # Lower alignment increases risk
        risk = 1.0 - (alignment * impact)
        return min(risk, 1.0)
    
    def _assess_technical_risk(self, action: Dict[str, Any], context: Dict[str, Any]) -> float:
        """Assess technical risk."""
        reliability = action.get("reliability", 0.8)
        scalability = action.get("scalability", 0.7)
        security = action.get("security", 0.9)
        
        # Average of risk factors (inverse of positive metrics)
        risk = 1.0 - ((reliability + scalability + security) / 3.0)
        return min(risk, 1.0)
    
    def _determine_risk_level(self, score: float) -> RiskLevel:
        """Determine risk level from score."""
        if score >= self.risk_thresholds[RiskLevel.CRITICAL]:
            return RiskLevel.CRITICAL
        elif score >= self.risk_thresholds[RiskLevel.HIGH]:
            return RiskLevel.HIGH
        elif score >= self.risk_thresholds[RiskLevel.MEDIUM]:
            return RiskLevel.MEDIUM
        elif score >= self.risk_thresholds[RiskLevel.LOW]:
            return RiskLevel.LOW
        else:
            return RiskLevel.MINIMAL
    
    async def _generate_recommendations(
        self, 
        risk_level: RiskLevel, 
        risks: List[Dict[str, Any]],
        action: Dict[str, Any]
    ) -> List[str]:
        """Generate risk mitigation recommendations."""
        recommendations = []
        
        if risk_level in [RiskLevel.CRITICAL, RiskLevel.HIGH]:
            recommendations.append("Consider alternative actions with lower risk")
            recommendations.append("Implement additional safeguards and monitoring")
        
        # Category-specific recommendations
        for risk in risks:
            if risk["score"] > 0.7:
                category = risk["category"]
                if category == RiskCategory.FINANCIAL:
                    recommendations.append("Review budget allocation and cost optimization")
                elif category == RiskCategory.OPERATIONAL:
                    recommendations.append("Simplify operation or reduce dependencies")
                elif category == RiskCategory.STRATEGIC:
                    recommendations.append("Ensure better alignment with strategic goals")
                elif category == RiskCategory.TECHNICAL:
                    recommendations.append("Enhance technical reliability and security measures")
        
        if not recommendations:
            recommendations.append("Risk level acceptable, proceed with caution")
        
        return recommendations
    
    async def add_mitigation_strategy(
        self, 
        risk_category: RiskCategory, 
        strategy: Dict[str, Any]
    ) -> bool:
        """
        Add a mitigation strategy for a risk category.
        
        Args:
            risk_category: Risk category
            strategy: Mitigation strategy details
            
        Returns:
            Success status
        """
        try:
            if risk_category not in self.mitigation_strategies:
                self.mitigation_strategies[risk_category] = []
            
            strategy["added_at"] = datetime.utcnow().isoformat()
            self.mitigation_strategies[risk_category].append(strategy)
            
            logger.info(f"Added mitigation strategy for {risk_category}")
            return True
        except Exception as e:
            logger.error(f"Failed to add mitigation strategy: {e}")
            return False
    
    async def get_risk_profile(self) -> Dict[str, Any]:
        """Get overall risk profile based on historical assessments."""
        if not self.risk_assessments:
            return {
                "total_assessments": 0,
                "average_risk_score": 0.0,
                "risk_distribution": {},
                "status": "no_data"
            }
        
        scores = [a["overall_risk_score"] for a in self.risk_assessments]
        levels = [a["risk_level"] for a in self.risk_assessments]
        
        # Risk distribution
        risk_distribution = {}
        for level in RiskLevel:
            risk_distribution[level.value] = levels.count(level)
        
        return {
            "total_assessments": len(self.risk_assessments),
            "average_risk_score": np.mean(scores),
            "median_risk_score": np.median(scores),
            "max_risk_score": np.max(scores),
            "risk_distribution": risk_distribution,
            "status": "operational"
        }
    
    async def get_risk_status(self) -> Dict[str, Any]:
        """Get current status of Risk Layer."""
        return {
            "total_assessments": len(self.risk_assessments),
            "active_rules": len(self.risk_rules),
            "mitigation_strategies": sum(len(v) for v in self.mitigation_strategies.values()),
            "status": "operational"
        }
