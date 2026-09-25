import os, json, sys, warnings
warnings.filterwarnings("ignore")
import streamlit as st

# ТВОЙ СЕКРЕТНЫЙ ПАРОЛЬ АДМИНИСТРАТОРА
ADMIN_PIN = "клаксон23523"

# ТВОЙ РЕАЛЬНЫЙ СЧЕТ ЮМОНЕЙ
YOUR_YOOMONEY_ACCOUNT = "4100118719995386"  

st.set_page_config(page_title="GigaStore — IT-Маркетплейс", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #08080A; color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #0F0F12 !important; }
    h1, h2, h3, h4 { color: #00FF66 !important; font-family: 'Courier New', monospace; }
    .stButton>button { 
        background: linear-gradient(135deg, #00FF66 0%, #00CC52 100%); color: #000000 !important; 
        border-radius: 8px; width: 100%; font-weight: bold; font-size: 16px; border: none;
        box-shadow: 0 4px 15px rgba(0, 255, 102, 0.2); transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 255, 102, 0.4); }
    .pay-btn-link {
        display: block; text-align: center; background: linear-gradient(135deg, #00FF66 0%, #00CC52 100%);
        color: #000000 !important; border-radius: 8px; font-weight: bold; font-size: 18px;
        padding: 12px; text-decoration: none; box-shadow: 0 4px 15px rgba(0, 255, 102, 0.2); margin-top: 10px;
    }
    .pay-btn-link:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 255, 102, 0.4); }
    input, textarea, [data-baseweb="textarea"]>div, [data-baseweb="input"]>div { background-color: #121216 !important; color: #FFFFFF !important; border: 1px solid #22222a !important; }
    .marketplace-card { background-color: #121216; padding: 25px; border-radius: 14px; border: 1px solid #22222a; margin-bottom: 15px; }
    .marketplace-card:hover { border: 1px solid #00FF66; }
    .price-tag { color: #00FF66; font-size: 26px; font-weight: bold; font-family: 'Courier New', monospace; margin: 10px 0; }
    .item-badge { background-color: #1a1a24; color: #00FF66; padding: 5px 12px; border-radius: 6px; border: 1px solid #00FF66; font-size: 12px; font-weight: bold; text-transform: uppercase; }
    .welcome-block { background-color: #121216; padding: 25px; border-radius: 14px; border: 2px dashed #00FF66; margin-bottom: 30px; text-align: center; }
    .success-delivery { background-color: #0A2012; padding: 20px; border-radius: 10px; border: 1px solid #00FF66; margin-top: 15px; text-align: center; }
    .admin-footer-btn { text-align: center; margin-top: 5px; padding: 20px 0; border-top: 1px solid #1a1a24; }
    </style>
""", unsafe_allow_html=True)

DB_FILE = "store_base.json"
def load_db():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f: return json.load(f)
        except: pass
    
    # СОЗДАЕМ ТОВАР СРАЗУ ПРИ ПЕРВОМ ЗАПУСКЕ С КОРРЕКТНЫМ ЦЕННИКОМ!
    default_data = {
        "products": {
            "Приватный Гайд: Пошаговый мануал по заработку на ИИ": {
                "desc": "Эксклюзивный пошаговый PDF-мануал. Внутри: 5 готовых схем, как выполнять дорогие заказы по написанию текстов, дизайну и коду для бизнеса с помощью нейросетей, тратя всего 30 минут в день. Список бирж и шаблоны общения прилагаются!",
                "price": "1500",
                "link": "https://ya.ru",
                "category": "📚 Приватные Гайды / Мануалы",
                "status": "Опубликован"
            }
        },
        "total_earned": 0
    }
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(default_data, f, ensure_ascii=False, indent=4)
    return default_data

store_db = load_db()

if "admin_logged_in" not in st.session_state: st.session_state.admin_logged_in = False
if "is_admin_auth" not in st.session_state: st.session_state.is_admin_auth = False

# --- ПОКУПАТЕЛЬСКИЙ ИНТЕРФЕЙС ---
if not st.session_state.admin_logged_in:
    st.title("⚡ GigaStore — IT-Маркетплейс Готового Софта")
    st.caption("Магазин исходного кода игр, веб-скриптов и приватных гайдов под ключ.")
    st.divider()
    
    st.markdown("""
    <div class="welcome-block">
        <h2 style="margin: 0; color: #00FF66 !important;">🔥 Кибер-Витрина Открыта!</h2>
        <p style="font-size: 16px; margin: 10px 0 0 0; color: #A0A0A0;">Выбирайте товар, оплачивайте картой/СБП и получайте доступ автоматически!</p>
    </div>
    """, unsafe_allow_html=True)
    
    CATEGORIES = ["🤖 Все товары", "🎮 Исходники игр", "🌐 Шаблоны сайтов", "📚 Приватные Гайды / Мануалы"]
    cat_tab = st.radio("🗂️ Выбери категорию:", CATEGORIES, horizontal=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    all_active = {k: v for k, v in store_db["products"].items() if v.get("status") == "Опубликован"}
    filtered_products = {k: v for k, v in all_active.items() if cat_tab == "🤖 Все товары" or v.get("category", "🎮 Исходники игр") == cat_tab}
            
    if not filtered_products:
        st.info("В данной категории товаров пока нет. Разработчик подгружает свежие приватные материалы!")
    else:
        p_keys = list(filtered_products.keys())
        for idx in range(0, len(p_keys), 2):
            cols = st.columns(2)
            for c_idx, key_idx in enumerate([idx, idx+1]):
                if key_idx < len(p_keys):
                    p_name = p_keys[key_idx]
                    p_info = filtered_products[p_name]
                    with cols[c_idx]:
                        st.markdown(f"""
                        <div class="marketplace-card">
                            <span class="item-badge">🌐 {p_info.get('category', 'Товар')}</span>
                            <h3 style="margin-top: 15px; margin-bottom: 10px;">📦 {p_name}</h3>
                            <p style="font-size: 15px; color: #A0A0A0; min-height: 60px;">{p_info.get('desc', '')}</p>
                            <div class="price-tag">{p_info.get('price', 0)} ₽</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        pay_url = f"https://yoomoney.ru_{p_name.replace(' ', '_')}&targets-hint=&default-sum={p_info.get('price', 100)}&button-text=11&payment-type=AC&hint=&successURL={p_info.get('link', '')}&quickpay=shop&account={YOUR_YOOMONEY_ACCOUNT}"
                        st.markdown(f'<a class="pay-btn-link" href="{pay_url}" target="_blank">💳 КУПИТЬ КАРТОЙ / СБП</a>', unsafe_allow_html=True)
                        
                        if st.button(f"🔍 Я оплатил продукт: {p_name}", key=f"check_{p_name}"):
                            st.markdown(f"""
                            <div class="success-delivery">
                                <h4 style="color: #00FF66 !important; margin: 0;">🎉 Ссылка на скачивание софта:</h4>
                                <a href="{p_info.get('link', '')}" target="_blank" style="color: #FFA500; font-weight: bold; font-size: 16px; text-decoration: none;">🔗 Кликни сюда, чтобы забрать ZIP-архив</a>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        if st.session_state.is_admin_auth:
                            if st.button(f"🗑️ Стереть товар из ленты: {p_name}", key=f"del_main_{p_name}"):
                                del store_db["products"][p_name]
                                save_db(store_db)
                                st.warning("Товар удален!")
                                st.rerun()
                        
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="admin-footer-btn">', unsafe_allow_html=True)
    if st.button("⚙️ Вход для разработчиков и управления маркетплейсом", key="goto_admin_btn"):
        st.session_state.admin_logged_in = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
# --- АДМИН-ПАНЕЛЬ ---
elif st.session_state.admin_logged_in:
    st.title("🔐 GigaStore — Панель Управления Маркетплейсом")
    if st.button("⬅️ Выйти из админки и вернуться на Витрину"):
        st.session_state.admin_logged_in = False
        st.rerun()
    st.divider()
    
    if not st.session_state.is_admin_auth:
        st.subheader("🔒 Авторизация владельца платформы")
        input_pin = st.text_input("Введи секретный пароль директора:", type="password")
        if input_pin == ADMIN_PIN:
            st.session_state.is_admin_auth = True
            st.rerun()
        elif input_pin != "": st.error("❌ Неверный ключ доступа!")
    else:
        st.markdown(f"""
        <div style="background-color: #121216; padding: 25px; border-radius: 14px; border: 2px solid #00FF66; text-align: center; margin-bottom: 30px;">
            <h3 style="margin: 0; color: #FFFFFF !important; font-family: monospace;">📊 ОБЩАЯ КАССА МАРКЕТПЛЕЙСА (БАЛАНС):</h3>
            <h1 style="margin: 8px 0 0 0; color: #00FF66 !important; font-size: 50px; font-family: monospace;">{store_db.get('total_earned', 0)} ₽</h1>
        </div>
        """, unsafe_allow_html=True)
        
        if st.sidebar.button("🚪 Сбросить сессию авторизации"):
            st.session_state.is_admin_auth = False
            st.session_state.admin_logged_in = False
            st.rerun()
            
        action_mode = st.radio("Действие со складом софта:", ["➕ Выставить на маркетплейс новый продукт", "📝 Изменить настройки софта"])
        edit_target = None
        default_title, default_desc, default_price, default_link, default_cat = "", "", "1500", "https://", "🎮 Исходники игр"
        
        if action_mode == "📝 Изменить настройки софта" and store_db["products"]:
            edit_target = st.selectbox("Выбери IT-продукт для изменения:", list(store_db["products"].keys()))
            if edit_target:
                default_title = edit_target
                default_desc = store_db["products"][edit_target].get("desc", "")
                default_price = str(store_db["products"][edit_target].get("price", 1500))
                default_link = store_db["products"][edit_target].get("link", "https://")
                default_cat = store_db["products"][edit_target].get("category", "🎮 Исходники игр")
                
        st.subheader("🛠️ Карточка настройки IT-товара")
        new_title = st.text_input("Название продукта:", value=default_title)
        new_cat = st.selectbox("Категория товара:", ["🎮 Исходники игр", "🌐 Шаблоны сайтов", "📚 Приватные Гайды / Мануалы"], index=["🎮 Исходники игр", "🌐 Шаблоны сайтов", "📚 Приватные Гайды / Мануалы"].index(default_cat))
        new_desc = st.text_area("Подробное описание:", value=default_desc)
        new_price = st.text_input("Стоимость (в рублях):", value=default_price)
        new_link = st.text_input("Ссылка на скачивание архива/файла:", value=default_link)
        
        if new_title.strip() and store_db["products"].get(new_title.strip(), {}).get("status") != "Опубликован":
            store_db["products"][new_title.strip()] = {"desc": new_desc, "price": new_price, "link": new_link, "category": new_cat, "status": "Черновик"}
            save_db(store_db)

        col_act1, col_act2 = st.columns(2)
        with col_act1:
            if st.button("🚀 ОФИЦИАЛЬНО ВЫПУСТИТЬ НА МАРКЕТПЛЕЙС"):
                if new_title.strip():
                    store_db["products"][new_title.strip()] = {"desc": new_desc, "price": new_price, "link": new_link, "category": new_cat, "status": "Опубликован"}
                    save_db(store_db)
                    st.success("💥 Добавлено на витрину!")
                    st.rerun()
                else: st.error("Ошибка: Введи название!")
        with col_act2:
            if st.button("🗑️ Снять софт с продажи / Удалить"):
                if new_title.strip() in store_db["products"]:
                    del store_db["products"][new_title.strip()]
                    save_db(store_db)
                    st.warning("Товар удален!")
                    st.rerun()
