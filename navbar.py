import dash_bootstrap_components as dbc

# Navigation Bar function
def Navbar():
    navbar = dbc.NavbarSimple(children=[
        
#            dbc.NavItem(dbc.NavLink("Antecedentes", href='/antecedente')),
             dbc.NavItem(dbc.NavLink("Resultados", href='/res')),
             dbc.NavItem(dbc.NavLink("Banco de datos", href='/banco')),
             dbc.DropdownMenu(
             children=[
                dbc.DropdownMenuItem("2021", header=True, style={'fontSize':15,'color':'#13322B', 'textAlign':'center', 'font-weight': 'bold'}),
                dbc.DropdownMenuItem("2020", href="https://cie-encal20.herokuapp.com/res", style={'fontSize':15,'color':'#13322B', 'textAlign':'center'}),
                dbc.DropdownMenuItem("2019", href="#", style={'fontSize':15,'color':'#13322B', 'textAlign':'center'}),
            ],
            nav=True,
            in_navbar=True,
            label="Consultar más mediciones",
        ),
             
        ],
        brand="Sistema de Percepción Social",
        brand_href="https://sps-cie-imss.herokuapp.com",
        sticky="top",
        color= '#13322B',
        dark=True,
        expand='lg',)
    
    return navbar
