"""
🧠 NEXUS-9: Collective Intelligence & Global Decision Platform
World's First Decentralized Human-AI Collaboration Network
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
from datetime import datetime, timedelta
import time
import json
import random
import hashlib
import asyncio
from typing import Dict, List, Optional, Tuple, Set
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="🧠 NEXUS-9 - Collective Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .nexus-title {
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.3);
    }
    
    .nexus-subtitle {
        text-align: center;
        color: #888;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        letter-spacing: 1px;
    }
    
    .brain-cell {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        border: 2px solid transparent;
        transition: all 0.3s ease;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .brain-cell::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #667eea, #764ba2, #667eea);
        z-index: -1;
        border-radius: 17px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .brain-cell:hover::before {
        opacity: 1;
    }
    
    .brain-cell:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
    }
    
    .synapse {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #667eea;
    }
    
    .problem-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
    }
    
    .solution-card {
        background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
    }
    
    .contribution-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    
    .vote-button {
        background: transparent;
        border: 2px solid #667eea;
        color: #667eea;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .vote-button:hover {
        background: #667eea;
        color: white;
    }
    
    .neuron-pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .impact-meter {
        height: 10px;
        background: linear-gradient(90deg, #ff6b6b, #ffa726, #4caf50);
        border-radius: 5px;
        margin: 10px 0;
    }
    
    .leaderboard-item {
        padding: 15px;
        margin: 5px 0;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .consensus-bar {
        height: 20px;
        background: linear-gradient(90deg, #ff4444, #ffbb33, #00C851);
        border-radius: 10px;
        margin: 10px 0;
        position: relative;
    }
    
    .consensus-indicator {
        position: absolute;
        top: -5px;
        width: 30px;
        height: 30px;
        background: white;
        border-radius: 50%;
        border: 3px solid #333;
        transform: translateX(-15px);
    }
</style>
""", unsafe_allow_html=True)

# ==================== GLOBAL PROBLEM DATABASE ====================
class GlobalProblemDatabase:
    """Database of world's most critical problems"""
    
    def __init__(self):
        self.problems = self._initialize_problems()
        self.solutions = {}
        self.contributions = []
        
    def _initialize_problems(self):
        """Initialize with real-world critical problems"""
        return [
            {
                "id": "P001",
                "title": "🌍 Climate Change Acceleration",
                "description": "Global temperatures rising 0.2°C per decade, extreme weather events increasing 300%",
                "urgency": 95,
                "complexity": 90,
                "impact": 100,
                "affected_people": "8.1 billion",
                "economic_cost": "$500T by 2100",
                "category": "environment",
                "tags": ["climate", "environment", "sustainability"],
                "progress": 35,
                "last_updated": datetime.now()
            },
            {
                "id": "P002",
                "title": "💊 Global Healthcare Inequality",
                "description": "2 billion people lack access to essential medicines, life expectancy gap of 20 years between countries",
                "urgency": 90,
                "complexity": 85,
                "impact": 95,
                "affected_people": "2 billion",
                "economic_cost": "$300B/year",
                "category": "health",
                "tags": ["healthcare", "medicine", "equality"],
                "progress": 40,
                "last_updated": datetime.now()
            },
            {
                "id": "P003",
                "title": "🎓 Education Access Crisis",
                "description": "260 million children out of school, 750 million adults illiterate",
                "urgency": 85,
                "complexity": 80,
                "impact": 90,
                "affected_people": "1 billion",
                "economic_cost": "$100T lifetime loss",
                "category": "education",
                "tags": ["education", "literacy", "opportunity"],
                "progress": 45,
                "last_updated": datetime.now()
            },
            {
                "id": "P004",
                "title": "⚡ Energy Transition Gap",
                "description": "80% energy still from fossil fuels, renewable transition 30 years behind schedule",
                "urgency": 88,
                "complexity": 87,
                "impact": 92,
                "affected_people": "8.1 billion",
                "economic_cost": "$200T needed",
                "category": "energy",
                "tags": ["energy", "renewable", "transition"],
                "progress": 38,
                "last_updated": datetime.now()
            },
            {
                "id": "P005",
                "title": "🏛️ Political Corruption & Instability",
                "description": "$2.6T lost annually to corruption, 60 countries at high risk of conflict",
                "urgency": 82,
                "complexity": 95,
                "impact": 88,
                "affected_people": "4 billion",
                "economic_cost": "$2.6T/year",
                "category": "governance",
                "tags": ["corruption", "governance", "transparency"],
                "progress": 30,
                "last_updated": datetime.now()
            },
            {
                "id": "P006",
                "title": "💧 Water Scarcity Crisis",
                "description": "4 billion people face severe water scarcity, 70% freshwater used by agriculture",
                "urgency": 87,
                "complexity": 83,
                "impact": 91,
                "affected_people": "4 billion",
                "economic_cost": "$500B/year",
                "category": "resources",
                "tags": ["water", "scarcity", "agriculture"],
                "progress": 42,
                "last_updated": datetime.now()
            },
            {
                "id": "P007",
                "title": "🤖 AI Alignment & Job Displacement",
                "description": "300M jobs at risk from AI, no global framework for ethical AI development",
                "urgency": 84,
                "complexity": 92,
                "impact": 87,
                "affected_people": "300 million workers",
                "economic_cost": "$15T transition cost",
                "category": "technology",
                "tags": ["ai", "employment", "ethics"],
                "progress": 25,
                "last_updated": datetime.now()
            },
            {
                "id": "P008",
                "title": "🌾 Food Security Threat",
                "description": "828 million people hungry, 30% food wasted, climate impacting crop yields",
                "urgency": 86,
                "complexity": 81,
                "impact": 89,
                "affected_people": "828 million",
                "economic_cost": "$1T/year",
                "category": "food",
                "tags": ["hunger", "agriculture", "waste"],
                "progress": 48,
                "last_updated": datetime.now()
            }
        ]
    
    def get_problem_by_id(self, problem_id):
        """Get problem by ID"""
        for problem in self.problems:
            if problem["id"] == problem_id:
                return problem
        return None
    
    def add_solution(self, problem_id, solution_data):
        """Add solution to problem"""
        if problem_id not in self.solutions:
            self.solutions[problem_id] = []
        
        solution_data["id"] = f"S{len(self.solutions[problem_id])+1:03d}"
        solution_data["timestamp"] = datetime.now()
        solution_data["votes"] = {"up": 0, "down": 0}
        solution_data["contributors"] = []
        
        self.solutions[problem_id].append(solution_data)
        return solution_data
    
    def vote_on_solution(self, problem_id, solution_id, vote_type):
        """Vote on a solution"""
        if problem_id in self.solutions:
            for solution in self.solutions[problem_id]:
                if solution["id"] == solution_id:
                    if vote_type == "up":
                        solution["votes"]["up"] += 1
                    elif vote_type == "down":
                        solution["votes"]["down"] += 1
                    return True
        return False
    
    def add_contribution(self, problem_id, solution_id, contribution):
        """Add contribution to solution"""
        self.contributions.append({
            "problem_id": problem_id,
            "solution_id": solution_id,
            "contribution": contribution,
            "timestamp": datetime.now(),
            "contributor": "anonymous"
        })

# ==================== COLLECTIVE INTELLIGENCE ENGINE ====================
class CollectiveIntelligenceEngine:
    """Engine for collective intelligence processing"""
    
    def __init__(self):
        self.neurons = {}  # Users as neurons
        self.synapses = []  # Connections between users
        self.consensus_history = []
        
    def add_neuron(self, user_id, expertise):
        """Add user as neuron"""
        self.neurons[user_id] = {
            "id": user_id,
            "expertise": expertise,
            "contribution_score": 0,
            "influence": 1.0,
            "connections": [],
            "last_active": datetime.now()
        }
        return self.neurons[user_id]
    
    def create_synapse(self, from_user, to_user, strength):
        """Create connection between users"""
        synapse = {
            "id": f"SYN{len(self.synapses)+1:04d}",
            "from": from_user,
            "to": to_user,
            "strength": strength,
            "created": datetime.now()
        }
        self.synapses.append(synapse)
        
        # Update neuron connections
        if from_user in self.neurons:
            self.neurons[from_user]["connections"].append(to_user)
        if to_user in self.neurons:
            self.neurons[to_user]["connections"].append(from_user)
        
        return synapse
    
    def calculate_consensus(self, votes):
        """Calculate consensus from votes"""
        if not votes:
            return 50  # Neutral
        
        total = len(votes)
        positive = sum(1 for v in votes if v > 0)
        
        consensus = (positive / total) * 100
        self.consensus_history.append({
            "timestamp": datetime.now(),
            "consensus": consensus,
            "total_votes": total
        })
        
        return consensus
    
    def predict_outcome(self, problem_data, solutions):
        """Predict outcome based on collective intelligence"""
        # Factors: Urgency, Complexity, Progress, Consensus
        urgency = problem_data["urgency"] / 100
        complexity = problem_data["complexity"] / 100
        progress = problem_data["progress"] / 100
        
        # Calculate solution strength
        solution_strength = 0
        if solutions:
            total_votes = sum(s["votes"]["up"] + s["votes"]["down"] for s in solutions)
            if total_votes > 0:
                positive_votes = sum(s["votes"]["up"] for s in solutions)
                solution_strength = positive_votes / total_votes
        
        # Prediction formula
        prediction = (
            (urgency * 0.3) +
            ((1 - complexity) * 0.2) +
            (progress * 0.3) +
            (solution_strength * 0.2)
        ) * 100
        
        return min(100, max(0, prediction))
    
    def generate_insights(self, problem, solutions, contributions):
        """Generate AI insights from collective data"""
        insights = []
        
        # Insight 1: Problem complexity analysis
        if problem["complexity"] > 80:
            insights.append("🔍 **High Complexity Detected**: This problem requires multi-disciplinary approach")
        
        # Insight 2: Progress tracking
        if problem["progress"] < 30:
            insights.append("🚨 **Critical Progress Gap**: Acceleration needed in solution implementation")
        elif problem["progress"] > 70:
            insights.append("✅ **Good Progress**: Maintain momentum for completion")
        
        # Insight 3: Solution diversity
        if solutions and len(solutions) > 5:
            insights.append("💡 **Diverse Solutions Available**: Multiple approaches being explored")
        
        # Insight 4: Contribution patterns
        if contributions and len(contributions) > 50:
            insights.append("🤝 **Strong Community Engagement**: Collective intelligence emerging")
        
        # Insight 5: Urgency warning
        if problem["urgency"] > 90:
            insights.append("⏰ **Extreme Urgency**: Immediate action required")
        
        return insights

# ==================== DECISION MARKET ====================
class DecisionMarket:
    """Prediction market for problem outcomes"""
    
    def __init__(self):
        self.markets = {}
        self.trades = []
        self.portfolio = {}
        
    def create_market(self, problem_id, description):
        """Create prediction market for problem"""
        market_id = f"M{len(self.markets)+1:03d}"
        
        self.markets[market_id] = {
            "id": market_id,
            "problem_id": problem_id,
            "description": description,
            "yes_price": 50,  # Probability in percentage
            "no_price": 50,
            "volume": 0,
            "liquidity": 10000,
            "resolved": False,
            "created": datetime.now()
        }
        
        return self.markets[market_id]
    
    def trade(self, market_id, user_id, direction, amount, price):
        """Execute trade in prediction market"""
        trade_id = f"T{len(self.trades)+1:04d}"
        
        trade = {
            "id": trade_id,
            "market_id": market_id,
            "user_id": user_id,
            "direction": direction,  # "yes" or "no"
            "amount": amount,
            "price": price,
            "timestamp": datetime.now()
        }
        
        self.trades.append(trade)
        
        # Update market prices based on trade
        market = self.markets[market_id]
        if direction == "yes":
            # Buying yes increases yes price
            market["yes_price"] = min(95, market["yes_price"] + (amount / 100))
            market["no_price"] = 100 - market["yes_price"]
        else:
            # Buying no increases no price
            market["no_price"] = min(95, market["no_price"] + (amount / 100))
            market["yes_price"] = 100 - market["no_price"]
        
        market["volume"] += amount
        
        # Update user portfolio
        if user_id not in self.portfolio:
            self.portfolio[user_id] = {}
        
        if market_id not in self.portfolio[user_id]:
            self.portfolio[user_id][market_id] = {"yes": 0, "no": 0}
        
        if direction == "yes":
            self.portfolio[user_id][market_id]["yes"] += amount
        else:
            self.portfolio[user_id][market_id]["no"] += amount
        
        return trade
    
    def calculate_wisdom_of_crowds(self, market_id):
        """Calculate wisdom of crowds from market prices"""
        market = self.markets.get(market_id)
        if not market:
            return None
        
        # Current price reflects collective prediction
        prediction = market["yes_price"]  # Percentage probability of success
        
        # Volume indicates confidence
        confidence = min(100, market["volume"] / 100)
        
        # Number of traders indicates diversity of opinion
        traders = len(set(t["user_id"] for t in self.trades if t["market_id"] == market_id))
        diversity = min(100, traders * 5)
        
        return {
            "prediction": prediction,
            "confidence": confidence,
            "diversity": diversity,
            "wisdom_score": (prediction * confidence * diversity) / 10000
        }

# ==================== IMPACT TRACKER ====================
class ImpactTracker:
    """Track real-world impact of solutions"""
    
    def __init__(self):
        self.impacts = []
        self.metrics = {}
        
    def log_impact(self, problem_id, solution_id, impact_data):
        """Log real-world impact"""
        impact_id = f"I{len(self.impacts)+1:04d}"
        
        impact = {
            "id": impact_id,
            "problem_id": problem_id,
            "solution_id": solution_id,
            "timestamp": datetime.now(),
            "metrics": impact_data,
            "verified": False,
            "verified_by": None
        }
        
        self.impacts.append(impact)
        
        # Update aggregate metrics
        key = f"{problem_id}_{solution_id}"
        if key not in self.metrics:
            self.metrics[key] = []
        
        self.metrics[key].append(impact_data)
        
        return impact
    
    def calculate_total_impact(self, problem_id=None, solution_id=None):
        """Calculate total impact"""
        total = {
            "people_affected": 0,
            "economic_value": 0,
            "co2_reduced": 0,
            "lives_saved": 0,
            "jobs_created": 0
        }
        
        for impact in self.impacts:
            if problem_id and impact["problem_id"] != problem_id:
                continue
            if solution_id and impact["solution_id"] != solution_id:
                continue
            
            metrics = impact["metrics"]
            total["people_affected"] += metrics.get("people_affected", 0)
            total["economic_value"] += metrics.get("economic_value", 0)
            total["co2_reduced"] += metrics.get("co2_reduced", 0)
            total["lives_saved"] += metrics.get("lives_saved", 0)
            total["jobs_created"] += metrics.get("jobs_created", 0)
        
        return total
    
    def generate_impact_report(self, problem_id):
        """Generate impact report for problem"""
        impacts = [i for i in self.impacts if i["problem_id"] == problem_id]
        
        if not impacts:
            return None
        
        report = {
            "total_impacts": len(impacts),
            "time_span": (datetime.now() - impacts[0]["timestamp"]).days,
            "metrics_summary": self.calculate_total_impact(problem_id),
            "top_contributors": [],
            "trend": "positive" if len(impacts) > 10 else "emerging"
        }
        
        return report

# ==================== MAIN APPLICATION ====================
def main():
    """Main Application"""
    
    # Initialize session state
    if 'problem_db' not in st.session_state:
        st.session_state.problem_db = GlobalProblemDatabase()
    if 'intelligence_engine' not in st.session_state:
        st.session_state.intelligence_engine = CollectiveIntelligenceEngine()
    if 'decision_market' not in st.session_state:
        st.session_state.decision_market = DecisionMarket()
    if 'impact_tracker' not in st.session_state:
        st.session_state.impact_tracker = ImpactTracker()
    if 'user_id' not in st.session_state:
        st.session_state.user_id = f"USER_{hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}"
    if 'user_expertise' not in st.session_state:
        st.session_state.user_expertise = []
    
    # Initialize components
    problem_db = st.session_state.problem_db
    intelligence_engine = st.session_state.intelligence_engine
    decision_market = st.session_state.decision_market
    impact_tracker = st.session_state.impact_tracker
    
    # Add user as neuron
    if st.session_state.user_id not in intelligence_engine.neurons:
        intelligence_engine.add_neuron(
            st.session_state.user_id,
            st.session_state.user_expertise
        )
    
    # Header
    st.markdown('<h1 class="nexus-title">🧠 NEXUS-9</h1>', unsafe_allow_html=True)
    st.markdown('<p class="nexus-subtitle">Collective Intelligence Platform • Global Problem Solving • Real Impact</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3067/3067256.png", width=100)
        
        st.markdown(f"### 👤 Neuron: {st.session_state.user_id[:12]}...")
        
        # User stats
        neuron = intelligence_engine.neurons.get(st.session_state.user_id, {})
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Influence", f"{neuron.get('influence', 1.0):.1f}")
        with col2:
            st.metric("Connections", len(neuron.get('connections', [])))
        
        st.markdown("---")
        st.markdown("### 🎯 Quick Actions")
        
        if st.button("🔍 Find Problem to Solve", use_container_width=True):
            st.session_state.active_tab = "Explore"
            st.rerun()
        
        if st.button("💡 Propose Solution", use_container_width=True):
            st.session_state.active_tab = "Solve"
            st.rerun()
        
        if st.button("📊 View Impact", use_container_width=True):
            st.session_state.active_tab = "Impact"
            st.rerun()
        
        st.markdown("---")
        st.markdown("### 🌐 Global Stats")
        
        total_problems = len(problem_db.problems)
        total_solutions = sum(len(sols) for sols in problem_db.solutions.values())
        total_contributions = len(problem_db.contributions)
        
        st.metric("Active Problems", total_problems)
        st.metric("Solutions", total_solutions)
        st.metric("Contributions", total_contributions)
        
        st.markdown("---")
        st.markdown("### 🏆 Top Neurons This Week")
        
        # Simulated leaderboard
        leaders = [
            {"name": "QuantumThinker", "score": 2450},
            {"name": "ClimateWarrior", "score": 1980},
            {"name": "MedInnovator", "score": 1650},
            {"name": "EduRevolution", "score": 1420},
            {"name": "PolicyGenius", "score": 1280}
        ]
        
        for idx, leader in enumerate(leaders, 1):
            st.write(f"{idx}. **{leader['name']}** - {leader['score']} pts")
        
        st.markdown("---")
        st.markdown("*Be part of the solution*")
    
    # Main Tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🏠 Dashboard", 
        "🔍 Explore Problems", 
        "💡 Solve", 
        "📈 Predict", 
        "📊 Impact", 
        "🧬 Network"
    ])
    
    with tab1:
        # Dashboard
        st.markdown("## 🌍 Global Problem Dashboard")
        
        # Overview metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            avg_urgency = np.mean([p["urgency"] for p in problem_db.problems])
            st.metric("Avg. Urgency", f"{avg_urgency:.0f}/100", delta="Critical" if avg_urgency > 80 else "High")
        
        with col2:
            avg_progress = np.mean([p["progress"] for p in problem_db.problems])
            st.metric("Avg. Progress", f"{avg_progress:.0f}%", delta=f"{avg_progress - 30:.0f}%" if avg_progress > 30 else "-")
        
        with col3:
            total_neurons = len(intelligence_engine.neurons)
            st.metric("Active Neurons", total_neurons, delta="+12 today")
        
        with col4:
            market_volume = sum(m["volume"] for m in decision_market.markets.values())
            st.metric("Market Volume", f"${market_volume:,.0f}")
        
        # Problem matrix
        st.markdown("### 🎯 Problem Matrix")
        
        # Create problem matrix visualization
        problems_df = pd.DataFrame(problem_db.problems)
        
        fig = px.scatter(
            problems_df,
            x='complexity',
            y='urgency',
            size='impact',
            color='category',
            hover_name='title',
            hover_data=['progress', 'affected_people'],
            size_max=50,
            title='Problem Matrix: Urgency vs Complexity'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Recent activity
        st.markdown("### ⚡ Recent Collective Activity")
        
        col_act1, col_act2, col_act3 = st.columns(3)
        
        with col_act1:
            st.markdown("""
            <div class="brain-cell">
                <h4>🎯 New Focus</h4>
                <p><strong>AI Ethics Framework</strong></p>
                <p>1,245 neurons collaborating</p>
                <div class="impact-meter" style="width: 65%;"></div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_act2:
            st.markdown("""
            <div class="brain-cell">
                <h4>💡 Breakthrough</h4>
                <p><strong>Carbon Capture Tech</strong></p>
                <p>92% consensus reached</p>
                <div class="impact-meter" style="width: 78%;"></div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_act3:
            st.markdown("""
            <div class="brain-cell">
                <h4>🤝 Collaboration</h4>
                <p><strong>Global Education Initiative</strong></p>
                <p>43 countries participating</p>
                <div class="impact-meter" style="width: 55%;"></div>
            </div>
            """, unsafe_allow_html=True)
        
        # Collective insights
        st.markdown("### 🧠 Collective Insights")
        
        all_insights = []
        for problem in problem_db.problems[:3]:
            solutions = problem_db.solutions.get(problem["id"], [])
            contributions = [c for c in problem_db.contributions if c["problem_id"] == problem["id"]]
            
            insights = intelligence_engine.generate_insights(problem, solutions, contributions)
            all_insights.extend(insights)
        
        for insight in all_insights[:5]:
            st.markdown(f'<div class="synapse">{insight}</div>', unsafe_allow_html=True)
    
    with tab2:
        # Explore Problems
        st.markdown("## 🔍 Explore Global Problems")
        
        # Filter options
        col_filter1, col_filter2, col_filter3 = st.columns(3)
        
        with col_filter1:
            category_filter = st.selectbox(
                "Category",
                ["All", "environment", "health", "education", "energy", "governance", "resources", "technology", "food"]
            )
        
        with col_filter2:
            urgency_filter = st.slider("Minimum Urgency", 0, 100, 70)
        
        with col_filter3:
            sort_by = st.selectbox(
                "Sort by",
                ["Urgency", "Progress", "Complexity", "Impact"]
            )
        
        # Filter problems
        filtered_problems = problem_db.problems
        
        if category_filter != "All":
            filtered_problems = [p for p in filtered_problems if p["category"] == category_filter]
        
        filtered_problems = [p for p in filtered_problems if p["urgency"] >= urgency_filter]
        
        # Sort
        if sort_by == "Urgency":
            filtered_problems.sort(key=lambda x: x["urgency"], reverse=True)
        elif sort_by == "Progress":
            filtered_problems.sort(key=lambda x: x["progress"], reverse=True)
        elif sort_by == "Complexity":
            filtered_problems.sort(key=lambda x: x["complexity"], reverse=True)
        elif sort_by == "Impact":
            filtered_problems.sort(key=lambda x: x["impact"], reverse=True)
        
        # Display problems
        for problem in filtered_problems:
            st.markdown(f"""
            <div class="problem-card">
                <h3>{problem['title']}</h3>
                <p>{problem['description']}</p>
                <div style="display: flex; justify-content: space-between; margin-top: 15px;">
                    <span>🚨 Urgency: {problem['urgency']}/100</span>
                    <span>🎯 Progress: {problem['progress']}%</span>
                    <span>👥 Affected: {problem['affected_people']}</span>
                    <span>💰 Cost: {problem['economic_cost']}</span>
                </div>
                <div class="impact-meter" style="width: {problem['progress']}%; margin-top: 10px;"></div>
            </div>
            """, unsafe_allow_html=True)
            
            # Problem details and actions
            with st.expander(f"Details & Solutions for {problem['title']}"):
                col_detail1, col_detail2 = st.columns(2)
                
                with col_detail1:
                    st.markdown("**📊 Problem Metrics:**")
                    st.write(f"- Complexity: {problem['complexity']}/100")
                    st.write(f"- Impact Score: {problem['impact']}/100")
                    st.write(f"- Last Updated: {problem['last_updated'].strftime('%Y-%m-%d')}")
                    st.write(f"- Tags: {', '.join(problem['tags'])}")
                
                with col_detail2:
                    st.markdown("**🚀 Take Action:**")
                    
                    if st.button(f"💡 Propose Solution", key=f"propose_{problem['id']}"):
                        st.session_state.selected_problem = problem['id']
                        st.session_state.active_tab = "Solve"
                        st.rerun()
                    
                    if st.button(f"📈 Predict Outcome", key=f"predict_{problem['id']}"):
                        st.session_state.selected_problem = problem['id']
                        st.session_state.active_tab = "Predict"
                        st.rerun()
                    
                    if st.button(f"🤝 Join Discussion", key=f"discuss_{problem['id']}"):
                        st.session_state.selected_problem = problem['id']
                        st.rerun()
                
                # Show existing solutions
                solutions = problem_db.solutions.get(problem["id"], [])
                if solutions:
                    st.markdown("**💡 Existing Solutions:**")
                    
                    for solution in solutions[:3]:  # Show top 3
                        vote_ratio = solution["votes"]["up"] / max(1, solution["votes"]["up"] + solution["votes"]["down"])
                        
                        st.markdown(f"""
                        <div class="solution-card">
                            <h4>{solution.get('title', 'Solution')} ({vote_ratio*100:.0f}% approval)</h4>
                            <p>{solution.get('description', '')[:200]}...</p>
                            <div style="display: flex; gap: 10px; margin-top: 10px;">
                                <button class="vote-button" onclick="voteUp('{problem['id']}', '{solution['id']}')">👍 {solution['votes']['up']}</button>
                                <button class="vote-button" onclick="voteDown('{problem['id']}', '{solution['id']}')">👎 {solution['votes']['down']}</button>
                                <button class="vote-button">💬 Discuss</button>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
    
    with tab3:
        # Solve Problems
        st.markdown("## 💡 Propose & Improve Solutions")
        
        # Problem selection
        if 'selected_problem' in st.session_state:
            problem = problem_db.get_problem_by_id(st.session_state.selected_problem)
        else:
            problem_options = {p["id"]: p["title"] for p in problem_db.problems}
            selected_id = st.selectbox("Select Problem", options=list(problem_options.keys()), 
                                      format_func=lambda x: problem_options[x])
            problem = problem_db.get_problem_by_id(selected_id)
        
        if problem:
            st.markdown(f"""
            <div class="problem-card">
                <h3>{problem['title']}</h3>
                <p>{problem['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Solution proposal form
            st.markdown("### 🚀 Propose New Solution")
            
            with st.form(key="solution_form"):
                solution_title = st.text_input("Solution Title", 
                                              placeholder="e.g., Global Carbon Tax with Redistribution")
                
                solution_desc = st.text_area("Detailed Solution Description", height=200,
                                           placeholder="Describe your solution in detail...")
                
                solution_approach = st.selectbox("Primary Approach", 
                                                ["Technological", "Policy", "Economic", "Social", "Educational", "Hybrid"])
                
                estimated_cost = st.number_input("Estimated Cost (USD)", 
                                                min_value=0, 
                                                max_value=1000000000000, 
                                                value=1000000,
                                                step=1000000)
                
                timeline_years = st.slider("Estimated Timeline (years)", 1, 50, 10)
                
                feasibility = st.slider("Feasibility Score", 1, 100, 50)
                
                # Resources needed
                st.markdown("**Required Resources:**")
                col_res1, col_res2 = st.columns(2)
                with col_res1:
                    tech_resources = st.text_area("Technology", placeholder="Hardware, software, etc.")
                with col_res2:
                    human_resources = st.text_area("Human Resources", placeholder="Experts, workforce, etc.")
                
                submitted = st.form_submit_button("Submit Solution")
                
                if submitted and solution_title and solution_desc:
                    solution_data = {
                        "title": solution_title,
                        "description": solution_desc,
                        "approach": solution_approach,
                        "estimated_cost": f"${estimated_cost:,}",
                        "timeline_years": timeline_years,
                        "feasibility": feasibility,
                        "resources": {
                            "technology": tech_resources,
                            "human": human_resources
                        },
                        "proposer": st.session_state.user_id
                    }
                    
                    solution = problem_db.add_solution(problem["id"], solution_data)
                    
                    st.success("✅ Solution submitted to the collective!")
                    
                    # Add contribution
                    contribution = {
                        "type": "solution_proposal",
                        "details": f"Proposed solution: {solution_title}",
                        "impact_potential": "high"
                    }
                    
                    problem_db.add_contribution(problem["id"], solution["id"], contribution)
                    
                    # Create prediction market for this solution
                    market_desc = f"Will solution '{solution_title}' achieve 50% of its goals within {timeline_years} years?"
                    decision_market.create_market(problem["id"], market_desc)
            
            # Existing solutions to improve
            st.markdown("### 🔧 Improve Existing Solutions")
            
            solutions = problem_db.solutions.get(problem["id"], [])
            if solutions:
                for solution in solutions:
                    with st.expander(f"Improve: {solution.get('title', 'Untitled')}"):
                        col_imp1, col_imp2 = st.columns(2)
                        
                        with col_imp1:
                            st.markdown("**Current Solution:**")
                            st.write(solution.get('description', '')[:500] + "...")
                            st.write(f"**Feasibility:** {solution.get('feasibility', 'N/A')}")
                            st.write(f"**Cost:** {solution.get('estimated_cost', 'N/A')}")
                        
                        with col_imp2:
                            improvement = st.text_area(
                                f"Your improvement for {solution.get('title', 'this solution')}",
                                placeholder="Suggest improvements, identify gaps, propose alternatives...",
                                key=f"improve_{solution['id']}"
                            )
                            
                            if st.button("Submit Improvement", key=f"submit_imp_{solution['id']}"):
                                if improvement:
                                    contribution = {
                                        "type": "solution_improvement",
                                        "details": improvement,
                                        "original_solution": solution.get('title', '')
                                    }
                                    
                                    problem_db.add_contribution(problem["id"], solution["id"], contribution)
                                    st.success("Improvement submitted!")
            
            # Collective brainstorming
            st.markdown("### 🧠 Collective Brainstorming")
            
            brainstorm_topic = st.text_input("Start new brainstorming topic", 
                                           placeholder="e.g., How to implement this solution in developing countries?")
            
            if brainstorm_topic:
                st.info(f"Brainstorming: {brainstorm_topic}")
                
                # Simulated collective responses
                responses = [
                    "We could use blockchain for transparent fund distribution.",
                    "Local communities should be involved in implementation.",
                    "Partner with universities for research and development.",
                    "Create incentive programs for early adopters.",
                    "Use AI to optimize resource allocation."
                ]
                
                for response in responses:
                    st.markdown(f'<div class="contribution-card">{response}</div>', unsafe_allow_html=True)
                
                # User can add response
                user_response = st.text_area("Add your idea", key="brainstorm_response")
                
                if st.button("Submit Idea"):
                    if user_response:
                        contribution = {
                            "type": "brainstorming",
                            "topic": brainstorm_topic,
                            "idea": user_response
                        }
                        
                        problem_db.add_contribution(problem["id"], "BRAINSTORM", contribution)
                        st.success("Idea added to collective brainstorming!")
    
    with tab4:
        # Prediction Markets
        st.markdown("## 📈 Prediction Markets")
        
        col_pred1, col_pred2 = st.columns([2, 1])
        
        with col_pred1:
            st.markdown("### 🎯 Active Prediction Markets")
            
            for market_id, market in decision_market.markets.items():
                problem = problem_db.get_problem_by_id(market["problem_id"])
                problem_title = problem["title"] if problem else "Unknown Problem"
                
                wisdom = decision_market.calculate_wisdom_of_crowds(market_id)
                
                st.markdown(f"""
                <div class="brain-cell">
                    <h4>{problem_title}</h4>
                    <p>{market['description']}</p>
                    <div style="display: flex; justify-content: space-between; margin: 15px 0;">
                        <div>
                            <strong>YES:</strong> ${market['yes_price']:.1f}
                            <div style="background: #4CAF50; height: 10px; width: {market['yes_price']}%; border-radius: 5px;"></div>
                        </div>
                        <div>
                            <strong>NO:</strong> ${market['no_price']:.1f}
                            <div style="background: #f44336; height: 10px; width: {market['no_price']}%; border-radius: 5px;"></div>
                        </div>
                    </div>
                    <p>Volume: ${market['volume']:,.0f} • Wisdom Score: {wisdom['wisdom_score']:.2f}/100</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Trading interface
                with st.expander(f"Trade on {problem_title[:30]}..."):
                    col_trade1, col_trade2 = st.columns(2)
                    
                    with col_trade1:
                        trade_direction = st.radio("Direction", ["YES", "NO"], key=f"dir_{market_id}")
                        trade_amount = st.number_input("Amount ($)", min_value=10, max_value=10000, value=100, 
                                                      key=f"amt_{market_id}")
                    
                    with col_trade2:
                        current_price = market['yes_price'] if trade_direction == "YES" else market['no_price']
                        st.write(f"Current Price: ${current_price:.2f}")
                        st.write(f"Potential Return: ${trade_amount * (100/current_price - 1):.2f}")
                        
                        if st.button(f"Trade {trade_direction}", key=f"trade_{market_id}"):
                            trade = decision_market.trade(
                                market_id,
                                st.session_state.user_id,
                                trade_direction.lower(),
                                trade_amount,
                                current_price
                            )
                            st.success(f"Trade executed! ID: {trade['id']}")
        
        with col_pred2:
            st.markdown("### 🏆 Your Portfolio")
            
            portfolio = decision_market.portfolio.get(st.session_state.user_id, {})
            
            if portfolio:
                total_value = 0
                for market_id, positions in portfolio.items():
                    market = decision_market.markets.get(market_id)
                    if market:
                        position_value = (
                            positions.get("yes", 0) * (market["yes_price"] / 100) +
                            positions.get("no", 0) * (market["no_price"] / 100)
                        )
                        total_value += position_value
                        
                        st.write(f"**{market_id}:**")
                        st.write(f"YES: ${positions.get('yes', 0):.0f}")
                        st.write(f"NO: ${positions.get('no', 0):.0f}")
                        st.write(f"Value: ${position_value:.0f}")
                        st.write("---")
                
                st.metric("Total Portfolio Value", f"${total_value:,.0f}")
            else:
                st.info("No positions yet. Start trading!")
            
            st.markdown("---")
            st.markdown("### 🧠 Collective Wisdom")
            
            # Wisdom of crowds visualization
            wisdom_data = []
            for market_id, market in decision_market.markets.items():
                wisdom = decision_market.calculate_wisdom_of_crowds(market_id)
                if wisdom:
                    wisdom_data.append({
                        "market": market_id,
                        "prediction": wisdom["prediction"],
                        "confidence": wisdom["confidence"],
                        "diversity": wisdom["diversity"]
                    })
            
            if wisdom_data:
                wisdom_df = pd.DataFrame(wisdom_data)
                
                fig = go.Figure(data=[
                    go.Scatter3d(
                        x=wisdom_df['prediction'],
                        y=wisdom_df['confidence'],
                        z=wisdom_df['diversity'],
                        mode='markers',
                        marker=dict(
                            size=12,
                            color=wisdom_df['prediction'],
                            colorscale='Viridis',
                            showscale=True
                        ),
                        text=wisdom_df['market']
                    )
                ])
                
                fig.update_layout(
                    title='Wisdom of Crowds in 3D',
                    scene=dict(
                        xaxis_title='Prediction',
                        yaxis_title='Confidence',
                        zaxis_title='Diversity'
                    ),
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
    
    with tab5:
        # Impact Tracking
        st.markdown("## 📊 Real Impact Tracking")
        
        # Overall impact
        total_impact = impact_tracker.calculate_total_impact()
        
        col_imp1, col_imp2, col_imp3, col_imp4 = st.columns(4)
        
        with col_imp1:
            st.metric("People Affected", f"{total_impact['people_affected']:,.0f}")
        
        with col_imp2:
            st.metric("Economic Value", f"${total_impact['economic_value']:,.0f}")
        
        with col_imp3:
            st.metric("CO₂ Reduced", f"{total_impact['co2_reduced']:,.0f} tons")
        
        with col_imp4:
            st.metric("Lives Saved", f"{total_impact['lives_saved']:,.0f}")
        
        # Impact by problem
        st.markdown("### 🎯 Impact by Problem Area")
        
        impact_by_problem = []
        for problem in problem_db.problems:
            problem_impact = impact_tracker.calculate_total_impact(problem_id=problem["id"])
            if any(problem_impact.values()):
                impact_by_problem.append({
                    "problem": problem["title"],
                    "people": problem_impact["people_affected"],
                    "economic": problem_impact["economic_value"],
                    "co2": problem_impact["co2_reduced"]
                })
        
        if impact_by_problem:
            impact_df = pd.DataFrame(impact_by_problem)
            
            fig = px.bar(
                impact_df,
                x='problem',
                y=['people', 'economic', 'co2'],
                title='Impact Metrics by Problem Area',
                barmode='group'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Success stories
        st.markdown("### 🌟 Success Stories")
        
        success_stories = [
            {
                "title": "Clean Water in Rural India",
                "problem": "Water Scarcity Crisis",
                "impact": "2 million people gained access to clean water",
                "solution": "Community-managed water purification systems",
                "neurons": "5,432 contributors",
                "timeline": "18 months"
            },
            {
                "title": "Digital Education in Africa",
                "problem": "Education Access Crisis",
                "impact": "500,000 students now using digital learning",
                "solution": "Offline digital classroom kits",
                "neurons": "8,912 contributors",
                "timeline": "2 years"
            },
            {
                "title": "Renewable Energy Microgrids",
                "problem": "Energy Transition Gap",
                "impact": "200 villages now 100% renewable powered",
                "solution": "Community-owned solar microgrids",
                "neurons": "12,345 contributors",
                "timeline": "3 years"
            }
        ]
        
        for story in success_stories:
            st.markdown(f"""
            <div class="solution-card">
                <h4>{story['title']}</h4>
                <p><strong>Problem:</strong> {story['problem']}</p>
                <p><strong>Impact:</strong> {story['impact']}</p>
                <p><strong>Solution:</strong> {story['solution']}</p>
                <div style="display: flex; justify-content: space-between; margin-top: 15px;">
                    <span>🧠 {story['neurons']}</span>
                    <span>⏱️ {story['timeline']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Log new impact
        st.markdown("### 📝 Log Real-World Impact")
        
        with st.form(key="impact_form"):
            impact_problem = st.selectbox(
                "Problem",
                options=[p["id"] for p in problem_db.problems],
                format_func=lambda x: problem_db.get_problem_by_id(x)["title"]
            )
            
            impact_solution = st.text_input("Solution Implemented")
            
            col_met1, col_met2 = st.columns(2)
            
            with col_met1:
                people_affected = st.number_input("People Affected", min_value=0, value=0)
                economic_value = st.number_input("Economic Value ($)", min_value=0, value=0)
            
            with col_met2:
                co2_reduced = st.number_input("CO₂ Reduced (tons)", min_value=0, value=0)
                lives_saved = st.number_input("Lives Saved", min_value=0, value=0)
            
            impact_description = st.text_area("Impact Description", 
                                            placeholder="Describe the real-world impact...")
            
            if st.form_submit_button("Log Impact"):
                impact_data = {
                    "people_affected": people_affected,
                    "economic_value": economic_value,
                    "co2_reduced": co2_reduced,
                    "lives_saved": lives_saved,
                    "jobs_created": 0,
                    "description": impact_description
                }
                
                impact = impact_tracker.log_impact(
                    impact_problem,
                    "IMP001",  # This would be linked to actual solution ID
                    impact_data
                )
                
                st.success(f"Impact logged! ID: {impact['id']}")
    
    with tab6:
        # Network Visualization
        st.markdown("## 🧬 Neural Network Visualization")
        
        # Create network graph
        G = nx.Graph()
        
        # Add neurons (users)
        for user_id, neuron in intelligence_engine.neurons.items():
            G.add_node(user_id, 
                      size=neuron.get('influence', 1) * 10,
                      color='#667eea',
                      label=user_id[:8])
        
        # Add synapses (connections)
        for synapse in intelligence_engine.synapses[:50]:  # Limit for performance
            G.add_edge(synapse["from"], synapse["to"], 
                      weight=synapse["strength"])
        
        # Generate positions
        pos = nx.spring_layout(G, k=1, iterations=50)
        
        # Create edge trace
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')
        
        # Create node trace
        node_x = []
        node_y = []
        node_text = []
        node_size = []
        node_color = []
        
        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_text.append(G.nodes[node].get('label', node))
            node_size.append(G.nodes[node].get('size', 5))
            node_color.append(G.nodes[node].get('color', '#667eea'))
        
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='YlGnBu',
                size=node_size,
                color=node_color,
                line_width=2))
        
        node_trace.text = node_text
        
        # Create figure
        fig = go.Figure(data=[edge_trace, node_trace],
                       layout=go.Layout(
                           title='Collective Intelligence Network',
                           showlegend=False,
                           hovermode='closest',
                           margin=dict(b=20,l=5,r=5,t=40),
                           xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                           yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                       )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Network statistics
        st.markdown("### 📊 Network Statistics")
        
        col_net1, col_net2, col_net3 = st.columns(3)
        
        with col_net1:
            st.metric("Total Neurons", G.number_of_nodes())
        
        with col_net2:
            st.metric("Total Synapses", G.number_of_edges())
        
        with col_net3:
            if G.number_of_nodes() > 0:
                avg_degree = sum(dict(G.degree()).values()) / G.number_of_nodes()
                st.metric("Avg. Connections", f"{avg_degree:.1f}")
        
        # Most connected neurons
        st.markdown("### 🏆 Most Connected Neurons")
        
        if G.number_of_nodes() > 0:
            degrees = dict(G.degree())
            top_neurons = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:10]
            
            for neuron_id, degree in top_neurons:
                st.markdown(f"""
                <div class="leaderboard-item">
                    <span>{neuron_id[:12]}...</span>
                    <span>{degree} connections</span>
                </div>
                """, unsafe_allow_html=True)
        
        # Create new connection
        st.markdown("### 🤝 Create New Connection")
        
        col_con1, col_con2 = st.columns(2)
        
        with col_con1:
            target_neurons = [n for n in intelligence_engine.neurons.keys() 
                            if n != st.session_state.user_id]
            target_neuron = st.selectbox("Connect to Neuron", target_neurons[:20])
        
        with col_con2:
            connection_strength = st.slider("Connection Strength", 1, 10, 5)
        
        if st.button("Create Connection"):
            synapse = intelligence_engine.create_synapse(
                st.session_state.user_id,
                target_neuron,
                connection_strength
            )
            st.success(f"Connection created! Synapse ID: {synapse['id']}")
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p style="font-size: 1.1rem;">
            🧠 <strong>NEXUS-9 v3.0</strong> | 
            🌍 Collective Intelligence Platform | 
            🎯 Solving Global Problems | 
            🤝 1,234,567 Active Neurons
        </p>
        <p>
            🔗 Every thought contributes | 
            💡 Every solution matters | 
            🌟 Every impact counts
        </p>
        <p style="font-size: 0.9rem; color: #999;">
            © 2024 NEXUS-9 Collective • Join the network: nexus-9.org • 
            Research: MIT Collective Intelligence Lab • 
            Impact: 245 problems actively being solved
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
