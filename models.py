# models.py
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD

def crear_modelo():
    # Definición de enfermedades
    # Tuberculosis, COVID_19, Bronquitis, Faringitis, Neumonia

    # Definición de síndromes
    # Sindrome respiratorio agudo, Sindrome infeccioso, Resfriado, Sindrome faríngeo,
    # Tos persistente, Sindrome constitucional, Sindrome pulmonar severo

    # Definición de síntomas
    # Fiebre, Tos, Fatiga, Dolor de garganta, Hemoptisis, Dificultad respiratoria,
    # Dolor en el pecho, Sudores nocturnos, Pérdida de peso

    relaciones = [
        # Relaciones de síndromes con síntomas
        # Relaciones de enfermedades con síndromes
        # La Tuberculosis puede causar Tos persistente.
        ("Tuberculosis", "Tos_persistente"),  # TBC puede causar Tos persistente
        ("Tuberculosis", "Sindrome_constitucional"),  # TBC puede causar Síndrome constitucional
        ("COVID_19", "Sindrome_infeccioso"),  # COVID-19 puede causar Síndrome infeccioso
        ("COVID_19", "Sindrome_respiratorio_agudo"),  # COVID-19 puede causar Síndrome respiratorio agudo
        ("Bronquitis", "Sindrome_infeccioso"),  # Bronquitis puede causar Síndrome infeccioso
        ("Bronquitis", "Resfriado"),  # Bronquitis puede causar Resfriado
        ("Faringitis", "Sindrome_faringeo"),  # Faringitis puede causar Síndrome faríngeo
        ("Neumonia", "Sindrome_respiratorio_agudo"),  # Neumonía puede causar Síndrome respiratorio agudo
        ("Neumonia", "Sindrome_pulmonar_severo"),  # Neumonía puede causar Síndrome pulmonar severo
        ("Resfriado", "Sindrome_faringeo"),
        ("Sindrome_infeccioso", "Fiebre"),  # Síndrome infeccioso puede causar Fiebre,
        ("Sindrome_infeccioso", "Tos"),  # Síndrome infeccioso puede causar Tos,
        ("Sindrome_infeccioso", "Fatiga"),  # Síndrome infeccioso puede causar Fatiga,
        ("Resfriado", "Tos"),  # Resfriado puede causar Tos,
        ("Resfriado", "Dolor_de_garganta"),  # Resfriado puede causar Dolor de garganta,
        ("Sindrome_faringeo", "Dolor_de_garganta"),  # Síndrome faríngeo puede causar Dolor de garganta,
        ("Sindrome_faringeo", "Fiebre"),  # Síndrome faríngeo puede causar Fiebre,
        ("Tos_persistente", "Tos"),  # Tos persistente puede causar Tos,
        ("Tos_persistente", "Hemoptisis"),  # Tos persistente puede causar Hemoptisis,
        ("Sindrome_respiratorio_agudo", "Dificultad_respiratoria"),  # Síndrome respiratorio agudo puede causar Dificultad respiratoria,
        ("Sindrome_respiratorio_agudo", "Dolor_en_el_pecho"),  # Síndrome respiratorio agudo puede causar Dolor en el pecho,
        ("Sindrome_constitucional", "Fatiga"),  # Síndrome constitucional puede causar Fatiga,
        ("Sindrome_constitucional", "Sudores_nocturnos"),  # Síndrome constitucional puede causar Sudores nocturnos,
        ("Sindrome_constitucional", "Perdida_de_peso"),  # Síndrome constitucional puede causar Pérdida de peso,
        ("Sindrome_pulmonar_severo", "Fiebre"),  # Síndrome pulmonar severo puede causar Fiebre,
        ("Sindrome_pulmonar_severo", "Dificultad_respiratoria"),  # Síndrome pulmonar severo puede causar Dificultad respiratoria,
        ("Sindrome_pulmonar_severo", "Hemoptisis"),  # Síndrome pulmonar severo puede causar Hemoptisis
    ]
    model = DiscreteBayesianNetwork(relaciones)

    cpd_tuberculosis = TabularCPD(variable='Tuberculosis', variable_card=2, values=[[0.99], [0.01]])  # P(No) = 0.999, P(Sí) = 0.001
    cpd_covid = TabularCPD(variable='COVID_19', variable_card=2, values=[[0.95], [0.05]])       # P(No) = 0.95, P(Sí) = 0.05
    cpd_bronquitis = TabularCPD(variable='Bronquitis', variable_card=2, values=[[0.95], [0.05]]) # P(No) = 0.95, P(Sí) = 0.05
    cpd_faringitis = TabularCPD(variable='Faringitis', variable_card=2, values=[[0.93], [0.08]])   # P(No) = 0.9, P(Sí) = 0.1
    cpd_neumonia = TabularCPD(variable='Neumonia', variable_card=2, values=[[0.94], [0.06]])     # P(No) = 0.94, P(Sí) = 0.06


    cpd_sindrome_infeccioso = TabularCPD(
    variable='Sindrome_infeccioso',
    variable_card=2,
    values=[
        [0.95, 0.8, 0.7, 0.5, 0.85, 0.6, 0.4, 0.1],  # P(No | combinaciones de padres)
        [0.05, 0.2, 0.3, 0.5, 0.15, 0.4, 0.6, 0.9]   # P(Sí | combinaciones de padres)
    ],
    evidence=['Fiebre', 'Tos', 'Fatiga'],
    evidence_card=[2, 2, 2]
    )

    cpd_s_constitucional = TabularCPD(
    variable='Sindrome_constitucional',
    variable_card=2,
    values=[
        [0.9, 0.7, 0.6, 0.3, 0.8, 0.5, 0.4, 0.1],  # P(No | combinaciones)
        [0.1, 0.3, 0.4, 0.7, 0.2, 0.5, 0.6, 0.9]   # P(Sí | combinaciones)
    ],
    evidence=['Fatiga', 'Sudores_nocturnos', 'Perdida_de_peso'],
    evidence_card=[2, 2, 2]
    )

    cpd_s_pulmonar_severo = TabularCPD(
    variable='Sindrome_pulmonar_severo',
    variable_card=2,
    values=[
        [0.95, 0.9, 0.85, 0.8, 0.7, 0.6, 0.5, 0.4, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1,
         0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.15, 0.1, 0.5, 0.4, 0.3, 0.2, 0.15, 0.1, 0.05, 0.01],
        [0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
         0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.99]
    ],
    evidence=['Dificultad_respiratoria', 'Dolor_en_el_pecho', 'Sudores_nocturnos', 'Perdida_de_peso', 'Hemoptisis'],
    evidence_card=[2, 2, 2, 2, 2]
    )

    cpd_sindrome_respiratorio_agudo = TabularCPD(
    variable='Sindrome_respiratorio_agudo',
    variable_card=2,
    values=[
        [0.1395, 0.93, 0.15, 0.9405],  # P(No)
        [0.8605, 0.07, 0.85, 0.0595]   # P(Sí)
    ],
    evidence=['COVID_19', 'Neumonia'],
    evidence_card=[2, 2]
    )
    # Orden de combinaciones:
    # COVID_19 = 0, Neumonia = 0 → P(No) = 0.8605, P(Sí) = 0.1395
    # COVID_19 = 0, Neumonia = 1 → P(No) = 0.2095, P(Sí) = 0.7905
    # COVID_19 = 1, Neumonia = 0 → P(No) = 0.9895, P(Sí) = 0.0105
    # COVID_19 = 1, Neumonia = 1 → P(No) = 0.9405, P(Sí) = 0.0595
    # Valores calculados asumiendo independencia condicional entre COVID_19 y Neumonia respecto al Síndrome respiratorio agudo.

    cpd_sindrome_infeccioso = TabularCPD(
        variable='Sindrome_infeccioso',
        variable_card=2,
        values=[
            [0.01, 0.1, 0.1, 0.19],  # P(No) en cada combinación
            [0.99, 0.9, 0.9, 0.81]   # P(Sí) en cada combinación
        ],
        evidence=['COVID_19', 'Bronquitis'],
        evidence_card=[2, 2]
    )


    cpd_resfriado = TabularCPD(
        variable='Resfriado',
        variable_card=2,
        values=[
            [0.33, 0.67],  # P(No) | Bronquitis = 0, 1
            [0.67, 0.33]   # P(Sí)  | Bronquitis = 0, 1
        ],
        evidence=['Bronquitis'],
        evidence_card=[2]
    )

    cpd_sindrome_faringeo = TabularCPD(
        variable='Sindrome_faringeo',
        variable_card=2,
        values=[
        
            [0.99, 0.2, 0.3, 0.01],  # P(No)
            [0.01, 0.8, 0.7, 0.99]   # P(Sí)
        ],
        evidence=['Resfriado', 'Faringitis'],
        evidence_card=[2, 2]
    )

    cpd_tos_persistente = TabularCPD(
        variable='Tos_persistente',
        variable_card=2,
        values=[
            [0.90, 0.10],  # P(No) | Tuberculosis = 0, 1
            [0.10, 0.90]   # P(Sí) | Tuberculosis = 0, 1
        ],
        evidence=['Tuberculosis'],
        evidence_card=[2]
    )

    cpd_sindrome_constitucional = TabularCPD(
        variable='Sindrome_constitucional',
        variable_card=2,
        values=[
            [0.25, 0.75],  # P(No) | Tuberculosis = 0, 1
            [0.75, 0.25]   # P(Sí) | Tuberculosis = 0, 1
        ],
        evidence=['Tuberculosis'],
        evidence_card=[2]
    )

    cpd_sindrome_pulmonar_severo = TabularCPD(
        variable='Sindrome_pulmonar_severo',
        variable_card=2,
        values=[
            [0.40, 0.60],  # P(No) | Neumonia = 0, 1
            [0.60, 0.40]   # P(Sí) | Neumonia = 0, 1
        ],
        evidence=['Neumonia'],
        evidence_card=[2]
    )

    cpd_fiebre = TabularCPD(
        variable='Fiebre',
        variable_card=2,
        values=[
            [0.84985, 0.64965, 0.91915, 0.81135, 0.95515, 0.72915, 0.94635, 0.76905],  # P(No)
            [0.15015, 0.35035, 0.08085, 0.18865, 0.04485, 0.27085, 0.05365, 0.23095]   # P(Sí)
        ],
        evidence=['Sindrome_infeccioso', 'Sindrome_faringeo', 'Sindrome_pulmonar_severo'],
        evidence_card=[2, 2, 2]
    )
    # Orden de combinaciones:
    # (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
    # (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)
    # Valores calculados asumiendo independencia condicional entre los síndromes respecto a Fiebre.
    cpd_tos = TabularCPD(
        variable='Tos',
        variable_card=2,
        values=[
            [1.00, 1.00, 0.79, 0.91, 1.00, 1.00, 0.51, 0.79],  # P(No)
            [0.00, 0.00, 0.21, 0.09, 0.00, 0.00, 0.49, 0.21]   # P(Sí)
        ],
        evidence=['Sindrome_infeccioso', 'Tos_persistente', 'Resfriado'],
        evidence_card=[2, 2, 2]
    )

    cpd_fatiga = TabularCPD(
        variable='Fatiga',
        variable_card=2,
        values=[
            [0.21, 0.7, 0.3, 0.79],  # P(No) para cada combinación
            [0.79, 0.3, 0.7, 0.21]   # P(Sí) para cada combinación
        ],
        evidence=['Sindrome_infeccioso', 'Sindrome_constitucional'],
        evidence_card=[2, 2]
    )

    cpd_dolor_de_garganta = TabularCPD(
        variable='Dolor_de_garganta',
        variable_card=2,
        values=[
            [0.21, 0.7, 0.3, 0.79],  # P(No) para cada combinación
            [0.79, 0.3, 0.7, 0.21]   # P(Sí) para cada combinación
        ],
        evidence=['Resfriado', 'Sindrome_faringeo'],
        evidence_card=[2, 2]
    )

    cpd_hemoptisis = TabularCPD(
        variable='Hemoptisis',
        variable_card=2,
        values=[
            [0.16, 0.4, 0.4, 0.64],  # P(No) en cada combinación
            [0.84, 0.6, 0.6, 0.36]   # P(Sí) en cada combinación
        ],
        evidence=['Tos_persistente', 'Sindrome_pulmonar_severo'],
        evidence_card=[2, 2]
    )


    cpd_dificultad_respiratoria = TabularCPD(
        variable='Dificultad_respiratoria',
        variable_card=2,
        values=[
            [0.184, 0.4, 0.46, 0.676],  # P(No) en cada combinación
            [0.816, 0.6, 0.54, 0.324]   # P(Sí) en cada combinación
        ],
        evidence=['Sindrome_respiratorio_agudo', 'Sindrome_pulmonar_severo'],
        evidence_card=[2, 2]
    )


    cpd_dolor_en_el_pecho = TabularCPD(
        variable='Dolor_en_el_pecho',
        variable_card=2,
        values=[
            [0.16, 0.84],  # P(No)
            [0.84, 0.16]   # P(Sí)
        ],
        evidence=['Sindrome_respiratorio_agudo'],
        evidence_card=[2]
    )

    cpd_sudores_nocturnos = TabularCPD(
        variable='Sudores_nocturnos',
        variable_card=2,
        values=[
            [0.45, 0.55],  # P(No)
            [0.55, 0.45]   # P(Sí)
        ],
        evidence=['Sindrome_constitucional'],
        evidence_card=[2]
    )


    cpd_perdida_de_peso = TabularCPD(
        variable='Perdida_de_peso',
        variable_card=2,
        values=[
            [0.55, 0.45],  # P(No)
            [0.45, 0.55]   # P(Sí)
        ],
        evidence=['Sindrome_constitucional'],
        evidence_card=[2]
    )

    model.add_cpds(
        cpd_tuberculosis,
        cpd_covid,
        cpd_bronquitis,
        cpd_faringitis,
        cpd_neumonia,
        cpd_sindrome_infeccioso,
        cpd_s_constitucional,
        cpd_s_pulmonar_severo,
        cpd_sindrome_respiratorio_agudo,
        cpd_resfriado,
        cpd_sindrome_faringeo,
        cpd_tos_persistente,
        cpd_sindrome_constitucional,
        cpd_sindrome_pulmonar_severo,
        cpd_fiebre,
        cpd_tos,
        cpd_fatiga,
        cpd_dolor_de_garganta,
        cpd_hemoptisis,
        cpd_dificultad_respiratoria,
        cpd_dolor_en_el_pecho,
        cpd_sudores_nocturnos,
        cpd_perdida_de_peso
    )

    assert model.check_model()
    return model
