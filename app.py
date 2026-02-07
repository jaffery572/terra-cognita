"""
🤖 AI-SPARK: Real-Time Universal AI Assistant
Pakistan ka pehla complete AI solution platform
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import json
import os
import io
from PIL import Image
import base64
from typing import Dict, List, Optional
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="🤖 AI-SPARK - Universal AI Assistant",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }
    
    .card-icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 12px;
        margin: 10px 0;
    }
    
    .solution-box {
        background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
    }
    
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        margin: 10px 0;
    }
    
    .chat-bubble {
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        max-width: 80%;
    }
    
    .user-bubble {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: auto;
    }
    
    .ai-bubble {
        background: #f0f2f6;
        color: #333;
        margin-right: auto;
    }
</style>
""", unsafe_allow_html=True)

# Pakistan-Specific Data
PAKISTAN_DATA = {
    "cities": ["Karachi", "Lahore", "Islamabad", "Rawalpindi", "Faisalabad", "Multan", "Peshawar", "Quetta", "Gujranwala", "Sialkot"],
    "languages": ["Urdu", "Punjabi", "Sindhi", "Pashto", "Balochi", "Saraiki", "English"],
    "emergency_numbers": {
        "Police": "15",
        "Ambulance": "1122",
        "Fire Brigade": "16",
        "Rescue 1122": "1122",
        "Women Helpline": "1099",
        "Child Protection": "1121"
    },
    "government_websites": {
        "NADRA": "https://www.nadra.gov.pk",
        "FBR": "https://www.fbr.gov.pk",
        "HEC": "https://www.hec.gov.pk",
        "Punjab Police": "https://punjabpolice.gov.pk",
        "Sindh Police": "https://sindhpolice.gov.pk"
    }
}

# AI Modules Database
AI_MODULES = {
    "medical": {
        "name": "🏥 Medical Assistant",
        "icon": "🏥",
        "description": "Medical diagnosis, medicine information, doctor recommendations",
        "capabilities": [
            "Symptom checker",
            "Medicine information",
            "Doctor/hospital finder",
            "First aid guidance",
            "Mental health support"
        ]
    },
    "legal": {
        "name": "⚖️ Legal Assistant",
        "icon": "⚖️",
        "description": "Legal advice, document review, lawyer matching",
        "capabilities": [
            "Legal document review",
            "Case analysis",
            "Lawyer matching",
            "Legal rights information",
            "Court procedure guidance"
        ]
    },
    "education": {
        "name": "🎓 Education Assistant",
        "icon": "🎓",
        "description": "Homework help, career guidance, scholarship finder",
        "capabilities": [
            "Homework solutions",
            "Career counseling",
            "Scholarship finder",
            "University admissions",
            "Skill development"
        ]
    },
    "business": {
        "name": "💼 Business Assistant",
        "icon": "💼",
        "description": "Business plans, market analysis, funding guidance",
        "capabilities": [
            "Business plan generator",
            "Market research",
            "Funding opportunities",
            "Tax guidance",
            "Legal compliance"
        ]
    },
    "technical": {
        "name": "💻 Technical Assistant",
        "icon": "💻",
        "description": "Code debugging, tech solutions, device troubleshooting",
        "capabilities": [
            "Code debugging",
            "Tech solutions",
            "Device troubleshooting",
            "Software recommendations",
            "IT support"
        ]
    },
    "government": {
        "name": "🏛️ Government Services",
        "icon": "🏛️",
        "description": "Government form filling, service information, complaint registration",
        "capabilities": [
            "Form filling assistance",
            "Service information",
            "Complaint registration",
            "Document requirements",
            "Procedure guidance"
        ]
    },
    "agriculture": {
        "name": "🌾 Agriculture Assistant",
        "icon": "🌾",
        "description": "Crop advice, weather information, market prices",
        "capabilities": [
            "Crop selection advice",
            "Weather information",
            "Market prices",
            "Fertilizer guidance",
            "Disease identification"
        ]
    },
    "personal": {
        "name": "👤 Personal Assistant",
        "icon": "👤",
        "description": "Daily planning, finance management, life coaching",
        "capabilities": [
            "Daily planning",
            "Finance management",
            "Life coaching",
            "Health tracking",
            "Goal setting"
        ]
    }
}

class AISparkAssistant:
    """Main AI Assistant Class"""
    
    def __init__(self):
        self.user_history = []
        self.solutions_provided = 0
        
    def analyze_problem(self, problem_text, category):
        """Analyze user problem and provide solution"""
        solutions = {
            "medical": self._medical_solution,
            "legal": self._legal_solution,
            "education": self._education_solution,
            "business": self._business_solution,
            "technical": self._technical_solution,
            "government": self._government_solution,
            "agriculture": self._agriculture_solution,
            "personal": self._personal_solution
        }
        
        if category in solutions:
            return solutions[category](problem_text)
        else:
            return self._general_solution(problem_text)
    
    def _medical_solution(self, problem):
        """Generate medical solution"""
        common_issues = {
            "fever": {
                "diagnosis": "Possible viral infection or other illness",
                "immediate_action": [
                    "Take paracetamol 500mg (if no allergies)",
                    "Drink plenty of fluids",
                    "Rest and monitor temperature"
                ],
                "when_to_see_doctor": "If fever persists >3 days or temperature >103°F",
                "recommended_doctors": ["General Physician", "Internal Medicine"],
                "hospitals": ["Aga Khan Hospital", "Shaukat Khanum", "CMH Hospital"],
                "home_remedies": [
                    "Use wet cloth on forehead",
                    "Drink ginger tea",
                    "Take steam inhalation"
                ]
            },
            "headache": {
                "diagnosis": "Could be tension headache, migraine, or stress-related",
                "immediate_action": [
                    "Take rest in dark room",
                    "Drink plenty of water",
                    "Massage temples gently"
                ],
                "when_to_see_doctor": "If headache is severe, sudden, or with vision problems",
                "recommended_medicines": ["Paracetamol", "Ibuprofen (if no stomach issues)"],
                "prevention": [
                    "Regular sleep schedule",
                    "Stay hydrated",
                    "Reduce screen time"
                ]
            }
        }
        
        # Simple keyword matching (in real app, use NLP)
        problem_lower = problem.lower()
        
        if any(word in problem_lower for word in ['fever', 'temperature', 'heat']):
            return common_issues['fever']
        elif any(word in problem_lower for word in ['headache', 'head pain', 'migraine']):
            return common_issues['headache']
        else:
            return self._general_medical_advice(problem)
    
    def _legal_solution(self, problem):
        """Generate legal solution"""
        return {
            "issue_type": "Legal Matter",
            "recommended_actions": [
                "Document all evidence related to your case",
                "Consult with a licensed lawyer in your area",
                "Check statute of limitations for your case type",
                "Gather witness statements if applicable"
            ],
            "pakistan_specific": [
                f"Contact District Bar Association in your city",
                "Visit https://www.supremecourt.gov.pk for high court matters",
                "Legal aid available through Punjab Legal Aid Society"
            ],
            "document_checklist": [
                "CNIC copy",
                "Related documents",
                "Witness details",
                "Previous correspondence"
            ],
            "estimated_timeline": "3-6 months for most civil cases",
            "approximate_cost": "PKR 20,000 - 100,000 depending on case complexity"
        }
    
    def _education_solution(self, problem):
        """Generate education solution"""
        return {
            "problem_type": "Educational",
            "solutions": [
                "Break down complex topics into smaller parts",
                "Use visual aids and diagrams",
                "Practice with past papers",
                "Form study groups"
            ],
            "pakistan_resources": [
                "HEC Digital Library: https://digitallibrary.edu.pk",
                "Punjab IT Board e-Learn",
                "Virtual University resources"
            ],
            "career_guidance": "Consider taking career assessment tests",
            "scholarship_info": "Check HEC scholarship portal regularly",
            "skill_development": [
                "Coursera (financial aid available)",
                "EdX free courses",
                "Google Digital Garage"
            ]
        }
    
    def _business_solution(self, problem):
        """Generate business solution"""
        return {
            "business_type": "Startup/Small Business",
            "key_actions": [
                "Register your business with SECP",
                "Open a business bank account",
                "Get NTN from FBR",
                "Create a simple business plan"
            ],
            "pakistan_support": [
                "Small and Medium Enterprises Development Authority (SMEDA)",
                "Punjab Small Industries Corporation",
                "Youth Entrepreneurship Scheme"
            ],
            "funding_options": [
                "Bank loans (for established businesses)",
                "Angel investors network",
                "Government startup grants"
            ],
            "marketing_strategies": [
                "Social media marketing (low cost)",
                "Local networking events",
                "Collaborate with complementary businesses"
            ],
            "estimated_costs": "PKR 50,000 - 500,000 depending on business type"
        }
    
    def _technical_solution(self, problem):
        """Generate technical solution"""
        problem_lower = problem.lower()
        
        if any(word in problem_lower for word in ['wifi', 'internet', 'connection']):
            return {
                "issue": "Internet/WiFi Problem",
                "troubleshooting_steps": [
                    "1. Restart your router/modem",
                    "2. Check if other devices can connect",
                    "3. Move closer to router",
                    "4. Change WiFi channel in router settings",
                    "5. Contact ISP if problem persists"
                ],
                "pakistan_isp_contacts": {
                    "PTCL": "1218",
                    "Nayatel": "111-111-111",
                    "StormFiber": "111-111-666",
                    "Transworld": "111-123-456"
                }
            }
        elif any(word in problem_lower for word in ['phone', 'mobile', 'device']):
            return {
                "issue": "Mobile Device Problem",
                "solutions": [
                    "Perform soft reset (restart)",
                    "Clear app cache from settings",
                    "Check for software updates",
                    "Backup data and perform factory reset if severe"
                ],
                "service_centers": [
                    "Apple: iSquare, Mac station",
                    "Samsung: Authorized service centers",
                    "Other brands: Hafeez Center, Lahore"
                ]
            }
        else:
            return {
                "issue": "Technical Problem",
                "general_solutions": [
                    "Search error message online",
                    "Check official documentation",
                    "Join relevant online forums",
                    "Contact technical support"
                ]
            }
    
    def _government_solution(self, problem):
        """Generate government services solution"""
        return {
            "service_type": "Government Service",
            "common_services": [
                "CNIC application/renewal - Visit NADRA center",
                "Passport application - Visit passport office",
                "Vehicle registration - Excise & Taxation office",
                "Property registration - Registrar office"
            ],
            "online_portals": [
                "NADRA: https://www.nadra.gov.pk",
                "FBR: https://iris.fbr.gov.pk",
                "Passport: https://onlinemrp.dgip.gov.pk",
                "Excise & Taxation: https://excise.punjab.gov.pk"
            ],
            "required_documents": [
                "Original CNIC",
                "Recent photographs",
                "Proof of address",
                "Relevant application forms"
            ],
            "processing_time": "Varies from 1 day to 2 weeks",
            "fees": "PKR 100 - 5,000 depending on service"
        }
    
    def _agriculture_solution(self, problem):
        """Generate agriculture solution"""
        return {
            "crop_type": "General Agriculture",
            "seasonal_advice": [
                "Rabbi season (Oct-Mar): Wheat, Barley, Gram",
                "Kharif season (Apr-Sep): Rice, Cotton, Sugarcane"
            ],
            "government_support": [
                "Kissan Card scheme",
                "Subsidized fertilizers",
                "Free agricultural advisory services"
            ],
            "market_prices": "Check local mandi rates daily",
            "weather_advisory": "Follow Pakistan Meteorological Department updates",
            "disease_prevention": [
                "Use certified seeds",
                "Practice crop rotation",
                "Monitor for pests regularly"
            ]
        }
    
    def _personal_solution(self, problem):
        """Generate personal assistant solution"""
        return {
            "area": "Personal Development",
            "daily_planning": [
                "Set 3 main goals for the day",
                "Use Pomodoro technique (25 min work, 5 min break)",
                "Review progress at end of day"
            ],
            "finance_management": [
                "Track all expenses for one month",
                "Create basic budget (50% needs, 30% wants, 20% savings)",
                "Start emergency fund (aim for 3-6 months expenses)"
            ],
            "health_tips": [
                "30 minutes daily exercise",
                "7-8 hours sleep",
                "Balanced diet with local seasonal foods"
            ],
            "skill_development": "Spend 1 hour daily learning new skill"
        }
    
    def _general_solution(self, problem):
        """General solution for uncategorized problems"""
        return {
            "approach": "General Problem Solving",
            "steps": [
                "1. Clearly define the problem",
                "2. Break it into smaller parts",
                "3. Research each part separately",
                "4. Seek expert advice if needed",
                "5. Implement solution step by step"
            ],
            "resources": [
                "Google search with specific keywords",
                "YouTube tutorials",
                "Online forums (Reddit, Stack Exchange)",
                "Local community groups"
            ]
        }
    
    def _general_medical_advice(self, problem):
        """General medical advice"""
        return {
            "important_note": "⚠️ This is AI-generated advice. Always consult a doctor for medical issues.",
            "general_advice": [
                "Describe symptoms clearly to doctor",
                "Note when symptoms started",
                "List any medications you're taking",
                "Mention any allergies"
            ],
            "emergency_signs": [
                "Difficulty breathing",
                "Severe pain",
                "High fever with rash",
                "Loss of consciousness"
            ],
            "immediate_actions": [
                "If emergency, go to nearest hospital",
                "Otherwise, book appointment with GP",
                "Keep hydrated and rest"
            ]
        }
    
    def generate_implementation_plan(self, solution, timeline_days=7):
        """Generate step-by-step implementation plan"""
        days = timeline_days
        
        plan = {}
        for i in range(1, days + 1):
            if i == 1:
                plan[f"Day {i}"] = ["Research and gather information", "Make list of required resources"]
            elif i == 2:
                plan[f"Day {i}"] = ["Consult with relevant expert", "Finalize approach"]
            elif i == 3:
                plan[f"Day {i}"] = ["Start implementation", "Document progress"]
            elif i <= days - 2:
                plan[f"Day {i}"] = ["Continue implementation", "Make adjustments as needed"]
            elif i == days - 1:
                plan[f"Day {i}"] = ["Review progress", "Fix any issues"]
            else:
                plan[f"Day {i}"] = ["Final review", "Document learnings", "Plan next steps"]
        
        return plan
    
    def format_solution_for_display(self, solution, problem_text):
        """Format solution for beautiful display"""
        formatted = f"## 🔍 **Problem Analysis**\n\n"
        formatted += f"*Problem:* {problem_text}\n\n"
        formatted += f"## 🎯 **Recommended Solution**\n\n"
        
        for key, value in solution.items():
            if isinstance(value, list):
                formatted += f"### {key.replace('_', ' ').title()}:\n"
                for item in value:
                    formatted += f"- {item}\n"
                formatted += "\n"
            elif isinstance(value, dict):
                formatted += f"### {key.replace('_', ' ').title()}:\n"
                for sub_key, sub_value in value.items():
                    formatted += f"**{sub_key.replace('_', ' ').title()}:** {sub_value}\n"
                formatted += "\n"
            else:
                formatted += f"**{key.replace('_', ' ').title()}:** {value}\n\n"
        
        return formatted

class ProblemTracker:
    """Track user problems and solutions"""
    
    def __init__(self):
        self.problems = []
    
    def add_problem(self, category, problem, solution):
        """Add problem to tracker"""
        self.problems.append({
            "timestamp": datetime.now(),
            "category": category,
            "problem": problem,
            "solution": solution,
            "resolved": False
        })
    
    def get_stats(self):
        """Get statistics"""
        if not self.problems:
            return {"total": 0, "resolved": 0, "categories": {}}
        
        stats = {
            "total": len(self.problems),
            "resolved": sum(1 for p in self.problems if p["resolved"]),
            "categories": {}
        }
        
        for problem in self.problems:
            cat = problem["category"]
            stats["categories"][cat] = stats["categories"].get(cat, 0) + 1
        
        return stats

def main():
    """Main Application"""
    
    # Initialize session state
    if 'ai_assistant' not in st.session_state:
        st.session_state.ai_assistant = AISparkAssistant()
    if 'problem_tracker' not in st.session_state:
        st.session_state.problem_tracker = ProblemTracker()
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    ai = st.session_state.ai_assistant
    tracker = st.session_state.problem_tracker
    
    # Header
    st.markdown('<h1 class="main-header">🤖 AI-SPARK</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Pakistan\'s First Universal AI Assistant • Real-Time Problem Solving • 100% Free</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3067/3067256.png", width=100)
        st.markdown("### 📊 Dashboard")
        
        stats = tracker.get_stats()
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Problems Solved", stats["total"])
        with col2:
            if stats["total"] > 0:
                st.metric("Resolved", stats["resolved"])
            else:
                st.metric("Resolved", 0)
        
        st.markdown("---")
        st.markdown("### 🎯 Quick Categories")
        
        # Category buttons
        categories_grid = st.columns(3)
        categories = list(AI_MODULES.keys())[:6]  # First 6 categories
        
        for idx, cat in enumerate(categories):
            with categories_grid[idx % 3]:
                if st.button(AI_MODULES[cat]["icon"], help=AI_MODULES[cat]["name"], use_container_width=True):
                    st.session_state.selected_category = cat
                    st.rerun()
        
        st.markdown("---")
        st.markdown("### 🚨 Emergency Info (Pakistan)")
        
        with st.expander("Emergency Numbers"):
            for service, number in PAKISTAN_DATA["emergency_numbers"].items():
                st.write(f"**{service}:** `{number}`")
        
        with st.expander("Government Websites"):
            for dept, url in PAKISTAN_DATA["government_websites"].items():
                st.write(f"[{dept}]({url})")
        
        st.markdown("---")
        st.markdown("Made with ❤️ in Pakistan")
    
    # Main Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Home", 
        "💬 Problem Solver", 
        "📊 Progress Tracker", 
        "📚 Resources", 
        "🆘 Emergency Help"
    ])
    
    with tab1:
        # Hero Section
        st.markdown("## 🚀 Welcome to AI-SPARK!")
        st.markdown("""
        Your personal AI assistant for solving **real-world problems** in Pakistan. 
        From medical advice to business guidance, technical issues to legal matters - 
        we've got you covered!
        """)
        
        # Features Grid
        st.markdown("## 🔥 Key Features")
        
        features_cols = st.columns(3)
        
        with features_cols[0]:
            st.markdown("""
            <div class="card">
                <div class="card-icon">🏥</div>
                <h3>Medical Assistant</h3>
                <p>Symptom checking, medicine info, doctor recommendations</p>
            </div>
            """, unsafe_allow_html=True)
        
        with features_cols[1]:
            st.markdown("""
            <div class="card">
                <div class="card-icon">⚖️</div>
                <h3>Legal Assistant</h3>
                <p>Legal advice, document review, lawyer matching</p>
            </div>
            """, unsafe_allow_html=True)
        
        with features_cols[2]:
            st.markdown("""
            <div class="card">
                <div class="card-icon">🎓</div>
                <h3>Education Assistant</h3>
                <p>Homework help, career guidance, scholarship finder</p>
            </div>
            """, unsafe_allow_html=True)
        
        features_cols2 = st.columns(3)
        
        with features_cols2[0]:
            st.markdown("""
            <div class="card">
                <div class="card-icon">💼</div>
                <h3>Business Assistant</h3>
                <p>Business plans, market analysis, funding guidance</p>
            </div>
            """, unsafe_allow_html=True)
        
        with features_cols2[1]:
            st.markdown("""
            <div class="card">
                <div class="card-icon">💻</div>
                <h3>Technical Assistant</h3>
                <p>Code debugging, tech solutions, device troubleshooting</p>
            </div>
            """, unsafe_allow_html=True)
        
        with features_cols2[2]:
            st.markdown("""
            <div class="card">
                <div class="card-icon">🏛️</div>
                <h3>Government Services</h3>
                <p>Form filling, service info, complaint registration</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Quick Start
        st.markdown("## ⚡ Quick Start")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🎯 How to Use:
            1. **Select your problem category**
            2. **Describe your problem in detail**
            3. **Get AI-powered solution**
            4. **Follow step-by-step guide**
            5. **Track your progress**
            """)
        
        with col2:
            st.markdown("""
            ### 💡 Pro Tips:
            - Be specific about your problem
            - Include relevant details
            - Follow the implementation plan
            - Save important solutions
            - Share with friends who need help
            """)
        
        # Stats
        st.markdown("## 📈 Real-time Statistics")
        stat_cols = st.columns(4)
        
        with stat_cols[0]:
            st.metric("Active Users", "1,234", "+123 today")
        with stat_cols[1]:
            st.metric("Problems Solved", "5,678", "+45 today")
        with stat_cols[2]:
            st.metric("Success Rate", "92%", "+2%")
        with stat_cols[3]:
            st.metric("Avg. Resolution Time", "2.3 hrs", "-0.5 hrs")
    
    with tab2:
        st.markdown("## 💬 AI Problem Solver")
        
        # Category Selection
        st.markdown("### 1️⃣ Select Problem Category")
        
        categories = st.columns(4)
        category_keys = list(AI_MODULES.keys())
        
        selected_category = st.session_state.get('selected_category', 'medical')
        
        for idx in range(0, len(category_keys), 4):
            cols = st.columns(4)
            for j in range(4):
                if idx + j < len(category_keys):
                    cat_key = category_keys[idx + j]
                    cat_data = AI_MODULES[cat_key]
                    
                    with cols[j]:
                        if st.button(
                            f"{cat_data['icon']} {cat_data['name'].split()[1]}",
                            use_container_width=True,
                            type="primary" if cat_key == selected_category else "secondary"
                        ):
                            selected_category = cat_key
                            st.session_state.selected_category = cat_key
                            st.rerun()
        
        # Problem Input
        st.markdown(f"### 2️⃣ Describe Your {AI_MODULES[selected_category]['name']} Problem")
        
        problem_text = st.text_area(
            "Be specific and include all relevant details:",
            height=150,
            placeholder=f"Example: I have fever for 2 days, temperature is 101°F..."
            if selected_category == "medical" else
            f"Describe your {selected_category} problem in detail..."
        )
        
        # Additional Details
        with st.expander("📋 Additional Details (Optional)"):
            col1, col2 = st.columns(2)
            
            with col1:
                location = st.selectbox(
                    "Your City",
                    ["Select city"] + PAKISTAN_DATA["cities"]
                )
            
            with col2:
                urgency = st.select_slider(
                    "Urgency Level",
                    ["Low", "Medium", "High", "Critical"]
                )
            
            budget = st.slider("Approximate Budget (PKR)", 0, 1000000, 10000, 1000)
            
            timeline = st.selectbox(
                "Preferred Timeline",
                ["Immediate", "Within a week", "Within a month", "Flexible"]
            )
        
        # Solve Button
        if st.button("🚀 GET AI SOLUTION", type="primary", use_container_width=True):
            if problem_text.strip():
                with st.spinner(f"🤖 Analyzing your {selected_category} problem..."):
                    time.sleep(1)
                    
                    # Get solution
                    solution = ai.analyze_problem(problem_text, selected_category)
                    
                    # Track problem
                    tracker.add_problem(selected_category, problem_text, solution)
                    
                    # Display solution
                    st.success("✅ Solution Generated!")
                    
                    # Solution display
                    st.markdown("---")
                    st.markdown(f'<div class="solution-box"><h3>✨ AI-Generated Solution</h3></div>', unsafe_allow_html=True)
                    
                    formatted_solution = ai.format_solution_for_display(solution, problem_text)
                    st.markdown(formatted_solution)
                    
                    # Implementation Plan
                    st.markdown("---")
                    st.markdown("## 📋 Implementation Plan")
                    
                    plan_days = st.slider("Plan duration (days)", 1, 30, 7)
                    implementation_plan = ai.generate_implementation_plan(solution, plan_days)
                    
                    for day, tasks in implementation_plan.items():
                        with st.expander(f"{day}: {tasks[0]}"):
                            for task in tasks:
                                st.write(f"• {task}")
                    
                    # Resources
                    st.markdown("---")
                    st.markdown("## 🔗 Helpful Resources")
                    
                    resource_cols = st.columns(2)
                    
                    with resource_cols[0]:
                        st.markdown("### 📞 Local Contacts")
                        if selected_category == "medical":
                            st.write("""
                            - **Aga Khan Hospital:** 021-111-911-911
                            - **Shaukat Khanum:** 042-111-911-911
                            - **Jinnah Hospital:** 042-992-313-00
                            """)
                        elif selected_category == "legal":
                            st.write("""
                            - **District Bar Association:** Visit local office
                            - **Legal Aid:** 0800-66666
                            - **Police Complaint:** 15 or 8787
                            """)
                    
                    with resource_cols[1]:
                        st.markdown("### 🌐 Online Resources")
                        st.write("""
                        - **Government Portal:** [Pakistan.gov.pk](https://www.pakistan.gov.pk)
                        - **Consumer Protection:** [Punjab Consumer Protection Council](https://pcpc.punjab.gov.pk)
                        - **Emergency Services:** Rescue 1122
                        """)
                    
                    # Download option
                    st.markdown("---")
                    st.markdown("### 💾 Save Solution")
                    
                    solution_data = {
                        "problem": problem_text,
                        "category": selected_category,
                        "solution": solution,
                        "generated_at": datetime.now().isoformat(),
                        "implementation_plan": implementation_plan
                    }
                    
                    json_str = json.dumps(solution_data, indent=2, ensure_ascii=False)
                    
                    st.download_button(
                        label="📥 Download Solution as JSON",
                        data=json_str,
                        file_name=f"ai_spark_solution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                        mime="application/json"
                    )
            else:
                st.error("Please describe your problem first!")
    
    with tab3:
        st.markdown("## 📊 Your Progress Tracker")
        
        stats = tracker.get_stats()
        
        if stats["total"] > 0:
            # Stats overview
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Problems", stats["total"])
            
            with col2:
                resolution_rate = (stats["resolved"] / stats["total"] * 100) if stats["total"] > 0 else 0
                st.metric("Resolution Rate", f"{resolution_rate:.1f}%")
            
            with col3:
                st.metric("Active Issues", stats["total"] - stats["resolved"])
            
            # Category distribution
            st.markdown("### 📈 Problem Categories")
            
            if stats["categories"]:
                categories_df = pd.DataFrame({
                    'Category': list(stats["categories"].keys()),
                    'Count': list(stats["categories"].values())
                })
                
                fig = px.pie(categories_df, values='Count', names='Category', 
                            title='Problem Distribution by Category')
                st.plotly_chart(fig, use_container_width=True)
            
            # Problem history
            st.markdown("### 📝 Problem History")
            
            for idx, problem in enumerate(reversed(tracker.problems[-10:]), 1):
                with st.expander(f"Problem #{len(tracker.problems) - idx + 1}: {problem['category'].title()} - {problem['timestamp'].strftime('%Y-%m-%d %H:%M')}"):
                    st.write(f"**Problem:** {problem['problem'][:200]}...")
                    st.write(f"**Category:** {problem['category'].title()}")
                    st.write(f"**Status:** {'✅ Resolved' if problem['resolved'] else '🔄 In Progress'}")
                    
                    col_res1, col_res2 = st.columns(2)
                    
                    with col_res1:
                        if not problem['resolved']:
                            if st.button(f"Mark as Resolved", key=f"resolve_{idx}"):
                                problem['resolved'] = True
                                st.rerun()
                    
                    with col_res2:
                        if st.button(f"View Solution", key=f"view_{idx}"):
                            st.write("**Solution Summary:**")
                            st.json(problem['solution'])
        else:
            st.info("No problems tracked yet. Go to the Problem Solver tab to get started!")
            
            # Sample progress visualization
            st.markdown("### 📊 How Progress Tracking Works")
            
            sample_data = pd.DataFrame({
                'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
                'Problems Solved': [0, 2, 5, 8],
                'Resolution Rate %': [0, 50, 70, 85]
            })
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=sample_data['Week'], y=sample_data['Problems Solved'],
                                    mode='lines+markers', name='Problems Solved'))
            fig.add_trace(go.Scatter(x=sample_data['Week'], y=sample_data['Resolution Rate %'],
                                    mode='lines+markers', name='Resolution Rate %', yaxis='y2'))
            
            fig.update_layout(
                title='Sample Progress Tracking',
                yaxis=dict(title='Problems Solved'),
                yaxis2=dict(title='Resolution Rate %', overlaying='y', side='right'),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.markdown("## 📚 Free Resources & Templates")
        
        resource_categories = st.selectbox(
            "Select Resource Category",
            ["Medical", "Legal", "Education", "Business", "Technical", "Government", "All"]
        )
        
        # Resource Database
        RESOURCES = {
            "Medical": [
                {"name": "📋 Medical History Template", "desc": "Keep track of medical history", "download": True},
                {"name": "💊 Medicine Tracker", "desc": "Track medications and dosage", "download": True},
                {"name": "🏥 Hospital Checklist", "desc": "What to bring to hospital", "download": True},
                {"name": "🌡️ Symptom Diary", "desc": "Daily symptom tracking template", "download": True},
            ],
            "Legal": [
                {"name": "📄 Basic Agreement Template", "desc": "Simple legal agreement", "download": True},
                {"name": "⚖️ Consumer Complaint Form", "desc": "For product/service complaints", "download": True},
                {"name": "📝 Rental Agreement", "desc": "Basic house rental agreement", "download": True},
                {"name": "📑 Affidavit Template", "desc": "For sworn statements", "download": True},
            ],
            "Education": [
                {"name": "📓 Study Planner", "desc": "Weekly study schedule", "download": True},
                {"name": "🎯 Career Planning Worksheet", "desc": "Plan your career path", "download": True},
                {"name": "💰 Scholarship Tracker", "desc": "Track scholarship applications", "download": True},
                {"name": "📚 Research Template", "desc": "Academic research organization", "download": True},
            ],
            "Business": [
                {"name": "📊 Business Plan Template", "desc": "Complete business plan", "download": True},
                {"name": "💰 Expense Tracker", "desc": "Business expense tracking", "download": True},
                {"name": "📈 Financial Projections", "desc": "3-year financial projections", "download": True},
                {"name": "📋 Startup Checklist", "desc": "Step-by-step startup guide", "download": True},
            ],
            "Technical": [
                {"name": "🐛 Bug Report Template", "desc": "Standard bug reporting", "download": True},
                {"name": "💻 Project Documentation", "desc": "Software documentation template", "download": True},
                {"name": "🔧 Maintenance Checklist", "desc": "System maintenance schedule", "download": True},
                {"name": "📱 App Requirements", "desc": "Mobile app requirements doc", "download": True},
            ],
            "Government": [
                {"name": "🆔 CNIC Application Checklist", "desc": "Documents needed for CNIC", "download": True},
                {"name": "📄 Passport Requirements", "desc": "Passport application checklist", "download": True},
                {"name": "🚗 Vehicle Transfer Process", "desc": "Step-by-step guide", "download": True},
                {"name": "🏠 Property Registration", "desc": "Property registration process", "download": True},
            ]
        }
        
        # Display resources
        if resource_categories == "All":
            for category, resources in RESOURCES.items():
                st.markdown(f"### {category} Resources")
                cols = st.columns(2)
                
                for idx, resource in enumerate(resources):
                    with cols[idx % 2]:
                        st.markdown(f"""
                        <div class="feature-card">
                            <strong>{resource['name']}</strong>
                            <p>{resource['desc']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if resource['download']:
                            # Create sample content for download
                            sample_content = f"""# {resource['name']}
                            
This is a sample template for {resource['desc'].lower()}
Generated by AI-SPARK on {datetime.now().strftime('%Y-%m-%d')}

Instructions:
1. Fill in your information
2. Save a copy
3. Use as needed

Note: This is a template. Consult with professionals for important matters.
                            """
                            
                            st.download_button(
                                label="📥 Download Template",
                                data=sample_content,
                                file_name=f"{resource['name'].replace(' ', '_')}.txt",
                                mime="text/plain",
                                key=f"dl_{category}_{idx}"
                            )
        else:
            if resource_categories in RESOURCES:
                resources = RESOURCES[resource_categories]
                cols = st.columns(2)
                
                for idx, resource in enumerate(resources):
                    with cols[idx % 2]:
                        st.markdown(f"""
                        <div class="feature-card">
                            <strong>{resource['name']}</strong>
                            <p>{resource['desc']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if resource['download']:
                            sample_content = f"""# {resource['name']}
                            
Template for {resource['desc'].lower()}
AI-SPARK Resource - {datetime.now().strftime('%Y-%m-%d')}

This template helps you organize and track relevant information.
For official matters, always use approved forms and consult authorities.
                            """
                            
                            st.download_button(
                                label="📥 Download",
                                data=sample_content,
                                file_name=f"{resource['name'].replace(' ', '_')}.txt",
                                mime="text/plain",
                                key=f"dl_{resource_categories}_{idx}"
                            )
        
        # Online Courses Section
        st.markdown("---")
        st.markdown("## 🎓 Free Online Courses (Pakistan)")
        
        courses = [
            {"name": "Digital Skills", "platform": "Google Digital Garage", "duration": "10 hours", "link": "https://learndigital.withgoogle.com/digitalgarage"},
            {"name": "AI For Everyone", "platform": "Coursera", "duration": "12 hours", "link": "https://www.coursera.org/learn/ai-for-everyone"},
            {"name": "Financial Literacy", "platform": "State Bank of Pakistan", "duration": "8 hours", "link": "https://www.sbp.org.pk/finca/"},
            {"name": "Entrepreneurship", "platform": "SMEDA", "duration": "15 hours", "link": "https://smeda.org/"},
            {"name": "Freelancing", "platform": "DigiSkills.pk", "duration": "20 hours", "link": "https://digiskills.pk/"},
            {"name": "Coding Basics", "platform": "Code.org", "duration": "15 hours", "link": "https://code.org/"},
        ]
        
        course_cols = st.columns(3)
        for idx, course in enumerate(courses):
            with course_cols[idx % 3]:
                st.markdown(f"""
                <div style='padding: 15px; background: #f8f9fa; border-radius: 10px; margin: 10px 0;'>
                    <strong>{course['name']}</strong><br>
                    <small>{course['platform']} • {course['duration']}</small><br>
                    <a href='{course['link']}' target='_blank'>🔗 Visit Course</a>
                </div>
                """, unsafe_allow_html=True)
    
    with tab5:
        st.markdown("## 🆘 Emergency Help Center")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="warning-box"><h3>🚨 Immediate Emergency</h3></div>', unsafe_allow_html=True)
            
            emergency_options = st.selectbox(
                "Select Emergency Type",
                ["Medical Emergency", "Police Help", "Fire", "Natural Disaster", "Women/Child Abuse", "Mental Health Crisis"]
            )
            
            if emergency_options == "Medical Emergency":
                st.markdown("""
                ### 🏥 Immediate Actions:
                1. **Call 1122** for ambulance
                2. **Don't move** the patient if serious injury
                3. **Check breathing** and pulse
                4. **Perform CPR** if trained
                5. **Gather medicines** and medical history
                
                ### 📞 Hospital Emergency Numbers:
                - Aga Khan Hospital: **021-111-911-911**
                - Shaukat Khanum: **042-111-911-911**
                - Jinnah Hospital: **042-992-313-00**
                - Civil Hospital: **021-992-157-00**
                """)
            
            elif emergency_options == "Police Help":
                st.markdown("""
                ### 👮 Police Emergency:
                1. **Call 15** for police
                2. **Call 1122** for rescue
                3. **Call 0800-66666** for legal aid
                4. **Women Helpline: 1099**
                5. **Child Protection: 1121**
                
                ### 📍 Nearby Police Stations:
                - Use Google Maps to find nearest station
                - Contact Dolphin Force in big cities
                - Download Punjab Police app for help
                """)
            
            elif emergency_options == "Mental Health Crisis":
                st.markdown("""
                ### 🧠 Mental Health Support:
                1. **Umang Pakistan:** 0311-778-6264
                2. **Taskeen:** 0311-111-000
                3. **Mental Health Helpline:** 1133
                4. **Mari Abdul Wali Khan Hospital:** 091-922-1401
                
                ### 💬 Immediate Help:
                - Talk to someone you trust
                - Practice deep breathing
                - Remove yourself from stressful situation
                - Remember: This too shall pass
                """)
            
            # Emergency Button
            if st.button("🆘 CALL EMERGENCY SERVICES NOW", type="secondary", use_container_width=True):
                st.warning("Dialing emergency number... Please stay calm and provide clear information.")
                st.info("**Location:** Share your exact location\n**Problem:** Describe emergency clearly\n**People:** Mention number of people affected")
        
        with col2:
            st.markdown('<div class="solution-box"><h3>📞 Important Contacts</h3></div>', unsafe_allow_html=True)
            
            contacts = {
                "Rescue 1122": "1122",
                "Police": "15",
                "Fire Brigade": "16",
                "Women Helpline": "1099",
                "Child Protection": "1121",
                "Electricity Complaint": "118",
                "Gas Emergency": "119",
                "PTCL Helpline": "1218"
            }
            
            for service, number in contacts.items():
                col_num, col_btn = st.columns([2, 1])
                with col_num:
                    st.markdown(f"**{service}:** `{number}`")
                with col_btn:
                    st.button(f"Call", key=f"call_{service}", use_container_width=True)
            
            st.markdown("---")
            st.markdown("### 📍 Find Nearby Services")
            
            service_type = st.selectbox(
                "Find nearest:",
                ["Hospital", "Police Station", "Fire Station", "Pharmacy", "Blood Bank"]
            )
            
            if st.button("🔍 Search on Google Maps", use_container_width=True):
                st.info(f"Searching for nearest {service_type}... Open Google Maps to see results.")
                st.write("""
                **Pro Tip:** 
                - Enable location services
                - Check reviews and ratings
                - Call ahead to confirm availability
                - Note down address and contact number
                """)
            
            st.markdown("---")
            st.markdown("### 🆘 Emergency Kit Checklist")
            
            with st.expander("View Emergency Kit Items"):
                st.write("""
                **Essential Items:**
                - First aid kit
                - Flashlight with batteries
                - Bottled water
                - Non-perishable food
                - Medications (7-day supply)
                - Copies of important documents
                - Cash (small bills)
                - Phone charger/power bank
                
                **For Pakistan:**
                - CNIC copies
                - Health insurance card
                - Emergency contact numbers
                - Local map
                """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p style="font-size: 1.1rem;">
            🤖 <strong>AI-SPARK v2.0</strong> | 
            🇵🇰 Made for Pakistan | 
            🆓 100% Free Forever | 
            🔒 Privacy First
        </p>
        <p>
            📧 Contact: support@ai-spark.pk | 
            📞 Helpline: 0800-AI-HELP | 
            🕒 24/7 Available
        </p>
        <p style="font-size: 0.9rem; color: #999;">
            © 2024 AI-SPARK Project • All solutions are AI-generated advice • 
            Always consult professionals for critical matters • 
            Report bugs: github.com/ai-spark
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
