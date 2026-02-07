"""
🌍 GEO-SAPIENS: Planetary Intelligence & Civilization Manager
Real-time Earth Management System with Climate Control & Civilization Simulation
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import json
import math
import random
from typing import Dict, List, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="🌍 GEO-SAPIENS - Planetary Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for futuristic interface
st.markdown("""
<style>
    .main-title {
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 30px rgba(0, 114, 255, 0.3);
    }
    
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        letter-spacing: 2px;
    }
    
    .planet-card {
        background: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(0, 198, 255, 0.3);
        box-shadow: 0 10px 40px rgba(0, 114, 255, 0.2);
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .planet-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 50px rgba(0, 114, 255, 0.3);
        border-color: rgba(0, 198, 255, 0.6);
    }
    
    .metric-hologram {
        background: linear-gradient(135deg, rgba(0, 0, 30, 0.9) 0%, rgba(0, 20, 60, 0.9) 100%);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(0, 198, 255, 0.5);
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .metric-hologram::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(transparent, rgba(0, 198, 255, 0.1), transparent 30%);
        animation: rotate 4s linear infinite;
    }
    
    @keyframes rotate {
        100% { transform: rotate(360deg); }
    }
    
    .control-panel {
        background: rgba(0, 10, 30, 0.9);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(0, 198, 255, 0.3);
        margin: 10px 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 1rem;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0, 114, 255, 0.4);
    }
    
    .warning-pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(255, 0, 0, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(255, 0, 0, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 0, 0, 0); }
    }
    
    .success-glow {
        box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
    }
    
    .timeline-event {
        background: rgba(0, 20, 40, 0.8);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #00c6ff;
    }
    
    .satellite-track {
        position: relative;
        overflow: hidden;
    }
    
    .satellite-track::after {
        content: '🛰️';
        position: absolute;
        animation: satellite 10s linear infinite;
    }
    
    @keyframes satellite {
        0% { transform: translateX(-50px) translateY(-50px); }
        100% { transform: translateX(calc(100vw + 50px)) translateY(calc(100vh + 50px)); }
    }
    
    .status-indicator {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
    }
    
    .status-green { background: #00ff00; box-shadow: 0 0 10px #00ff00; }
    .status-yellow { background: #ffff00; box-shadow: 0 0 10px #ffff00; }
    .status-red { background: #ff0000; box-shadow: 0 0 10px #ff0000; }
    .status-blue { background: #00c6ff; box-shadow: 0 0 10px #00c6ff; }
</style>
""", unsafe_allow_html=True)

# ==================== PLANETARY DATABASE ====================
class PlanetaryDatabase:
    """Earth and celestial bodies database"""
    
    def __init__(self):
        self.earth_data = self._initialize_earth_data()
        self.satellites = self._initialize_satellites()
        self.civilizations = self._initialize_civilizations()
        self.resources = self._initialize_resources()
        
    def _initialize_earth_data(self):
        """Initialize Earth's core data"""
        return {
            "radius_km": 6371,
            "surface_area_km2": 510100000,
            "population": 8100000000,
            "atmosphere_composition": {
                "nitrogen": 78.08,
                "oxygen": 20.95,
                "argon": 0.93,
                "carbon_dioxide": 0.04,
                "other": 0.002
            },
            "rotation_period_hours": 23.93,
            "orbital_period_days": 365.25,
            "axial_tilt_degrees": 23.44,
            "magnetic_field_strength_tesla": 0.000025,
            "core_temperature_c": 6000,
            "surface_temperature_c": 15,
            "sea_level_rise_mm_year": 3.3
        }
    
    def _initialize_satellites(self):
        """Initialize Earth satellites data"""
        return [
            {"name": "ISS", "type": "Space Station", "altitude_km": 408, "velocity_km_s": 7.66, "crew": 7},
            {"name": "Hubble", "type": "Telescope", "altitude_km": 547, "velocity_km_s": 7.5, "crew": 0},
            {"name": "GPS-III", "type": "Navigation", "altitude_km": 20200, "velocity_km_s": 3.87, "crew": 0},
            {"name": "GOES-16", "type": "Weather", "altitude_km": 35786, "velocity_km_s": 3.07, "crew": 0},
            {"name": "Landsat 9", "type": "Earth Observation", "altitude_km": 705, "velocity_km_s": 7.5, "crew": 0},
            {"name": "James Webb", "type": "Telescope", "altitude_km": 1500000, "velocity_km_s": 1.5, "crew": 0},
            {"name": "Starlink-1234", "type": "Communications", "altitude_km": 550, "velocity_km_s": 7.5, "crew": 0},
            {"name": "Terra", "type": "Climate Research", "altitude_km": 705, "velocity_km_s": 7.5, "crew": 0}
        ]
    
    def _initialize_civilizations(self):
        """Initialize major civilizations/countries"""
        return [
            {"name": "United States", "gdp_trillion": 26.9, "population_million": 331, "co2_emissions_gt": 4.7, "technology_index": 95},
            {"name": "China", "gdp_trillion": 17.7, "population_million": 1412, "co2_emissions_gt": 10.7, "technology_index": 88},
            {"name": "India", "gdp_trillion": 3.7, "population_million": 1428, "co2_emissions_gt": 2.6, "technology_index": 65},
            {"name": "European Union", "gdp_trillion": 18.3, "population_million": 447, "co2_emissions_gt": 2.8, "technology_index": 92},
            {"name": "Russia", "gdp_trillion": 2.2, "population_million": 144, "co2_emissions_gt": 1.8, "technology_index": 75},
            {"name": "Japan", "gdp_trillion": 4.2, "population_million": 125, "co2_emissions_gt": 1.1, "technology_index": 94},
            {"name": "Brazil", "gdp_trillion": 2.1, "population_million": 216, "co2_emissions_gt": 0.5, "technology_index": 60},
            {"name": "Pakistan", "gdp_trillion": 0.34, "population_million": 242, "co2_emissions_gt": 0.2, "technology_index": 45}
        ]
    
    def _initialize_resources(self):
        """Initialize Earth's resources"""
        return {
            "fossil_fuels": {
                "oil_billion_barrels": 1700,
                "gas_trillion_cubic_meters": 200,
                "coal_billion_tonnes": 1100,
                "years_remaining": 50
            },
            "renewables": {
                "solar_potential_twh_year": 23000000,
                "wind_potential_twh_year": 850000,
                "hydro_potential_twh_year": 16000,
                "geothermal_potential_twh_year": 2000
            },
            "minerals": {
                "iron_billion_tonnes": 800,
                "copper_million_tonnes": 870,
                "gold_tonnes": 54000,
                "lithium_million_tonnes": 86
            },
            "water": {
                "total_km3": 1386000000,
                "fresh_water_percent": 2.5,
                "available_fresh_water_percent": 0.3
            },
            "food": {
                "annual_production_million_tonnes": 9500,
                "annual_need_million_tonnes": 11000,
                "waste_percent": 30
            }
        }

# ==================== CLIMATE ENGINE ====================
class ClimateEngine:
    """Real-time climate simulation and control"""
    
    def __init__(self):
        self.current_temp = 15.0  # Global average in °C
        self.co2_ppm = 420  # Current CO2 level
        self.sea_level_m = 0  # Sea level rise in meters
        self.ice_melt_gt = 280  # Ice melt in gigatons per year
        self.history = []
        
    def simulate_time_step(self, years=1, human_intervention=None):
        """Simulate climate for given years"""
        # Base changes (without intervention)
        temp_increase = 0.02 * years  # °C per year
        co2_increase = 2.3 * years  # ppm per year
        sea_level_rise = 0.0033 * years  # meters per year
        ice_melt = 280 * years  # gigatons per year
        
        # Apply human intervention if any
        if human_intervention:
            if human_intervention.get("co2_reduction_percent"):
                reduction = human_intervention["co2_reduction_percent"] / 100
                co2_increase *= (1 - reduction)
                temp_increase *= (1 - reduction * 0.5)
            
            if human_intervention.get("carbon_capture_gt"):
                captured = human_intervention["carbon_capture_gt"]
                co2_increase -= captured * 0.47  # 1 GT CO2 captured ≈ 0.47 ppm reduction
            
            if human_intervention.get("geoengineering"):
                if human_intervention["geoengineering"] == "solar_shading":
                    temp_increase *= 0.7
                elif human_intervention["geoengineering"] == "cloud_brightening":
                    temp_increase *= 0.8
        
        # Update values
        self.current_temp += temp_increase
        self.co2_ppm += co2_increase
        self.sea_level_m += sea_level_rise
        self.ice_melt = ice_melt
        
        # Add to history
        self.history.append({
            "year": datetime.now().year + len(self.history),
            "temperature": self.current_temp,
            "co2_ppm": self.co2_ppm,
            "sea_level_m": self.sea_level_m,
            "ice_melt_gt": self.ice_melt
        })
        
        return {
            "temperature_change": temp_increase,
            "co2_change": co2_increase,
            "sea_level_change": sea_level_rise,
            "new_temperature": self.current_temp,
            "new_co2": self.co2_ppm,
            "new_sea_level": self.sea_level_m
        }
    
    def get_climate_projection(self, years=100):
        """Get climate projection for future years"""
        projections = []
        temp = self.current_temp
        co2 = self.co2_ppm
        sea = self.sea_level_m
        
        for year in range(1, years + 1):
            # Business as usual scenario
            temp += 0.02
            co2 += 2.3
            sea += 0.0033
            
            projections.append({
                "year": datetime.now().year + year,
                "temperature_c": round(temp, 2),
                "co2_ppm": round(co2, 1),
                "sea_level_m": round(sea, 3),
                "category": "critical" if temp > 2 else ("warning" if temp > 1.5 else "normal")
            })
        
        return projections
    
    def calculate_impact(self, temperature_change):
        """Calculate impact of temperature change"""
        impacts = []
        
        if temperature_change > 2:
            impacts = [
                "🔥 Extreme heatwaves (40% of land area)",
                "🌊 1-2 meter sea level rise",
                "🌪️ 50% increase in hurricane intensity",
                "🌾 30% crop yield reduction",
                "🏜️ Desert expansion by 25%",
                "🐼 30% species extinction"
            ]
        elif temperature_change > 1.5:
            impacts = [
                "🔥 Severe heatwaves (30% of land area)",
                "🌊 0.5-1 meter sea level rise",
                "🌪️ 30% increase in storm intensity",
                "🌾 15% crop yield reduction",
                "🏜️ Desert expansion by 15%",
                "🐼 20% species extinction"
            ]
        else:
            impacts = [
                "🌡️ Moderate temperature increase",
                "🌊 Limited sea level rise (0.3m)",
                "🌪️ Slight increase in extreme weather",
                "🌾 Minor crop yield changes",
                "🐼 Limited biodiversity impact"
            ]
        
        return impacts

# ==================== RESOURCE MANAGER ====================
class ResourceManager:
    """Manage planetary resources"""
    
    def __init__(self):
        self.resources = {
            "energy": {
                "total_twh": 180000,
                "renewable_percent": 30,
                "storage_capacity_twh": 2000,
                "demand_growth_percent": 2.5
            },
            "water": {
                "available_km3": 42000,
                "consumption_km3_year": 4000,
                "renewable_km3_year": 45000,
                "stress_level": "medium"
            },
            "food": {
                "production_mt": 9500,
                "demand_mt": 11000,
                "waste_percent": 30,
                "distribution_efficiency": 70
            },
            "minerals": {
                "rare_earth_years": 50,
                "lithium_years": 80,
                "copper_years": 40,
                "recycling_rate_percent": 20
            }
        }
        
    def optimize_distribution(self, resource_type, optimization_target):
        """Optimize resource distribution"""
        optimizations = {
            "energy": [
                "Deploy smart grid with AI load balancing",
                "Increase renewable capacity by 15%",
                "Implement demand response programs",
                "Deploy grid-scale battery storage"
            ],
            "water": [
                "Implement smart irrigation systems",
                "Upgrade to water-efficient appliances",
                "Develop desalination plants in coastal areas",
                "Implement rainwater harvesting systems"
            ],
            "food": [
                "Optimize supply chain with blockchain",
                "Reduce food waste through AI monitoring",
                "Implement vertical farming in urban areas",
                "Promote sustainable agricultural practices"
            ],
            "minerals": [
                "Increase recycling to 50%",
                "Develop urban mining technologies",
                "Find substitute materials",
                "Implement circular economy models"
            ]
        }
        
        return optimizations.get(resource_type, ["No optimization available"])

# ==================== CIVILIZATION SIMULATOR ====================
class CivilizationSimulator:
    """Simulate human civilization development"""
    
    def __init__(self):
        self.year = 2024
        self.population = 8100000000
        self.technology_level = 0.73  # Kardashev scale
        self.peace_index = 65
        self.enlightenment_index = 58
        
    def advance_year(self, decisions=None):
        """Advance civilization by one year"""
        # Base growth
        self.year += 1
        self.population *= 1.008  # 0.8% growth
        self.technology_level += 0.005
        
        # Apply decisions
        if decisions:
            if decisions.get("invest_science"):
                self.technology_level += decisions["invest_science"] * 0.01
            
            if decisions.get("invest_peace"):
                self.peace_index = min(100, self.peace_index + decisions["invest_peace"])
            
            if decisions.get("invest_education"):
                self.enlightenment_index = min(100, self.enlightenment_index + decisions["invest_education"])
        
        # Random events
        event = self._generate_random_event()
        
        return {
            "year": self.year,
            "population": int(self.population),
            "technology_level": round(self.technology_level, 3),
            "peace_index": int(self.peace_index),
            "enlightenment_index": int(self.enlightenment_index),
            "event": event
        }
    
    def _generate_random_event(self):
        """Generate random civilization event"""
        events = [
            ("📚", "Scientific breakthrough in quantum computing"),
            ("🕊️", "Major peace treaty signed"),
            ("🌱", "Breakthrough in sustainable agriculture"),
            ("⚡", "New clean energy source discovered"),
            ("🌍", "Global environmental agreement reached"),
            ("🤖", "AI achieves human-level reasoning"),
            ("🚀", "Successful Mars colony established"),
            ("💡", "Universal basic income implemented globally"),
            ("🌌", "First contact with extraterrestrial intelligence"),
            ("🔄", "Circular economy becomes mainstream")
        ]
        
        return random.choice(events)
    
    def predict_future(self, years=100):
        """Predict civilization future"""
        predictions = []
        
        for i in range(years):
            year = self.year + i
            tech = self.technology_level + (i * 0.005)
            pop = self.population * (1.008 ** i)
            
            if tech >= 1.0 and i < 30:
                predictions.append(f"Year {year}: 🌟 Type I Civilization achieved - Full planetary energy control")
            elif tech >= 2.0 and i < 100:
                predictions.append(f"Year {year}: 🚀 Type II Civilization - Dyson sphere construction begins")
            elif tech >= 3.0 and i < 500:
                predictions.append(f"Year {year}: 🌌 Type III Civilization - Galactic energy network")
            
            if pop >= 10000000000 and i < 50:
                predictions.append(f"Year {year}: 👥 Population reaches 10 billion")
            
            if self.peace_index + (i * 0.5) >= 90 and i < 80:
                predictions.append(f"Year {year}: 🕊️ World peace achieved (Peace Index > 90)")
        
        return predictions[:10]  # Return top 10 predictions

# ==================== INTERSTELLAR COMMUNICATIONS ====================
class InterstellarCommunications:
    """Handle communications with other celestial bodies"""
    
    def __init__(self):
        self.exoplanets = self._initialize_exoplanets()
        self.messages_sent = []
        self.messages_received = []
        
    def _initialize_exoplanets(self):
        """Initialize known exoplanets"""
        return [
            {"name": "Proxima Centauri b", "distance_ly": 4.24, "type": "Rocky", "habitable": True, "confidence": 85},
            {"name": "TRAPPIST-1e", "distance_ly": 39.5, "type": "Rocky", "habitable": True, "confidence": 90},
            {"name": "Kepler-452b", "distance_ly": 1400, "type": "Super-Earth", "habitable": True, "confidence": 75},
            {"name": "Gliese 581g", "distance_ly": 20.3, "type": "Rocky", "habitable": True, "confidence": 80},
            {"name": "HD 40307g", "distance_ly": 42.4, "type": "Super-Earth", "habitable": True, "confidence": 70}
        ]
    
    def send_message(self, exoplanet, message):
        """Send message to exoplanet"""
        travel_time = exoplanet["distance_ly"]  # One-way in years
        
        self.messages_sent.append({
            "timestamp": datetime.now(),
            "destination": exoplanet["name"],
            "distance_ly": exoplanet["distance_ly"],
            "message": message,
            "arrival_year": datetime.now().year + int(travel_time),
            "round_trip_years": int(travel_time * 2)
        })
        
        return {
            "status": "Message transmitted",
            "destination": exoplanet["name"],
            "distance_light_years": exoplanet["distance_ly"],
            "estimated_arrival": datetime.now().year + int(travel_time),
            "round_trip_time_years": int(travel_time * 2),
            "message_id": len(self.messages_sent)
        }
    
    def simulate_reply(self, message_id):
        """Simulate reply from exoplanet (for demo)"""
        if message_id <= len(self.messages_sent):
            original = self.messages_sent[message_id - 1]
            
            replies = [
                "Greetings from another world. We have been observing your civilization.",
                "Your mathematical patterns are intriguing. We share similar concepts.",
                "Peace and knowledge. We propose exchange of scientific information.",
                "Detected your radio signals centuries ago. Welcome to the galactic community.",
                "Your planet's biosphere is unique. We value biodiversity.",
                "We have been silent observers. Your technological progress is remarkable.",
                "Proceed with caution. Advanced technology requires wisdom.",
                "The universe is vast. Cooperation ensures survival.",
                "Your art and music frequencies are beautiful. Share more.",
                "Time is relative. Your century is our moment."
            ]
            
            reply = random.choice(replies)
            
            self.messages_received.append({
                "timestamp": datetime.now(),
                "source": original["destination"],
                "original_message_id": message_id,
                "reply": reply,
                "translation_confidence": random.randint(75, 98)
            })
            
            return {
                "source": original["destination"],
                "reply": reply,
                "translation_confidence": f"{random.randint(75, 98)}%",
                "estimated_distance": original["distance_ly"],
                "time_traveled_years": original["distance_ly"]
            }
        
        return {"error": "Message not found"}

# ==================== TIME MANIPULATION ENGINE ====================
class TimeManipulationEngine:
    """Advanced time manipulation and simulation"""
    
    def __init__(self):
        self.current_timeline = "Prime Timeline"
        self.alternate_timelines = []
        self.temporal_energy = 100
        
    def create_alternate_timeline(self, divergence_point, change_description):
        """Create alternate timeline"""
        timeline_id = f"ATL-{len(self.alternate_timelines) + 1:04d}"
        
        consequences = self._calculate_consequences(change_description)
        
        timeline = {
            "id": timeline_id,
            "divergence_point": divergence_point,
            "change": change_description,
            "created": datetime.now(),
            "consequences": consequences,
            "stability": random.randint(30, 90),
            "energy_cost": 10
        }
        
        self.alternate_timelines.append(timeline)
        self.temporal_energy -= 10
        
        return timeline
    
    def _calculate_consequences(self, change):
        """Calculate consequences of timeline change"""
        consequences = []
        
        if "war" in change.lower():
            consequences = [
                "Military technology advanced by 20 years",
                "Global population reduced by 15%",
                "Space exploration delayed by 50 years",
                "Environmental regulations abandoned"
            ]
        elif "peace" in change.lower():
            consequences = [
                "Global cooperation increased",
                "Science funding tripled",
                "Space colonization accelerated",
                "Renewable energy dominant by 2040"
            ]
        elif "technology" in change.lower():
            consequences = [
                "AI singularity achieved earlier",
                "Quantum computing mainstream",
                "Interstellar travel possible",
                "Post-scarcity economy emerges"
            ]
        elif "environment" in change.lower():
            consequences = [
                "Climate crisis averted",
                "Biodiversity restored",
                "Circular economy achieved",
                "Human lifespan increased"
            ]
        else:
            consequences = [
                "Butterfly effect creates unforeseen changes",
                "Cultural evolution takes different path",
                "Technological development
