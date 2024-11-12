import streamlit as st

st.logo('https://www.afacontrole.fr/wp-content/uploads/2022/04/AFA-CONTROLE-Verifications-reglementaires-logo.png')

st.set_page_config(page_title="Calculateur de frais de déplacement", page_icon="🚗")

# Function to calculate the total costs
def calculate_travel_costs(duration_hours, km_total, hotel_nights, toll_fees, parking_fees, flight_or_train_costs,cost_per_km, hotel_cost):
    # Calculer les frais de mise à disposition selon la durée
    if duration_hours == 0:
        travel_cost = 0
    elif 1 <= duration_hours < 4:
        travel_cost = 250.0
    elif 4 <= duration_hours < 8:
        travel_cost = 500.0
    else:
        # Plus de 8h nécessite une validation
        travel_cost = 0
        st.error("Le montant pour un trajet de plus de 8h doit être validé par le siège.")

    km_cost = km_total * cost_per_km
    hotel_cost = hotel_nights * hotel_cost

    # Calculer le total
    total_cost = travel_cost + km_cost + hotel_cost + toll_fees + parking_fees + flight_or_train_costs

    return total_cost

st.markdown("# Calculateur de frais de déplacement")

st.info("""Spécificités : 

Voici les frais d’hôtel à indiquer  : 
- NATUP et filiale / UAPL et filiale facturer :  80 /90 € Jour + frais Km et péage classique 
- SEVEPI / TEREOS / SALEFACTORY    100/ 110 € Jour + frais Km et péage classique 
- Super U :    150 € /Jour + 

Inférieur à 300 kms	au réel () / De 300 à 499 kms	150 € / De 500 à 699 kms	175 € / De 700 à 999 kms	240 € / Supérieur à 1000 kms	300 €""", icon="💡")

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
    cost_per_km = st.number_input("Coût au km (€)", min_value=0.01, step=0.01)

col1, col2 = st.columns(2)  
with col1:
    hotel_nights = st.number_input("Nuit d'hôtel", min_value=0, step=1)

with col2:
    hotel_cost = st.number_input("Coût par nuit d'hôtel (€), par défaut : 150", min_value=0, step=1, value=150)
    
toll_fees = st.number_input("Péage (€)", min_value=0, step=1)
parking_fees = st.number_input("Parking (€)", min_value=0, step=1)
flight_or_train_costs = st.number_input("Billet avion / train (€)", min_value=0, step=1)

if st.button("Calculer les frais"):
    if duration_hours < 8:
        total_cost = calculate_travel_costs(duration_hours, km_total, hotel_nights, toll_fees, parking_fees, flight_or_train_costs, cost_per_km, hotel_cost)
        st.info(f"Le montant total des frais de déplacement est de {total_cost:.3f} euros.")
    else:
        st.error("Le montant pour un trajet de plus de 8h doit être validé par le siège.")