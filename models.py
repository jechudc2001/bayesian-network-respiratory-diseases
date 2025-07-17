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

    cpd_tuberculosis = TabularCPD(variable='Tuberculosis', variable_card=2, values=[[0.999], [0.001]])  # P(No) = 0.999, P(Sí) = 0.001
    cpd_covid = TabularCPD(variable='COVID_19', variable_card=2, values=[[0.95], [0.05]])       # P(No) = 0.95, P(Sí) = 0.05
    cpd_bronquitis = TabularCPD(variable='Bronquitis', variable_card=2, values=[[0.95], [0.05]]) # P(No) = 0.95, P(Sí) = 0.05
    cpd_faringitis = TabularCPD(variable='Faringitis', variable_card=2, values=[[0.9], [0.1]])   # P(No) = 0.9, P(Sí) = 0.1
    cpd_neumonia = TabularCPD(variable='Neumonia', variable_card=2, values=[[0.94], [0.06]])     # P(No) = 0.94, P(Sí) = 0.06




    cpd_sindrome_constitucional = TabularCPD(
        variable='Sindrome_constitucional',
        variable_card=2,
      
        values=[
        [0.75, 0.25],  # P(No | TBC=0)=0.75, P(No | TBC=1)=0.25
        [0.25, 0.75]   # P(Si | TBC=0)=0.25, P(Si | TBC=1)=0.75
        ],
        evidence=['Tuberculosis'],
        evidence_card=[2]
    )

    cpd_sindrome_pulmonar_severo = TabularCPD(
        variable='Sindrome_pulmonar_severo',
        variable_card=2,
       
        values=[
        [0.60, 0.40],  # P(SP='No'  | Neumonia=0), P(SP='No'  | Neumonia=1)
        [0.40, 0.60]   # P(SP='Si'  | Neumonia=0), P(SP='Si'  | Neumonia=1)
        ],
        evidence=['Neumonia'],
        evidence_card=[2]
    )

    cpd_sindrome_respiratorio_agudo = TabularCPD(
    variable='Sindrome_respiratorio_agudo',
    variable_card=2,
    values=[
        [0.8605, 0.85, 0.07, 0.9405],
        [0.1395, 0.15, 0.93, 0.0595]
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
            [0.99, 0.9, 0.9, 0.81],
            [0.01, 0.1, 0.1, 0.19]  # P(No) en cada combinación  # P(Sí) en cada combinación
        ],
        evidence=['COVID_19', 'Bronquitis'],
        evidence_card=[2, 2]
    )


    cpd_resfriado = TabularCPD(
        variable='Resfriado',
        variable_card=2,
        values=[
            [0.67, 0.33],
            [0.33, 0.67],  # P(No) | Bronquitis = 0, 1# P(Sí)  | Bronquitis = 0, 1
        ],
        evidence=['Bronquitis'],
        evidence_card=[2]
    )

    cpd_sindrome_faringeo = TabularCPD(
        variable='Sindrome_faringeo',
        variable_card=2,
        values=[
            [0.99, 1.00, 0.30, 0.01],  # P(No) para (Resfriado,Faringitis) = (0,0),(0,1),(1,0),(1,1)
            [0.01, 0.00, 0.70, 0.99]   # P(Sí) ...
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



    cpd_fiebre = TabularCPD(
        'Fiebre', 2,
        [
        [0.84985, 0.30, 0.65, 0.81135, 0.77,   0.72915, 0.94635, 0.76905],
        [0.15015, 0.70, 0.35, 0.18865, 0.23,   0.27085, 0.05365, 0.23095]
        ],
        ['Sindrome_infeccioso','Sindrome_faringeo','Sindrome_pulmonar_severo'],
        [2,2,2]
    )
    
    cpd_tos = TabularCPD(
        'Tos', 2,
        [
            [1.0, 0.7, 0.0, 0.0, 0.3, 0.21, 0.0, 0.0],  # P(Tos=No | Inf, Pers, Res)
            [0.0, 0.3, 1.0, 1.0, 0.7, 0.79, 1.0, 1.0]   # P(Tos= Sí | Inf, Pers, Res)
        ],
        ['Sindrome_infeccioso', 'Tos_persistente', 'Resfriado'],
        [2, 2, 2]
    )

    cpd_fatiga = TabularCPD(
        'Fatiga', 2,
        [
            [0.21, 0.30, 0.70, 0.79],  # P(No) | (Inf,Const) = (0,0),(1,0),(0,1),(1,1)
            [0.79, 0.70, 0.30, 0.21]   # P(Sí) | (Inf,Const) = (0,0),(1,0),(0,1),(1,1)
        ],
        ['Sindrome_infeccioso', 'Sindrome_constitucional'],
        [2, 2]
    )

    cpd_dolor_de_garganta = TabularCPD(
        'Dolor_de_garganta', 2,
        [
            [0.21, 0.00, 0.00, 0.00],  # P(No) | (Resfriado,Síndrome_faringeo) = (0,0),(0,1),(1,0),(1,1)
            [0.79, 1.00, 1.00, 1.00]   # P(Sí)                             
        ],
        ['Resfriado', 'Sindrome_faringeo'],
        [2, 2]
    )

    cpd_hemoptisis = TabularCPD(
        'Hemoptisis', 2,
        [
            [1.00, 0.40, 0.40, 0.16],  # P(No | Tos=0,SPul=0),(0,1),(1,0),(1,1)
            [0.00, 0.60, 0.60, 0.84]   # P(Sí | Tos=0,SPul=0),(0,1),(1,0),(1,1)
        ],
        ['Tos_persistente', 'Sindrome_pulmonar_severo'],
        [2, 2]
    )


    cpd_dificultad_respiratoria = TabularCPD(
        'Dificultad_respiratoria', 2,
        [
            [0.184, 0.46, 0.40, 0.676],  # P(No)  | (SR=0,SP=0),(0,1),(1,0),(1,1)
            [0.816, 0.54, 0.60, 0.324]   # P(Sí)  | (SR=0,SP=0),(0,1),(1,0),(1,1)
        ],
        ['Sindrome_respiratorio_agudo', 'Sindrome_pulmonar_severo'],
        [2, 2]
    )


    cpd_dolor_en_el_pecho = TabularCPD(
        'Dolor_en_el_pecho', 2,
        [
            [1.00, 0.84],  # P(Dolor_pecho=No  | SRA=0)=1.00,  P(Dolor_pecho=No  | SRA=1)=0.84
            [0.00, 0.16]   # P(Dolor_pecho=Sí  | SRA=0)=0.00,  P(Dolor_pecho=Sí  | SRA=1)=0.16
        ],
        ['Sindrome_respiratorio_agudo'],
        [2]
    )


    cpd_sudores_nocturnos = TabularCPD(
        'Sudores_nocturnos', 2,
        [
            [0.45, 0.55],  # P(No | Sindrome_constitucional=0), P(No | =1)
            [0.55, 0.45]   # P(Sí | Sindrome_constitucional=0), P(Sí | =1)
        ],
        ['Sindrome_constitucional'],
        [2]
    )


    cpd_perdida_de_peso = TabularCPD(
        'Perdida_de_peso', 2,
        [
            [0.55, 0.45],  # P(No | Sindrome_constitucional=0), P(No | Sindrome_constitucional=1)
            [0.45, 0.55]   # P(Sí | Sindrome_constitucional=0), P(Sí | Sindrome_constitacional=1)
        ],
        ['Sindrome_constitucional'],
        [2]
    )

    model.add_cpds(
        cpd_tuberculosis,
        cpd_covid,
        cpd_bronquitis,
        cpd_faringitis,
        cpd_neumonia,
        cpd_sindrome_infeccioso,
        cpd_sindrome_constitucional,
        cpd_sindrome_pulmonar_severo,
        cpd_sindrome_respiratorio_agudo,
        cpd_resfriado,
        cpd_sindrome_faringeo,
        cpd_tos_persistente,
        cpd_fiebre,
        cpd_tos,
        cpd_fatiga,
        cpd_dolor_de_garganta,
        cpd_hemoptisis,
        cpd_dificultad_respiratoria,
        cpd_dolor_en_el_pecho,   # sólo UNA vez
        cpd_sudores_nocturnos,
        cpd_perdida_de_peso
    )

    assert model.check_model()
    print(model.get_cpds('Fiebre'))
    return model
    
