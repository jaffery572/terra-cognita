import numpy as np
from sklearn.ensemble import RandomForestClassifier

class RogueDroneAI:
    def __init__(self):
        self.tactics_model = self.train_evasion_model()
    
    def predict_evasion(self, jammer_detected, interceptor_range):
        """ML predicts best counter-tactic per threat type"""
        features = np.array([[jammer_detected, interceptor_range]])
        return self.tactics_model.predict(features)[0]  # ['terrain_mask', 'altitude_spike', 'swarm_split']
