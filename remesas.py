# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 20:08:21 2022

@author: Mauricio Lerner
"""
import streamlit as st

st.title('Generar remesa para carga masiva')
st.caption('Se debe cargar el excel generado al aceptar la vinculación de los ECHEQs')
st.caption('Como resultado se obtendrá otro excel listo para subir por medio de la opción de Carga Masiva*')




import pandas as pd 
import numpy as np
import math
import datetime
import base64

segmento = st.radio('Please select a kind of ECHEQ', ('No Garantizado', 'Garantizado'))
file = st.file_uploader(' ')

if file is not None:
        
    
    if segmento == 'No Garantizado':
        datos_input = pd.read_excel(file)

        carga_df = pd.DataFrame(columns = ['banco', 'sucursal', 'plaza', 'verificadorruta', 'cheque', 'verificadorcheque','cuenta','verifcuenta', 'librador', 'beneficiario', 'endosos', 'segmento', 'nalo', 'sinrecurso', 'nrocomitv', 'feclib', 'fecvto', 'monto', 'exponelibrador', 'custodio', 'echeqid', 'tipoinstrumento'])


        banco_lis = []
        sucursal_lis = []
        plaza_lis = []
        verifruta_lis = []
        cheque_lis = []
        vericheque_lis = []
        cuenta_lis = []
        verifcuenta_lis = []
        librador_lis = []
        beneficiario_lis = []
        endosos_lis = []
        segmento_lis = []
        nalo_lis = []
        sinrecurso_lis = []
        comitente_lis = []
        feclib_lis = []
        fecvto_lis = []
        monto_lis = []
        exponelib_lis = []
        custodio_lis = []
        echeq_lis = []
        instrumento_lis = []
        n = 0
        nogarantizado_text = 'No Garantizado'
        nalo_text = 'no'
        nalosi_text = 'si'
        recurso_text = 'no'
        expone_text = 'si'
        custio_text = 'CVSA'
        instrumento_text = 'ECHEQ'
    
        filas = datos_input.axes[0]
    
        comitentesal = datos_input['SUBCUENTA COMITENTE'][0]
    
        for n in filas:
            cuit_varlis = str(datos_input.iloc[n,27])
            cuit_varlis2 = cuit_varlis[0:2] + '-' + cuit_varlis[2:10] + '-' + cuit_varlis[10:11]
            librador_lis.append(cuit_varlis2)
            cuit_var = str(datos_input.iloc[n,35])
            cuit_var2 = cuit_var[0:2] + '-' + cuit_var[2:10] + '-' + cuit_var[10:11]
            beneficiario_lis.append(cuit_var2)
            segmento_lis.append(nogarantizado_text)
            nalo_lis.append(nalo_text)
            sinrecurso_lis.append(recurso_text)
            comitente_var = datos_input.iloc[n, 44]
            comitente_lis.append(comitente_var)
            fecha_var = datos_input.iloc[n, 5]
            fecha_var = fecha_var[0:10]
            fecha_var = fecha_var.split('-')
            fecha_fin = '/'.join(fecha_var)
            fecha_fina = fecha_fin.split()
            fecha_fina = pd.to_datetime(fecha_fina[0], dayfirst=True)
            fecha_fin2 = fecha_fina.strftime('%d/%m/%Y')
            feclib_lis.append(fecha_fin2)
            fecha_var2 = str(datos_input.iloc[n, 4])
            fecha_var2 = fecha_var2[0:10]
            fecha_var2 = fecha_var2.split('-')
            fecvto_fin = '/'.join(fecha_var2)
            fecvto_fin = pd.to_datetime(fecvto_fin, dayfirst=True)
            fecvto_fin2 = fecvto_fin.strftime('%d/%m/%Y')
            fecvto_lis.append(fecvto_fin2)
            monto_var = datos_input.iloc[n,3]
            monto_var2 = monto_var.astype(float)
            monto_var2 = str(monto_var2).replace('.', ',')
            monto_lis.append(monto_var2) #SOLUCIONAR ***********************
            exponelib_lis.append(expone_text)
            custodio_lis.append(custio_text)
            echeq_var = datos_input.iloc[n,1]
            echeq_lis.append(echeq_var) 
            instrumento_lis.append(instrumento_text )
            fecha_var2 = 0


        carga_df['banco'] = banco_lis
        carga_df['sucursal'] = sucursal_lis 
        carga_df['plaza'] = plaza_lis 
        carga_df['verificadorruta'] = verifruta_lis 
        carga_df['cheque'] = cheque_lis 
        carga_df['verificadorcheque'] = vericheque_lis
        carga_df['cuenta'] = cuenta_lis
        carga_df['verifcuenta'] = verifcuenta_lis 
        carga_df['librador'] = librador_lis  
        carga_df['beneficiario'] = beneficiario_lis 
        carga_df['segmento'] = segmento_lis 
        carga_df['nalo'] = nalo_lis 
        carga_df['sinrecurso'] = sinrecurso_lis 
        carga_df['nrocomitv'] = comitente_lis 
        carga_df['feclib'] = feclib_lis 
        carga_df['fecvto'] = fecvto_lis 
        carga_df['monto'] = carga_df['monto'].astype(float)
        carga_df['monto'] = monto_lis 
        carga_df['exponelibrador'] = exponelib_lis 
        carga_df['custodio'] = custodio_lis 
        carga_df['echeqid'] = echeq_lis 
        carga_df['tipoinstrumento'] = instrumento_lis 
    
    
    #csv_salida = carga_df.to_csv('datos remesa mav.csv', index=False, sep=';', header=False)
    
    
    #if(st.button('Generar Remesa')):
        #st.download_button(label='Download excel', data=carga_df, file_name='Carga remesas', mime='text/csv')
    #    b64 = base64.b64encode(csv_salida.encode()).decode()       
    #    linko= f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Download csv file</a>'
    #    st.markdown(linko, unsafe_allow_html=True)
        #st.download_button('Download CSV', pd.read_csv(csv_salida), 'remesa.csv', 'text/csv')
        #st.write(carga_df)
        @st.cache
        def convert_df(carga_df):
            return carga_df.to_csv(index=False, header=False, sep=';')

        csv = convert_df(carga_df)
    
    #st.write(csv)
        st.download_button('Press to download', csv, 'archivo.csv', 'text/csv', key='download-csv')
    
    else:
        st.write('Unavailable function')

st.subheader(' ')
st.subheader(' ')

st.caption('*Se debe ingresar en Cheques-->Autorizados-->Nueva carga masiva')
st.caption('Luego de procesado los cheques quedarán en el listado de remesas para ser enviados')

