import streamlit as st

# Membuat sidebar
st.sidebar.header('Menu')

# Menambahkan pilihan menu
menu_options = ['Concentration Calculator', 'Material', 'Table', 'Calculator']
selected_option = st.sidebar.selectbox('Select Option', menu_options)

# Menampilkan konten berdasarkan pilihan menu
if selected_option == 'Concentration Calculator':
    st.markdown(
        """
        <h1 style='text-align: center;'>Concentration Calculator</h1>
        """,
        unsafe_allow_html=True)
    
    import streamlit as st
    from PIL import Image

    image = Image.open('calculator.png')
    st.image(image, caption='', width=350, use_column_width=False)
    
    import streamlit as st
    paragraf1 = "<p style='text-indent: 40px;'>Konsentrasi larutan adalah salah satu konsep penting dalam kimia yang mengacu pada jumlah zat yang terlarut dalam suatu pelarut. Konsentrasi larutan biasanya diukur dalam empat cara yaitu molaritas, normalitas, molalitas dan fraksi mol.</p>"
    paragraf2 = "<p style='text-indent: 40px;'>Molaritas adalah cara untuk mengukur konsentrasi larutan dengan membandingkan jumlah mol zat terlarut dengan volume pelarut dalam liter. Normalitas adalah cara untuk mengukur konsentrasi larutan dengan menghitung jumlah setara zat terlarut dalam volume pelarut dalam liter. Molalitas adalah cara untuk mengukur konsentrasi larutan dengan membandingkan jumlah mol zat terlarut dengan massa pelarut dalam kilogram. Sedangkan, fraksi mol adalah suatu zat yang menyatakan perbandingan banyaknya mol zat tersebut terhadap jumlah mol seluruh komponen dalam larutan.</p>"
    paragraf3 = "<p style='text-indent: 40px;'>Konsentrasi larutan sering kali digunakan dalam dunia analis kimia, oleh karena itu kami memutuskan untuk membuat sebuah website aplikasi mengenai perhitungan konsentrasi guna mempermudah para analis dalam mencari konsentrasi secara cepat dan efisien sehingga mempersingkat waktu dalam menghitung dan mengolah data. Website aplikasi ini dinamai dengan “Concentration Calculator”.<p>"
    st.markdown(paragraf1 + paragraf2 + paragraf3, unsafe_allow_html=True)
    st.subheader('Identitas Kelompok')
    st.write('1. Atra Aqila Tirtasuwanda (2219041)')
    st.write('2. Nasywa Raudhatul Janah (2219125)')
    st.write('3. Siti Rahmawati (2219169)')
    st.write('4. Vidya Diva Febrinda (2219180)')
    st.write('5. Zulfa Laillatansa (2219188)')
    
elif selected_option == 'Material':
    st.markdown(
        """
        <h1 style='text-align: center;'>Materi &#x1F4DD;</h1>
        """,
        unsafe_allow_html=True)
    st.subheader(':blue[Normalitas]')
    st.markdown('Normalitas adalah ukuran yang menunjukkan konsentrasi dengan berat setara dalam gram per liter larutan, dimana berat setara itu sendiri adalah ukuran kapasitas reaktif dari suatu molekul yang terlarut dalam larutan. Dalam reaksi, peran zat terlarut tersebut adalah akan menentukan normalitas suatu larutan. Normalitas juga dikenal dengan sebagai satuan konsentrasi larutan yang setara.')
    st.markdown('Komponen asam pada umumnya merupakan jumlah ion H+ yang berada dalam larutan asam, sedangkan komponen basa adalah ion terlarut OH– dalam larutan basa.')
    st.markdown('Sesuai definisinya, normalitas dapat dirumuskan sebagai berat setara zat terlarut dalam satu liter larutan. Normalitas dari suatu larutan dapat dihitung dengan diketahuinya massa dan volume dari larutan tersebut.')
    st.latex(r'''Normalitas\ (N) = \left(\frac{Jumlah\ mol\ ekivalen\ zat\ terlarut}{Volume\ larutan}\right)''')
    st.latex(r'''Normalitas\ (N) = \left(\frac{Massa\ zat\ terlarut}{Bobot\ ekivalen}\right) x \left(\frac{1000}{mL\ larutan}\right)''')
    st.subheader(':blue[Molaritas]')
    st.markdown('Molaritas merupakan pendeskrispsian hubungan antara mol terlarut dan volume larutan. Molaritas juga dapat dimaknai dengan salah satu ukuran kelarutan yang menyatakan jumlah mol suatu zat per volume larutan. Molaritas dilambangkan dengan huruf “M” dengan satuannya adalah molar atau M yang setara dengan mol/liter.')
    st.latex(r'''Molaritas\ (M) = \left(\frac{Massa\ zat\ terlarut}{Bobot\ ekivalen}\right) x \left(\frac{1000}{mL\ larutan}\right)''')
    st.subheader(':blue[Molalitas]')
    st.markdown('Kemolalan atau molalitas adalah konsentrasi larutan yang menyatakan jumlah mol (n) zat terlarut dalam 1 kg atau 1000 gram pelarut. Mol adalah satuan dasar Internasional yang mengukur jumlah zat. Istilah “mol” pertama kali diciptakan oleh seorang Wilhem Ostwald pada tahun 1893, walaupun sebelumnya telah terdapat konsep massa ekuivalen yang pernah dipakai seabad sebelumnya.')
    st.latex(r'''Molalitas\ (M) = \left(\frac{Jumlah\ mol\ zat\ pelarut}{1\ kg\ zat\ pelarut}\right)''')
    st.latex(r'''Molalitas\ (M) = \left(\frac{Massa\ zat\ terlarut}{molekul\ relatif}\right) x \left(\frac{1000}{mL\ larutan}\right)''')
    st.subheader(':blue[Fraksi Mol]')
    st.markdown('Fraksi mol adalah ukuran konsentrasi larutan yang menyatakan perbandingan jumlah mol sebagian zat terhadap jumlah mol total komponen larutan. Fraksi mol juga sering disebut fraksi jumlah dan slalu identik dengan fraksi angka, yang digambarkan sebagai jumlah molekul suatu konstituen dibangi dengan jumlah total semua molekul. Konsep ini hanya merupakan salah satu cara menunjukkan adanya komposisi campuran dengan satuan tak berdimensi. Fraksi mol kadang-kadang dilambangkan dengan huruf Yunani daripada abjad Romawi.')
    st.latex(r'''Fraksi\ mol\ pelarut = \left(\frac{np}{np\ + nt}\right)''')
    st.latex(r'''Fraksi\ mol\ terlarut = \left(\frac{nt}{np\ + nt}\right)''')
    st.write('Keterangan :')
    st.write('np = Jumlah mol zat pelarut')
    st.write('nt = Jumlah mol zat terlarut')
    st.latex(r'''Mol = \left(\frac{Massa}{Molekul\ relatif}\right)''')
    
    
elif selected_option == 'Table':
    st.title('Tabel Molekul Relatif')
    
    import streamlit as st
    from PIL import Image

    image = Image.open('Screenshot (36).png')
    st.image(image, caption='Molekul Relatif Unsur')
    
    image = Image.open('Screenshot (40).png')
    st.image(image, caption='')
    image = Image.open('Screenshot (82).png')
    st.image(image, caption='Molekul Relatif Senyawa')

else:
    st.markdown(
        """
        <h1 style='text-align: center;'>Calculator &#x1F5A9;</h1>
        """,
        unsafe_allow_html=True)
    st.write('Silakan pilih jenis konsentrasi yang ingin dihitung:')
    option = st.selectbox('Menghitung Konsentrasi',
                      ['Normalitas', 'Molaritas', 'Molalitas','Fraksi Mol'])

    if option == 'Normalitas':
        gram = st.number_input('Massa zat (gram):', min_value=0.0, step=0.1, value=0.1)
        liter = st.number_input('Volume (L):', min_value=0.0, step=0.1, value=0.1)
        berat_ekivalen = st.number_input('berat ekivalen (g/Grek):', min_value=0.0, step=0.1, value=0.1)        

        if st.button('Hitung'):
            normalitas = gram / (liter * berat_ekivalen)
            st.write(f'Normalitas = massa zat / (volume x berat ekivalen)')
            st.write(f'Normalitas = {gram} / ({liter} x {berat_ekivalen})')
            st.info(f'Normalitas = {normalitas} N (grek/L)')

    elif option == 'Molaritas':

        def calculate_molarity(mass, molecular_weight, volume):
            molarity = (mass / molecular_weight) * (1000 / volume)
            return molarity

        mass = st.number_input('Massa zat (gram)', min_value=0.0, step=0.1, value=0.1)
        molecular_weight = st.number_input('Molekul relatif (g/mol)', min_value=0.0, step=0.1, value=0.1)
        volume = st.number_input('Volume larutan (mL)', min_value=0.0, step=0.1, value=0.1)

        if st.button('Hitung'):
            molarity = calculate_molarity(mass, molecular_weight, volume)
            st.write(f'Molaritas = (Massa zat / molekul relatif) x (1000 / volume)')
            st.write(f'Molaritas = ({mass} / {molecular_weight}) / ({1000} x {volume})')    
            st.info(f'Molaritas = {molarity:.2f} M (mol/L)')

    elif option == 'Molalitas':

        def calculate_molality(mass_solvent, mol_solute, mol_weight_solute):
            molality = ((mass_solvent / mol_solute) * (1000 /mol_weight_solute))
            return molality

        mass_solvent = st.number_input('Massa zat (gram): ', min_value=0.0, step=0.1, value=0.1)
        mol_solute = st.number_input('Molekul relatif (g/mol): ', min_value=0.0, step=0.1, value=0.1)
        mol_weight_solute = st.number_input('Massa zat pelarut (gram): ', min_value=0.0, step=0.1, value=0.1)

        if st.button("Hitung"):
            molality = calculate_molality(mass_solvent, mol_solute, mol_weight_solute)
            st.write(f'Molalitas = (Massa zat / molekul relatif) x (1000 / massa zat pelarut)')
            st.write(f'Molalitas = ({mass_solvent} / {mol_solute}) / ({1000} x {mol_weight_solute})')    
            st.info(f'Molalitas = {molality} m (mol/Kg)')
    
    else:
        
        option = st.radio('Choose:', ['Fraksi Pelarut', 'Fraksi Terlarut'])

        if option == 'Fraksi Pelarut':
            massa_pelarut = st.number_input('massa zat pelarut (gram):', min_value=0.0, step=0.1, value=0.1)
            mr_pelarut = st.number_input('mr pelarut (g/mol):', min_value=0.0, step=0.1, value=0.1)
            massa_terlarut = st.number_input('massa zat terlarut (gram):', min_value=0.0, step=0.1, value=0.1)
            mr_terlarut = st.number_input('mr terlarut (g/mol):', min_value=0.0, step=0.1, value=0.1)


            if st.button('Hitung'):
                np = ((massa_pelarut / mr_pelarut) / ((massa_pelarut / mr_pelarut) + (massa_terlarut/mr_terlarut)))
                st.info(f'Fraksi pelarut = {np}')

        else:
            
            if option == 'Fraksi Terlarut':
                massa_pelarut = st.number_input('massa zat pelarut (gram):', min_value=0.0, step=0.1, value=0.1)
                mr_pelarut = st.number_input('mr pelarut (g/mol):', min_value=0.0, step=0.1, value=0.1)
                massa_terlarut = st.number_input('massa zat terlarut (gram):', min_value=0.0, step=0.1, value=0.1)
                mr_terlarut = st.number_input('mr terlarut (g/mol):', min_value=0.0, step=0.1, value=0.1)


                if st.button('Hitung'):
                    nt = ((massa_terlarut / mr_terlarut) / ((massa_pelarut / mr_pelarut) + (massa_terlarut/mr_terlarut)))
                    st.info(f'Fraksi terlarut = {nt}')
                  