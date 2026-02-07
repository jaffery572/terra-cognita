import streamlit as st
import plotly.graph_objects as go
import numpy as np
from physics_engine import DroneSwarmSimulator
from ai_tactics import RogueDroneAI
from scenario_library import load_scenario

st.set_page_config(page_title="C-UAS Training Simulator", layout="wide")
st.title("🎯 Counter-Drone Command Center")
st.markdown("**Real-time tactical training** - Anduril/Dedrone class scenarios")

# Mission selector (exportable to PDF)
mission = st.selectbox("Select Threat Scenario", 
    ["Shahed-136 Swarm (Ukraine)", "DJI Phantom Airport Breach", "Cargo Bay Smuggler"])

if mission:
    scenario = load_scenario(mission)
    sim = DroneSwarmSimulator(scenario['drones'], scenario['jammer_range'])
    
    # Live 3D battle view
    col1, col2 = st.columns([2,1])
    
    with col1:
        fig = go.Figure()
        # Drone positions + jammer coverage
        for drone_id, drone in sim.drones.items():
            fig.add_trace(go.Scatter3d(
                x=[drone.x], y=[drone.y], z=[drone.z],
                mode='markers+text', marker=dict(size=8, color='red'),
                text=f"Drone {drone_id}: {drone.altitude:.0f}m",
                name=f"Rogue {drone_id}"
            ))
        st.plotly_chart(fig, key="battlefield")
    
    with col2:
        st.metric("Threats Active", len(sim.drones))
        st.metric("Jammer Coverage", f"{sim.coverage_pct:.1f}%")
        
        # Tactical controls (RF Jam, Kinetic Intercept, Cyber takeover)
        action = st.radio("Engage with:", 
            ["RF Jam 2.4GHz", "High-Power Microwave", "Directed Energy", "Cyber Hijack"])
        
        if st.button("EXECUTE") and sim.is_active:
            success_rate = sim.execute_countermeasure(action)
            st.success(f"🟢 {success_rate:.1f}% neutralized")
            st.balloons()
    
    # After Action Review (AAR) - Military standard
    st.header("📊 Mission Debrief")
    metrics = sim.get_aar_metrics()
    col1, col2, col3 = st.columns(3)
    col1.metric("Time to Intercept", f"{metrics['tti']:.1f}s")
    col2.metric("Success Rate", f"{metrics['success']:.1f}%")
    col3.metric("Collateral Risk", f"{metrics['collateral']:.2f}%")
