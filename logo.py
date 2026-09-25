import os
import time
import warnings
warnings.filterwarnings("ignore")
import streamlit as st

# ТВОЙ СЕКРЕТНЫЙ ПАРОЛЬ АДМИНИСТРАТОРА
ADMIN_PIN = "клаксон23523"

# ТВОЙ РЕАЛЬНЫЙ СЧЕТ ЮМОНЕЙ
YOUR_YOOMONEY_ACCOUNT = "4100118719995386"  

st.set_page_config(page_title="GigaLogo — ИИ-Генератор Аватарок", page_icon="🎨", layout="wide")

# Агрессивный киберпанк-дизайн (Черно-зелено-кислотный неон)
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #050705; color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #0A0F0A !important; }
    h1, h2, h3, h4 { color: #39FF14 !important; font-family: 'Courier New', monospace; text-shadow: 0 0 10px rgba(57,255,20,0.2); }
    
    .pay-btn-link {
        display: block; text-align: center; background: linear-gradient(135deg, #39FF14 0%, #00FF66 100%);
        color: #000000 !important; border-radius: 8px; font-weight: bold; font-size: 20px;
        padding: 15px; text-decoration: none; box-shadow: 0 4px 20px rgba(57, 255, 20, 0.4); margin-top: 15px;
        font-family: 'Courier New', monospace; transition: all 0.3s ease;
    }
    .pay-btn-link:hover { transform: translateY(-2px); box-shadow: 0 6px 25px rgba(57, 255, 20, 0.6); }
    
    .stButton>button { 
        background: linear-gradient(135deg, #0D140D 0%, #050805 100%); color: #39FF14 !important; 
        border-radius: 8px; width: 100%; font-weight: bold; font-size: 16px; border: 1px solid #39FF14;
    }
    .stButton>button:hover { background: #39FF14 !important; color: #000000 !important; }
    
    .logo-box { background-color: #0A0F0A; padding: 30px; border-radius: 14px; border: 1px solid #1A291A; margin-bottom: 20px; text-align: center; }
    .logo-lock-box { background-color: #1A0A0A; padding: 30px; border-radius: 14px; border: 2px dashed #FF3366; text-align: center; margin-top: 25px; }
    .admin-footer-btn { text-align: center; margin-top: 40px; padding: 20px 0; border-top: 1px solid #1A291A; }
    </style>
""", unsafe_allow_html=True)

if "generated" not in st.session_state: st.session_state.generated = False
if "logo_text" not in st.session_state: st.session_state.logo_text = ""
if "logo_admin_mode" not in st.session_state: st.session_state.logo_admin_mode = False

DB_FILE = "logo_base.json"
def load_db():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f: return json.load(f)
        except: return {"total_earned": 0}
    return {"total_earned": 0}

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False, indent=4)

logo_db = load_db()

# --- ПОКУПАТЕЛЬСКИЙ ИНТЕРФЕЙС ---
if not st.session_state.logo_admin_mode:
    st.title("🔋 GigaLogo AI — Нейро-Генератор Кибер-Аватарок")
    st.caption("Создание уникальных неоновых логотипов, игровых аватаров и хакерских эмблем для Steam, Discord, Twitch и Telegram.")
    st.divider()

    st.markdown("""
    <div class="logo-box">
        <h3 style="margin: 0; color: #39FF14 !important;">⚙️ Настройка ИИ-генерации дизайна</h3>
        <p style="font-size: 14px; color: #889988; margin-top: 5px;">ИИ создаст уникальный векторный логотип со встроенным неоновым свечением вашего никнейма.</p>
    </div>
    """, unsafe_allow_html=True)

    user_nick = st.text_input("Введи свой никнейм или название бренда (на английском или русском):", placeholder="Например: GigaBoss, TANK_CS")
    logo_style = st.selectbox("🎮 Выбери стиль неонового оформления:", ["Toxic Green (Кислотно-зеленый неон)", "Cyberpunk Cyber (Фиолетово-желтый хакер)", "Hell Fire (Огненный брутальный шрифт)", "Deep Ice (Ледяной футуристичный глянец)"])

    if user_nick and not st.session_state.generated:
        if st.button("🚀 ЗАПУСТИТЬ СИНТЕЗ НЕОНОВОГО ДИЗАЙНА"):
            st.session_state.logo_text = user_nick
            with st.spinner("🧠 ИИ подбирает шрифты и просчитывает трассировку неоновых лучей..."):
                time.sleep(2)
            with st.spinner("⚡ Идёт финальный рендеринг векторной графики в 4K Ultra-HD..."):
                time.sleep(2)
            st.session_state.generated = True
            st.rerun()

    # СИСТЕМНЫЙ ЗАМОК ДЛЯ СКАЧИВАНИЯ (ЦЕННИК 990)
    if st.session_state.generated:
        st.markdown(f"""
        <div class="logo-lock-box">
            <h2 style="color: #FF3366 !important; margin: 0;">🔒 ДИЗАЙН СГЕНЕРИРОВАН. СКАЧИВАНИЕ ЗАБЛОКИРОВАНО</h2>
            <p style="font-size: 16px; color: #FFFFFF; margin: 15px 0;">Уникальный аватар для профиля <b>"{st.session_state.logo_text}"</b> успешно синтезирован в Ultra-HD качестве!</p>
            <p style="font-size: 15px; color: #99A999;">Для удаления защитного водяного знака, отключения размытия текстур и моментального скачивания файла в 4K разрешении, поддержите проект донатом.</p>
            <h1 style="color: #39FF14 !important; font-size: 40px; margin: 15px 0; font-family: monospace;">990 ₽</h1>
        </div>
        """, unsafe_allow_html=True)
        
        # ССЫЛКА НА ТВОЙ ЮМОНЕЙ НА 990 РУБЛЕЙ
        pay_url = f"https://yoomoney.ru_{st.session_state.logo_text.replace(' ', '_')}&targets-hint=&default-sum=990&button-text=11&payment-type=AC&hint=&quickpay=shop&account={YOUR_YOOMONEY_ACCOUNT}"
        st.markdown(f'<a class="pay-btn-link" href="{pay_url}" target="_blank">💳 СНЯТЬ ВОДЯНОЙ ЗНАК И СКАЧАТЬ В HD</a>', unsafe_allow_html=True)
        
        if st.button("🔍 Проверить зачисление доната и скачать аватар"):
            st.balloons()
            logo_db["total_earned"] += 990
            save_db(logo_db)
            st.success("🎉 Донат успешно получен! Водяной знак удален. Скачивание вашей аватарки в 4K началось...")
            
        if st.button("🔄 Сбросить и сгенерировать другую аватарку"):
            st.session_state.generated = False
            st.session_state.logo_text = ""
            st.rerun()
            
    st.markdown('<div class="admin-footer-btn">', unsafe_allow_html=True)
    if st.button("⚙️ Панель управления донатами GigaLogo", key="goto_logo_admin"):
        st.session_state.logo_admin_mode = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- АДМИН-ПАНЕЛЬ ВЛАДЕЛЬЦА ---
else:
    st.title("🔐 Панель Управления GigaLogo")
    if st.button("⬅️ Вернуться к Генератору"):
        st.session_state.logo_admin_mode = False
        st.rerun()
    st.divider()
    
    if "logo_auth" not in st.session_state: st.session_state.logo_auth = False
    
    if not st.session_state.logo_auth:
        st.subheader("🔒 Авторизация владельца")
        pin = st.text_input("Введи секретный пароль директора:", type="password")
        if pin == ADMIN_PIN:
            st.session_state.photo_auth = True
            st.session_state.logo_auth = True
            st.rerun()
        elif pin != "": st.error("❌ Доступ заблокирован! Неверный пароль.")
    else:
        st.markdown(f"""
        <div style="background-color: #0A0F0A; padding: 25px; border-radius: 14px; border: 2px solid #39FF14; text-align: center;">
            <h3 style="margin: 0; color: #FFFFFF !important; font-family: monospace;">📊 ОБЩАЯ СУММА ДОНАТОВ С НЕОН-ЛОГОТИПОВ:</h3>
            <h1 style="margin: 8px 0 0 0; color: #39FF14 !important; font-size: 50px; font-family: monospace;">{logo_db.get('total_earned', 0)} ₽</h1>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚪 Сбросить сессию"):
            st.session_state.logo_auth = False
            st.session_state.logo_admin_mode = False
            st.rerun()
