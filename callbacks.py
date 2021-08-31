import dash_table as dt
import dash_core_components as dcc
#import plotly.express as pxxs
import plotly.express as px
import dash_html_components as html
# import dash IO and graph objects
from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER
# Plotly graph objects to render graph plots

# Import dash html, bootstrap components, and tables for datatables
import dash_table

# Import app
from app import app
import pandas as pd

# Import custom data.py
import data



# Import data from data.py file


eni_complete=data.eni_complete

        
listado_resultados=['Nivel', 'Edad', 'Sexo', 
                    'Órgano de Operación Administrativa Desconcentrado (OOAD)', 'Regiones']
secciones_preg={'Actuación del IMSS ante la contingencia sanitaria por Covid-19': ['¿Cómo califica la actuación del IMSS ante la actual contingencia sanitaria Covid-19?', 
                                                                                   'Comparada con otras instituciones de salud, ¿cómo considera las medidas que ha ejercido el IMSS para enfrentar la pandemia por Covid-19?'], 
                'Condicionamiento en la entrega de medicamentos': ['¿Le condicionaron la entrega de medicamentos a cambio de regalos, favores o dinero?'], 
                'Diagnóstico de Covid-19 de personas usuarias y familiares': ['De noviembre de 2020 a la fecha, ¿usted ha sido diagnosticado con Covid-19?', 
                                                                              'En su hogar, ¿ha fallecido algún familiar por Covid-19 de noviembre de 2020 a la fecha?', 
                                                                              'De noviembre de 2020 a la fecha, ¿cuántos familiares en su hogar fueron diagnosticados con Covid-19?', 
                                                                              '¿Recuerda el mes de diagnóstico?', 
                                                                              '¿Cuántos familiares en su hogar fallecieron por Covid-19 de noviembre de 2020 a la fecha?'], 
                'Difusión de información sobre Covid-19': ['En los últimos 3 meses, ¿ha recibido, visto o escuchado algún tipo de información sobre el Covid-19, por parte del IMSS?'], 
                'Hospitalización por Covid-19 en el IMSS y en hospitales diferentes al IMSS': ['Debido al diagnóstico de Covid – 19, ¿fue usted internado en un hospital?', 
                                                                                               'De noviembre de 2020 a la fecha, debido al diagnóstico de Covid – 19, ¿algún familiar fue internado en un hospital?', 
                                                                                               '¿Cúantos familiares fueron internados?'],
                'Percepción de seguridad en las unidades médicas del IMSS': ['¿Qué tan protegido(a) se siente con las medidas de seguridad que ha establecido el IMSS, en las unidades médicas para evitar el contagio de Covid-19?'],
                'Preferencias en la atención': ['¿Considera que en las unidades médicas del IMSS se brinda atención igual a todas las personas usuarias?', 
                                                '¿Considera usted que el personal del IMSS atiende primero a sus amigos, familiares o conocidos?'],
                'Salud mental ante el distanciamiento social': ['El distanciamiento social, para proteger la salud de la comunidad, produce una serie de sensaciones en las personas ¿Cuál(es) considera usted que ha percibido/padecido en el último mes? Ansiedad', 
                                                                'El distanciamiento social, para proteger la salud de la comunidad, produce una serie de sensaciones en las personas ¿Cuál(es) considera usted que ha percibido/padecido en el último mes? Irritación', 
                                                                'El distanciamiento social, para proteger la salud de la comunidad, produce una serie de sensaciones en las personas ¿Cuál(es) considera usted que ha percibido/padecido en el último mes? Deprimido(a) sin esperanzas', 
                                                                'El distanciamiento social, para proteger la salud de la comunidad, produce una serie de sensaciones en las personas ¿Cuál(es) considera usted que ha percibido/padecido en el último mes? Poca energía para desarrollar actividades físicas', 
                                                                'El distanciamiento social, para proteger la salud de la comunidad, produce una serie de sensaciones en las personas ¿Cuál(es) considera usted que ha percibido/padecido en el último mes? Dificultad para dormir', 
                                                                'El distanciamiento social, para proteger la salud de la comunidad, produce una serie de sensaciones en las personas ¿Cuál(es) considera usted que ha percibido/padecido en el último mes? Alteraciones en su salud (dolor de cabeza, dolores estomacales, do'],
                'Satisfacción y trato': ['En general, ¿qué tan satisfecho(a) o insatisfecho(a) está con la atención que recibió en la unidad médica en su última visita durante la actual contingencia COVID?', 
                                         'En general, ¿cómo califica el trato que recibió en la unidad médica en su última visita?', 
                                         '¿Por qué motivo(s) está ni satisfecho ni insatisfecho, insatisfecho o muy insatisfecho? Mal trato del personal', 
                                         '¿Por qué motivo(s) está ni satisfecho ni insatisfecho, insatisfecho o muy insatisfecho? Falta de medicamentos', 
                                         '¿Por qué motivo(s) está ni satisfecho ni insatisfecho, insatisfecho o muy insatisfecho? Tiempo de espera largo', 
                                         '¿Por qué motivo(s) está ni satisfecho ni insatisfecho, insatisfecho o muy insatisfecho? Mal servicio en farmacia', 
                                         '¿Por qué motivo(s) está ni satisfecho ni insatisfecho, insatisfecho o muy insatisfecho? Mala limpieza de las instalaciones', 
                                         '¿Por qué motivo(s) está ni satisfecho ni insatisfecho, insatisfecho o muy insatisfecho? Falta de personal, médicos(as)/especialistas'],
                'Solicitud de atención médica en farmacias con consultorio privado': ['En los últimos 6 meses, ¿solicitó atención en una farmacia que cuente con consultorio médico privado por algún problema de salud?'],
                'Surtimiento de medicamentos': ['De las medicinas que acudió a surtir, ¿recuerda cuántos medicamentos le dieron en la farmacia de la unidad?'], 
                'Trabajo en casa': ['Durante la época actual de contingencia sanitaria por Covid-19, ¿en dónde desarrolla sus actividades laborales?'],
                'Transparencia y posibles acciones de corrupción': ['¿Con qué frecuencia ha observado que en las unidades médicas del IMSS se presentan actos que podrían percibirse como prácticas de corrupción?', 
                                                                    '¿Los servidores públicos o empleados de la unidad médica a la que acudió en su última visita, le solicitaron regalos, favores o dinero, para agilizar trámites, procedimientos o brindarle algún servicio?', 
                                                                    '¿Conoce algún medio (red social, oficina, módulo, etc'],
                'Vacunación contra Covid-19 y expectativas sobre el final de la pandemia': ['Si se vacunara contra el Covid-19, ¿cómo considera que será el nivel de protección en su salud ante un posible contagio de esta enfermedad?', 
                                                                                            '¿Qué tanta esperanza tiene de que estamos cerca del final de la pandemia y que pronto se volverá a las actividades normales?']}  







####Resultados



@app.callback(
    Output('container', 'children'),
    [Input('add-chart', 'n_clicks')],
    [State('container', 'children')]
)
def display_graphs(n_clicks, div_children):
    new_child = html.Div(
        style={'width': '100%', 'display': 'inline-block', 
               'padding': 0, 'font-family': 'Montserrat',},
        children=[
            dcc.Dropdown(
                style={'color':'#13322B','background':'#D4C19C', 'font-weight': 'bold', 'cursor': 'pointer'},
                id={
                    'type': 'dynamic-dpn-s',
                    'index': n_clicks
                },
                options=[{'label': s, 'value': s} for s in secciones_preg.keys()],
                value= 'Actuación del IMSS ante la contingencia sanitaria por Covid-19',
                clearable=False
            ),
            html.Hr(style={'border':'none'},),
            html.Label("Seleccionar pregunta", style={'fontSize':17,'color':'#13322B', 'textAlign':'left', 'font-style': 'italic', 'padding':0}),
            dcc.RadioItems(
                id={
                    'type': 'dynamic-choice',
                    'index': n_clicks
                },
                labelStyle={'display': 'block'},
                inputStyle={"margin-right": "20px"}  
            ),

          html.Hr(style={'border':'none'},),

            dcc.Dropdown(
                style={'width': '550px','color':'#13322B','background':'#DDCEB1', 'font-weight': 'bold', 'cursor': 'pointer'},
                id={
                    'type': 'dynamic-dpn-subs',
                    'index': n_clicks
                },
                options=[{'label': s, 'value': s} for s in listado_resultados],
                value='Nivel', 
                multi=False
            ),


             html.Hr(style={'border':'none'},),
             html.Label('.',style={'fontSize':0,'color':'white'},),

             html.Div(id={
                          'type': 'title-sec-preg-des', 
                          'index': n_clicks
                        }, 
                        style={"textAlign": "center"}
            ),

            html.Div(style={'textAlign': 'center',},
                     id={
                    'type': 'dynamic-table',
                    'index': n_clicks,
                },
    
            ),
            
             html.Hr(style={'border':'none'},),

              html.Div(id={
                          'type': 'regiones', 
                          'index': n_clicks
                        }
            ),

            dcc.Graph(
                id={
                    'type': 'dynamic-graph',
                    'index': n_clicks
                },
                figure={}
            )
        ]
    )
    div_children.append(new_child)
    return div_children

#Radio options

@app.callback(
    Output({'type': 'dynamic-choice', 'index': MATCH}, 'options'),
    Input({'type': 'dynamic-dpn-s', 'index': MATCH},'value'))
def set_variable_options(chosen_seccion):
    return [{'label': i, 'value': i} for i in secciones_preg[chosen_seccion]]


@app.callback(
    Output({'type': 'dynamic-choice', 'index': MATCH}, 'value'),
    Input({'type': 'dynamic-choice', 'index': MATCH},'options'))
def set_variable_value(available_options):
    return available_options[0]['value']



####Title: Section - Question - Reported


@app.callback(
     Output({'type': 'title-sec-preg-des', 'index': MATCH}, 'children'),
    [Input({'type': 'dynamic-dpn-s', 'index': MATCH},'value'),
     Input({'type': 'dynamic-choice', 'index': MATCH}, 'value'),
     Input({'type': 'dynamic-dpn-subs', 'index': MATCH},'value')]
    )
def display_title(seccion, pregunta, desglose):
    return html.Div([
        html.H3('{}'.format(seccion)),
        html.H3('{}'.format(pregunta)),
        html.H3('{}'.format(desglose))
        ])



####Result table
@app.callback(
    Output({'type': 'dynamic-table', 'index': MATCH}, 'children'),
    [Input({'type': 'dynamic-choice', 'index': MATCH}, 'value'),
    Input({'type': 'dynamic-dpn-subs', 'index': MATCH},'value')])
def set_display_table(pregunta_percep, subsecciones_percep):
    if (pregunta_percep != None):
        eninac_df_filter = eni_complete[eni_complete['pregunta'] == pregunta_percep]
        eninac_df_filter_nac = eninac_df_filter[eninac_df_filter['sub_cat'] == 'Nacional']
        eninac_df_filter_nac = eninac_df_filter_nac.sort_values('Codigo')
        column_list = eninac_df_filter_nac["lab_categoria"].tolist()
        column_list=['Desglose'] + column_list
        eninac_df_filter = eninac_df_filter[eninac_df_filter['sub_cat'] == subsecciones_percep]
        eninac_df_filter = eninac_df_filter_nac.append(eninac_df_filter)
        enanic_df_pivot = eninac_df_filter.pivot(index='Desglose', columns='lab_categoria')['Porcentaje'].reset_index()
        enanic_df_pivot = enanic_df_pivot.reindex(columns=column_list)
        enanic_df_pivot = enanic_df_pivot.sort_values(column_list[1], ascending=False)
        return  [dt.DataTable(style_data={'textAlign': 'center',},
                              style_header={'textAlign': 'center', 'font-weight':'bold',},
                              style_cell={'font-family':'Montserrat','width':95, 'maxWidth':95, 
                                            'minWidth':95, 'whiteSpace':'normal'},

                              
                id='table',
                columns=[{"name": i, "id":i} for i in enanic_df_pivot.columns],
                data=enanic_df_pivot.to_dict('records'),
                style_data_conditional=(
                    [{ 'if': {
                                'filter_query': '{Desglose} = Nacional'
                             },
                             'backgroundColor': '#EBEDEF',
                     },
                    ])
                )]
    else:
        print("Información no disponible")
        return[]


####Regions



@app.callback(
     Output({'type': 'regiones', 'index': MATCH}, 'children'),
     Input({'type': 'dynamic-dpn-subs', 'index': MATCH},'value')
    )
def display_title(desglose):
    if desglose == 'Regiones':
        return html.Div(
                    [
                    html.Div([
                        html.Div('Norte: AGS, COAH, CHIH, DGO, NL, SLP, TMS, ZAC'),
                        html.Div('Centro: CDMX S, CDMX N, MEX O, MEX P, HGO, GTO, MOR, PUE, QRO, TLAX'),
                        html.Div('Occidente: BC, BCS, COL, JAL, MICH, NAY, SIN, SON'),
                        html.Div('Sureste: CAMP, CHIS, GRO, OAX, QR, TAB, VER N, VER S, YUC')
                    ],style={'width': '49%', 'display':'inline-block', 'position': 'relative',
                             'float': 'left', 'top':'-25%', 'left': '25%', 
                             'transform': 'translate(-45%, 80%)'}),

                    html.Div(
                        html.Img(src=app.get_asset_url('Mapa de regiones Eni 2021.png'), 
                            style = {'height':'60%', 'width':'60%'}),
                        style={'width': '49%', 'display': 'flex',
                                'justify-content': 'center', 'align-items': 'center'}
                        )
        ])
    else:
        return  html.Div([
        html.Div(''),
        ])


####Callback to a Bar Chart Results, takes data request from dropdown
@app.callback(
    Output({'type': 'dynamic-graph', 'index': MATCH}, 'figure'),
    [Input({'type': 'dynamic-choice', 'index': MATCH}, 'value'),
    Input({'type': 'dynamic-dpn-subs', 'index': MATCH},'value')])
def update_bar_chart(pregunta_percep, subsecciones_percep):
    if (pregunta_percep != None):
        eninac_df_filter = eni_complete[eni_complete['pregunta'] == pregunta_percep]
        eninac_df_filter_nac = eninac_df_filter[eninac_df_filter['sub_cat'] == 'Nacional']
        eninac_df_filter_nac = eninac_df_filter_nac.sort_values('Codigo')
        column_list = eninac_df_filter_nac["lab_categoria"].tolist()
        column_list=['Desglose'] + column_list
        eninac_df_filter = eninac_df_filter[eninac_df_filter['sub_cat'] == subsecciones_percep]
        eninac_df_filter = eninac_df_filter_nac.append(eninac_df_filter)
        eninac_df_filter = eninac_df_filter.sort_values(by=['Codigo'])
        enanic_df_pivot = eninac_df_filter.pivot(index='Desglose', columns='lab_categoria')['Porcentaje'].reset_index()
        enanic_df_pivot = enanic_df_pivot.reindex(columns=column_list)
        enanic_df_pivot = enanic_df_pivot.sort_values(column_list[1], ascending=False)
        category_list = enanic_df_pivot["Desglose"].tolist()
        fig = px.bar(eninac_df_filter, x="Desglose", y="Porcentaje", color='lab_categoria',
            text = 'Porcentaje', template = "seaborn")
        fig.update_traces(texttemplate='%{text:2.0f}', textposition = "inside",
                 insidetextanchor = 'middle', textfont_size=14)
        fig.update_layout({
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)'
                        })
        fig.update_layout(uniformtext_minsize=14, uniformtext_mode='hide')
        fig.update_layout(
            xaxis={'categoryorder':'array', 'categoryarray':category_list,},            
            font=dict(
                    size = 14,
                    family='Montserrat',
                    ),
            legend=dict(title=None))
        return fig
    else:
        print("Información no disponible")
        return[]
    
    