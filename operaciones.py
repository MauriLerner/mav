# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:14:06 2022

@author: mlerner
"""

import pandas as pd 
import numpy as np
import math
import datetime
import streamlit as st

filas = 0
arancel_var = 0.002 #0.20%
arancel_pag_var = 0.001 #0.1%
iva_var = 0.21 #21%
dermercado_var = 0
neto_var = 0

operaciones_input = st.file_uploader('Insert cpd-regoperac here')
subastas_input = st.file_uploader('Insert subastas here')

if operaciones_input is not None:
    if subastas_input is not None:
        
        datos = pd.read_excel(operaciones_input,header=0)
        subastas = pd.read_excel(subastas_input,header=0) 

        salida_df = pd.DataFrame(columns = ['razon social', 'comitente', 'fecha', 'instrumento', 'cod cheque', 'nominal','arancel','IVA', 'moneda', 'derecho mercado', 'bruto', 'neto', 'nro banco', 'banco', 'fecha vto', 'dias', 'tasa', 'tipo cambio'])                                                                                                            
        subastas_df = pd.DataFrame(columns= ['subasta', 'sgr-librador', 'razon social'])

        subasta_sub = []
        sgrlib_sub = []
        razonsoc_sub = []

        nrofilas = subastas.axes[0]
        
        m = 0
        for m in nrofilas:
            subasta_sub.append(subastas.iloc[m,0])
            sgrlib_sub.append(subastas.iloc[m,22])
            razonsoc_sub.append(subastas.iloc[m,24])
    
        subastas_df['subasta'] = subasta_sub
        subastas_df['sgr-librador'] = sgrlib_sub
        subastas_df['razon social'] = razonsoc_sub

        totalrows=len(datos.axes[0]) #numero de filas
        filas = datos.axes[0]

        nrosubasta_sal = []
        comitente_sal = []
        concertacion_sal = []
        instrumento_sal = []
        codcheque_sal = []
        nominal_sal = []
        moneda_sal = []
        bruto_sal = []
        nrobanco_sal = []
        banco_sal = []
        fecvto_sal = []
        dias_sal = []
        tasa_sal = []
        tc_sal = []
        arancel_sal = []
        iva_sal = []
        dermercado_sal = []
        neto_sal = []
        listado_box = []
        librador_sal = []
        pagare = 'PAGARE'
        rdoquery = []
        
        comitente_ant = datos.iloc[0,33]

        for n in filas:
            concertacion = datos.iloc[n,0]
            subasta_datos = datos.iloc[n,3]
            instrumento = datos.iloc[n,5]
            moneda = datos.iloc[n,6]
            dias = datos.iloc[n,7]
            fecvto = datos.iloc[n,8]
            nrobanco = datos.iloc[n,9]
            banco = datos.iloc[n,10]
            codcheque = datos.iloc[n,14]
            tasa = datos.iloc[n,23]
            nominal = datos.iloc[n,24]
            bruto = datos.iloc[n,25]
            tc = datos.iloc[n,27]
            dermercadoc = datos.iloc[n,28]
            ivamercadoc = datos.iloc[n,29]
            comitente = datos.iloc[n,33]
            tasa_cobrar = 0
            monto_cobrar = 0
            iva_cobrar = 0
            dermercado_var = 0
            neto_var = 0
    
            if(math.isnan(comitente)):
                neto_var = 0
            else:
                if comitente != 0:
                    #print("***MUESTRO COMITENTE DIFERENTE DE CERO*****")
                    if comitente == comitente_ant:
                        concertacion_sal.append(concertacion)
                        instrumento_sal.append(instrumento)
                        moneda_sal.append(moneda)
                        dias_sal.append(dias)
                        fecvto_sal.append(fecvto)
                        nrobanco_sal.append(nrobanco)
                        banco_sal.append(banco)
                        codcheque_sal.append(codcheque)
                        tasa_sal.append(tasa)
                        nominal_sal.append(nominal)
                        bruto_sal.append(round(bruto, 2))
                        tc_sal.append(tc)
                        comitente_sal.append(round(comitente))                    
                                
                        dermercado_var = dermercadoc + ivamercadoc
                        dermercado_sal.append(dermercado_var)
                    
                        if instrumento == pagare:
                            tasa_pag_cobrar = arancel_pag_var * dias / 365
                            monto_cobrar = tasa_pag_cobrar * nominal * tc
                            iva_cobrar = iva_var * monto_cobrar
                            neto_var = (bruto * tc) + dermercado_var + monto_cobrar + iva_cobrar
                        else:
                            tasa_cobrar = arancel_var * dias / 365
                            monto_cobrar = tasa_cobrar * nominal
                            iva_cobrar = iva_var * monto_cobrar
                            neto_var = bruto + dermercado_var + monto_cobrar + iva_cobrar
                        
                        arancel_sal.append(round(monto_cobrar, 2))                                        
                        iva_sal.append(round(iva_cobrar, 2))
                        neto_sal.append(round(neto_var, 2))    
                    
                    
                        nrosubasta_query = subastas_df[subastas_df.subasta==subasta_datos]                    
                        variable1 = nrosubasta_query.iloc[0,2]
                        nrosubasta_sal.append(variable1)
                        
                    else:
                        concertacion_sal.append(concertacion)
                        instrumento_sal.append(instrumento)
                        moneda_sal.append(moneda)
                        dias_sal.append(dias)
                        fecvto_sal.append(fecvto)
                        nrobanco_sal.append(nrobanco)
                        banco_sal.append(banco)
                        codcheque_sal.append(codcheque)
                        tasa_sal.append(tasa)
                        nominal_sal.append(nominal)
                        bruto_sal.append(round(bruto, 2))
                        tc_sal.append(tc)
                        comitente_sal.append(round(comitente))                                                        
            
                        dermercado_var = dermercadoc + ivamercadoc
                        dermercado_sal.append(dermercado_var)
                    
                        if instrumento == pagare:
                            tasa_pag_cobrar = arancel_pag_var * dias / 365
                            monto_cobrar = tasa_pag_cobrar * nominal * tc
                            iva_cobrar = iva_var * monto_cobrar
                            neto_var = (bruto * tc) + dermercado_var + monto_cobrar + iva_cobrar
                        else:
                            tasa_cobrar = arancel_var * dias / 365
                            monto_cobrar = tasa_cobrar * nominal
                            iva_cobrar = iva_var * monto_cobrar
                            neto_var = bruto + dermercado_var + monto_cobrar + iva_cobrar
                    
                        iva_sal.append(round(iva_cobrar, 2))
                        arancel_sal.append(round(monto_cobrar, 2))
                        neto_sal.append(round(neto_var, 2))
                
                        comitente_ant = comitente
                        
                        nrosubasta_query = subastas_df[subastas_df.subasta==subasta_datos]
                        variable1 = nrosubasta_query.iloc[0,2]
                        nrosubasta_sal.append(variable1)

        salida_df['fecha'] = concertacion_sal
        salida_df['instrumento'] = instrumento_sal
        salida_df['moneda'] = moneda_sal
        salida_df['fecha vto'] = fecvto_sal
        salida_df['dias'] = dias_sal
        salida_df['nro banco'] = nrobanco_sal
        salida_df['banco'] = banco_sal
        salida_df['cod cheque'] = codcheque_sal
        salida_df['tasa'] = tasa_sal
        salida_df['nominal'] = nominal_sal
        salida_df['bruto'] = bruto_sal
        salida_df['tipo cambio'] = tc_sal
        salida_df['comitente'] = comitente_sal
        salida_df['arancel'] = arancel_sal
        salida_df['IVA'] = iva_sal
        salida_df['derecho mercado'] = dermercado_sal
        salida_df['neto'] = neto_sal
        salida_df['razon social'] = nrosubasta_sal

        ordenado = salida_df.groupby(by = 'comitente').mean()
        cantidadcomi = len(ordenado.index)

        fecha_var = str(concertacion) #modifico la fecha con formato dd/mm/aaaa a dd-mm-aaaa
        fecha_var = fecha_var[0:10]
        fecha_var = fecha_var.split('/')
        nueva_fecha = '-'.join(fecha_var)


        for j in range(cantidadcomi):
            listado_box.append(ordenado.index[j])

        for i in range(cantidadcomi):
            muestro = ordenado.index[i]
            imprimo = salida_df[salida_df['comitente'] == muestro]
            salida_final_df = pd.ExcelWriter('C:\Operaciones\operaciones ' + nueva_fecha + ' - cc ' + str(muestro) + '.xlsx')
            imprimo.to_excel(salida_final_df, 'operaciones')            
            salida_final_df.save()
            #st.download_button('Press to download', salida_final_df, 'comitente ' + str(muestro) + '.xls', 'text/xls', key='download-xls')
            st.write('comitente nro: ', muestro)   
            #if st.checkbox('descargar'):
                #st.download_button('Press to download', salida_final_df, 'comitente ' + str(muestro) + '.xls', 'text/xls', key='download-xls')
             #   st.text('aca descargo')
        
        st.write('Los archivos fueron generados en la carpeta C:\Operaciones ')
            
