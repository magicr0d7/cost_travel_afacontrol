import streamlit as st
st.logo('https://www.afacontrole.fr/wp-content/uploads/2022/04/AFA-CONTROLE-Verifications-reglementaires-logo.png')
COST_PER_KM = 0.427  # Barème kilométrique 2023
HOTEL_COST = 150   # Nuit d'hôtel (modifiable selon la région)
TRAJET_COST_1H_4H = 250.0
TRAJET_COST_4H_8H = 500.0
TRAJET_COST_OVER_8H = 0  # À valider manuellement

# Function to calculate the total costs
def calculate_travel_costs(duration_hours, km_total, hotel_nights, toll_fees, parking_fees, flight_or_train_costs):
    # Calculer les frais de mise à disposition selon la durée
    if duration_hours == 0:
        travel_cost = 0
    elif 1 <= duration_hours < 4:
        travel_cost = TRAJET_COST_1H_4H
    elif 4 <= duration_hours < 8:
        travel_cost = TRAJET_COST_4H_8H
    else:
        # Plus de 8h nécessite une validation
        travel_cost = TRAJET_COST_OVER_8H
        st.write("Le montant pour un trajet de plus de 8h doit être validé par le siège.")

    # Calculer les frais de déplacement
    km_cost = km_total * COST_PER_KM
    hotel_cost = hotel_nights * HOTEL_COST

    # Calculer le total
    total_cost = travel_cost + km_cost + hotel_cost + toll_fees + parking_fees + flight_or_train_costs

    return total_cost

st.markdown("# Calculateur de frais de déplacement")
st.subheader("Frais de mise à disposition")
col1, col2 = st.columns(2)
with col1:
    duration_hours = st.number_input("Durée en h du déplacement", min_value=0, step=1)
with col2:
    st.write('P.U. : 250 € | 4 à 8h de trajet : 500 €')
    st.write("Au-delà de 8h : montant à faire valider par le siège avant envoi au client.")

st.subheader("Frais de déplacement")
col1, col2 = st.columns(2)
with col1:
    km_total = st.number_input("Nombre de Km total", min_value=0, step=1)
with col2:
    cost_per_km = st.number_input("Coût au km (€), par défaut : 0.427", min_value=0.1, step=0.1, value=COST_PER_KM)

col1, col2 = st.columns(2)  
with col1:
    hotel_nights = st.number_input("Nuit d'hôtel", min_value=0, step=1)

with col2:
    hotel_cost = st.number_input("Coût par nuit d'hôtel (€), par défaut : 150", min_value=0, step=1, value=HOTEL_COST)
    
toll_fees = st.number_input("Péage (€)", min_value=0, step=1)
parking_fees = st.number_input("Parking (€)", min_value=0, step=1)
flight_or_train_costs = st.number_input("Billet avion / train (€)", min_value=0, step=1)

if st.button("Calculer les frais"):
    total_cost = calculate_travel_costs(duration_hours, km_total, hotel_nights, toll_fees, parking_fees, flight_or_train_costs)
    st.write(f"Le montant total des frais de déplacement est de {total_cost} euros.")