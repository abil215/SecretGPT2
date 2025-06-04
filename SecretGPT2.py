import streamlit as st
import requests
import PyPDF2
import docx
import io

# Dictionary of friends
teman = {
    "Apple14": {"nama": "andy saptono", "pesan": "Halo, ini pesan pribadi Abil untuk Bp. Andy Saptono.", "kesan": "Kalo ibaratnya saya pedangnya K3, bapak adalah perisainya. Orang paling kalem dan cerdas di DR. Bapak mengajarkan banyak kepada saya, akan saya bawa selama karir dan hidup saya ke depan. Pesan terakhir saya dalam konteks perpisahan ini, manfaatkan spotlight dan medan politik yang ada saat ini untuk bapak dan K3 yang senantiasa mendukung bapak. Tetap jadi Pak Andy yang bisa diandalkan dan bisa diajak ngobrol oleh semua orang. Sukses terus dalam menjadi tumpuan K3 pak, semoga reputasi baik untuk uker yang kita bangun tetap berlangsung meski tanpa saya. Insyaallah bapak segera promosi dalam waktu dekat ini. Aamiin."},
    "Silverqueen19": {"nama": "Silvia Sri Mustika", "pesan": "Halo, ini pesan pribadi Abil untuk Ibu Silvia Sri Mustika.", "kesan": "Kalo ibaratnya saya adalah tangan kanannya K3, ibu adalah jantungnya yang mampu merasakan apa yang tidak terlihat oleh kasat mata dan juga yang terus memberikan kami motivasi untuk bekerja sebaik mungkin. Pendekatan ibu kepada seluruh lapisan K3 dan DR akan saya jadikan contoh dalam berkarir di BI ke depan. Terima kasih banyak atas semua kepercayaan dan kesempatan yang ibu berikan kepada saya untuk unjuk gigi membawa nama K3, saya berharap kita bisa saling mendukung karir satu sama lain apabila diberikan kesempatan. Sukses terus untuk ibu secara personal dan dalam menjadi koordinator K3."},
    "Ebenezer16": {"nama": "Ebrinda Daisy G.", "pesan": "Halo, ini pesan pribadi Abil untuk Mbak Rinda.", "kesan": "Meski kita jarang berpandangan yang sama, saya sejujurnya respect sama mbak. Apabila diterjunkan dalam keadaan hidup yang sama, tidak jauh beda keputusan-keputusan kecil maupun besar yang kita ambil. Terima kasih sudah banyak sabar dengan saya. Karena teh rinda lebih senior dan berpengalaman daripada saya, saya rasa belum bisa memberikan pesan seperti ke K3 lainnya. Namun, kalo boleh izin reminder, dalam perjalanan meraih apa yang kita inginkan, sebaiknya kita mengupayakan segala usaha agar kita pantas meraih keinginan tersebut. Semakin besar tanggung jawab yang kita emban, semakin besar kompetensi yang diperlukan, semakin besar risiko posisi tersebut, semakin banyak yang akan tepuk tangan bila kita jatuh."},
    "Hozier36": {"nama": "Hanni Attarfi", "pesan": "Halo, ini pesan pribadi Abil untuk Hanni.", "kesan": "Kalo ibaratnya saya pedang ya K3 yang selama ini sudah berjuang mengangkat derajat K3 di DR dan DR di KP dan Satgas P2DD, dirimu kuproyeksikan sebagai senapan yang menggantikan senjata K3 yang sudah kuno ini. Dari awal (konsi buku kasus), semua orang sudah mengakui kemampuannya hanni dalam menganalisa, apalagi barang tersebut baru untuk dirimu dan juga kita semua. Dengan tepat dan cepat bisa selesaikan tugas  dengan citra yang lebih halus dari caraku. Pesanku, tetap kalem dan tembak setiap musuh (tugas) yang menerjang K3, jangan sampai down karena semua orang berharap pada dirimu. Kalo butuh bantuan/support jarak jauh, you know who to call."},
    "Midnigther87": {"nama": "Mualam Noor", "pesan": "Halo, ini pesan pribadi Abil untuk Bp. Mualam Noor.", "kesan": "Kalo ibaratnya saya adalah pedangnya K3, bapak ada orang martil yang membantu proses pembentukan saya. Setiap nasehat yang bapak berikan saat kita ngobrol membentuk pikiran saya, dan banyak mencerahkan hal-hal yang sebelumnya gelap di mata saya. Saya akan segera daftar haji, setelah saya pulang S2 dan beli mobil untuk keluarga. Optimisme bapak terkait karir dan saran bapak ke saya akan saya pegang ke depan, sekali lagi saya mohon dukungan bapak dalam berkarir di BI. Terima kasih atas segala kepercayaan dan kesempatan yang bapak berikan kepada saya."},
    "Erasmus31": {"nama": "Ervin Budi Febriawan", "pesan": "Halo, ini pesan pribadi Abil untuk Mas Ervin.", "kesan": "Saya tau dirimu lebih tua dan saya sendiri belum pantas untuk menasehati soal ini, tapi Broku, semoga semakin rajin sholat. Dirimu salah satu orang paling enak diajak ngobrol dan kerja selama di DR. Kemampuan kerja sudah diakui semuanya, meski masih ada yg kambing hitamkan dirimu atas kejadian tahun lalu. Meski bukan urusanku, saya rasa yg hambat sebagian rezekimu adalah karena kurang sholat. Saya yakin dirimu juga tidak mau jadi arsiparis selamanya, dan saya rasa dirimu memang layak untuk dapat rezeki lebih. Terima kasih atas segala bantuan dan makanan selama ini, kerja di DR tidak mungkin tanpa Mas Ervin."},
    "Indigo32": {"nama": "Intan Safara", "pesan": "Halo, ini pesan pribadi Abil untuk Intan.", "kesan": "Ini saya tulis dengan baik-baik dan dengan nada yang tenang, jadi tolong baca dengan suasana yang sama. Hambatan terbesarmu menurutku adalah dirimu adalah mindset yang berbeda dengan orang BI, termasuk saya. Memang tidak semua orang diciptakan untuk kerja di institusi polemik ini. Butuh pengalaman jatuh ke titik terendah dalam hidup dahulu agar bisa berdiri tegak di instansi ini. Saya rasa dengan backgroundmu yang serba kecukupan, belum ada drivemu untuk bekerja dan berpikir seperti top performer di BI. Saya harap konflik kita akhir2 ini bisa sedikit mengubah mindsetmu dan menjadi driver agar bisa mematahkan persepsiku terhadap dirimu. Kalo mau bertahan di BI, kuncinya lebih banyak belajar hal yang perlu, lebih banyak mendengar daripada bertanya maupun menjawab, dan untuk tim teknis kecepatan adalah nomor 1."},
    "Artabanus99": {"nama": "Arief Hartawan", "pesan": "Halo, ini pesan pribadi Abil untuk Pak Arief.", "kesan": "Orang yang memimpin DR harusnya orang yang cerdas dan berwibawa, karena kita menjadi narahubung langit dan bumi. Menurut hemat saya, bapak orang yang pantas untuk itu. Terbukti dari bapak menjadi salah satu pembicara terbaik di REKBI tahun 2024, yang mana meskipun pointers yang diberikan isinya sangat terbatas (akibat kurasi yang menurut saya berlebihan tengah malamnya). Jujur, pak, saat di pagi harinya dengar bahwa ada perlombaan, saya sendiri sudah takut duluan karena khawatir dimarahi karena pointersnya yang lebih tergolong kriteria minimum standard, bukan standard minimum. Tapi ternyata, against all odds, bapak berhasil masuk podium terbaik. Terima kasih atas kepercayaan dan kesempatan yang bapak berikan kepada saya dalam mendorong kinerja DR. Semoga karir dan persona saya di masa depan, bisa sehebat bapak. Dengan segala kerendahan hati, saya memohon dukungan bapak dalam karir saya kedepan."},
    "Firenze99": {"nama": "M. Firdauz Muttaqin", "pesan": "Halo, ini pesan pribadi Abil untuk Bp. Firdauz.", "kesan": "Komunikatif, visioner, namun memahami konsep bahwa kesempurnaan hanya milik Allah SWT. Pertama dan yang paling utama yang saya ucapakan adalah terima kasih atas atensi yang baik dari bapak kepada saya pribadi dan rekan-rekan K3. Kehadiran bapak merupakan angin segar bagi kami yang kesekian tahun sebelumnya merasa menjadi anak tiri di DR ini. Atas bimbingan dan dukungan bapak selama ini, saat ini saya rasa belum cukup membalas kebaikan bapak. Saya harap bisa lebih lama di DR untuk mengabdi mengangkat kinerja Satker dan KPwDN. Semoga hal yang dapat saya kontribusikan untuk Satker bernilai baik di mata bapak, dengan segala kerendahan hati mohon dukungan bapak dalam dukungan karir saya ke depannya. Semoga kebaikan bapak dibalas dengan hal yang lebih baik dari Allah SWT. "},
    "Brompton99": {"nama": "Bayu Martanto", "pesan": "Halo, ini pesan pribadi Abil untuk Bp. Bayu.", "kesan": "Sebelum bapak masuk ke DR, teman angkatan saya infokan bahwa bapak salah satu pimpinan yang baik di Satker sebelumnya. Ternyata terbukti bahwa bapak menjadi fine addition Satker kecil kami tahun ini. Persona bapak sebagai Change Coordinator membantu penciptaan ide-ide program kerja dengan proses yang lebih santai namun target oriented. Saya sebenarnya berambisi untuk menjadi usulan CA terbaik DR tahun ini, namun sepertinya tidak bisa dipaksakan ditakdirkannya saya S2 terlebih dahulu. Saat ini ada program kerja CP yang saya prakarsai dan sedang berjalan, yaitu chatbot ketentuan industri SP sebagai bagian program ANDALAS BI Prestasi sekaligus Output Aktivitas Tim Integrasi inovasi-digital (di bawah komando bu silvi dan mas ryan). Semoga program tersebut bermanfaat bagi DR dan Industri SP dan harapannya membawakan prestasi CP bagi DR tahun ini. Semoga kontribusi saya bernilai baik di mata bapak. Dengan segala kerendahan hati, mohon dukungan bapak dalam karir dan harapan promosi saya menjadi asmen senior tahun ini dan manajer tahun depan."},
    "Brilliant99": {"nama": "Bandoe Widiarto", "pesan": "Halo, ini pesan pribadi Abil untuk Bp. Bandoe.", "kesan": "Kita pertama kali ketemu saat ikut melakukan pengawasan PJP di Surabaya 2024. Saya mewakili teman-teman KPwDN melaporkan hasil temuan ke bapak di ruangan bapak, bersama pak FX Widarto. Kesan pertama saya adalah bapak sosok pimpinan yang kalem dan tidak mempressure bawahannya. Saya merasakan persepsi saya masih sama saat di DR. Di beberapa bulan ini dan yang merupakan bulan-bulan terakhir bapak di BI, arahan bapak clear untuk kami jalankan meski dengan tantangan stakheholder satker lain pada saat membahas kastip dan buku pandawa. Sebagai sesama pegawai yang akan meninggalkan DR dalam waktu dekat ini, sosok bapak akan saya ingat dengan nuansa positif. Semoga bapak dan keluarga senantiasa diberikan kebaikan dari Allah SWT dalam masa purna bakti bapak. Dengan segala kerendahan hati, mohon dukungan bapak dalam karir saya kedepan."},
}

OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "https://localhost:8501",  # Updated to https
    "X-Title": "SecretGPT Chatbot",
    "Content-Type": "application/json"  # Added content type header
}
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Sidebar configuration
with st.sidebar:
    st.title("⚙️ Settings")

    # Model selection
    selected_model = st.selectbox(
        "Select AI Model",
        ["deepseek/deepseek-chat-v3-0324", "gpt-3.5-turbo", "gpt-4"],
        index=0
    )

    # Temperature slider
    temperature = st.slider(
        "Creativity (Temperature)",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Higher values make output more random, lower values make it more deterministic"
    )

    # Max tokens
    max_tokens = st.slider(
        "Max Response Length",
        min_value=100,
        max_value=2000,
        value=1000,
        step=100
    )

    st.markdown("---")
    st.markdown("### 📁 File Upload")
    st.info("Upload PDF/DOCX/TXT files to analyze their content")


# Main app
st.title("SecretGPT.com")
st.markdown(f"Powered by {selected_model} via OpenRouter 🤖")


# ========== FITUR HALAMAN AWAL SECRET MESSAGE =============
if "entered_secret" not in st.session_state:
    st.session_state.entered_secret = False
if "secret_message" not in st.session_state:
    st.session_state.secret_message = ""

if not st.session_state.entered_secret:
    st.title("🔒 Selamat Datang di Secret GPT!")
    st.markdown("""
    <div style='text-align:center; margin-bottom:30px;'>
        <h2>Masukkan kode unik untuk melihat secret message spesial untukmu!</h2>
        <p style='color:#888;'>Jika tidak punya kode, klik <b>Lewati</b> untuk lanjut ke chat biasa.</p>
    </div>
    """, unsafe_allow_html=True)
    kode_input = st.text_input("Masukkan kode unik kamu di sini:", placeholder="Contoh: Apple14", key="kode_unik")
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("🔍 Lihat Secret Message", key="cek_kode"):
            if kode_input in teman:
                person = teman[kode_input]
                st.session_state.secret_message = f"""
**Nama:** {person['nama']}
**Pesan:** {person['pesan']}
**Kesan:** {person['kesan']}
"""
                st.session_state.entered_secret = True
            else:
                st.warning("Kode tidak ditemukan. Silakan cek kembali atau klik Lewati.")
    with col2:
        if st.button("⏭️ Lewati", key="skip_kode"):
            st.session_state.entered_secret = True
            st.session_state.secret_message = ""
    if st.session_state.secret_message:
        st.success("Secret message ditemukan!")
        st.markdown(st.session_state.secret_message)
        st.markdown("<hr>", unsafe_allow_html=True)
        if st.button("Masuk ke Chat", key="masuk_chat"):
            st.session_state.secret_message = ""
    st.stop()
# ========== END FITUR HALAMAN AWAL SECRET MESSAGE =========


# File uploader moved to main area for better UX
uploaded_file = st.file_uploader("Upload file (PDF/DOCX/TXT)", type=['pdf', 'docx', 'txt'])
file_content = ""

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            file_content += page.extract_text() + "\n"

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            file_content += para.text + "\n"

    else:  # For txt files
        file_content = uploaded_file.getvalue().decode("utf-8")

    if file_content:
        st.success("File berhasil diunggah!")
        with st.expander("Isi File"):
            st.text(file_content[:500] + "..." if len(file_content) > 500 else file_content)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

user_input = st.chat_input("Tulis pesan di sini...")

if user_input:
    st.chat_message("user").markdown(user_input)
    
    # Check if input matches any code in teman dictionary
    if user_input in teman:
        person = teman[user_input]
        response_text = f"""
**Nama:** {person['nama']}
**Pesan:** {person['pesan']}
**Kesan:** {person['kesan']}
"""
        st.chat_message("assistant").markdown(response_text)
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "assistant", "content": response_text})
    
    else:
        # Continue with normal chatbot functionality
        content_to_send = user_input
        if file_content:
            content_to_send = f"File Content:\n{file_content}\n\nUser Question:\n{user_input}"
        
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.spinner("Mengetik..."):
            try:
                messages = [
                    {"role": "system", "content": "You are a helpful assistant. You can analyze documents and answer questions about them."},
                    {"role": "user", "content": content_to_send}
                ]
                
                payload = {
                    "model": selected_model,
                    "messages": messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "headers": HEADERS
                }
                
                response = requests.post(
                    API_URL,
                    headers=HEADERS,
                    json=payload,
                    timeout=60  # Added timeout
                )
                
                if response.status_code == 401:
                    st.error("API key unauthorized. Please check your OpenRouter API key.")
                    bot_reply = "⚠️ Authentication failed. Please check the API key configuration."
                else:
                    response.raise_for_status()
                    bot_reply = response.json()['choices'][0]['message']['content']
                
            except requests.exceptions.RequestException as e:
                bot_reply = f"⚠️ Network Error: {str(e)}"
            except Exception as e:
                bot_reply = f"⚠️ Error: {str(e)}"
            
            st.chat_message("assistant").markdown(bot_reply)
            st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})